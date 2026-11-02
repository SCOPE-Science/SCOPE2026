#!/usr/bin/env python3
"""Finite independent language enumeration for a lacunary binary word."""

def expected(n):
    out = set()
    if n == 3:
        out.add('111')
    if n == 4:
        out.update(('0011', '1011'))
    d = n - 1
    if d >= 1 and (d & (d - 1)):
        out.add('1' + '0' * (d - 1) + '1')
    k = 1
    while 3 * (1 << (k - 1)) + 1 <= n:
        if 3 * (1 << (k - 1)) + 1 == n:
            out.add('0' * (1 << (k - 1)) + '1' + '0' * ((1 << k) - 1) + '1')
        k += 1
    k = 0
    while 3 * (1 << k) + 1 <= n:
        if 3 * (1 << k) + 1 == n:
            out.add('1' + '0' * ((1 << k) - 1) + '1' + '0' * (1 << (k + 1)))
        k += 1
    return out


def check(max_length=160, prefix_length=8192):
    assert prefix_length > 16 * max_length
    w = ''.join('1' if i > 0 and i & (i - 1) == 0 else '0'
                for i in range(prefix_length))
    old = {''}
    totals = 0
    for n in range(1, max_length + 1):
        current = {w[i:i + n] for i in range(prefix_length - n + 1)}
        if n >= 2:
            got = {a + v for a in '01' for v in old if
                   a + v not in current and (a + v)[:-1] in old}
            want = expected(n)
            assert got == want, (n, sorted(got - want), sorted(want - got))
            totals += len(got)
        old = current
    print(f'PASS: exhaustive factor-language comparison through length {max_length}; '
          f'{totals} minimal-absent-word instances across lengths 2..{max_length}.')
    print('Counts n=2..16:', [len(expected(n)) for n in range(2, 17)])


if __name__ == '__main__':
    check()
