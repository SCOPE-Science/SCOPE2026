#!/usr/bin/env python3
"""Exact-integer checks for the bilinear-forms spectrum used in RESULT.md."""

from fractions import Fraction


def qbinom(n, k, q):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    num = 1
    den = 1
    for i in range(k):
        num *= q ** (n - i) - 1
        den *= q ** (k - i) - 1
    assert num % den == 0
    return num // den


def rank_count(d, e, r, q):
    if r == 0:
        return 1
    num = 1
    den = 1
    for j in range(r):
        num *= (q ** d - q ** j) * (q ** e - q ** j)
        den *= q ** r - q ** j
    assert num % den == 0
    return num // den


def bilinear_eigenvalue(d, e, j, i, q):
    total = 0
    for h in range(j + 1):
        if h > d - i:
            continue
        total += ((-1) ** (j - h)
                  * q ** (e * h + (j - h) * (j - h - 1) // 2)
                  * qbinom(d - h, d - j, q)
                  * qbinom(d - i, h, q))
    return total


def optimum(d, e, r, q):
    return Fraction(
        q ** (d + e - r) - q ** d - q ** e + 1,
        (q ** d - 1) * (q ** e - 1),
    )


def check_family(q, d, e, r):
    count = rank_count(d, e, r, q)
    vals = [Fraction(bilinear_eigenvalue(d, e, r, s, q), count)
            for s in range(d + 1)]
    assert vals[0] == 1
    assert vals[1] == optimum(d, e, r, q)
    assert vals[1] > 0
    for s in range(2, d + 1):
        assert abs(vals[s]) < vals[1]
    assert optimum(d, e, r, q) < Fraction(1, q ** r)


def main():
    tested = 0
    for q in (3, 4, 5, 7):
        for d in range(2, 9):
            for e in range(d, d + 4):
                for r in range(1, d):
                    check_family(q, d, e, r)
                    tested += 1
    for d in range(2, 9):
        for e in range(d + 1, d + 4):
            for r in range(1, d):
                check_family(2, d, e, r)
                tested += 1

    # The excluded binary-square regime is genuinely different: for rank d-1,
    # rank-one frequency need not maximize the shell Fourier magnitude.
    q, d, e, r = 2, 3, 3, 2
    count = rank_count(d, e, r, q)
    shell = [Fraction(abs(bilinear_eigenvalue(d, e, r, s, q)), count)
             for s in range(1, d + 1)]
    assert shell[2] > shell[0]

    print(f"PASS: {tested} eligible parameter tuples checked exactly")
    print("PASS: rank-one coefficient equals the stated minimax value")
    print("PASS: all tested nontrivial higher-rank Fourier magnitudes are smaller")
    print("PASS: the stated value is strictly below q^{-r}")
    print("PASS: binary square (d,e,r)=(3,3,2) exhibits the excluded spectral exception")


if __name__ == "__main__":
    main()
