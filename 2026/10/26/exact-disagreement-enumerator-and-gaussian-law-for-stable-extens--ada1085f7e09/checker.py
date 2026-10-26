"""Exact arithmetic checks for stable-extension disagreement on bidirected cycles.

Run: python3 checker.py (Python standard library only).
This checks the transfer characteristic factorization, finite distance
polynomials against independent exhaustive enumeration, and extremal terms.
"""

from collections import defaultdict
from itertools import product


def add(dst, src, scale=1, shift=0):
    for degree, coefficient in src.items():
        degree += shift
        dst[degree] = dst.get(degree, 0) + scale * coefficient
        if not dst[degree]:
            del dst[degree]


def mul(a, b):
    out = {}
    for i, u in a.items():
        for j, v in b.items():
            out[i + j] = out.get(i + j, 0) + u * v
    return {i: v for i, v in out.items() if v}


def transfer():
    letters = list(product((0, 1), repeat=2))
    states = list(product(letters, repeat=2))
    indices = {state: i for i, state in enumerate(states)}
    edges = [[] for _ in states]
    for i, (a, b) in enumerate(states):
        for c in letters:
            if all(not (a[k] == b[k] == 1)
                   and not (a[k] == b[k] == c[k] == 0)
                   for k in (0, 1)):
                edges[i].append((indices[(b, c)], int(c[0] != c[1])))
    return edges


def mat_right_multiply(matrix, edges):
    n = len(edges)
    out = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                for k, exponent in edges[j]:
                    add(out[i][k], matrix[i][j], shift=exponent)
    return out


def traces(limit=18):
    edges = transfer()
    n = len(edges)
    matrix = [[({0: 1} if i == j else {}) for j in range(n)]
              for i in range(n)]
    result = [{}]
    for power in range(1, limit + 1):
        matrix = mat_right_multiply(matrix, edges)
        tr = {}
        for i in range(n):
            add(tr, matrix[i][i])
        result.append(tr)
    return result


def determinant_coefficients(trace):
    # Newton identities: det(I-zT) = sum d_k z^k, with
    # k d_k = -sum_{j=1}^k tr(T^j) d_{k-j}.
    result = [{0: 1}]
    for k in range(1, 17):
        numerator = {}
        for j in range(1, k + 1):
            add(numerator, mul(trace[j], result[k - j]))
        assert all(v % k == 0 for v in numerator.values())
        result.append({i: -v // k for i, v in numerator.items()})
    return result


def factor_product():
    p = {0: {0: 1}, 1: {1: 1}, 3: {2: -1}}
    q = {0: {0: 1}, 1: {1: -1}, 2: {0: -1},
         3: {0: -1, 1: 1, 2: -1}, 4: {1: 1},
         5: {2: -1}, 6: {2: 1}}
    out = {}
    for i, u in p.items():
        for j, v in q.items():
            out.setdefault(i + j, {})
            add(out[i + j], mul(u, v))
    return out


def exhaustive_polynomial(n):
    # Enumeration independent of transfer matrix: inspect all subsets.
    good = []
    for mask in range(1 << n):
        bits = [(mask >> i) & 1 for i in range(n)]
        if any(bits[i] and bits[(i + 1) % n] for i in range(n)):
            continue
        if any(not(bits[(i - 1) % n] or bits[i] or bits[(i + 1) % n])
               for i in range(n)):
            continue
        good.append(mask)
    out = defaultdict(int)
    for a in good:
        for b in good:
            out[(a ^ b).bit_count()] += 1
    return dict(out), len(good)


def run():
    trace = traces(18)
    det = determinant_coefficients(trace)
    expected = factor_product()
    for i in range(17):
        assert det[i] == expected.get(i, {}), (i, det[i], expected.get(i, {}))
    print('FACTOR_CHECK_OK: exact 16 x 16 characteristic polynomial')
    perrin = {3: 3, 4: 2, 5: 5}
    for n in range(6, 19):
        perrin[n] = perrin[n - 2] + perrin[n - 3]
    for n in range(3, 17):
        direct, count = exhaustive_polynomial(n)
        assert direct == trace[n], (n, direct, trace[n])
        assert count == perrin[n]
        assert sum(direct.values()) == perrin[n] ** 2
        maximum = n if n % 2 == 0 else n - 1
        assert max(direct) == maximum
        assert direct[maximum] == (2 if n % 2 == 0 else 2 * n)
        assert direct.get(1, 0) == 0
        assert direct[0] == perrin[n]
    print('ENUMERATION_OK: every pair on all cycles 3 <= n <= 16')
    print('EXTREMA_OK: Perrin diagonals and parity-sharp extremal counts')
    assert trace[3] == {0: 3, 2: 6}
    assert trace[4] == {0: 2, 4: 2}
    assert trace[5] == {0: 5, 2: 10, 4: 10}
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    run()
