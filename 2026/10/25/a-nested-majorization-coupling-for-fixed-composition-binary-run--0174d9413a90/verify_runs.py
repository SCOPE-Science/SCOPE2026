"""Exact independent checks for fixed-content binary run refinement.

No external dependencies. Enumerates every binary word for 1 <= a,b <= 7;
checks conditional square-length expectation and longest-run stochastic order.
Independently enumerates the combinatorial cut-growth kernel and its target law.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb


def run_lengths(word):
    runs = []
    prev = None
    for v in word:
        if v != prev:
            runs.append(1)
            prev = v
        else:
            runs[-1] += 1
    return tuple(runs)


def f(n, k):
    return Fraction(n * (2*n-k+1), k+1)


def target_counts(a, b, r):
    if r % 2 == 0:
        k = r // 2
        return [(k, k, 2*comb(a-1,k-1)*comb(b-1,k-1))]
    k = r // 2
    out = []
    if k+1 <= a and k <= b:
        out.append((k+1,k,comb(a-1,k)*comb(b-1,k-1)))
    if k+1 <= b and k <= a:
        out.append((k,k+1,comb(a-1,k-1)*comb(b-1,k)))
    return out


def conditional_expectation_Q(a,b,r):
    tot = sum(c for _,_,c in target_counts(a,b,r))
    return sum(Fraction(c,tot)*(f(a,ra)+f(b,rb))
               for ra,rb,c in target_counts(a,b,r))


def check(a,b):
    n=a+b
    by_r=defaultdict(list)
    for indices in combinations(range(n), a):
        ones=set(indices)
        w=[int(i in ones) for i in range(n)]
        lengths=run_lengths(w)
        r=len(lengths)
        by_r[r].append((max(lengths),sum(t*t for t in lengths)))
    for r,rows in by_r.items():
        q=Fraction(sum(x[1] for x in rows),len(rows))
        assert q==conditional_expectation_Q(a,b,r),(a,b,r,q,conditional_expectation_Q(a,b,r))
        assert len(rows)==sum(c for _,_,c in target_counts(a,b,r)),(a,b,r)
    for r in range(min(by_r),max(by_r)):
        x=by_r[r]; y=by_r[r+1]
        assert sum(q for _,q in x)*len(y)>sum(q for _,q in y)*len(x), (a,b,r,'strict Q failure')
        for t in range(1,n+1):
            assert sum(m>=t for m,_ in x)*len(y) >= sum(m>=t for m,_ in y)*len(x),(a,b,r,t,'tail failure')


def cut_sets(n,k):
    return list(combinations(range(1,n),k-1))


def test_cut_kernel(a,b):
    # Each state: (A internal cut-set, B internal cut-set) probability,
    # representing joint run partitions, orientation integrated out.
    states={((),()):Fraction(1)}
    for r in range(2,2*min(a,b)+1+int(a!=b)):
        empirical=defaultdict(Fraction)
        for state,p in states.items():
            empirical[state]+=p
        # exact target partition distribution via stars-and-bars
        expected=defaultdict(Fraction)
        if r%2==0:
            k=r//2
            for aa in cut_sets(a,k):
                for bb in cut_sets(b,k):
                    expected[(aa,bb)]+=Fraction(1,comb(a-1,k-1)*comb(b-1,k-1))
        else:
            k=r//2
            counts=target_counts(a,b,r)
            den=sum(z for _,_,z in counts)
            for ka,kb,num in counts:
                for aa in cut_sets(a,ka):
                    for bb in cut_sets(b,kb):
                        expected[(aa,bb)]+=Fraction(num,den*comb(a-1,ka-1)*comb(b-1,kb-1))
        assert dict(empirical)==dict(expected),(a,b,r,'kernel law mismatch')
        if r==2*min(a,b)+int(a!=b):break
        nxt=defaultdict(Fraction)
        for (sa,sb),p in states.items():
            ka,kb=len(sa)+1,len(sb)+1
            if ka==kb:
                free_a=[v for v in range(1,a) if v not in sa]
                free_b=[v for v in range(1,b) if v not in sb]
                available=len(free_a)+len(free_b)
                assert available>0
                for v in free_a:nxt[(tuple(sorted(sa+(v,))),sb)]+=p/Fraction(available)
                for v in free_b:nxt[(sa,tuple(sorted(sb+(v,))))]+=p/Fraction(available)
            elif ka==kb+1:
                free_b=[v for v in range(1,b) if v not in sb]
                assert free_b
                for v in free_b:nxt[(sa,tuple(sorted(sb+(v,))))]+=p/Fraction(len(free_b))
            elif kb==ka+1:
                free_a=[v for v in range(1,a) if v not in sa]
                assert free_a
                for v in free_a:nxt[(tuple(sorted(sa+(v,))),sb)]+=p/Fraction(len(free_a))
            else:raise AssertionError('invalid state')
        states=dict(nxt)


def main():
    tested=0
    for a in range(1,8):
        for b in range(1,8):
            check(a,b)
            test_cut_kernel(a,b)
            tested+=1
    print(f'PASS: {tested} (a,b) pairs, all binary words, all attainable run counts,')
    print('all longest-run thresholds, exact conditional Q, and exact cut kernel states.')

if __name__=='__main__':main()
