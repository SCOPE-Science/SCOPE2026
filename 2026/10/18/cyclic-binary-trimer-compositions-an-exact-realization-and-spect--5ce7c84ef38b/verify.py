"""Reproduce binary circular length-three composition observations.

The infinite theorem requires the proof, not these finite checks.
Run with Python 3.9+: python verify.py
"""
from itertools import product
from math import comb


def admissible(c):
    a, p, q, d = c
    if min(c) < 0:
        return False
    if p == q == 0:
        return (a > 0 and d == 0) or (d > 0 and a == 0)
    return (p - q) % 3 == 0 and (a == 0 or p >= 2) and (d == 0 or q >= 2)


def predicted(n):
    assert n >= 1
    return {
        (a, p, q, n-a-p-q)
        for a in range(n+1)
        for p in range(n-a+1)
        for q in range(n-a-p+1)
        if admissible((a,p,q,n-a-p-q))
    }


def direct(n):
    profiles = set()
    for w in product((0,1),repeat=n):
        counts = [0]*4
        for i in range(n):
            counts[w[i] + w[(i+1)%n] + w[(i+2)%n]] += 1
        profiles.add(tuple(counts))
    return profiles


def dynamic(n):
    if n == 1:
        return {(1,0,0,0),(0,0,0,1)}
    # Independent de Bruijn-state propagation: no run lengths or feasibility tests.
    states = {(a,b,a,b,0,0,0,0) for a in range(2) for b in range(2)}
    for pos in range(2,n):
        nxt = set()
        for a,b,x,y,c0,c1,c2,c3 in states:
            for v in (0,1):
                cs = [c0,c1,c2,c3]
                cs[x+y+v] += 1
                nxt.add((a,b,y,v,*cs))
        states = nxt
    profiles = set()
    for a,b,x,y,c0,c1,c2,c3 in states:
        cs=[c0,c1,c2,c3]
        cs[x+y+a]+=1
        cs[y+a+b]+=1
        profiles.add(tuple(cs))
    return profiles


def gf_coefficient(n):
    # Exact partial fractions: F(z) = 1 + 2z + z^2 + 4/[9(1+z+z^2)]
    # +4/(z-1) +32/[9(z-1)^2] +4/[3(z-1)^3]+1/[3(z-1)^4].
    periodic = (1,-1,0)[n%3]
    numerator = (3*comb(n+3,3)-12*comb(n+2,2)
                 +32*(n+1)-36+4*periodic)
    assert numerator % 9 == 0
    return (1 if n==0 or n==2 else 2 if n==1 else 0) + numerator//9


def main():
    counts=[]
    for n in range(1,17):
        d=direct(n)
        p=predicted(n)
        assert d==p,(n,'direct versus closed characterization',d^p)
        assert len(d)==gf_coefficient(n),(n,'generating function')
        counts.append(len(d))
    print('Exhaustive direct words through n=16: OK',counts)
    for n in range(1,49):
        d=dynamic(n)
        p=predicted(n)
        assert d==p,(n,'independent de Bruijn DP versus characterization',len(d),len(p),list(d^p)[:8])
        assert len(d)==gf_coefficient(n),(n,'rational generating function')
    print('Independent de Bruijn-state DP for n=1..48: OK')
    print('Coefficient and residue formula n=1..48: OK')
    print('FINITE CHECKS PASSED; theorem for all n is proved in RESULT.md')

if __name__=='__main__':
    main()
