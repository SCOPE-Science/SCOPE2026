#!/usr/bin/env python3
"""Finite checks for a theorem about conference-graph switching two-graphs.
Only Python 3 standard library is required. No asymptotic conclusions are inferred
from the finite tests: those follow from the proof's conference matrix identity.
"""
from itertools import combinations, product


def finite_field(p, m, polynomial):
    """Return addition, subtraction, multiplication in F_p[X]/(polynomial)."""
    q = p ** m
    def digits(n):
        return [(n // p ** i) % p for i in range(m)]
    def add(a, b):
        aa, bb = digits(a), digits(b)
        return sum(((aa[i] + bb[i]) % p) * p ** i for i in range(m))
    def neg(a):
        aa = digits(a)
        return sum((-aa[i] % p) * p ** i for i in range(m))
    def mul(a, b):
        aa, bb = digits(a), digits(b)
        out = [0] * (2 * m - 1)
        for i in range(m):
            for j in range(m):
                out[i+j] = (out[i+j] + aa[i] * bb[j]) % p
        for k in range(2*m-2, m-1, -1):
            v = out[k]
            for j in range(m):
                out[k-m+j] = (out[k-m+j] - v*polynomial[j]) % p
        return sum(out[i] * p ** i for i in range(m))
    return q, add, lambda a,b:add(a,neg(b)), mul


def analyze(p,m,poly):
    q,add,sub,mul=finite_field(p,m,poly)
    nonzero_squares={mul(i,i) for i in range(1,q)}
    assert len(nonzero_squares)==(q-1)//2
    def S(a,b):
        return 0 if a==b else (1 if sub(a,b) in nonzero_squares else -1)
    def R(a,b,c):
        return S(a,b)*S(b,c)*S(c,a)
    for a in range(q):
        assert sum(S(a,b)==1 for b in range(q))==(q-1)//2
    for a,b in combinations(range(q),2):
        assert sum(S(a,x)*S(b,x) for x in range(q))==-1
    low=999; patterns_tested=0
    for a,b,c in combinations(range(q),3):
        tau=R(a,b,c)
        for eps in product((-1,1),repeat=3):
            if eps[0]*eps[1]*eps[2]!=tau:
                continue
            actual=sum((R(a,b,x),R(a,c,x),R(b,c,x))==eps for x in range(q) if x not in (a,b,c))
            # Pair terms obtained from S^2=qI-J.
            ab,ac,bc=S(a,b),S(a,c),S(b,c)
            numerator=q-3-(ab+tau)*eps[0]-(ac+tau)*eps[1]-(bc+tau)*eps[2]
            assert numerator%4==0
            formula=numerator//4
            assert formula==actual,(q,a,b,c,eps,actual,formula)
            low=min(low,actual)
            patterns_tested+=1
    if q>=9:
        assert low==(q-9)//4
    allpos4=any(all(R(*triple)==1 for triple in combinations(quad,3))
                for quad in combinations(range(q),4))
    missing_pos3=any(R(a,b,c)==1 and not any(
                 all(R(u,v,x)==1 for u,v in ((a,b),(a,c),(b,c)))
                 for x in range(q) if x not in (a,b,c))
                 for a,b,c in combinations(range(q),3))
    if q==5:assert not allpos4
    if q==9:assert allpos4 and missing_pos3
    if q>=13:assert allpos4 and not missing_pos3 and low>=1
    if q>=13:
        w=(q-9)//4
        # A triangle of adjacent vertices must exist; for its all-positive
        # continuation, exactly w witnesses occur. Removing precisely them
        # leaves a violated one-point-extension request.
        a,b,c=next(tri for tri in combinations(range(q),3)
                   if all(S(u,v)==1 for u,v in combinations(tri,2)))
        candidates=[x for x in range(q) if x not in (a,b,c)
                    and all(R(u,v,x)==1 for u,v in ((a,b),(a,c),(b,c)))]
        assert len(candidates)==w
    print(f'q={q}: S-matrix identity PASS; {patterns_tested} compatible triple extensions PASS; '
          f'min={low}; all-positive-4={allpos4}; missing-positive-3={missing_pos3}'
          + (f'; sharp-deletion={w}' if q>=13 else ''))

if __name__=='__main__':
    for args in [(5,1,[0]),(3,2,[1,0]),(13,1,[0]),(17,1,[0]),
                 (5,2,[2,0]),(29,1,[0])]:
        analyze(*args)
    print('ALL FINITE CHECKS PASS')
