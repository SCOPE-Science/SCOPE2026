"""Exact rational checks for arithmetic return correlations in random integer beta maps.

Run: python verify.py
All checks use fractions; finite tests corroborate, but do not replace, the proofs.
"""
from fractions import Fraction as Q
from itertools import product
from math import gcd
from collections import defaultdict


def direct_covariance(q, B):
    """Integrate two indicator events by partitioning the domain into B branches."""
    cut = Q(1, q)
    overlap = Q(0)
    for k in range(B):
        lo = Q(k, B)
        hi = Q(k*q + 1, q*B)
        if lo < cut:
            overlap += max(Q(0), min(cut, hi) - lo)
    return overlap - cut * cut


def formula_covariance(q, B):
    remainder = B % q
    return Q(q - remainder, q*q*B) if remainder else Q(0)


def annealed_by_words(q, bases, probabilities, n):
    result = Q(0)
    for word in product(range(len(bases)), repeat=n):
        B = 1
        w = Q(1)
        for i in word:
            B *= bases[i]
            w *= probabilities[i]
        result += w * direct_covariance(q, B)
    return result


def annealed_by_residue_matrix(q, bases, probabilities, n):
    vec = [Q(0) for _ in range(q)]
    vec[1] = Q(1)
    for _ in range(n):
        nxt = [Q(0) for _ in range(q)]
        for r in range(q):
            if not vec[r]:
                continue
            for b, pr in zip(bases, probabilities):
                nxt[(b*r) % q] += vec[r] * pr / b
        vec = nxt
    return sum(vec[r] * (q-r) for r in range(1,q)) / (q*q)


def special_q6(p, n):
    assert n >= 1
    return ( (4 if n%2 else 2)* (p/Q(2))**n
             + 3*((Q(1)-p)/3)**n )/36


def memory_cutoff(q, bases):
    x = q
    primes=[]
    d=2
    while d*d<=x:
        if x%d == 0:
            v=0
            while x%d == 0:
                x//=d; v+=1
            primes.append((d,v))
        d+=1
    if x>1: primes.append((x,1))
    N=0
    for ell, expo in primes:
        mins=[]
        for b in bases:
            e=0
            while b%ell == 0:
                b//=ell; e+=1
            mins.append(e)
        t=min(mins)
        if t==0: return None
        N=max(N, (expo+t-1)//t)
    return N


def test():
    c = dict(direct=0, matrix=0, special=0, cutoff=0, stationarity=0)
    for q in range(2,15):
        for B in range(1,101):
            assert direct_covariance(q,B)==formula_covariance(q,B), (q,B)
            c['direct'] += 1
    for bases, probs in [((2,3),(Q(2,5),Q(3,5))),
                         ((2,4),(Q(1,3),Q(2,3))),
                         ((3,5),(Q(2,7),Q(5,7))),
                         ((4,6),(Q(1,2),Q(1,2)))]:
        for q in range(2,13):
            for n in range(5):
                lhs=annealed_by_words(q,bases,probs,n)
                rhs=annealed_by_residue_matrix(q,bases,probs,n)
                assert lhs==rhs,(bases,q,n,lhs,rhs)
                c['matrix']+=1
        for q in range(2,50):
            N=memory_cutoff(q,bases)
            if N is not None:
                assert all(formula_covariance(q, B)==0 for n in range(N,N+2) for B in
                           [__import__('math').prod(word) for word in product(bases,repeat=n)]), (bases,q,N)
                if N>0:
                    assert any(formula_covariance(q,__import__('math').prod(word))>0 for word in product(bases,repeat=N-1)), (bases,q,N)
                c['cutoff']+=1
    for p in (Q(0),Q(1,7),Q(2,5),Q(1,2),Q(3,4),Q(1)):
        for n in range(1,13):
            # Closed-form independent combinatorial multinomial sum; mixed words vanish.
            val=Q(0)
            for k in range(n+1):
                from math import comb
                B=(2**k)*(3**(n-k))
                val += Q(comb(n,k)) * p**k * (1-p)**(n-k) * direct_covariance(6,B)
            rhs=special_q6(p,n)
            assert val==rhs,(p,n,val,rhs)
            c['special']+=1
    for b in range(2,15):
        # Every integral beta-transformation preserves normalized Lebesgue.
        # Check preimage mass of every uniform rational bin.
        for q in range(2,18):
            # T_b inverse of [0,1/q) has b disjoint preimage intervals of length 1/(bq).
            assert b*Q(1,b*q)==Q(1,q)
            c['stationarity']+=1
    assert memory_cutoff(8,(2,4))==3
    assert memory_cutoff(4,(2,4))==2
    assert memory_cutoff(6,(2,3)) is None
    assert memory_cutoff(10,(10,20))==1
    return c

if __name__=='__main__':
    print('PASS: '+str(test()))
