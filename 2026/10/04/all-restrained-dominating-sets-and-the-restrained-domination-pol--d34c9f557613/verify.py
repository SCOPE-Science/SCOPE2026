#!/usr/bin/env python3
from itertools import product
from math import comb


def padd(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]


def psub(a, b):
    n = max(len(a), len(b))
    r = [(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0) for i in range(n)]
    while len(r) > 1 and r[-1] == 0:
        r.pop()
    return r


def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def binpoly(n):
    return [comb(n, k) for k in range(n + 1)]


def monomial(n):
    return [0] * n + [1]


def nonempty(n):
    return psub(binpoly(n), [1])


def proper_nonempty(n):
    return psub(nonempty(n), monomial(n))


def formula(alpha, beta):
    p = len(alpha)
    q = [1]
    for a in range(p):
        for b in range(p):
            if b < a:
                fa = pmul(nonempty(alpha[a]), binpoly(sum(alpha[a + 1:])))
                fb = pmul(binpoly(sum(beta[:b])), nonempty(beta[b]))
            elif b == a:
                fa = psub(
                    pmul(nonempty(alpha[a]), binpoly(sum(alpha[a + 1:]))),
                    monomial(sum(alpha[a:])),
                )
                fb = psub(
                    pmul(binpoly(sum(beta[:b])), nonempty(beta[b])),
                    monomial(sum(beta[:b + 1])),
                )
            else:
                fa = pmul(
                    pmul(nonempty(alpha[a]), binpoly(sum(alpha[a + 1:b]))),
                    proper_nonempty(sum(alpha[b:])),
                )
                fb = pmul(
                    pmul(proper_nonempty(sum(beta[:a + 1])), binpoly(sum(beta[a + 1:b]))),
                    nonempty(beta[b]),
                )
            q = padd(q, pmul(fa, fb))
    return q


def build(alpha, beta):
    vertices = []
    for i, n in enumerate(alpha):
        for k in range(n):
            vertices.append(("A", i, k))
    for j, n in enumerate(beta):
        for k in range(n):
            vertices.append(("B", j, k))
    n = len(vertices)
    adj = [set() for _ in range(n)]
    for u, (side_u, idx_u, _) in enumerate(vertices):
        for v, (side_v, idx_v, _) in enumerate(vertices):
            if side_u == "A" and side_v == "B" and idx_v <= idx_u:
                adj[u].add(v)
            elif side_u == "B" and side_v == "A" and idx_u <= idx_v:
                adj[u].add(v)
    return vertices, adj


def is_restrained(mask, adj):
    n = len(adj)
    allv = set(range(n))
    s = {v for v in range(n) if (mask >> v) & 1}
    t = allv - s
    for v in t:
        if not (adj[v] & s):
            return False
        if not (adj[v] & t):
            return False
    return True


def boundary_characterization(mask, vertices):
    n = len(vertices)
    s = {v for v in range(n) if (mask >> v) & 1}
    t = set(range(n)) - s
    if not t:
        return True
    ta = [v for v in t if vertices[v][0] == "A"]
    tb = [v for v in t if vertices[v][0] == "B"]
    if not ta or not tb:
        return False
    a = min(vertices[v][1] for v in ta)
    b = max(vertices[v][1] for v in tb)
    prefix_b = [v for v, z in enumerate(vertices) if z[0] == "B" and z[1] <= a]
    suffix_a = [v for v, z in enumerate(vertices) if z[0] == "A" and z[1] >= b]
    t_prefix = sum(v in t for v in prefix_b)
    t_suffix = sum(v in t for v in suffix_a)
    return 0 < t_prefix < len(prefix_b) and 0 < t_suffix < len(suffix_a)


def brute(alpha, beta):
    vertices, adj = build(alpha, beta)
    n = len(vertices)
    coeff = [0] * (n + 1)
    for mask in range(1 << n):
        rd = is_restrained(mask, adj)
        bc = boundary_characterization(mask, vertices)
        if rd != bc:
            raise AssertionError((alpha, beta, mask, rd, bc))
        if rd:
            complement_size = n - mask.bit_count()
            coeff[complement_size] += 1
    return coeff


def main():
    profiles = 0
    subsets = 0
    classification_checks = 0
    coefficient_checks = 0
    max_order = 0
    for p in range(1, 5):
        for alpha in product(range(1, 4), repeat=p):
            for beta in product(range(1, 4), repeat=p):
                n = sum(alpha) + sum(beta)
                if n > 11:
                    continue
                profiles += 1
                max_order = max(max_order, n)
                subsets += 1 << n
                classification_checks += 1 << n
                got = brute(alpha, beta)
                want = formula(alpha, beta)
                want = want + [0] * (len(got) - len(want))
                if want != got:
                    raise AssertionError((alpha, beta, want, got))
                coefficient_checks += len(got)
    print(
        "VERIFY_OK "
        f"profiles={profiles} subsets={subsets} "
        f"classification_checks={classification_checks} "
        f"coefficient_checks={coefficient_checks} max_order={max_order}"
    )


if __name__ == "__main__":
    main()
