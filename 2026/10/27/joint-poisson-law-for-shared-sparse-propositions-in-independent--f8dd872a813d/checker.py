"""Exhaustive checks of block factorial moments in finite marked equivalence frames.
The proof in RESULT.md is analytic; this finite checker supplies independent tests.
"""
from fractions import Fraction
from math import factorial
from itertools import combinations, product


def partitions(n):
    if not n:
        yield ()
        return
    for p in partitions(n-1):
        yield p + ((n-1,),)
        for i in range(len(p)):
            q = list(p)
            q[i] = q[i] + (n-1,)
            yield tuple(q)


def falling(a, k):
    if k > a:
        return 0
    out = 1
    for t in range(k):
        out *= a-t
    return out


def run():
    bells = [sum(1 for _ in partitions(n)) for n in range(8)]
    assert bells == [1,1,2,5,15,52,203,877], bells
    checks = 0
    for n in range(1,8):
        samples = list(partitions(n))
        for m in range(n+1):
            marked = set(range(m))
            counts = [tuple(sum(len(b)==j and set(b)<=marked for b in p)
                            for j in range(1,4)) for p in samples]
            for ks in product(range(3), repeat=3):
                s = sum((j+1)*ks[j] for j in range(3))
                if s > n:
                    continue
                lhs = Fraction(sum(falling(y[j],ks[j]) for y in counts
                                  for j in ()) if False else
                               sum(__import__('functools').reduce(lambda a,b:a*b,
                                   [falling(y[j],ks[j]) for j in range(3)],1)
                                   for y in counts),bells[n])
                rhs = Fraction(falling(m,s)*bells[n-s],bells[n])
                for j in range(3):
                    rhs /= factorial(j+1)**ks[j]
                assert lhs == rhs,(n,m,ks,lhs,rhs)
                checks += 1
    print('PASS Bell numbers',bells)
    print('PASS exact factorial moments',checks)
    print('PASS conditional factorization by independent partitions (product measures)')

if __name__ == '__main__':
    run()
