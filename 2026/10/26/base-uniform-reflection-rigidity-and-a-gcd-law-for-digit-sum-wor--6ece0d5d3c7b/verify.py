#!/usr/bin/env python3
"""Finite checks of the exact base-b generalized digit-sum reflection theorem.

The infinite claim follows from the proof; no finite-prefix completeness
assumption is used in that proof. Standard-library Python only.
"""
from math import gcd


def pairs(base, modulus):
    d=gcd(base-1,modulus)
    return {(a,c) for a in range(modulus) for c in range(modulus) if (c-a-1)%d==0}


def factors_small(base, modulus, length):
    Q=pairs(base, modulus)
    ans=set()
    for a,c in Q:
        for start in range(base):
            v=tuple((a+start+i)%modulus if start+i<base else (c+start+i-base)%modulus for i in range(length))
            if length <= base+1:
                ans.add(v)
    return ans


def count_reflection(F):
    return len({min(w,w[::-1]) for w in F})


def test():
    cases=0
    for b in range(3,11):
      for m in range(3,16):
        d=gcd(b-1,m)
        P=pairs(b,m)
        assert len(P)==m*m//d
        F3=factors_small(b,m,3)
        F4=factors_small(b,m,4)
        assert len(F3)==2*m*m//d-m,(b,m,len(F3))
        assert len(F4)==3*m*m//d-2*m,(b,m,len(F4))
        assert all((w==w[::-1]) or (w[::-1] not in F3) for w in F3)
        assert all(w[::-1] not in F4 for w in F4)
        r2=m*(m+1)//2 if d==1 else (m*m//4 if d==2 else m*m//d)
        assert count_reflection(P)==r2
        assert count_reflection(F3)==len(F3)
        assert count_reflection(F4)==len(F4)
        cases+=1
    direct=0
    for b,m,power in [(3,3,10),(3,4,10),(3,5,10),(3,6,10),
                       (4,3,8),(4,4,8),(4,5,8),(4,6,8),
                       (5,3,7),(5,4,7),(5,5,7),(6,3,6),(6,4,6)]:
      N=b**power
      ss=[0]*N
      for i in range(1,N):ss[i]=ss[i//b]+i%b
      w=bytes(x%m for x in ss)
      for n in (2,3,4):
        observed={tuple(w[i:i+n]) for i in range(N-n+1)}
        predicted=pairs(b,m) if n==2 else factors_small(b,m,n)
        assert observed==predicted,(b,m,n,len(observed),len(predicted))
        direct+=1
      for n in (5,6,7,8):
        obs={tuple(w[i:i+n]) for i in range(N-n+1)}
        assert all(t[::-1] not in obs for t in obs),(b,m,n)
    print('GENERALIZED_BASE_REFLECTION_PASS symbolic_cases=',cases,'exact_finite_factor_tests=',direct,
          'direct_bases=3..6','direct_lengths=2..8')

if __name__=='__main__':test()
