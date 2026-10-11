"""Numerical finite-instance checks for four-node cyclic Fourier determinants.

This file is independent of the all-moduli proof. Run:
    python3 verify.py
It uses only Python's standard library. Floating-point comparisons are
consistency checks, not certificates of an infinite theorem.
"""
from cmath import exp, pi
from itertools import combinations, permutations
from math import cos, sin, gcd


def direct_det_modulus(n, b):
    z = [exp(2j * pi * k / n) for k in b]
    # Independent Leibniz expansion of the 4x4 character matrix.
    s = 0j
    for p in permutations(range(4)):
        inv = sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4))
        v = 1 + 0j
        for t in range(4):
            v *= z[p[t]] ** t
        s += (-1 if inv % 2 else 1) * v
    return abs(s)


def chord_formula(n, b):
    p = [b[1]-b[0], b[2]-b[1], b[3]-b[2], n+b[0]-b[3]]
    a,c = p[0],p[2]
    return 64.0 * (sin(pi*p[0]/n)*sin(pi*p[1]/n)*
                   sin(pi*p[2]/n)*sin(pi*p[3]/n)*
                   sin(pi*(p[0]+p[1])/n)*sin(pi*(p[1]+p[2])/n))


def optimum(n):
    q, r = divmod(n, 4)
    if r == 0: return 16.0
    if r == 2: return 16.0 * cos(pi/n)**2
    h = cos(pi/(2*n))**2
    if r == 1:
        return 64.0 * sin(pi*q/n)**3 * sin(pi*(q+1)/n) * h
    return 64.0 * sin(pi*q/n) * sin(pi*(q+1)/n)**3 * h


def predicted_best(n, b):
    a = [b[1]-b[0], b[2]-b[1], b[3]-b[2], n+b[0]-b[3]]
    q, r = divmod(n, 4)
    return (
        all(x == q for x in a) if r == 0 else
        sorted(a) == [q, q, q, q+1] if r == 1 else
        a in ([q, q+1, q, q+1], [q+1, q, q+1, q]) if r == 2 else
        sorted(a) == [q, q+1, q+1, q+1]
    )


def main():
    # Fixing one point at 0 removes translation repetitions, not any shapes.
    # To count sets globally, enumerate all four-subsets; small N suffices.
    total = 0
    for n in range(4, 25):
        expected = optimum(n)
        best = 0.0
        actual_sets = []
        for b in combinations(range(n), 4):
            d = direct_det_modulus(n, b)
            c = chord_formula(n, b)
            assert abs(d-c) < 3e-10, (n, b, d, c)
            assert d <= expected + 3e-10, (n, b, d, expected)
            good = abs(d-expected) < 3e-10
            assert good == predicted_best(n, b), (n, b, d, expected)
            if good: actual_sets.append(b)
            if d > best: best = d
            total += 1
        assert abs(best-expected) < 3e-10
        assert len(actual_sets) == n // gcd(n,4), (n,len(actual_sets))
        print('N=%d maximum=%.12g optimizers=%d' % (n, best, len(actual_sets)))
    print('CHECK_OK', total)


if __name__ == '__main__':
    main()
