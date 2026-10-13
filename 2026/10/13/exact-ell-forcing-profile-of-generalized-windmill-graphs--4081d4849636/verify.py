from itertools import combinations
from math import comb


def make_graph(r, m):
    n = 1 + r * m
    adj = [set() for _ in range(n)]
    for i in range(r):
        blade = [1 + i * m + j for j in range(m)]
        for v in blade:
            adj[0].add(v)
            adj[v].add(0)
        for a in range(m):
            for b in range(a + 1, m):
                u, v = blade[a], blade[b]
                adj[u].add(v)
                adj[v].add(u)
    return adj


def ell_forces(adj, S, ell):
    black = set(S)
    while True:
        add = set()
        for v in tuple(black):
            white = adj[v] - black
            if 0 < len(white) <= ell:
                add |= white
        if not add:
            break
        black |= add
    return len(black) == len(adj)


def criterion(r, m, S, ell):
    center_black = 0 in S
    white_counts = []
    for i in range(r):
        blade = {1 + i * m + j for j in range(m)}
        white_counts.append(len(blade - set(S)))
    full = sum(w == m for w in white_counts)

    if ell < m:
        if center_black:
            return all(w <= ell for w in white_counts)
        return all(w <= ell for w in white_counts) and any(
            w <= ell - 1 for w in white_counts
        )

    s = ell // m
    if center_black:
        return full <= s
    return full <= s and full < r


def poly_add(a, b):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return out


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_pow(a, e):
    out = [1]
    for _ in range(e):
        out = poly_mul(out, a)
    return out


def closed_coeffs(r, m, ell):
    n = 1 + r * m
    if ell < m:
        A = [0] * (m + 1)
        for j in range(ell + 1):
            A[m - j] += comb(m, j)
        P = poly_mul([1, 1], poly_pow(A, r))
        deg = r * (m - ell)
        P += [0] * (n + 1 - len(P))
        P[deg] -= comb(m, ell) ** r
        return P[: n + 1]

    if ell < r * m:
        B = [comb(m, d) for d in range(m + 1)]
        B[0] -= 1
        s = ell // m
        Q = [0]
        for f in range(s + 1):
            term = [comb(r, f) * c for c in poly_pow(B, r - f)]
            Q = poly_add(Q, term)
        P = poly_mul([1, 1], Q)
        return P + [0] * (n + 1 - len(P))

    return [0] + [comb(n, d) for d in range(1, n + 1)]


def minimum_formula(r, m, ell):
    if ell < m:
        return r * (m - ell) + 1
    if ell < m * (r - 1):
        return r - (ell // m)
    return 1


def minimum_count_formula(r, m, ell):
    if ell < m:
        c = comb(m, ell)
        return c**r + r * comb(m, ell - 1) * c ** (r - 1)
    if ell < m * (r - 1):
        s = ell // m
        return comb(r, s) * m ** (r - s)
    return r * m + (1 if ell == r * m else 0)


subset_checks = 0
polynomial_checks = 0
minimum_checks = 0
parameter_pairs = 0

for r in range(2, 5):
    for m in range(2, 5):
        adj = make_graph(r, m)
        n = len(adj)
        for ell in range(1, r * m + 1):
            parameter_pairs += 1
            actual = [0] * (n + 1)
            for mask in range(1 << n):
                S = {v for v in range(n) if (mask >> v) & 1}
                dynamic = ell_forces(adj, S, ell)
                structural = criterion(r, m, S, ell)
                subset_checks += 1
                if dynamic != structural:
                    raise AssertionError(("criterion", r, m, ell, S, dynamic, structural))
                if dynamic:
                    actual[len(S)] += 1

            expected = closed_coeffs(r, m, ell)
            if actual != expected:
                raise AssertionError(("polynomial", r, m, ell, actual, expected))
            polynomial_checks += 1

            minimum = next(i for i, count in enumerate(actual) if count)
            if minimum != minimum_formula(r, m, ell):
                raise AssertionError(("minimum", r, m, ell, minimum))
            if actual[minimum] != minimum_count_formula(r, m, ell):
                raise AssertionError(("minimum_count", r, m, ell, actual[minimum]))
            minimum_checks += 1

print(
    "VERIFY_OK "
    f"parameter_pairs={parameter_pairs} "
    f"subset_checks={subset_checks} "
    f"polynomial_checks={polynomial_checks} "
    f"minimum_checks={minimum_checks} "
    f"max_order={1 + 4 * 4}"
)
