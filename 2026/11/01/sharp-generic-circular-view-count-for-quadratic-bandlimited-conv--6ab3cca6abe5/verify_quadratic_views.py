"""Exact finite-dimensional checks for circular two-plane measurements of quadratic supports.

The rank certificates are modular over the prime 1000003. Full rank modulo a prime
implies full rank over the rationals; finite dimensions checked here do not prove
an all-dimensional statement, which has a separate analytic proof.
"""
import random

MOD = 1000003


def tracefree_basis(n):
    out = []
    for i in range(n - 1):
        M = [[0] * n for _ in range(n)]
        M[i][i] = 1
        M[-1][-1] = -1
        out.append(M)
    for i in range(n):
        for j in range(i + 1, n):
            M = [[0] * n for _ in range(n)]
            M[i][j] = M[j][i] = 1
            out.append(M)
    assert len(out) == n * (n + 1) // 2 - 1
    return out


def bilinear(v, M, w):
    return sum(v[i] * M[i][j] * w[j] for i in range(len(v)) for j in range(len(w)))


def measurement_rows(n, x, y, basis):
    sx = sum(a * a for a in x)
    sy = sum(a * a for a in y)
    xy = sum(a * b for a, b in zip(x, y))
    assert sx * sy > xy * xy, 'plane basis degenerate'
    first = []
    second = []
    for M in basis:
        xx = bilinear(x, M, x)
        yy = bilinear(y, M, y)
        qxy = bilinear(x, M, y)
        first.append((sx * qxy - xy * xx) % MOD)
        second.append((sx * yy - sy * xx) % MOD)
    return first, second


def mod_rank(rows):
    A = [list(row) for row in rows]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    rank = 0
    for j in range(n):
        pivot = next((i for i in range(rank, m) if A[i][j] % MOD), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        inv = pow(A[rank][j] % MOD, -1, MOD)
        A[rank] = [(a * inv) % MOD for a in A[rank]]
        for i in range(rank + 1, m):
            if A[i][j]:
                c = A[i][j]
                A[i] = [(a - c * b) % MOD for a, b in zip(A[i], A[rank])]
        rank += 1
        if rank == min(m, n):
            break
    return rank


def certificate(n):
    rng = random.Random(91731 + n)
    basis = tracefree_basis(n)
    D = len(basis)
    m = (D + 1) // 2
    for attempt in range(30):
        rows = []
        planes = []
        for _ in range(m):
            x = [rng.randint(-5, 5) for _ in range(n)]
            y = [rng.randint(-5, 5) for _ in range(n)]
            if not any(x) or not any(y) or sum(z * z for z in x) * sum(z * z for z in y) == sum(a * b for a, b in zip(x, y)) ** 2:
                break
            a, b = measurement_rows(n, x, y, basis)
            rows += [a, b]
            planes.append((x, y))
        if len(planes) != m:
            continue
        rank = mod_rank(rows)
        if rank == D:
            assert mod_rank(rows[:-2]) <= D - 1
            return {'ambient_dimension':n, 'quadratic_dim':D, 'planes':m, 'rank':rank, 'attempt':attempt+1}
    raise AssertionError(f'No full rank found in dimension {n}: {rank=}')


if __name__ == '__main__':
    for n in range(3, 13):
        print(certificate(n))
    print('All exact modular rank certificates passed.')
