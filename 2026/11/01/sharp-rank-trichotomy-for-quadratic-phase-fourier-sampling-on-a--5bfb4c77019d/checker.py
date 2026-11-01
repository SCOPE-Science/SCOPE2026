"""Independent finite sanity checks for a quadratic-phase Fourier matrix.

Run with: python checker.py
Requires: numpy
The infinite-prime assertion is proved algebraically in RESULT.md, not by these tests.
"""
from math import isqrt
import numpy as np


def isprime(n):
    if n < 2: return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def expected(p, a, b):
    return p if a % p else ((p + 1) // 2 if b % p else 1)


def matrix(p, a, b):
    z = np.exp(2j * np.pi / p)
    return np.array([[z ** ((a*s*t + b*s*s*t*t) % p)
                      for t in range(p)] for s in range(p)], dtype=complex)


def unique_nonzero_fiber(p, a, b):
    if a % p == 0: return False
    if b % p:
        u = (-a * pow(2*b, -1, p)) % p
        v = (-a*a * pow(4*b, -1, p)) % p
    else:
        u, v = 1, a % p
    return (u != 0 and v != 0 and
            sum(1 for x in range(1, p)
                if (a*x+b*x*x) % p == v) == 1 and
            (a*u+b*u*u) % p == v)


def run():
    cases = 0
    for p in (3, 5, 7, 11, 13, 17, 19):
        assert isprime(p)
        pairs = ((a,b) for a in range(p) for b in range(p)) if p <= 11 else ((0,0),(0,1),(1,0),(1,1),(2,1),(1,2))
        for a,b in pairs:
            if a:
                assert unique_nonzero_fiber(p, a, b), (p,a,b)
            vals = np.linalg.svd(matrix(p,a,b), compute_uv=False)
            rank = sum(v > 1e-7 for v in vals)
            want = expected(p,a,b)
            assert rank == want, (p,a,b,rank,want,vals)
            cases += 1
        print(f"p={p}: all selected rank and singleton checks passed")
    print(f"ALL {cases} PARAMETER PAIRS PASSED; finite checks are not an infinite proof")

if __name__ == '__main__':
    run()
