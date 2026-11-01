"""Finite exhaustive verifier for threshold-two, three-state GHM on complete bipartite graphs.

Run from directory containing certificate.tsv: python verify.py
Only the Python standard library is required.
"""
from collections import Counter
from itertools import product
from math import comb, factorial
from pathlib import Path

BASE=Path(__file__).resolve().parent


def step_cohort(s,w):
    exc_a=sum(w[j] for j in range(3) if s[j]==1)
    exc_b=sum(w[j] for j in range(3,6) if s[j]==1)
    out=[]
    for j,x in enumerate(s):
        if x<0:out.append(-1)
        elif x==1:out.append(2)
        elif x==2:out.append(0)
        else:out.append(1 if (exc_b if j<3 else exc_a)>=2 else 0)
    return tuple(out)


def cohort_profile(w):
    s=tuple(j%3 if w[j] else -1 for j in range(6))
    seen={};t=0
    while s not in seen:
        if t>=100:raise AssertionError(('unbounded finite search',w))
        seen[s]=t;s=step_cohort(s,w);t+=1
    return seen[s],t-seen[s]


def feasible(w,n):
    return sum(w)<=n and (2 in w or sum(w)==n)


def compositions(n):
    for c0 in range(n+1):
        for c1 in range(n-c0+1):
            yield (c0,c1,n-c0-c1)


def weight_of(c):
    n=sum(c)
    return factorial(n)//(factorial(c[0])*factorial(c[1])*factorial(c[2]))


def macro_census(a,b,profiles):
    out=Counter()
    for ca in compositions(a):
        for cb in compositions(b):
            w=tuple(min(2,z) for z in ca+cb)
            out[profiles[w]]+=weight_of(ca)*weight_of(cb)
    return out


def period3_count(n):
    return sum(weight_of(c) for c in compositions(n) if all(x>=2 for x in c))


def balanced_binary(n):
    return sum(comb(n,k) for k in range(2,n-1))


def step_vertices(x,a,b):
    ea=sum(v==1 for v in x[:a]); eb=sum(v==1 for v in x[a:])
    return tuple((v+1)%3 if v else (1 if (eb if i<a else ea)>=2 else 0) for i,v in enumerate(x))


def direct_profile(x,a,b):
    seen={}; s=x; t=0
    while s not in seen:
        assert t<100
        seen[s]=t; t+=1; s=step_vertices(s,a,b)
    return seen[s],t-seen[s]


def verify():
    patterns=[w for w in product(range(3),repeat=6) if sum(w[:3]) and sum(w[3:])]
    assert len(patterns)==676
    profiles={w:cohort_profile(w) for w in patterns}
    expected={(0,1):4,(0,3):1,(0,4):2,(1,1):60,(1,4):10,
              (2,1):324,(2,4):30,(3,1):160,(3,4):8,
              (4,1):51,(4,4):2,(5,1):24}
    assert Counter(profiles.values())==Counter(expected)
    assert sorted({p for t,p in profiles.values()})==[1,3,4]
    assert max(t for t,p in profiles.values())==5
    lines=['a0\ta1\ta2\tb0\tb1\tb2\ttransient\tperiod']
    lines.extend('\t'.join(map(str,w+(profiles[w]))) for w in patterns)
    certificate=(BASE/'certificate.tsv').read_text(encoding='utf-8')
    assert certificate == '\n'.join(lines)+'\n'

    max_expected=((2,3,3,3,3,3),(3,3,4,4,4,4),(3,4,4,5,5,5),
                  (3,4,5,5,5,5),(3,4,5,5,5,5),(3,4,5,5,5,5))
    for a in range(1,7):
        for b in range(1,7):
            allowed=[profiles[w] for w in patterns if feasible(w[:3],a) and feasible(w[3:],b)]
            assert allowed
            assert max(t for t,p in allowed)==max_expected[a-1][b-1]
            assert (3 in (p for t,p in allowed)) == (a>=6 and b>=6)
            assert (4 in (p for t,p in allowed)) == (a>=4 and b>=4)
            dist=macro_census(a,b,profiles)
            assert sum(dist.values())==3**(a+b)
            assert dist[0,1]==1
            assert dist[0,3]==period3_count(a)*period3_count(b)
            assert dist[0,4]==2*balanced_binary(a)*balanced_binary(b)
            assert not any(p not in (1,3,4) for t,p in dist)
            assert not any(t>5 for t,p in dist)

    direct_total=0
    for a,b in list(product(range(1,5),repeat=2))+[(5,5)]:
        for x in product(range(3),repeat=a+b):
            c_a=tuple(x[:a].count(j) for j in range(3))
            c_b=tuple(x[a:].count(j) for j in range(3))
            w=tuple(min(2,z) for z in c_a+c_b)
            assert direct_profile(x,a,b)==profiles[w], (a,b,x)
            direct_total+=1
    assert direct_total==73449
    print('GHM_THRESHOLD_TWO_BICLIQUE_VERIFY_OK')
    print('exact_weight_signatures:',len(patterns))
    print('signature_preperiod_period_histogram:',sorted(expected.items()))
    print('size_threshold_table_1_to_6:',max_expected)
    print('direct_labelled_configurations:',direct_total)
    print('periodic_counts_K_6_6: fixed=1, period3_states=8100, period4_states=5000')

if __name__=='__main__':
    verify()
