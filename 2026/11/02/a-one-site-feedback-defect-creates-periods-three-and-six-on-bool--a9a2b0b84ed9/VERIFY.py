"""Independent finite-dimensional checks for a one-site parity defect on Q_d.

Run: python3 hypercube_single_site_verify.py
No third-party dependencies.
"""
from collections import Counter


def matrix(d):
    n = 1 << d
    return [((1 << v) if v == 0 else 0) ^
            sum((1 << (v ^ (1 << j))) for j in range(d))
            for v in range(n)]


def rank(rows):
    pivots = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def product(a, b):
    out = []
    for row in a:
        value = 0
        while row:
            bit = row & -row
            value ^= b[bit.bit_length() - 1]
            row -= bit
        out.append(value)
    return out


def ident(n):
    return [1 << j for j in range(n)]


def xor_identity(a):
    return [row ^ (1 << j) for j, row in enumerate(a)]


def power(a, t):
    n = len(a)
    b = ident(n)
    while t:
        if t & 1:
            b = product(b, a)
        t >>= 1
        if t:
            a = product(a, a)
    return b


def advance(state, d):
    n = 1 << d
    new_state = 0
    for v in range(n):
        bit = (state & 1) if v == 0 else 0
        for coordinate in range(d):
            bit ^= (state >> (v ^ (1 << coordinate))) & 1
        new_state |= bit << v
    return new_state


def exact_cycle_and_entry(state, d):
    seen = {}
    now = state
    t = 0
    while now not in seen:
        seen[now] = t
        now = advance(now, d)
        t += 1
        assert t <= 8  # all tested d have theoretical bound <= 6
    return seen[now], t - seen[now]


def main():
    for d in range(2, 9):
        n = 1 << d
        b = matrix(d)
        delta = d & 1
        h = [r ^ ((1 << j) if delta else 0) ^ ((1 << j) if j == 0 else 0)
             for j, r in enumerate(b)]
        assert product(h, h) == [0] * n
        assert rank(h) == n // 2
        assert rank(b if d % 2 == 0 else xor_identity(b)) == n // 2 + 1
        if d % 2 == 0:
            assert [rank(power(b, t)) for t in range(5)] == [n, n//2+1, 2, 1, 1]
            assert power(b, 3) == power(b, 4)
            if d <= 4:
                counts = Counter(exact_cycle_and_entry(x, d)[0]
                                 for x in range(1 << n))
                expected = {0: 2, 1: 2**(n//2)-2,
                            2: 2**(n-1)-2**(n//2), 3: 2**(n-1)}
                assert dict(counts) == expected, (d, counts, expected)
        else:
            q = xor_identity(b)
            assert [rank(power(q, t)) for t in range(4)] == [n, n//2+1, 2, 2]
            assert power(b, 6) == ident(n)
            f1 = 2**(n//2-1)
            f2 = 2**(n-2)
            f3 = 2**(n//2+1)
            for t, count in [(1, f1), (2, f2), (3, f3), (6, 2**n)]:
                assert 2**(n-rank(xor_identity(power(b,t)))) == count
            assert (2**n - f2 - f3 + f1) % 6 == 0
            star = 1 | sum((1 << (1 << j)) for j in range(d))
            assert [advance(1,d),advance(star,d),advance(star^1,d)] == [star,star^1,1]
            if d == 3:
                counts = Counter(exact_cycle_and_entry(x,d) for x in range(1<<n))
                assert {t: sum(c for (entry,period),c in counts.items() if period==t)
                        for t in [1,2,3,6]} == {
                        1:f1,2:f2-f1,3:f3-f1,
                        6:2**n-f2-f3+f1}
                assert all(entry == 0 for entry,period in counts)
        print('d=%d dimension=%d rank checks and identity verified' % (d,n))
    print('HYPERCUBE_ONE_SITE_VERIFY_OK')


if __name__ == '__main__':
    main()
