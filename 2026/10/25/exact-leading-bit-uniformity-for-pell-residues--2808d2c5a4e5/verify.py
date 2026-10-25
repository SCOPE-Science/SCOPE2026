#!/usr/bin/env python3
"""Finite consistency checks for the Pell leading-bit distribution theorem."""

def valuation2(x):
    x = abs(x)
    if x == 0:
        raise ValueError("valuation of zero is not used in this check")
    return (x & -x).bit_length() - 1


def pell_residues(k):
    modulus = 1 << k
    a, b = 0, 1
    out = []
    for _ in range(modulus):
        out.append(a)
        a, b = b, (a + 2 * b) % modulus
    return out


def pell_exact(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n):
        a, b = b, 2 * b + a
    return a


def main():
    distribution_checks = 0
    indices_checked = 0
    for k in range(3, 11):
        vals = pell_residues(k)
        indices_checked += len(vals)
        for r in range(1, k - 1):
            counts = [0] * (1 << r)
            for x in vals:
                counts[x >> (k - r)] += 1
            assert counts == [1 << (k - r)] * (1 << r), (k, r, counts)
            distribution_checks += 1

    valuation_checks = 0
    pell = [pell_exact(n) for n in range(0, 800)]
    for n in range(64):
        for s in range(2, 8):
            for u in (1, 3, 5):
                d = (1 << s) * u
                assert valuation2(pell[n + d] - pell[n]) == s, (n, s, u)
                valuation_checks += 1

    # Boundary example: modulo 16, the top three bits are not uniform.
    vals = pell_residues(4)
    bins = [0] * 8
    for x in vals:
        bins[x >> 1] += 1
    assert bins == [3, 1, 3, 1, 3, 1, 3, 1], bins
    print(f"VERIFY_OK distribution_checks={distribution_checks} indices_checked={indices_checked} valuation_checks={valuation_checks} boundary_bins={bins}")


if __name__ == "__main__":
    main()
