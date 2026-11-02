"""Finite independent checks for the transposed-output parity automaton.

Python 3, standard library only. Run: python verify.py
Finite tests corroborate but do not replace the general proof.
"""
from collections import Counter


def rows(n, swap=False):
    a = [(1 << ((j - 1) % n)) | (1 << ((j + 1) % n)) for j in range(n)]
    if swap:
        a[0], a[1] = a[1], a[0]
    return a


def image(a, v):
    return sum(((v & row).bit_count() & 1) << j for j, row in enumerate(a))


def product(a, b):
    result = []
    for row in a:
        z = 0
        while row:
            low = row & -row
            z ^= b[low.bit_length() - 1]
            row ^= low
        result.append(z)
    return result


def rank(a):
    v = a[:]
    r = 0
    for j in range(len(v)):
        k = next((k for k in range(r, len(v)) if (v[k] >> j) & 1), None)
        if k is None:
            continue
        v[r], v[k] = v[k], v[r]
        for i in range(len(v)):
            if i != r and ((v[i] >> j) & 1):
                v[i] ^= v[r]
        r += 1
    return r


def count_expected(n, t, swap):
    d = n & -n
    base = 1 << (n-d)
    if t == 0:
        return base
    if swap:
        if t == 1:
            return 3 * base
        return base * (1 << t) if 2 <= t <= d - 1 else 0
    return base * 3 * (1 << (2 * t - 2)) if 1 <= t <= d // 2 else 0


def check_source_rule(n):
    a = rows(n, True)
    mask = (1 << n) - 1
    for v in range(min(1 << n, 1 << 12)):
        y = (((v << 1) | (v >> (n - 1))) ^ ((v >> 1) | (v << (n - 1)))) & mask
        z = y ^ (((y & 1) ^ ((y >> 1) & 1)) * 3)
        assert z == image(a, v), ('source definition', n, v)


def check(n, exhaustive=False):
    d = n & -n
    assert n >= 4 and not n % 2
    check_source_rule(n)
    for swap in (False, True):
        a = rows(n, swap)
        power = [(1 << i) for i in range(n)]
        for t in range(1, d + 2):
            power = product(power, a)
            observed = rank(power)
            expected = n - min(d, t + 1) if swap else n - min(d, 2 * t)
            assert observed == expected, ('rank', n, swap, t, observed, expected)
        if exhaustive:
            counts = Counter()
            for x in range(1 << n):
                seen = {}
                y = x
                while y not in seen:
                    seen[y] = len(seen)
                    y = image(a, y)
                counts[seen[y]] += 1
            for t in range(d + 1):
                expected = count_expected(n, t, swap)
                assert counts[t] == expected, ('preperiod', n, swap, t, counts[t], expected)
            assert sum(counts.values()) == 1 << n
        horizon = d - 1 if swap else d // 2
        print(f'n={n:3d} swap={int(swap)} 2-primary={d:3d} max-preperiod={horizon:3d} exhaustive={exhaustive}')


if __name__ == '__main__':
    cases = list(range(4, 25, 2)) + [28, 30, 32, 36, 40, 48, 64, 96, 128]
    for n in cases:
        check(n, exhaustive=(n <= 12 or n == 16))
    print('VERIFY_OK')
