#!/usr/bin/env python3
"""Exact finite tests of the four-run minimal-unique-factor classification.

The exhaustive checks corroborate, but do not replace, the unrestricted
mathematical proof supplied with the result.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb


def literal_mus(w):
    occ = Counter(w[i:j] for i in range(len(w)) for j in range(i+1, len(w)+1))
    return {u for u,c in occ.items() if c==1 and
            (len(u)==1 or (occ[u[:-1]] >= 2 and occ[u[1:]] >= 2))}


def predicted_mus(a,b,c,d):
    s={'10'}
    if a != c: s.add('0'*max(a,c))
    if b != d: s.add('1'*max(b,d))
    if abs(a-c) >= 2: s.add('0'*(min(a,c)+1)+'1')
    if abs(b-d) >= 2: s.add('0'+'1'*(min(b,d)+1))
    return s


def signed_gap(x,y):
    return int(x!=y)+int(abs(x-y)>=2)


def finite_pair_coefficient(m,j):
    """[z^m t^j] (z^2+2tz^3+2t^2z^4/(1-z))/(1-z^2)."""
    if m<2: return 0
    if j==0: return int(m%2==0)
    if j==1: return 2*int(m>=3 and m%2==1)
    if j==2: return 2*((m-2)//2) if m>=4 else 0
    return 0


def gf_coefficient(n,k):
    # factor 2 for orientation; central t for the always-unique 10 or 01.
    return 2*sum(finite_pair_coefficient(m,j)*finite_pair_coefficient(n-m,k-1-j)
                 for m in range(2,n-1) for j in range(3))


def run():
    quadruples=0
    total_literals=0
    for a,b,c,d in product(range(1,8),repeat=4):
        w='0'*a+'1'*b+'0'*c+'1'*d
        got=literal_mus(w)
        exp=predicted_mus(a,b,c,d)
        assert got==exp, ((a,b,c,d),got,exp)
        total_literals+=len(got)
        quadruples+=1

    counted=Counter()
    for n in range(4,23):
        for a in range(1,n-2):
            for b in range(1,n-a-1):
                for c in range(1,n-a-b):
                    d=n-a-b-c
                    if d<1:continue
                    w='0'*a+'1'*b+'0'*c+'1'*d
                    k=len(literal_mus(w))
                    counted[n,k]+=2
        assert sum(counted[n,k] for k in range(1,6)) == 2*comb(n-1,3)
        for k in range(1,6):
            expect=gf_coefficient(n,k)
            assert counted[n,k]==expect,(n,k,counted[n,k],expect)
        if n>=8:
            j=(n-8)//2
            extreme=(4*(j+1)*(j+2)*(2*j+3)//3 if n%2==0 else
                     8*(j+1)*(j+2)*(j+3)//3)
            assert counted[n,5]==extreme,(n,counted[n,5],extreme)
        else:
            assert counted[n,5]==0
    print(f'VERIFY_OK complete_quadruples={quadruples} literal_mus={total_literals} '
          f'length_coefficients={19*5} max_length=22 maximum=5 first_attainment=8')


if __name__=='__main__': run()
