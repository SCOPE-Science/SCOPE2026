#!/usr/bin/env python3
from fractions import Fraction
import random

def ebh(values, alpha):
    K = len(values)
    order = sorted(range(K), key=lambda i: values[i], reverse=True)
    kstar = 0
    for k in range(1, K + 1):
        if values[order[k-1]] >= Fraction(K, 1) / (alpha * k):
            kstar = k
    if kstar == 0:
        return set()
    cutoff = Fraction(K, 1) / (alpha * kstar)
    return {i for i, v in enumerate(values) if v >= cutoff}

def check():
    rng = random.Random(310043)
    alphas = [Fraction(1, 20), Fraction(1, 10), Fraction(1, 5), Fraction(1, 2)]
    for K in range(2, 11):
        for alpha in alphas:
            for r in range(1, K + 1):
                c = Fraction(K, 1) / (alpha * r)
                old = [c] * r + [Fraction(0)] * (K-r)
                R = ebh(old, alpha)
                assert R == set(range(r)), (K, alpha, r, R)

                # Sharp one-coordinate failure for every b<c tested.
                b = c * Fraction(999, 1000)
                nxt = old[:]
                nxt[0] = b
                assert ebh(nxt, alpha) == set(), (K, alpha, r, ebh(nxt, alpha))

                # Persistence under arbitrary outsider values when old rejections keep the floor.
                for _ in range(50):
                    vals = [c + Fraction(rng.randrange(0, 1000), 100)] * r
                    vals += [Fraction(rng.randrange(0, 20000), 100) for _ in range(K-r)]
                    R2 = ebh(vals, alpha)
                    assert set(range(r)).issubset(R2), (K, alpha, r, vals, R2)

                # Affine expectation check for two-point factors with mean <= 1.
                e = c + Fraction(7, 3)
                for p in [Fraction(1,4), Fraction(1,2), Fraction(3,4)]:
                    x0 = Fraction(0)
                    x1 = Fraction(1, p.denominator) / p  # equals 1/p.denominator divided by p
                    # Rescale if necessary to guarantee mean <= 1.
                    mean = p * x1 + (1-p) * x0
                    assert mean <= 1
                    expected = c + (e-c) * mean
                    assert expected <= e
                    assert c + (e-c) * x0 >= c
                    assert c + (e-c) * x1 >= c
    print('VERIFY_OK')

if __name__ == '__main__':
    check()
