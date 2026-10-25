"""Exact finite checks for random-map colour-rigidity critical window.

Python 3, no dependencies. Run: python verify_colored_mapping.py
"""
from itertools import product, permutations
from math import comb, exp
from fractions import Fraction
import random


def leaf_twin_count(f, colors):
    n=len(f)
    indeg=[0]*n
    for y in f: indeg[y]+=1
    return sum(indeg[x]==0 and indeg[y]==0 and f[x]==f[y] and colors[x]==colors[y]
               for x in range(n) for y in range(x+1,n))


def leaf_twins(f, colors):
    n=len(f)
    indeg=[0]*n
    for y in f: indeg[y]+=1
    for x in range(n):
        if indeg[x]: continue
        for y in range(x+1,n):
            if indeg[y]==0 and f[x]==f[y] and colors[x]==colors[y]:
                return True
    return False


def is_rigid_exact(f, colors):
    n=len(f)
    for p in permutations(range(n)):
        if all(p[i]==i for i in range(n)):
            continue
        if all(colors[p[i]]==colors[i] and f[p[i]]==p[f[i]] for i in range(n)):
            return False
    return True


def expected_twins_formula(n, k):
    if n<3: return 0.0
    return comb(n,2)*(n-2)/n**2*((n-2)/n)**(n-2)/k


def check_small():
    # Exhaustively check the predicate and the complete automorphism group.
    for n,k in ((2,2),(3,3),(4,3)):
        total=rigid=twins=twins_nonrigid=pair_sum=0
        for f in product(range(n),repeat=n):
            for colors in product(range(k),repeat=n):
                total+=1
                t=leaf_twins(f,colors)
                pair_sum+=leaf_twin_count(f,colors)
                r=is_rigid_exact(f,colors)
                rigid+=r
                twins+=t
                twins_nonrigid+=t and not r
                assert not (t and r)
        assert twins==twins_nonrigid
        if n>=3:
            expected=Fraction(comb(n,2)*(n-2),n*n*k)*Fraction(n-2,n)**(n-2)
            assert Fraction(pair_sum,total)==expected, (n,k, pair_sum,total,expected)
        p=twins/total
        e=expected_twins_formula(n,k)
        print('EXACT',n,k,'models',total,'rigid',rigid,'twin_probability',round(p,8),'E_X',round(e,8))


def monte_carlo():
    rng=random.Random(0x305E2026)
    for n,trials in ((100,3000),(300,1500),(1000,1000)):
        k=n
        no_twins=0
        for _ in range(trials):
            f=[rng.randrange(n) for j in range(n)]
            colors=[rng.randrange(k) for j in range(n)]
            no_twins+=not leaf_twins(f,colors)
        target=exp(-exp(-2)/2)
        print('SAMPLE',n,'no_twins',round(no_twins/trials,5),'limit',round(target,5))


if __name__=='__main__':
    check_small()
    monte_carlo()
    print('COLOURED_RANDOM_MAP_RIGIDITY_OK')
