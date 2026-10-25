#!/usr/bin/env python3
"""Independent exact-fraction checks of the finite prime-period tent-map formulas.

Usage: python3 verify_prime_tent.py
All checks use Python's exact Fraction arithmetic. The universal theorem is
proved separately and is not inferred from these finite computations.
"""
from fractions import Fraction

checks = 0


def check(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)


def tent(x):
    return 2*x if x <= Fraction(1, 2) else 2*(1-x)


def fixed_grid(n):
    N = 1 << n
    return [Fraction(j, N-1) if j % 2 == 0 else Fraction(j+1, N+1)
            for j in range(N)]


def period(x, max_period):
    y = x
    for k in range(1, max_period+1):
        y = tent(y)
        if y == x:
            return k
    return None


def radius(points):
    return max([points[0], 1-points[-1]] +
               [(b-a)/2 for a,b in zip(points, points[1:])])


def star(points):
    m = len(points)
    return max(max(Fraction(k, m)-x, x-Fraction(k-1, m))
               for k,x in enumerate(points, start=1))


def test_prime(p):
    N = 1 << p
    grid = fixed_grid(p)
    check(len(grid) == N, f'grid count p={p}')
    for j, x in enumerate(grid):
        check(Fraction(j, N) <= x <= Fraction(j+1, N), f'branch cell p={p}, j={j}')
        check(period(x, p) in (1, p), f'exact period divides prime p={p}, j={j}')
    points = [x for x in grid if period(x, p) == p]
    check(len(points) == N-2, f'primitive count p={p}')
    check(points[0] == Fraction(2, N+1), f'first point p={p}')
    check(len(set(points)) == len(points), f'no duplicate p={p}')
    d = Fraction(2, N+1)
    check(star(points) == d, f'star discrepancy p={p}')
    check(radius(points) == d, f'covering radius p={p}')
    check(max(points[i+1]-points[i] for i in range(len(points)-1)) ==
          (Fraction(2, N-1) if p >= 3 else Fraction(2, 5)),
          f'max interior gap p={p}')
    for k, x in enumerate(points, 1):
        check(Fraction(k, len(points))-x <= d, f'right tail p={p} k={k}')
        check(x-Fraction(k-1, len(points)) <= d, f'left tail p={p} k={k}')
    print(f'prime p={p:2d}, points={len(points):5d}, D*=W_infty=Haus={d}')


for p in [2, 3, 5, 7, 11, 13]:
    test_prime(p)

# Composite periods are deliberately outside the prime-only statement:
for n in [4, 6, 8]:
    x = fixed_grid(n)
    points = [y for y in x if period(y, n) == n]
    check(len(points) != 2**n-2, f'composite has smaller primitive count n={n}')
    print(f'composite n={n:2d}, primitive points={len(points):3d}, D*={star(points)}, Haus={radius(points)}')

print(f'{checks} exact assertions passed.')
