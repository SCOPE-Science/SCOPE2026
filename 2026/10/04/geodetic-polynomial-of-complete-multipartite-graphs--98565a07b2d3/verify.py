#!/usr/bin/env python3
from itertools import product
from collections import deque
from math import comb

MAX_ORDER = 9
MAX_PARTS = 5


def profiles():
    for r in range(2, MAX_PARTS + 1):
        for ns in product(range(1, MAX_ORDER + 1), repeat=r):
            if sum(ns) <= MAX_ORDER:
                yield ns


def graph(ns):
    part = []
    for i, n in enumerate(ns):
        part += [i] * n
    N = len(part)
    adj = [[] for _ in range(N)]
    for u in range(N):
        for v in range(u + 1, N):
            if part[u] != part[v]:
                adj[u].append(v)
                adj[v].append(u)
    return part, adj


def distances(adj):
    N = len(adj)
    D = [[N + 1] * N for _ in range(N)]
    for s in range(N):
        D[s][s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if D[s][v] > D[s][u] + 1:
                    D[s][v] = D[s][u] + 1
                    q.append(v)
    return D


def literal_geodetic(mask, D):
    N = len(D)
    S = [v for v in range(N) if (mask >> v) & 1]
    if not S:
        return False
    covered = set(S)
    for a in range(len(S)):
        for b in range(a + 1, len(S)):
            x, y = S[a], S[b]
            dxy = D[x][y]
            for v in range(N):
                if D[x][v] + D[v][y] == dxy:
                    covered.add(v)
    return len(covered) == N


def structural(mask, ns, part):
    s = [0] * len(ns)
    for v, i in enumerate(part):
        if (mask >> v) & 1:
            s[i] += 1
    heavy = {i for i, x in enumerate(s) if x >= 2}
    return all(s[i] == ns[i] or bool(heavy - {i}) for i in range(len(ns)))


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_add(a, b, sign=1):
    n = max(len(a), len(b))
    out = a + [0] * (n - len(a))
    for i, x in enumerate(b):
        out[i] += sign * x
    return out


def formula_coeffs(ns):
    N = sum(ns)
    total = [comb(N, s) for s in range(N + 1)]
    A = [[1, n] for n in ns]
    B = []
    for n in ns:
        p = [comb(n, s) for s in range(n + 1)]
        p[0] -= 1
        if n >= 1:
            p[1] -= n
        B.append(p)

    noheavy = [1]
    for a in A:
        noheavy = poly_mul(noheavy, a)
    ans = poly_add(total, noheavy, -1)

    for i in range(len(ns)):
        q = B[i]
        for j, a in enumerate(A):
            if j != i:
                q = poly_mul(q, a)
        ans = poly_add(ans, q, -1)

    for i, n in enumerate(ns):
        if n < 2:
            continue
        q = [0] * n + [1]
        for j, a in enumerate(A):
            if j != i:
                q = poly_mul(q, a)
        ans = poly_add(ans, q, +1)

    if max(ns) == 1:
        q = [0] * N + [1]
        ans = poly_add(ans, q, +1)
    ans += [0] * (N + 1 - len(ans))
    return ans[:N + 1]


def min_formula(ns):
    N = sum(ns)
    nonsingle = [n for n in ns if n >= 2]
    if not nonsingle:
        return N
    m = min(nonsingle)
    if len(nonsingle) == 1:
        return m
    return min(m, 4)


def main():
    profile_count = subset_checks = criterion_checks = coefficient_checks = min_checks = 0
    for ns in profiles():
        profile_count += 1
        part, adj = graph(ns)
        D = distances(adj)
        N = sum(ns)
        counts = [0] * (N + 1)
        minimum = None
        for mask in range(1 << N):
            subset_checks += 1
            a = literal_geodetic(mask, D)
            b = structural(mask, ns, part)
            criterion_checks += 1
            if a != b:
                raise AssertionError(("criterion", ns, mask, a, b))
            if a:
                k = mask.bit_count()
                counts[k] += 1
                minimum = k if minimum is None else min(minimum, k)
        f = formula_coeffs(ns)
        for k in range(N + 1):
            coefficient_checks += 1
            if counts[k] != f[k]:
                raise AssertionError(("coefficient", ns, k, counts[k], f[k]))
        min_checks += 1
        if minimum != min_formula(ns):
            raise AssertionError(("minimum", ns, minimum, min_formula(ns)))
    print(
        "VERIFY_OK"
        f" profiles={profile_count}"
        f" subset_checks={subset_checks}"
        f" criterion_checks={criterion_checks}"
        f" coefficient_checks={coefficient_checks}"
        f" min_checks={min_checks}"
        f" max_order={MAX_ORDER}"
        f" max_parts={MAX_PARTS}"
    )


if __name__ == "__main__":
    main()
