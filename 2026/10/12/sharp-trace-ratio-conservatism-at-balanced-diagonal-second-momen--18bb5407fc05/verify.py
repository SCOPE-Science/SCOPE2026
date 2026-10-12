"""Exact arithmetic spot checks for a sharp diagonal trace-ratio bound.

This program checks only finite samples and equality examples; the proof is analytic.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def ratio(values):
    n = len(values)
    mean = sum(values) / n
    inv1 = sum(1 / x for x in values)
    inv2 = sum(1 / (x * x) for x in values)
    return mean * inv2 / inv1


def sharp_for_integer_root(root):
    k = root * root
    return F((k - root + 1) ** 2, k)


def verify():
    checked = 0
    for t in (1, 2, 3, 4, 5, 7, 10, 20):
        k = t * t
        cap = sharp_for_integer_root(t)
        witness = [F(1)] + [F(k)] * t
        assert ratio(witness) == cap, (t, ratio(witness), cap)
        for n in range(1, 6):
            grid = sorted({F(1), F(k), F(t), F(k + 3, 4), F(3*k + 1, 4)})
            grid = [x for x in grid if 1 <= x <= k]
            for vals in product(grid, repeat=n):
                if min(vals) == max(vals):
                    assert ratio(vals) == 1
                assert 1 <= ratio(vals) <= cap, (vals, cap)
                checked += 1
    rng = Random(260512878)
    for t in range(2, 35):
        k = t*t
        cap = sharp_for_integer_root(t)
        for _ in range(220):
            n=rng.randrange(1,45)
            values=[F(rng.randrange(1,12*k+1), 12) for _ in range(n)]
            values=[min(F(k),max(F(1),x)) for x in values]
            assert 1 <= ratio(values) <= cap
            checked += 1
    # A frozen expected preconditioner update at gamma*s_i = p_i^2.
    for t in (2, 3, 10):
        p=[F(1)]+[F(t*t)]*t
        gamma=F(2,3)
        s=[x*x/gamma for x in p]
        alpha=F(3,5)
        updated=[(x+alpha*gamma*si/x)/(1+alpha) for x,si in zip(p,s)]
        assert updated == p
        q=sum(si/x for x,si in zip(p,s))/sum(si/x**2 for x,si in zip(p,s))
        assert q == sum(p)/len(p)
        assert q / (sum(1/x for x in p)/sum(1/x**2 for x in p)) == sharp_for_integer_root(t)
    print('VERIFY_OK checked_examples=',checked,'exact_equality_families=8','stationary_examples=3')


if __name__ == '__main__':
    verify()
