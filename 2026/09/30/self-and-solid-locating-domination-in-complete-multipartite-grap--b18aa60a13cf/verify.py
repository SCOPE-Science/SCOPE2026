from itertools import product
from math import prod


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for x in range(lo, n + 1):
        for rest in partitions(n - x, x):
            yield (x,) + rest


def graph(parts):
    part_of = []
    for i, a in enumerate(parts):
        part_of += [i] * a
    N = len(part_of)
    closed = []
    for u in range(N):
        closed.append({u} | {v for v in range(N) if part_of[v] != part_of[u]})
    return closed


def ident(C, u, closed):
    return C & closed[u]


def is_dld(C, closed):
    V = set(range(len(closed)))
    U = V - C
    for u in U:
        if not ident(C, u, closed):
            return False
    for u in U:
        for v in U:
            if u != v and not (ident(C, u, closed) - ident(C, v, closed)):
                return False
    return True


def is_sld(C, closed):
    V = set(range(len(closed)))
    U = V - C
    for u in U:
        iu = ident(C, u, closed)
        if not iu:
            return False
        inter = set(V)
        for c in iu:
            inter &= closed[c]
        if inter != {u}:
            return False
    return True


def elementary(vals, k):
    dp = [1] + [0] * len(vals)
    for a in vals:
        for j in range(len(vals), 0, -1):
            dp[j] += a * dp[j - 1]
    return dp[k]


def predicted(parts):
    N = sum(parts)
    nons = [a for a in parts if a >= 2]
    p = len(nons)
    s = sum(a == 1 for a in parts)
    dld = [0] * (N + 1)
    sld = [0] * (N + 1)
    dld[N] = 1
    dld[N - 1] = N
    for k in range(2, p + 1):
        dld[N - k] = elementary(nons, k)
    sld[N] = 1
    if s == 1:
        sld[N - 1] = 1
    gamma_dld = N - max(1, p)
    gamma_sld = N - 1 if s == 1 else N
    min_count_dld = prod(nons) if p >= 2 else N
    min_count_sld = 1
    return dld, sld, gamma_dld, gamma_sld, min_count_dld, min_count_sld


types = 0
checks = 0
for N in range(2, 9):
    for parts in partitions(N):
        if len(parts) < 2:
            continue
        types += 1
        closed = graph(parts)
        dld = [0] * (N + 1)
        sld = [0] * (N + 1)
        for mask in range(1 << N):
            C = {v for v in range(N) if (mask >> v) & 1}
            k = len(C)
            if is_dld(C, closed):
                dld[k] += 1
            if is_sld(C, closed):
                sld[k] += 1
            checks += 2
        pd, ps, gd, gs, cd, cs = predicted(parts)
        assert dld == pd, (parts, 'DLD histogram', dld, pd)
        assert sld == ps, (parts, 'SLD histogram', sld, ps)
        assert next(k for k, x in enumerate(dld) if x) == gd
        assert next(k for k, x in enumerate(sld) if x) == gs
        assert dld[gd] == cd
        assert sld[gs] == cs

print('VERIFY_OK types', types, 'checks', checks)
