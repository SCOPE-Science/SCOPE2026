from itertools import product


def star_poset(p, q):
    # lower vertices 0,...,p-1; center p; upper p+1,...,p+q
    n = p + q + 1
    c = p
    leq = [[False] * n for _ in range(n)]
    for i in range(n):
        leq[i][i] = True
    for a in range(p):
        leq[a][c] = True
    for b in range(p + 1, n):
        leq[c][b] = True
    for a in range(p):
        for b in range(p + 1, n):
            leq[a][b] = True
    covers = [(a, c) for a in range(p)] + [(c, b) for b in range(p + 1, n)]
    return n, c, leq, covers


def intervals(n, leq, covers):
    ans = []
    for mask in range(1, 1 << n):
        S = {i for i in range(n) if mask >> i & 1}
        # convexity
        if any(
            leq[x][z] and leq[z][y] and z not in S
            for x in S for y in S for z in range(n)
        ):
            continue
        # connectedness in the induced Hasse graph
        seen = {next(iter(S))}
        changed = True
        while changed:
            changed = False
            for x, y in covers:
                if x in S and y in S and ((x in seen) != (y in seen)):
                    seen.add(x); seen.add(y); changed = True
        if seen == S:
            ans.append(frozenset(S))
    return ans


def minset(X, leq):
    return {x for x in X if not any(y != x and leq[y][x] for y in X)}


def maxset(X, leq):
    return {x for x in X if not any(y != x and leq[x][y] for y in X)}


def relative_downset(S, T, leq):
    return all(not leq[y][x] or y in S for x in S for y in T)


def relative_upset(C, T, leq):
    return all(not leq[x][y] or y in C for x in C for y in T)


def upper_extremal(S, T, leq, covers):
    if not relative_downset(S, T, leq):
        return False
    boundary = {y for x, y in covers if x in S and y in T - S}
    return boundary == maxset(set(T) - set(S), leq)


def lower_extremal(C, T, leq, covers):
    if not relative_upset(C, T, leq):
        return False
    boundary = {x for x, y in covers if y in C and x in T - C}
    return boundary == minset(set(T) - set(C), leq)


def aoki_gldim(p, q):
    n, c, leq, covers = star_poset(p, q)
    ints = intervals(n, leq, covers)
    best = -1
    best_pair = None
    for S in ints:
        for C in ints:
            W = [
                T for T in ints
                if S <= T and C <= T
                and upper_extremal(S, T, leq, covers)
                and lower_extremal(C, T, leq, covers)
            ]
            if len(W) == 1:  # saturated
                omega = len(maxset(set(C) - set(S), leq)) + len(minset(set(S) - set(C), leq))
                if omega > best:
                    best = omega
                    best_pair = (S, C, W[0])
    return best, len(ints), best_pair


if __name__ == '__main__':
    for r in range(1, 7):
        predicted = max(2, r)
        for p in range(r + 1):
            q = r - p
            got, nints, witness = aoki_gldim(p, q)
            assert got == predicted, (p, q, got, predicted, witness)
            print(f'r={r:2d} p={p:2d} q={q:2d} intervals={nints:3d} gldim={got}')
    print('All oriented stars with 1 <= r <= 6 match gldim = max(2,r).')
