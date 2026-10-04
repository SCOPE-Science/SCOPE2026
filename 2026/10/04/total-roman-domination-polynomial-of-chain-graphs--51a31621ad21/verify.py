from itertools import product
from collections import Counter


def compositions(n, k, prefix=()):
    if k == 1:
        if n >= 1:
            yield prefix + (n,)
        return
    for x in range(1, n - k + 2):
        yield from compositions(n - x, k - 1, prefix + (x,))


def poly_mul(a, b):
    out = Counter()
    for i, ai in a.items():
        for j, bj in b.items():
            out[i + j] += ai * bj
    return out


def poly_sub(a, b):
    out = Counter(a)
    for k, v in b.items():
        out[k] -= v
        if out[k] == 0:
            del out[k]
    return out


def F(n, zero_allowed, two_allowed):
    choices = [1]
    if zero_allowed:
        choices.append(0)
    if two_allowed:
        choices.append(2)
    out = Counter({0: 1})
    one = Counter(choices)
    for _ in range(n):
        out = poly_mul(out, one)
    return out


def E(n, zero_allowed, two_allowed):
    out = F(n, zero_allowed, two_allowed)
    if zero_allowed:
        out = poly_sub(out, Counter({0: 1}))
    return out


def H(n, zero_allowed):
    return poly_sub(F(n, zero_allowed, 1), F(n, zero_allowed, 0))


def formula(alpha, beta):
    p = len(alpha)
    N = sum(alpha) + sum(beta)
    ans = Counter({N: 1})

    # Label 2 occurs only on the A side; s is the largest A-index carrying a 2.
    for s in range(p):
        q = Counter({0: 1})
        for i, n in enumerate(alpha):
            if i < s:
                fac = F(n, 0, 1)
            elif i == s:
                fac = H(n, 0)
            else:
                fac = F(n, 0, 0)
            q = poly_mul(q, fac)
        for j, n in enumerate(beta):
            if j == 0:
                fac = E(n, 1, 0)
            elif j <= s:
                fac = F(n, 1, 0)
            else:
                fac = F(n, 0, 0)
            q = poly_mul(q, fac)
        ans.update(q)

    # Label 2 occurs only on the B side; r is the smallest B-index carrying a 2.
    for r in range(p):
        q = Counter({0: 1})
        for j, n in enumerate(beta):
            if j < r:
                fac = F(n, 0, 0)
            elif j == r:
                fac = H(n, 0)
            else:
                fac = F(n, 0, 1)
            q = poly_mul(q, fac)
        for i, n in enumerate(alpha):
            if i == p - 1:
                fac = E(n, 1, 0)
            elif i >= r:
                fac = F(n, 1, 0)
            else:
                fac = F(n, 0, 0)
            q = poly_mul(q, fac)
        ans.update(q)

    # Label 2 occurs on both sides; r and s are the extremal B/A 2-indices.
    for r in range(p):
        for s in range(p):
            q = Counter({0: 1})
            q = poly_mul(q, H(alpha[s], int(s >= r)))
            q = poly_mul(q, H(beta[r], int(r <= s)))
            for i, n in enumerate(alpha):
                if i == s or i == p - 1:
                    continue
                q = poly_mul(q, F(n, int(i >= r), int(i <= s)))
            if s != p - 1:
                q = poly_mul(q, E(alpha[p - 1], 1, 0))
            for j, n in enumerate(beta):
                if j == r or j == 0:
                    continue
                q = poly_mul(q, F(n, int(j <= s), int(j >= r)))
            if r != 0:
                q = poly_mul(q, E(beta[0], 1, 0))
            ans.update(q)
    return ans


def build(alpha, beta):
    p = len(alpha)
    verts = []
    for side, sizes in (("A", alpha), ("B", beta)):
        for i, n in enumerate(sizes):
            for k in range(n):
                verts.append((side, i, k))
    idx = {v: i for i, v in enumerate(verts)}
    adj = [set() for _ in verts]
    for i, a_n in enumerate(alpha):
        for k in range(a_n):
            u = idx[("A", i, k)]
            for j in range(i + 1):
                for ell in range(beta[j]):
                    v = idx[("B", j, ell)]
                    adj[u].add(v)
                    adj[v].add(u)
    return verts, adj


def is_roman(labels, adj):
    return all(x != 0 or any(labels[u] == 2 for u in adj[v])
               for v, x in enumerate(labels))


def is_total_roman(labels, adj):
    if not is_roman(labels, adj):
        return False
    return all(x == 0 or any(labels[u] > 0 for u in adj[v])
               for v, x in enumerate(labels))


def boundary_positive_roman(labels, verts, adj, p):
    if not is_roman(labels, adj):
        return False
    ap = any(x > 0 for x, v in zip(labels, verts)
             if v[0] == "A" and v[1] == p - 1)
    b1 = any(x > 0 for x, v in zip(labels, verts)
             if v[0] == "B" and v[1] == 0)
    return ap and b1


profiles = 0
labelings = 0
valid = 0
criterion_checks = 0
coefficient_checks = 0
gamma_checks = 0
max_order = 9

for N in range(2, max_order + 1):
    for p in range(1, N // 2 + 1):
        for comp in compositions(N, 2 * p):
            alpha = comp[:p]
            beta = comp[p:]
            verts, adj = build(alpha, beta)
            profiles += 1
            brute = Counter()
            for labels in product((0, 1, 2), repeat=N):
                labelings += 1
                direct = is_total_roman(labels, adj)
                boundary = boundary_positive_roman(labels, verts, adj, p)
                criterion_checks += 1
                if direct != boundary:
                    raise SystemExit(("CRITERION_FAIL", alpha, beta, labels, direct, boundary))
                if direct:
                    brute[sum(labels)] += 1
                    valid += 1
            closed = formula(alpha, beta)
            for weight in set(brute) | set(closed):
                coefficient_checks += 1
                if brute[weight] != closed[weight]:
                    raise SystemExit(("COEFF_FAIL", alpha, beta, weight,
                                      brute[weight], closed[weight]))
            expected = min(N, sum(alpha) + 2, sum(beta) + 2, 4)
            gamma_checks += 1
            if min(brute) != expected:
                raise SystemExit(("GAMMA_FAIL", alpha, beta, min(brute), expected))

print(f"VERIFY_OK profiles={profiles} labelings={labelings} valid_functions={valid} "
      f"criterion_checks={criterion_checks} coefficient_checks={coefficient_checks} "
      f"gamma_checks={gamma_checks} max_order={max_order}")
