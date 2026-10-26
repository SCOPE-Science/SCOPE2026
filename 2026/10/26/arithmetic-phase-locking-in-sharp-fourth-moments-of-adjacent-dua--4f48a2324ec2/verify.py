#!/usr/bin/env python3
"""Alternative exact Weyl-torus checks for paired SU(3) character moments.

Uses Python standard library only. The exact torus computations check finitely
many degrees; representation-theoretic arguments prove the all-degree theorem.
"""
import cmath
import math
from collections import defaultdict
from functools import lru_cache


def product(a, b):
    out = defaultdict(int)
    for (p, q), x in a.items():
        for (r, s), y in b.items():
            out[p+r, q+s] += x*y
    return dict(out)


def conjugate(a):
    return {(-p, -q): x for (p, q), x in a.items()}


@lru_cache(maxsize=None)
def symmetric_character(degree):
    # x_3=(x_1 x_2)^{-1}; complete homogeneous polynomial h_degree.
    out = defaultdict(int)
    for i in range(degree+1):
        for j in range(degree-i+1):
            k = degree-i-j
            out[i-k, j-k] += 1
    return dict(out)


IDENTITY = {(0, 0): 1}
VANDERMONDE = IDENTITY
for alpha, beta in ((1, -1), (2, 1), (1, 2)):
    VANDERMONDE = product(VANDERMONDE, {(0, 0): 1, (alpha, beta): -1})
    VANDERMONDE = product(VANDERMONDE, {(0, 0): 1, (-alpha, -beta): -1})


def exact_haar(characters):
    pol = IDENTITY
    for c in characters:
        pol = product(pol, c)
    numerator = sum(m * VANDERMONDE.get((-p, -q), 0)
                    for (p, q), m in pol.items())
    assert numerator % 6 == 0
    return numerator // 6


def q_formula(n, a, b):
    u, v = abs(a)**2, abs(b)**2
    cross = a * b.conjugate()
    result = (n+1)*u*u + (n+2)*v*v + 4*(n+1)*u*v
    if n % 3 == 1:
        result += 4*(u+v)*cross.real + 2*(cross*cross).real
    return result


def bisect_root(fun, lo, hi, steps=100):
    assert fun(lo) * fun(hi) < 0
    for _ in range(steps):
        mid = (lo + hi)/2
        if fun(mid) * fun(lo) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi)/2


def resonance_extrema(n):
    assert n % 3 == 1
    f_plus = lambda t: t**4 + (n+2)*t**3 - (n+1)*t - 1
    f_minus = lambda t: t**4 - (n+2)*t**3 + (n+1)*t - 1
    top = bisect_root(f_plus, 0, 1)
    low = bisect_root(f_minus, 1, n+4)
    return ((top, q_formula(n, top, 1)/(1+top*top)**2),
            (low, q_formula(n, -low, 1)/(1+low*low)**2))


def main():
    assertions = 0
    assert exact_haar([]) == 1
    assertions += 1
    for n in range(1, 10):
        x = symmetric_character(n)
        y = symmetric_character(n+1)
        vals = (
            exact_haar((x, x, conjugate(x), conjugate(x))),
            exact_haar((y, y, conjugate(y), conjugate(y))),
            exact_haar((x, y, conjugate(x), conjugate(y))),
            exact_haar((x, x, y, y)),
            exact_haar((x, x, y, conjugate(x))),
            exact_haar((y, y, x, conjugate(y))),
        )
        delta = int(n % 3 == 1)
        expected = (n+1, n+2, n+1, delta, delta, delta)
        assert vals == expected, (n, vals, expected)
        assertions += 6

    for n in range(1, 18):
        if n % 3 != 1:
            u = n/(2*n+1)
            qmax = n+2+n*n/(2*n+1)
            assert abs(q_formula(n, math.sqrt(u), math.sqrt(1-u))-qmax) < 1e-9
            assert abs(q_formula(n, 1, 0)-(n+1)) < 1e-9
            assertions += 2
        else:
            (tp, top), (tm, low) = resonance_extrema(n)
            assert 0 < tp < 1 < tm
            assert low < n+1 < top
            # The two first-order equations are independent of numerical optimization.
            assert abs(tp**4+(n+2)*tp**3-(n+1)*tp-1) < 1e-9
            assert abs(tm**4-(n+2)*tm**3+(n+1)*tm-1) < 1e-8
            assertions += 4
            for j in range(101):
                u = j/100
                for phase in (0, 0.37, 1.2, math.pi, 4.7):
                    a = math.sqrt(u)*cmath.exp(1j*phase)
                    b = math.sqrt(1-u)
                    score = q_formula(n, a, b)
                    assert low-1e-9 <= score <= top+1e-9, (n,u,phase,score,low,top)
                    assertions += 1
    for n in range(1, 50, 3):
        (tp, top), _ = resonance_extrema(n)
        nonres_next = (n+1)+2+(n+1)**2/(2*(n+1)+1)
        assert top > nonres_next
        assertions += 1
    print(f"ALL_CHECKS_PASSED assertions={assertions}")
    print("Weyl exact moments: n=1..9. Quantitative extremum grid: n=1..16.")
    print("Finite checks do not substitute for the all-degree Pieri proof.")


if __name__ == '__main__':
    main()
