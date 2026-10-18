#!/usr/bin/env python3
"""Exact independent finite checks of the prime-power Fourier triple-rank classification."""
import itertools
import math
import random
from collections import Counter


def vp(z, p, a):
    z %= p**a
    if not z:
        return a
    v = 0
    while z % p == 0:
        z //= p
        v += 1
    return v


def profile(T, p, a):
    vs = sorted(vp(x-y, p, a) for x, y in itertools.combinations(T, 2))
    assert vs[0] == vs[1]
    return (vs[0], vs[2])


def predicted_rank(X, Y, a):
    r,t = X
    s,u = Y
    if r+s >= a:
        return 1
    if t+s >= a or r+u >= a:
        return 2
    return 3


def reduce_cyclotomic(N, p, a, monomials):
    """Exact Z[X]/Phi_(p^a) reduction; monomials: (integer coeff, exponent)."""
    h = p**(a-1)
    coeff = [0] * ((p-1)*h)
    for sign, exponent in monomials:
        exponent %= N
        r = exponent % h
        top = exponent // h
        if top == p-1:
            for j in range(p-1):
                coeff[j*h + r] -= sign
        else:
            coeff[top*h+r] += sign
    return coeff


def exact_rank(R, C, p, a):
    N = p**a
    terms = []
    for perm in itertools.permutations(range(3)):
        sign = (-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        terms.append((sign, sum(R[i]*C[perm[i]] for i in range(3))))
    if any(reduce_cyclotomic(N,p,a,terms)):
        return 3
    for i,j in itertools.combinations(range(3),2):
        for k,l in itertools.combinations(range(3),2):
            if (R[i]-R[j])*(C[k]-C[l]) % N:
                return 2
    return 1


def weights(p,a):
    N=p**a
    w={}
    for r in range(a):
        w[(r,r)]=p**r * math.comb(p,3) * p**(3*(a-r-1))
        for t in range(r+1,a):
            w[(r,t)] = (N*(p-1)**2 * p**(2*a-r-t-2))//2
    return {t:n for t,n in w.items() if n}


def count_formula(p,a):
    w=weights(p,a)
    rank=Counter()
    for X,wx in w.items():
        for Y,wy in w.items():
            rank[predicted_rank(X,Y,a)]+=wx*wy
    assert sum(w.values()) == math.comb(p**a,3)
    assert sum(rank.values()) == math.comb(p**a,3)**2
    return rank


def run():
    rng = random.Random(20261014)
    allcases = [(2,2),(2,3),(2,4),(3,2)]
    for p,a in allcases:
        N = p**a
        triples = list(itertools.combinations(range(N),3))
        counted_profiles=Counter(profile(T,p,a) for T in triples)
        assert counted_profiles==weights(p,a),(p,a,counted_profiles,weights(p,a))
        measured=Counter()
        for R in triples:
            X=profile(R,p,a)
            for C in triples:
                predicted=predicted_rank(X,profile(C,p,a),a)
                observed=exact_rank(R,C,p,a)
                assert predicted==observed,(p,a,R,C,predicted,observed)
                measured[observed]+=1
        assert measured == count_formula(p,a)
        print('EXHAUSTIVE',p,a,N,len(triples)**2,dict(sorted(measured.items())))
    for p,a in [(3,3),(5,2),(2,5),(5,3),(7,2)]:
        N=p**a
        expected=count_formula(p,a)
        trials=40000
        for _ in range(trials):
            R=sorted(rng.sample(range(N),3))
            C=sorted(rng.sample(range(N),3))
            predicted=predicted_rank(profile(R,p,a),profile(C,p,a),a)
            observed=exact_rank(R,C,p,a)
            assert predicted==observed,(p,a,R,C,predicted,observed)
        if N<=27:
            counted_profiles=Counter(profile(T,p,a) for T in itertools.combinations(range(N),3))
            assert counted_profiles==weights(p,a)
        print('SAMPLED',p,a,N,trials,'rank_counts',dict(sorted(expected.items())))
    print('EXACT_VERIFY_OK')

if __name__=='__main__':
    run()
