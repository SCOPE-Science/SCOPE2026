#!/usr/bin/env python3
"""Independent finite modular checks of the accompanying Fibonacci--Lucas sumset theorem."""

def residues(m):
    mod = 1 << m
    f0, f1, l0, l1 = 0, 1, 2, 1
    fib, luc = set(), set()
    # The Fibonacci and Lucas state sequences are periodic modulo mod;
    # this deliberately over-samples the known dyadic Pisano period.
    for n in range(1, 6 * mod + 1):
        f0, f1 = f1, (f0 + f1) % mod
        l0, l1 = l1, (l0 + l1) % mod
        if n % 3 == 0:
            fib.add(f0 % mod)
            luc.add(l0 % mod)
    return fib, luc


def verify():
    checks = 0
    for m in range(3, 13):
        mod = 1 << m
        fib, luc = residues(m)
        both = {(a + b) % mod for a in fib for b in luc}
        expected = {n for n in range(mod) if n % 8 in (2, 4, 6)}
        assert both == expected, (m, 'two-summand mismatch')
        assert {n for n in range(mod) if n % 8 == 0} <= fib
        assert {n for n in range(mod) if n % 8 == 4} <= luc
        assert {n % 8 for n in fib} == {0, 2}
        assert {n % 8 for n in luc} == {2, 4}
        tffl = {(a + f) % mod for a in both for f in fib}
        tfll = {(a + l) % mod for a in both for l in luc}
        even = {n for n in range(mod) if n % 2 == 0}
        assert tffl == tfll == even, (m, 'three-summand mismatch')
        checks += 1

    mod = 1 << 24
    G = [0, 1]
    for i in range(2, 310):
        G.append((18 * G[-1] - G[-2]) % mod)
    shift_checks = 0
    for r in range(9):
        delta = 1 << r
        for t in range(32):
            assert (G[t + delta] - G[t] - delta) % (2 ** (r + 1)) == 0
            assert (G[t + delta] + G[t + delta + 1] - G[t] - G[t + 1] - 2 * delta) % (2 ** (r + 2)) == 0
            shift_checks += 2
    print(f'VERIFY_OK modulus_exponents={checks} shift_congruences={shift_checks} largest_modulus=4096')


if __name__ == '__main__':
    verify()
