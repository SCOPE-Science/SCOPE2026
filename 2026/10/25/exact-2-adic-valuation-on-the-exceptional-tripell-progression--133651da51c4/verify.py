#!/usr/bin/env python3
"""Exact-arithmetic checks for the exceptional Tripell valuation formula."""


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def mmul_mod(a, b, modulus):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) % modulus
             for j in range(3)] for i in range(3)]


def mpow_mod(a, exponent, modulus):
    out = eye(3)
    while exponent:
        if exponent & 1:
            out = mmul_mod(out, a, modulus)
        a = mmul_mod(a, a, modulus)
        exponent >>= 1
    return out


def mv_mod(a, v, modulus):
    return [sum(a[i][j] * v[j] for j in range(3)) % modulus
            for i in range(3)]


def v2(x):
    if x == 0:
        return float("inf")
    return (x & -x).bit_length() - 1


def tripell_mod(n, modulus, m, v0):
    return mv_mod(mpow_mod(m, n, modulus), v0, modulus)[2]


def main():
    m = [[2, 1, 1], [1, 0, 0], [0, 1, 0]]
    ident = eye(3)
    v0 = [2, 1, 0]
    m7 = mpow_mod(m, 7, 2**16)
    assert m7 == [[545, 298, 214], [214, 117, 84], [84, 46, 33]]
    e = [[(m7[i][j] - ident[i][j]) // 2 for j in range(3)]
         for i in range(3)]
    e2 = mmul_mod(e, e, 2)
    fmod2 = [[(e[i][j] + e2[i][j]) % 2 for j in range(3)]
             for i in range(3)]
    assert fmod2 == [[1, 0, 1], [1, 1, 1], [1, 1, 0]]

    # The 2^9-step matrix lift and the odd coefficient that makes the
    # normalized exceptional progression a 2-adic isometry.
    nmat = mpow_mod(m, 1792, 2**10)
    assert nmat == [[513, 0, 512], [512, 513, 512], [512, 512, 1]]
    m1280_mod2 = mpow_mod(m, 1280, 2)
    assert m1280_mod2 == [[0, 1, 0], [0, 0, 1], [1, 0, 1]]
    hv = mv_mod(fmod2, [x % 2 for x in v0], 2)
    coeff = mv_mod(m1280_mod2, hv, 2)[2]
    assert coeff == 1
    assert tripell_mod(1280, 2**13, m, v0) == 2**12

    # Every term on the exceptional progression is divisible by 2^9.
    for t in range(0, 129):
        assert tripell_mod(1280 + 1792*t, 2**9, m, v0) == 0

    # Check the isometry law on a finite grid; the symbolic matrix lift
    # proves it for all 2-adic inputs.
    modulus = 2**40
    vals = [tripell_mod(1280 + 1792*t, modulus, m, v0) // 2**9
            for t in range(32)]
    for s in range(32):
        for t in range(s + 1, 32):
            assert v2(vals[t] - vals[s]) == v2(t - s), (s, t)

    # Hensel-style unique root lifts for tau modulo 2^m, m=1..20.
    tau = 0
    residues = {0: 0}
    for level in range(0, 20):
        mod_next = 2**(10 + level)
        a = tripell_mod(1280 + 1792*tau, mod_next, m, v0) == 0
        b = tripell_mod(1280 + 1792*(tau + 2**level), mod_next, m, v0) == 0
        assert a != b, (level, tau, a, b)
        if b:
            tau += 2**level
        residues[level + 1] = tau
        assert tripell_mod(1280 + 1792*tau, 2**(10 + level), m, v0) == 0
    assert tau == 534216
    assert residues[3] == 0 and residues[4] == 8
    assert residues[6] == 8 and residues[7] == 72
    assert residues[8] == 200 and residues[10] == 712
    assert residues[13] == 1736 and residues[19] == 9928

    print("VERIFY_OK: exact matrix lift and odd isometry coefficient; "
          "129 divisibility checks; 496 finite isometry comparisons; "
          "unique root lifts through 2^20")
    print("tau mod 2^20 = 534216")


if __name__ == "__main__":
    main()
