#!/usr/bin/env python3
"""Exact arithmetic checks of metallic-mean row memberships."""
from math import isqrt


def sequences(c, mmax):
    f, l = [0, 1], [2, c]
    while len(l) <= mmax:
        f.append(c * f[-1] + f[-2])
        l.append(c * l[-1] + l[-2])
    return f, l


def row_indices(c, n, f, l):
    def floor_power(k, i):
        z = k * f[i]
        return (k * l[i] + isqrt((c*c+4)*z*z)) // 2

    def belongs(i):
        lo, hi = 1, n+1
        while lo < hi:
            mid = (lo+hi)//2
            if floor_power(mid, i) < n:
                lo = mid+1
            else:
                hi = mid
        return floor_power(lo, i) == n

    return [i for i in range(1, len(f)) if belongs(i)]


def main():
    tests = 0
    for c in (2, 3, 4):
        f, l = sequences(c, 24)
        for m in (3, 7, 11):
            expected = list(range(1, (m-1)//2+1, 2)) + [m]
            actual = row_indices(c, l[m], f, l)
            assert actual == expected, (c, m, actual, expected)
            tests += 1
        for n in range(1, 251):
            rows = row_indices(c, n, f, l)
            def floor_inverse(t, i):
                z = t * f[i]
                a = isqrt((c*c+4)*z*z)
                if i % 2:
                    return (-t*l[i] + a)//2
                return (t*l[i] - a - 1)//2
            independent = [i for i in range(1, len(f)) if floor_inverse(n+1, i) - floor_inverse(n, i) == 1]
            assert rows == independent, (c, n, rows, independent)
            tests += 1
    print('VERIFY_OK', tests)


if __name__ == '__main__':
    main()
