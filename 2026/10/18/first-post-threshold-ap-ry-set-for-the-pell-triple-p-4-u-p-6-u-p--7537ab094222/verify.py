"""Independent finite checks for the first exceptional Pell-triple p-Apery set.

Run with Python 3: python verify.py
No nonstandard packages, network access, or reference files are needed.
"""

def pell(u, n):
    x, y = 0, 1
    for _ in range(n):
        x, y = y, u * y + x
    return x


def verify(u):
    s = u * u + 2
    p = u * u
    a, b, c = (pell(u, i) for i in (4, 6, 9))
    candidates = [
        (p * s + j) * b + z * c - ((s - 1) * a if j == s - 1 else 0)
        for j in range(s)
        for z in range(u)
    ]
    assert len(set(m % a for m in candidates)) == a
    limit = max(candidates)
    # Coefficients of (1-X^a)^(-1)(1-X^b)^(-1)(1-X^c)^(-1).
    ways = [0] * (limit + 1)
    ways[0] = 1
    for coin in (a, b, c):
        for n in range(coin, limit + 1):
            ways[n] += ways[n - coin]
    for m in candidates:
        assert ways[m] == p + 1, (u, m, 'boundary')
        assert ways[m - a] == p, (u, m, 'preceding value')
    g = max(candidates) - a
    n_p = sum(ways[n] <= p for n in range(g + 1))
    expected_g = (s * s - s - 1) * b + (u - 1) * c - s * a
    expected_n = p * s * b + ((s - 1) * b + (u - 1) * c - a + 1) // 2 - u * (s - 1)
    assert g == expected_g
    assert n_p == expected_n
    assert (2 * sum(candidates) - a * (a - 1)) == 2 * a * expected_n
    return u, p, g, n_p


if __name__ == '__main__':
    for u in (2, 3, 4, 5):
        print(*verify(u), sep='\t')
