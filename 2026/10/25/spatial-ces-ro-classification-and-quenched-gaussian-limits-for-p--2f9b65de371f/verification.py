"""Finite exact checks for the Pascal-sign correlation bound and renewal identity.

The infinite classification is established analytically, not by these finite checks.
"""
from fractions import Fraction
from itertools import product
from math import comb
import random


def signs(beta):
    return [(-1)**sum(((comb(s,k)&1)*beta[k]) for k in range(s+1))
            for s in range(len(beta))]


def popcount(n):
    return n.bit_count()


def pair_expectation(s,t,parameters):
    p=Fraction(1)
    for k in range(t+1):
        if (comb(s,k) if k<=s else 0)&1 != (comb(t,k)&1):
            p*=1-2*parameters[k]
    return p


def test():
    count=0
    # Invertibility of the triangular Pascal parity transform; every sign word
    # occurs exactly once as beta runs over all binary coefficient words.
    for dimension in range(1,9):
        words={tuple(signs(bits)) for bits in product((0,1),repeat=dimension)}
        assert len(words)==2**dimension
        count+=len(words)
    # Exact Lucas differing-mask bound, including nonpower-of-two endpoints.
    for t in range(1,193):
        expected=2**(popcount(t)-1)
        for s in range(t):
            differing=sum(1 for k in range(t+1)
                          if ((comb(t,k)&1) != (bool(k<=s and comb(s,k)&1))))
            assert differing>=expected,(s,t,differing,expected)
            count+=1
    # Independently compute the random-beta pair correlations by enumerating
    # all coefficient assignments and compare with the exact product formula.
    n=7
    parameters=[Fraction(k+2,k+5) for k in range(n)]
    for s in range(n):
        for t in range(s+1,n):
            val=Fraction(0)
            for bits in product((0,1),repeat=n):
                weight=Fraction(1)
                for k,b in enumerate(bits):
                    weight*=parameters[k] if b else (1-parameters[k])
                fs=signs(bits)
                val+=weight*fs[s]*fs[t]
            assert val==pair_expectation(s,t,parameters),(s,t,val)
            count+=1
    # Renewal occupation decomposition: for a single path, each complete
    # level's occupancy is its geometric holding time; the final level is partial.
    rng=random.Random(841722)
    for trial in range(50):
        n=10000
        xi=[-1 if rng.getrandbits(1) else 1 for _ in range(n)]
        m=0
        occ=[0]*(n+1)
        signed=0
        f=lambda z: 1 if z%7 in (0,1,3) else -1
        for x in xi:
            occ[m]+=1
            signed+=f(m)
            if x==-1: m+=1
        assert signed==sum(occ[s]*f(s) for s in range(m+1))
        assert abs(signed/n-sum(f(s) for s in range(n//2))/(n//2))<0.12
        count+=1
    return count

if __name__=='__main__':
    print('PASS:',test(),'finite exact or path checks')
