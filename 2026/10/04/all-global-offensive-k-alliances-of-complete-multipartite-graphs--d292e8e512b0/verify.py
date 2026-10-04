from math import comb


def profiles(total):
    out = []
    def rec(rem, last, cur):
        if rem == 0:
            if len(cur) >= 2:
                out.append(tuple(cur))
            return
        for x in range(last, rem + 1):
            rec(rem - x, x, cur + [x])
    rec(total, 1, [])
    return out


def build(ns):
    parts = []
    idx = 0
    for n in ns:
        part = list(range(idx, idx + n))
        parts.append(part)
        idx += n
    part_of = [0] * idx
    for i, part in enumerate(parts):
        for v in part:
            part_of[v] = i
    adj = [set() for _ in range(idx)]
    for u in range(idx):
        for v in range(idx):
            if u != v and part_of[u] != part_of[v]:
                adj[u].add(v)
    return parts, adj


def literal(ns, mask, k):
    parts, adj = build(ns)
    n = sum(ns)
    selected = {v for v in range(n) if (mask >> v) & 1}
    if not selected:
        return False
    for v in range(n):
        if v not in selected:
            inside = len(adj[v] & selected)
            outside = len(adj[v] - selected)
            if inside < outside + k:
                return False
    return True


def criterion(ns, mask, k):
    parts, _ = build(ns)
    n = sum(ns)
    s = mask.bit_count()
    if s == 0:
        return False
    for ni, part in zip(ns, parts):
        si = sum((mask >> v) & 1 for v in part)
        if si < ni:
            h = (n - ni + k + 1) // 2
            if s - si < h:
                return False
    return True


def formula_coeffs(ns, k):
    n = sum(ns)
    coeff = [0] * (n + 1)
    for s in range(1, n + 1):
        poly = [1]
        for ni in ns:
            h = (n - ni + k + 1) // 2
            u = min(ni - 1, s - h)
            fac = [0] * (ni + 1)
            if u >= 0:
                for j in range(u + 1):
                    fac[j] = comb(ni, j)
            fac[ni] = 1
            nxt = [0] * (len(poly) + ni)
            for a, av in enumerate(poly):
                for j, bv in enumerate(fac):
                    nxt[a + j] += av * bv
            poly = nxt
        coeff[s] = poly[s]
    return coeff


def published_bipartite_gamma(ns, k):
    t, r = sorted(ns)
    if k >= t + 1:
        return r
    q = (r + k + 1) // 2 + (t + k + 1) // 2
    return t if q >= t else q


def published_bipartite_k1_set(ns, mask):
    m, n = ns
    parts, _ = build(ns)
    a, b = parts
    selected = {v for v in range(m + n) if (mask >> v) & 1}
    if set(a) <= selected or set(b) <= selected:
        return True
    sa = len(set(a) & selected)
    sb = len(set(b) & selected)
    return sa >= 1 + m // 2 and sb >= 1 + n // 2


profile_count = 0
parameter_checks = 0
subset_checks = 0
criterion_checks = 0
coefficient_checks = 0
bipartite_gamma_checks = 0
bipartite_k1_set_checks = 0

for n in range(2, 10):
    for ns in profiles(n):
        profile_count += 1
        delta = n - min(ns)
        for k in range(1, delta + 1):
            parameter_checks += 1
            exact = [0] * (n + 1)
            for mask in range(1 << n):
                subset_checks += 1
                a = literal(ns, mask, k)
                b = criterion(ns, mask, k)
                criterion_checks += 1
                if a != b:
                    raise AssertionError(("criterion", ns, k, mask, a, b))
                if a:
                    exact[mask.bit_count()] += 1
                if len(ns) == 2 and k == 1 and min(ns) >= 2:
                    c = published_bipartite_k1_set(ns, mask)
                    bipartite_k1_set_checks += 1
                    if a != c:
                        raise AssertionError(("bipartite-k1-set", ns, mask, a, c))
            formula = formula_coeffs(ns, k)
            for s in range(n + 1):
                coefficient_checks += 1
                if exact[s] != formula[s]:
                    raise AssertionError(("coefficient", ns, k, s, exact[s], formula[s]))
            if len(ns) == 2:
                gamma = next(s for s, count in enumerate(exact) if count)
                expected = published_bipartite_gamma(ns, k)
                bipartite_gamma_checks += 1
                if gamma != expected:
                    raise AssertionError(("bipartite-gamma", ns, k, gamma, expected))

print(
    "VERIFY_OK "
    f"profiles={profile_count} "
    f"parameter_checks={parameter_checks} "
    f"subset_checks={subset_checks} "
    f"criterion_checks={criterion_checks} "
    f"coefficient_checks={coefficient_checks} "
    f"bipartite_gamma_checks={bipartite_gamma_checks} "
    f"bipartite_k1_set_checks={bipartite_k1_set_checks} "
    "max_order=9"
)
