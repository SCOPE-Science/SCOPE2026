"""Exact checks of stationary Moran-forest two-component probabilities.
Python 3 standard library only. Independent-parent enumeration, no simulation.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial


def exhaustive(n):
    counts = Counter()
    possibilities = [[v for v in range(1,n+1) if v != j] for j in range(1,n+1)]
    for choices in product(*possibilities):
        root = list(range(n+1))
        def find(u):
            while root[u] != u:
                u = root[u]
            return u
        for j,u in enumerate(choices,1):
            if u < j:
                root[find(j)] = find(u)
        sizes=Counter(find(j) for j in range(1,n+1))
        shape=tuple(sorted(Counter(sizes.values()).elements()))
        counts[shape] += 1
    return counts


def partition_probability(n,a,b):
    assert a+b==n and a>=1 and b>=1
    return Fraction(factorial(a-1)*factorial(b-1)*(n*n-1)*(a*b-1),
                    (n-1)**n*(a+1)*(b+1))


def harmonic(m):
    return sum((Fraction(1,j) for j in range(1,m+1)),Fraction(0))


def probability_n2(n):
    return Fraction(factorial(n-2),(n-1)**(n-2))*((n-1)*harmonic(n-2)-(n-2))


def check():
    for n in range(3,8):
        counts=exhaustive(n)
        den=(n-1)**n
        total=Fraction(0)
        for s in range(1,n//2+1):
            b=n-s
            how_many=Fraction(comb(n,s),2 if s==b else 1)
            theoretical=how_many*partition_probability(n,s,b)
            observed=Fraction(counts[(s,b)],den)
            assert theoretical==observed, (n,s,theoretical,observed)
            total+=theoretical
        assert total==probability_n2(n), (n,total,probability_n2(n))
        print('EXHAUSTIVE_UA_PASS n=',n,'assignments=',den,'two_tree_probability=',total)
    for n in range(3,101):
        total=sum((Fraction(comb(n,s),2 if s==n-s else 1)*partition_probability(n,s,n-s) for s in range(1,n//2+1)),Fraction(0))
        assert total == probability_n2(n)
    print('EXACT_NORMALIZATION_PASS n=3..100')
    print('VERIFY_OK')

if __name__=='__main__':
    check()
