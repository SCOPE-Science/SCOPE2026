#!/usr/bin/env python3
"""Finite reproducibility checks for the binary 11-block arithmetic-progression theorem.

Uses Python's standard library only. These tests support, but do not replace,
the general bit-concatenation proof in RESULT.md.
"""

def rudin_shapiro_bit(n: int) -> int:
    assert n >= 0
    digits = format(n, 'b')
    return sum(digits[t] == digits[t+1] == '1'
               for t in range(len(digits)-1)) % 2


def witness(k: int):
    assert k >= 1 and k % 2 == 1
    if k == 1:
        return (3, None, None)
    Q = 1 << (2*k*(k-1)-1).bit_length()
    a = Q//(k-1)
    if a % 2 == 0:
        a -= 1
    assert a % 2 == 1 and a > 0
    assert (k-2)*a < Q <= k*a < 2*Q
    d = a*(2*Q+1)
    assert 0 < d < 32*k**3
    return d, Q, a


def first_change(d: int, limit: int):
    for j in range(1, limit + 1):
        if rudin_shapiro_bit(j*d):
            return j
    raise AssertionError(('limit too small', d, limit))


def main():
    double_checks = 20001
    for n in range(double_checks):
        assert rudin_shapiro_bit(2*n) == rudin_shapiro_bit(n)

    concatenation_checks = 0
    for L in range(1, 14):
        shift = 1 << L
        for x in range(shift):
            expected = (x & 1) * ((x >> (L-1)) & 1)
            assert rudin_shapiro_bit((shift+1)*x) == expected
            concatenation_checks += 1

    constructed = 0
    for k in range(1, 400, 2):
        d, Q, a = witness(k)
        assert all(rudin_shapiro_bit(j*d) == 0 for j in range(1, k))
        assert rudin_shapiro_bit(k*d) == 1
        assert first_change(d, k) == k
        constructed += 1

    small_d = 0
    for d in range(1, 1025):
        j = first_change(d, 4*d + 16)
        assert j % 2 == 1
        small_d += 1

    # Different dyadic choices yield infinitely many distinct witnesses per k.
    for k in range(3, 52, 2):
        d0, Q0, _ = witness(k)
        Q = 2*Q0
        a = Q // (k-1)
        if not a % 2:
            a -= 1
        d1 = a*(2*Q+1)
        assert d1 > d0
        assert (k-2)*a < Q <= k*a < 2*Q
        assert all(rudin_shapiro_bit(j*d1) == 0 for j in range(1, k))
        assert rudin_shapiro_bit(k*d1) == 1

    print('VERIFY_OK double_checks=%s concatenation_checks=%s constructed_odd_k=%s '
          'small_d=%s second_witness_k=%s' % (double_checks, concatenation_checks,
              constructed, small_d, len(range(3, 52, 2))))

if __name__ == '__main__':
    main()
