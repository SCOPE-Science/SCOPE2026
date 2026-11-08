"""Exact finite checks for mutual-dyad / oriented-triangle covariance.

Run with Python 3 standard library: python verify_covariance.py
Only finite instances are checked; the general proof is in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb


def theoretical(n, k, self_loops):
    s = n if self_loops else n - 1
    p = Fraction(k, s)
    q = 1 - p
    return (n * (n - 2) * p**3 * q * (2 * p - 1) if self_loops
            else -n * (n - 1) * p**3 * q**2)


def pair_expansion(n, k, self_loops):
    s = n if self_loops else n - 1
    p = Fraction(k, s)
    r = Fraction(k * (k - 1), s * (s - 1))
    a = n * (n - 1) * (n - 2)
    b = a * (n - 3)
    return a * p**2 * (r - p**3) + b * p**3 * (r - p**2)


def enumerate_graphs(n, k, self_loops):
    options = []
    for u in range(n):
        eligible = [v for v in range(n) if self_loops or v != u]
        options.append([sum(1 << v for v in target)
                        for target in combinations(eligible, k)])
    sr = st = srt = total = 0
    for rows in product(*options):
        total += 1
        r = sum(bool(rows[u] & (1 << v)) and bool(rows[v] & (1 << u))
                for u in range(n) for v in range(u + 1, n))
        t3 = sum(bool(rows[u] & (1 << v)) and
                 bool(rows[v] & (1 << w)) and
                 bool(rows[w] & (1 << u))
                 for u in range(n) for v in range(n) for w in range(n)
                 if len({u, v, w}) == 3)
        assert t3 % 3 == 0
        t = t3 // 3
        sr += r
        st += t
        srt += r * t
    return total, Fraction(sr, total), Fraction(st, total), (
        Fraction(srt, total) - Fraction(sr * st, total**2))


def main():
    algebra = enumerated = cases = 0
    for n in range(3, 31):
        for loops in (False, True):
            s = n if loops else n - 1
            for k in range(s + 1):
                assert theoretical(n, k, loops) == pair_expansion(n, k, loops)
                algebra += 1
    for n in (3, 4, 5):
        for loops in (False, True):
            s = n if loops else n - 1
            for k in range(s + 1):
                if comb(s, k)**n > 100000:
                    continue
                size, er, et, cov = enumerate_graphs(n, k, loops)
                p = Fraction(k, s)
                assert er == comb(n, 2) * p**2
                assert et == (n * (n - 1) * (n - 2) // 3) * p**3
                assert cov == theoretical(n, k, loops)
                enumerated += size
                cases += 1
    print(f"PASS: {algebra} exact algebraic parameter tests, "
          f"{cases} exhaustively enumerated parameter cases, "
          f"{enumerated} distinct labeled directed graphs checked.")


if __name__ == '__main__':
    main()
