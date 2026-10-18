"""Independent exact checks for the rank-two symmetric Toeplitz projective curve."""
from itertools import product


def rank_mod(matrix, prime):
    rows = [list(row) for row in matrix]
    rank = 0
    n = len(rows)
    for j in range(len(rows[0])):
        pivot = next((i for i in range(rank, n) if rows[i][j] % prime), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        multiplier = pow(rows[rank][j], -1, prime)
        rows[rank] = [(value * multiplier) % prime for value in rows[rank]]
        for i in range(rank + 1, n):
            c = rows[i][j]
            if c:
                rows[i] = [(a - c * b) % prime for a, b in zip(rows[i], rows[rank])]
        rank += 1
        if rank > 2:
            return rank
    return rank


def norm(vector, prime):
    vector = tuple(x % prime for x in vector)
    first = next((x for x in vector if x), None)
    if first is None:
        return None
    inv = pow(first, -1, prime)
    return tuple(x * inv % prime for x in vector)


def cheb(n, u, prime):
    values = [1, u]
    while len(values) < n:
        values.append((2 * u * values[-1] - values[-2]) % prime)
    return norm(values[:n], prime)


def all_points(n, prime):
    for leading_zeroes in range(n):
        for remainder in product(range(prime), repeat=n - leading_zeroes - 1):
            yield (0,) * leading_zeroes + (1,) + remainder


def poly_add(a, b, sign=1):
    return [(a[i] if i < len(a) else 0) + sign * (b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))]


def poly_mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def test_polynomials():
    T = [[1], [0, 1]]
    U = [[1], [0, 2]]
    for _ in range(2, 11):
        T.append(trim(poly_add(poly_mul([0, 2], T[-1]), T[-2], -1)))
        U.append(trim(poly_add(poly_mul([0, 2], U[-1]), U[-2], -1)))
    for i in range(10):
        for j in range(10):
            first = poly_mul(T[i], T[j])
            second = [0] if i == 0 or j == 0 else poly_mul([1, 0, -1], poly_mul(U[i-1], U[j-1]))
            assert trim(poly_add(first, second)) == T[abs(i-j)], (i, j)


def test_points():
    for n, prime in ((4, 3), (4, 5), (5, 3), (5, 5), (6, 3), (6, 5)):
        observed = set()
        for v in all_points(n, prime):
            if rank_mod([[v[abs(i-j)] for j in range(n)] for i in range(n)], prime) <= 2:
                observed.add(v)
        c = {cheb(n, u, prime) for u in range(prime)}
        c.add((0,) * (n-1) + (1,))
        l = {norm(tuple(1 if i % 2 == 0 else a for i in range(n)), prime) for a in range(prime)}
        l.add(norm(tuple(0 if i % 2 == 0 else 1 for i in range(n)), prime))
        assert len(c) == prime + 1
        assert len(l) == prime + 1
        assert len(c & l) == 2
        assert observed == c | l, (n, prime, len(observed), len(c | l))
        assert len(observed) == 2 * prime
        print('field', prime, 'size', n, 'points', len(observed), 'OK')


if __name__ == '__main__':
    test_polynomials()
    test_points()
    print('VERIFY_OK')
