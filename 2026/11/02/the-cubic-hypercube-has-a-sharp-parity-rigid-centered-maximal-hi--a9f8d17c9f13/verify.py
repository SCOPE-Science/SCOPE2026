"""Exact-rational finite certificate for the centered ball maximal norm on Q_3.

The analysis of all radius-selection matrices is finite and exhaustive:
there are four balls per vertex and eight vertices. No floating point or
external algebra package is used in the certificate.
"""
from itertools import product
from collections import deque
from fractions import Fraction

N = 8
SCALE = 56                       # lcm(1, 4, 7, 8)
TAU_NUM = 317                    # strict separation threshold 317/200
TAU_DEN = 200


def distances():
    # Independent graph-based shortest paths, with no use of Hamming distances.
    adj = [[v ^ (1 << j) for j in range(3)] for v in range(N)]
    d = [[-1] * N for _ in range(N)]
    for root in range(N):
        d[root][root] = 0
        q = deque([root])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if d[root][v] == -1:
                    d[root][v] = d[root][u] + 1
                    q.append(v)
    if not all(d[i][j] == (i ^ j).bit_count() for i in range(N) for j in range(N)):
        raise AssertionError("distance reconstruction")
    return d


def ball_rows():
    d = distances()
    result = []
    for v in range(N):
        rows = []
        for radius in range(4):
            ball = [int(d[v][u] <= radius) for u in range(N)]
            size = sum(ball)
            if not (size in (1, 4, 7, 8) and SCALE % size == 0):
                raise AssertionError("ball size")
            rows.append([b * (SCALE // size) for b in ball])
        if [sum(r) for r in rows] != [SCALE] * 4:
            raise AssertionError("row stochasticity")
        result.append(rows)
    return result


def positive_definite_integer(a):
    """Sylvester's criterion via symmetric fraction-free Bareiss elimination.

    At step k, the positive pivot is the (k+1)-st leading principal minor
    (not a floating-point approximation). The updates are exact by the determinant identity.
    """
    a = [row.copy() for row in a]
    prior = 1
    for k in range(N):
        pivot = a[k][k]
        if pivot <= 0:
            return False
        if k == N - 1:
            return True
        for i in range(k + 1, N):
            for j in range(i, N):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                q, r = divmod(numerator, prior)
                if r != 0:
                    raise AssertionError(("nonintegral update", k, i, j))
                a[i][j] = q
        for i in range(k + 1, N):
            for j in range(i + 1, N):
                a[j][i] = a[i][j]
            a[i][k] = 0
        prior = pivot
    raise AssertionError('unreachable')


def certificate():
    rows = ball_rows()
    parity = [i.bit_count() % 2 for i in range(N)]
    exceptional = {tuple(parity), tuple(1 - t for t in parity)}
    checked = 0
    seen_exceptional = set()
    for selection in product(range(4), repeat=N):
        if selection in exceptional:
            seen_exceptional.add(selection)
            continue
        b = [rows[v][selection[v]] for v in range(N)]
        gram = [[sum(b[k][i] * b[k][j] for k in range(N))
                 for j in range(N)] for i in range(N)]
        # C = 200*56^2*(317/200*I - (B/56)^T(B/56)).
        c = [[(TAU_NUM * SCALE * SCALE if i == j else 0)
              - TAU_DEN * gram[i][j] for j in range(N)]
             for i in range(N)]
        if not positive_definite_integer(c):
            raise AssertionError(("failed positive definiteness", selection))
        checked += 1
    if len(seen_exceptional) != 2:
        raise AssertionError("exceptional selection count")
    if checked != 4**N - 2 or checked != 65534:
        raise AssertionError("exhaustive enumeration count")
    # Exceptional block has adjacency J-P: row/column sums 3,
    # and A^T A has eigenvalues 9 (once) and 1 (thrice).
    for selection in exceptional:
        b = [rows[v][selection[v]] for v in range(N)]
        idclass = [v for v in range(N) if selection[v] == 0]
        avgclass = [v for v in range(N) if selection[v] == 1]
        if len(idclass) != 4 or len(avgclass) != 4:
            raise AssertionError("parity classes")
        a = [[int(distances()[v][u] == 1) for u in idclass]
             for v in avgclass]
        if [sum(row) for row in a] != [3] * 4:
            raise AssertionError("degree rows")
        if [sum(a[j][i] for j in range(4)) for i in range(4)] != [3] * 4:
            raise AssertionError("degree columns")
        for i in range(4):
            for j in range(4):
                # Explicit A^T A: diagonal 3, off-diagonal 2.
                if sum(a[k][i] * a[k][j] for k in range(4)) != (3 if i == j else 2):
                    raise AssertionError("bipartite singular values")
        for v in idclass:
            if b[v][v] != 56 or sum(b[v]) != 56:
                raise AssertionError("radius zero block")
        for v in avgclass:
            if sum(b[v]) != 56 or b[v][v] != 14:
                raise AssertionError("radius one block")
    # Exact root location: sqrt(17)>103/25, hence winning lambda >317/200.
    if not Fraction(17) > Fraction(103, 25)**2:
        raise AssertionError("strict eigenvalue separation")
    print('CERTIFICATE_OK selections=65536 strict=65534 exceptional=2', flush=True)


if __name__ == '__main__':
    certificate()
