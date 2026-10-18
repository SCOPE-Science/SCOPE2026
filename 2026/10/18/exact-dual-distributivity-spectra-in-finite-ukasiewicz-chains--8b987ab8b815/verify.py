#!/usr/bin/env python3
"""Exact independent finite checks for dual distributivity in MV chains.

No external packages are required.  Integer arithmetic represents elements
of the chain with n+1 elements; n is its denominator, not cardinality.
"""

def direct(n, a, b, c):
    def s(u, v):
        return min(n, u + v)
    def t(u, v):
        return max(0, u + v - n)
    forward = t(a, s(b, c)) == s(t(a, b), t(a, c))
    reverse = s(a, t(b, c)) == t(s(a, b), s(a, c))
    return forward, reverse


def forward_regions(n, a, b, c):
    if a == 0 or a == n:
        return True
    t = n - a
    if b <= t and c <= t:
        return b + c <= t
    if b > t and c <= t:
        return c == 0 or b == n
    if c > t and b <= t:
        return b == 0 or c == n
    return b + c == 2 * n - a


def joint_regions(n, a, b, c):
    if a == 0 or a == n:
        return True
    t = n - a
    return (
        (b == 0 and c >= t)
        or (c == 0 and b >= t)
        or (b == n and c <= t)
        or (c == n and b <= t)
        or (0 < b < n and 0 < c < n and b + c in (t, 2 * n - a))
    )


def run(limit=45):
    triples = 0
    for n in range(1, limit + 1):
        f = g = both = 0
        for a in range(n + 1):
            for b in range(n + 1):
                for c in range(n + 1):
                    x, y = direct(n, a, b, c)
                    assert x == forward_regions(n, a, b, c), (n, a, b, c, 'forward')
                    assert y == forward_regions(n, n - a, n - b, n - c), (n, a, b, c, 'dual')
                    assert (x and y) == joint_regions(n, a, b, c), (n, a, b, c, 'joint')
                    f += x
                    g += y
                    both += x and y
                    triples += 1
        assert f == (n ** 3 + 30 * n ** 2 + 5 * n + 12) // 6, (n, f)
        assert (n ** 3 + 30 * n ** 2 + 5 * n + 12) % 6 == 0
        assert g == f, (n, g, f)
        assert both == 5 * n ** 2 + n + 2, (n, both)
    print(f'VERIFY_OK denominators=1..{limit} triples={triples} direct_vs_regions=PASS counts=PASS')


if __name__ == '__main__':
    run()
