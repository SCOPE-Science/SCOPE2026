#!/usr/bin/env python3
"""Finite checks for the dimension-three four-request all-symbol result."""
from itertools import combinations, combinations_with_replacement


def rank_mod(rows, p):
    a = [list(map(lambda x: x % p, row)) for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c] % p), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] % p:
                f = a[i][c] % p
                a[i] = [(a[i][j] - f * a[r][j]) % p for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def in_span(v, vectors, p):
    if not vectors:
        return all(x % p == 0 for x in v)
    r1 = rank_mod([list(x) for x in vectors], p)
    r2 = rank_mod([list(x) for x in vectors] + [list(v)], p)
    return r1 == r2


def minimal_recovery_masks(columns, target, p):
    n = len(columns)
    good = []
    for mask in range(1, 1 << n):
        if any((g & mask) == g for g in good):
            continue
        vecs = [columns[i] for i in range(n) if (mask >> i) & 1]
        if in_span(target, vecs, p):
            good.append(mask)
    return good


def can_serve(request, recoveries):
    request = sorted(request, key=lambda x: len(recoveries[x]))

    def dfs(i, used):
        if i == len(request):
            return True
        for mask in recoveries[request[i]]:
            if mask & used == 0 and dfs(i + 1, used | mask):
                return True
        return False

    return dfs(0, 0)


def explicit_columns(p):
    minus = (-1) % p
    return [
        (1, 0, 0), (0, 1, 0), (0, 0, 1),
        (minus, minus, 0), (minus, 0, minus), (0, minus, minus),
        (1, 1, 1), (1, 1, 1),
    ]


def check_asb(p):
    cols = explicit_columns(p)
    unique = []
    for v in cols:
        if v not in unique:
            unique.append(v)
    recoveries = {v: minimal_recovery_masks(cols, v, p) for v in unique}
    total = 0
    for req in combinations_with_replacement(unique, 4):
        total += 1
        if not can_serve(req, recoveries):
            return False, total, req
    return True, total, None


def normalize_projective(v, p):
    for x in v:
        if x % p:
            inv = pow(x % p, -1, p)
            return tuple((y * inv) % p for y in v)
    raise ValueError("zero vector")


def projective_points(p):
    pts = set()
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if (x, y, z) != (0, 0, 0):
                    pts.add(normalize_projective((x, y, z), p))
    return sorted(pts)


def collinear(a, b, c, p):
    return rank_mod([a, b, c], p) <= 2


def perfect_matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        rest = items[1:j] + items[j + 1:]
        for tail in perfect_matchings(rest):
            yield ((a, b),) + tail


def has_local_matchings(S, p):
    S = tuple(S)
    for i, x in enumerate(S):
        rest = [S[j] for j in range(len(S)) if j != i]
        ok = False
        for matching in perfect_matchings(rest):
            if all(collinear(x, a, b, p) for a, b in matching):
                ok = True
                break
        if not ok:
            return False
    return True


def check_pg23_obstruction():
    p = 3
    pts = projective_points(p)
    tested = 0
    admissible = 0
    for idxs in combinations(range(len(pts)), 7):
        S = [pts[i] for i in idxs]
        if rank_mod(S, p) < 3:
            continue
        tested += 1
        if has_local_matchings(S, p):
            admissible += 1
    return len(pts), tested, admissible


if __name__ == "__main__":
    for p in (3, 5, 7):
        ok, total, bad = check_asb(p)
        print(f"F_{p}: checked {total} four-request multisets; ASB verification = {ok}")
        if bad is not None:
            print("first failing request:", bad)
    npts, tested, admissible = check_pg23_obstruction()
    print(f"PG(2,3): {npts} points; tested {tested} spanning 7-subsets; admissible = {admissible}")
