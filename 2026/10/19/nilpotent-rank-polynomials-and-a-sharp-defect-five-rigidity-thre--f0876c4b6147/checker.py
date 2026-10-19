"""Exact rank-polynomial verification for order/fence/parity partial injections.
Python 3 standard library only. Prints VERIFY_OK on success.
"""
from itertools import combinations


def rank_polynomials(nmax):
    """Coefficient vectors for the diagonal-prefix recurrence."""
    zero = (0,) * (nmax + 1)
    f = [[zero for _ in range(nmax + 1)] for _ in range(nmax + 1)]
    p = [[zero for _ in range(nmax + 1)] for _ in range(nmax + 1)]

    def read(table, i, j):
        return table[i][j] if i >= 1 and j >= 1 else zero

    for i in range(1, nmax + 1):
        for j in range(1, nmax + 1):
            if i != j and (i - j) % 2 == 0:
                one = read(f, i - 1, j - 1)
                even = read(p, i - 2, j - 2)
                odd = read(p, i - 3, j - 3)
                f[i][j] = (0,) + tuple(
                    int(k == 0) + one[k] + even[k] + odd[k]
                    for k in range(nmax)
                )
            a = read(p, i - 2, j)
            b = read(p, i, j - 2)
            c = read(p, i - 2, j - 2)
            p[i][j] = tuple(f[i][j][k] + a[k] + b[k] - c[k]
                            for k in range(nmax + 1))

    answer = [None]
    for n in range(1, nmax + 1):
        total = [int(k == 0) for k in range(nmax + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for k, coefficient in enumerate(f[i][j]):
                    total[k] += coefficient
        answer.append(tuple(total[:n+1]))
    return answer


def fence_leq(x, y):
    return x == y or (x % 2 == 1 and y == x + 1) or (
        x % 2 == 1 and y == x - 1)


def valid_map(domain, image):
    """Directly use the up-fence partial-order relations, not Proposition 1."""
    if any((u - v) % 2 for u, v in zip(domain, image)):
        return False
    return all(fence_leq(u, v) == fence_leq(x, y)
               for u, x in zip(domain, image)
               for v, y in zip(domain, image))


def is_nilpotent(domain, image):
    mapping = dict(zip(domain, image))
    if not mapping:
        return True
    # Power n+1 is empty exactly when no periodic component remains.
    for start in domain:
        seen = set()
        x = start
        while x in mapping:
            if x in seen:
                return False
            seen.add(x)
            x = mapping[x]
    return True


def direct_polynomial(n):
    counts = [0] * (n + 1)
    for r in range(n + 1):
        subsets = list(combinations(range(1, n + 1), r))
        for domain in subsets:
            for image in subsets:
                if not valid_map(domain, image):
                    continue
                nil = is_nilpotent(domain, image)
                assert nil == all(u != v for u, v in zip(domain, image))
                if nil:
                    counts[r] += 1
                    if r >= n - 4 and n - r <= 4 and r > 0:
                        shifts = set(y - x for x, y in zip(domain, image))
                        assert len(shifts) == 1
                        assert list(shifts)[0] in (-4, -2, 2, 4)
    return tuple(counts)


def main():
    N = 20
    fast = rank_polynomials(N)
    for n in range(1, 10):
        assert fast[n] == direct_polynomial(n), (n, fast[n], direct_polynomial(n))
    for n in range(3, N + 1):
        assert fast[n][n-2] == 2
        if n >= 4:
            assert fast[n][n-3] == 2 * (n - 2)
        if n >= 5:
            assert fast[n][n-4] == (n - 2) * (n - 3) + 2
        assert fast[n][n] == 0 and fast[n][n-1] == 0
    assert fast[7] == (1, 18, 32, 22, 10, 2, 0, 0)
    assert fast[9] == (1, 32, 116, 142, 98, 44, 14, 2, 0, 0)
    for n in range(7, N + 1):
        domain = (1,) + tuple(range(3, n - 3))
        image = (3,) + tuple(range(7, n + 1))
        assert len(domain) == n - 5 and len(image) == n - 5
        assert valid_map(domain, image) and is_nilpotent(domain, image)
        assert len(set(v - u for u, v in zip(domain, image))) > 1
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
