from collections import deque
from itertools import product


def inv_mod(a, p):
    return pow(a, p - 2, p)


def canonical_projective_vector(v, p):
    for x in v:
        if x % p:
            c = inv_mod(x % p, p)
            return tuple((c * y) % p for y in v)
    raise ValueError("zero vector")


def projective_vectors(p, d):
    points = set()
    for v in product(range(p), repeat=d):
        if any(v):
            points.add(canonical_projective_vector(v, p))
    return sorted(points)


def rank_mod(rows, p):
    A = [list(r) for r in rows if any(x % p for x in r)]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c] % p), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        z = inv_mod(A[r][c] % p, p)
        A[r] = [(z * x) % p for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] % p:
                z = A[i][c] % p
                A[i] = [(A[i][j] - z * A[r][j]) % p for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def verify(p, d):
    # One copy indexes projective points x; the other indexes hyperplanes ker(a).
    vectors = projective_vectors(p, d)
    n = len(vectors)
    neighborhoods = []
    for x in vectors:
        mask = 0
        for j, a in enumerate(vectors):
            if sum(x[t] * a[t] for t in range(d)) % p != 0:
                mask |= 1 << j
        neighborhoods.append(mask)

    degrees = [m.bit_count() for m in neighborhoods]
    assert len(set(degrees)) == 1
    assert degrees[0] == p ** (d - 1)
    assert len(set(neighborhoods)) == n

    adjacency = [[] for _ in range(2 * n)]
    for i, mask in enumerate(neighborhoods):
        for j in range(n):
            if (mask >> j) & 1:
                adjacency[i].append(n + j)
                adjacency[n + j].append(i)
    seen = {0}
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    assert len(seen) == 2 * n

    # Exhaustively check the point-side linear-algebra criterion. By duality the
    # same criterion holds on the hyperplane side.
    if n > 16:
        raise ValueError("test case too large for exhaustive subset verification")
    all_hyperplanes = (1 << n) - 1
    for subset in range(1 << n):
        rows = [vectors[i] for i in range(n) if (subset >> i) & 1]
        rank = rank_mod(rows, p)
        covered = 0
        for i in range(n):
            if (subset >> i) & 1:
                covered |= neighborhoods[i]
        assert (covered == all_hyperplanes) == (rank == d)
        for i in range(n):
            if not ((subset >> i) & 1):
                legal = (covered | neighborhoods[i]) != covered
                rank2 = rank_mod(rows + [vectors[i]], p)
                assert legal == (rank2 == rank + 1)

    return n, degrees[0]


for p, d in [(2, 2), (2, 3), (2, 4), (3, 2), (3, 3)]:
    n, degree = verify(p, d)
    print(
        f"p={p} d={d}: order={2*n}, degree={degree}, "
        f"forced_total_sequence_length={2*d}: PASS"
    )
