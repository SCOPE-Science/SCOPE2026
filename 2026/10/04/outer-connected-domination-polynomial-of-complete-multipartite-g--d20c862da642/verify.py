from itertools import product
from math import comb


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for a in range(lo, n + 1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


def graph(ns):
    part = []
    for i, n in enumerate(ns):
        part.extend([i] * n)
    N = len(part)
    adj = [[u != v and part[u] != part[v] for v in range(N)] for u in range(N)]
    return part, adj


def connected_nonempty(adj, vertices):
    vertices = set(vertices)
    if not vertices:
        return False
    start = next(iter(vertices))
    seen = {start}
    stack = [start]
    while stack:
        u = stack.pop()
        for v in vertices:
            if v not in seen and adj[u][v]:
                seen.add(v)
                stack.append(v)
    return seen == vertices


def literal_ocd(ns, mask):
    part, adj = graph(ns)
    N = len(part)
    D = {v for v in range(N) if (mask >> v) & 1}
    if len(D) == N:
        return True
    if not D:
        return False
    for v in range(N):
        if v not in D and not any(adj[v][u] for u in D):
            return False
    C = set(range(N)) - D
    return connected_nonempty(adj, C)


def criterion(ns, mask):
    N = sum(ns)
    D = {v for v in range(N) if (mask >> v) & 1}
    if len(D) == N:
        return True
    ds = []
    p = 0
    for n in ns:
        ds.append(sum((mask >> v) & 1 for v in range(p, p + n)))
        p += n
    cs = [n - d for n, d in zip(ns, ds)]
    complement_connected = sum(cs) == 1 or sum(c > 0 for c in cs) >= 2
    support = sum(d > 0 for d in ds)
    dominates = support >= 2 or any(support == 1 and ds[i] == ns[i] for i in range(len(ns)))
    return complement_connected and dominates


def formula_coefficients(ns):
    N = sum(ns)
    coeff = [comb(N, k) for k in range(N + 1)]
    coeff[0] -= 1
    for n in ns:
        for d in range(1, n):
            coeff[d] -= comb(n, d)
        for c in range(2, n + 1):
            coeff[N - c] -= comb(n, c)
    return coeff


def published_gamma(ns):
    # Theorem 4(iii) in arXiv:1112.0846: sizes are nondecreasing.
    if len(ns) == 2 and ns[0] == 1:
        return ns[1]
    if len(ns) >= 3 and ns[0] == 1:
        return 1
    return 2


profiles = subset_checks = valid_sets = coefficient_checks = gamma_checks = star_checks = 0
for N in range(2, 11):
    for ns in partitions(N):
        if len(ns) < 2:
            continue
        profiles += 1
        counts = [0] * (N + 1)
        for mask in range(1 << N):
            a = literal_ocd(ns, mask)
            b = criterion(ns, mask)
            subset_checks += 1
            if a != b:
                raise AssertionError(("criterion", ns, mask, a, b))
            if a:
                counts[mask.bit_count()] += 1
                valid_sets += 1
        pred = formula_coefficients(ns)
        coefficient_checks += N + 1
        if counts != pred:
            raise AssertionError(("polynomial", ns, counts, pred))
        gamma = next(k for k, v in enumerate(counts) if v)
        gamma_checks += 1
        if gamma != published_gamma(ns):
            raise AssertionError(("published_gamma", ns, gamma, published_gamma(ns)))
        if len(ns) == 2 and ns[0] == 1:
            n = ns[1]
            star = [0] * (N + 1)
            star[n] = n + 1
            star[n + 1] = 1
            star_checks += 1
            if counts != star:
                raise AssertionError(("published_star_polynomial", ns, counts, star))
print(f"VERIFY_OK profiles={profiles} subset_checks={subset_checks} valid_sets={valid_sets} coefficient_checks={coefficient_checks} gamma_checks={gamma_checks} star_checks={star_checks} max_order=10")
