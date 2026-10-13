#!/usr/bin/env python3
from math import isqrt

M_MAX = 12
TAIL = 2000
SHIFT_MAX = 80
A_MAX = 120
E_MAX = 300
N_WITNESS_MAX = 2000

def make_g(m):
    L = 2 * m - 1
    def g(e):
        if e == 0:
            return 0
        if 1 <= e <= m - 2:
            return e + 1
        if e == m - 1:
            return 0
        if m <= e <= 2 * m - 3:
            return e + 1
        if e == 2 * m - 2:
            return 0
        # Here e >= L.
        return 1 if isqrt(e) ** 2 == e else m
    return L, g

def iterate(g, e, k):
    for _ in range(k):
        e = g(e)
    return e

def odd_part_and_v2(n):
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return n, e

def f_iter(n, m, k):
    L, g = make_g(m)
    u, e = odd_part_and_v2(n)
    return (2 ** iterate(g, e, k)) * u

def main():
    shift_checks = 0
    signature_checks = 0
    witness_checks = 0
    for m in range(2, M_MAX + 1):
        L, g = make_g(m)
        for e in range(L, L + TAIL):
            sq = isqrt(e) ** 2 == e
            for k in range(1, m):
                expected = k if sq else m + k - 1
                assert iterate(g, e, k) == expected, (m, e, k)
            assert iterate(g, e, m) == 0, (m, e, 'collapse')

        for k in range(1, m):
            for d in range(1, SHIFT_MAX + 1):
                found = False
                t = isqrt(L) + 1
                while t * t < L + TAIL * 10:
                    E = t * t
                    if isqrt(E + d) ** 2 != E + d:
                        assert iterate(g, E, k) != iterate(g, E + d, k)
                        found = True
                        break
                    t += 1
                assert found, (m, k, d)
                shift_checks += 1

            sigs = {}
            for a in range(1, A_MAX + 1):
                sig = tuple(f_iter(a * (2 ** e), m, k) for e in range(E_MAX + 1))
                assert sig not in sigs, (m, k, a, sigs.get(sig))
                sigs[sig] = a
                signature_checks += 1

        a = 2 ** L
        b = 2 ** (L + 1)
        for n in range(1, N_WITNESS_MAX + 1):
            assert f_iter(a * n, m, m) == f_iter(b * n, m, m)
            witness_checks += 1

    print('VERIFY_OK')
    print('m_max=' + str(M_MAX))
    print('shift_checks=' + str(shift_checks))
    print('bounded_signature_checks=' + str(signature_checks))
    print('nonquasi_witness_checks=' + str(witness_checks))

if __name__ == '__main__':
    main()
