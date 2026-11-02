"""Exact-arithmetic finite checks for weighted network trust-game core thresholds.

Run: python verify.py
This checks finite sample instances; the general theorems require the accompanying proof.
"""
from fractions import Fraction as F
from random import Random


def coalitions(n):
    return [s for s in range(1 << n)]


def valuation(weights, subset, alpha):
    n = len(weights)
    inside = F(0)
    external = F(0)
    for j in range(n):
        if not ((subset >> j) & 1):
            continue
        inside += sum((weights[i][j] for i in range(n) if (subset >> i) & 1 and weights[i][j] is not None), F(0))
        outgoing = [weights[i][j] for i in range(n)
                    if not ((subset >> i) & 1) and weights[i][j] is not None]
        if outgoing:
            external += min(outgoing)
    return alpha * inside + (1 - alpha) * external


def positive_components(weights):
    n = len(weights)
    seen = set()
    comps = []
    for i in range(n):
        if i in seen:
            continue
        stack = [i]
        cc = set()
        while stack:
            v = stack.pop()
            if v in cc:
                continue
            cc.add(v)
            for u in range(n):
                if u != v and ((weights[v][u] is not None and weights[v][u] > 0)
                               or (weights[u][v] is not None and weights[u][v] > 0)):
                    stack.append(u)
        seen |= cc
        comps.append(cc)
    return comps


def rational_rank(columns, n):
    """Independent exact Gaussian-elimination rank of edge-transfer vectors."""
    mat = [[F(0) for _ in columns] for __ in range(n)]
    for j, (u, v) in enumerate(columns):
        mat[u][j] = F(1)
        mat[v][j] = F(-1)
    rank = 0
    for col in range(len(columns)):
        p = next((r for r in range(rank, n) if mat[r][col] != 0), None)
        if p is None:
            continue
        mat[rank], mat[p] = mat[p], mat[rank]
        z = mat[rank][col]
        mat[rank] = [t/z for t in mat[rank]]
        for r in range(n):
            if r != rank and mat[r][col]:
                c = mat[r][col]
                mat[r] = [a-c*b for a, b in zip(mat[r], mat[rank])]
        rank += 1
    return rank


def check_case(weights, alpha):
    n = len(weights)
    full = (1 << n) - 1
    v = lambda s: valuation(weights, s, alpha)
    edges = [(i, j, weights[i][j]) for i in range(n) for j in range(n)
             if i != j and weights[i][j] is not None and weights[i][j] > 0]
    W = sum((w for _, _, w in edges), F(0))
    D = [sum((w for i, j, w in edges if j == k), F(0)) for k in range(n)]
    O = [sum((w for i, j, w in edges if i == k), F(0)) for k in range(n)]
    assert v(full) == alpha * W
    assert sum((v(full) - v(full & ~(1 << i)) for i in range(n)), F(0)) == (3 * alpha - 1) * W
    for i in range(n):
        assert v(full) - v(full & ~(1 << i)) == alpha * D[i] + (2 * alpha - 1) * O[i]
    if W == 0:
        assert all(v(s) == 0 for s in coalitions(n))
        return
    if alpha < F(1, 2):
        assert (3 * alpha - 1) * W < alpha * W
        return
    # One weighted endpoint-split per arc gives a point of the induced-edge game's core.
    rng = Random(n * 101 + len(edges) * 17 + int(alpha * 100))
    y = [F(0) for _ in range(n)]
    for i, j, w in edges:
        t = F(rng.randrange(5), 4)
        y[i] += w * t
        y[j] += w * (1 - t)
    x = [(1-alpha) * D[i] + (2 * alpha - 1) * y[i] for i in range(n)]
    assert sum(x, F(0)) == v(full)
    for s in coalitions(n):
        assert sum((x[i] for i in range(n) if (s >> i) & 1), F(0)) >= v(s), (n, alpha, s)
    if alpha == F(1, 2):
        assert x == [d/2 for d in D]
    else:
        comps = positive_components(weights)
        assert rational_rank([(i, j) for i, j, w in edges], n) == n - len(comps)
        for C in comps:
            s = sum(1 << i for i in C)
            assert v(s) + v(full ^ s) == v(full)
            assert sum((x[i] for i in C), F(0)) == v(s)
        # For any positive edge, shifting its split changes the full-game core point.
        for i, j, w in edges:
            z = x.copy()
            z[i] += (2*alpha-1)*w/2
            z[j] -= (2*alpha-1)*w/2
            # First ensure both endpoints had enough split freedom by constructing a midpoint base below.
            assert z[i] != x[i]
        ym = [F(0) for _ in range(n)]
        for i, j, w in edges:
            ym[i] += w/2
            ym[j] += w/2
        xm = [(1-alpha)*D[i] + (2*alpha-1)*ym[i] for i in range(n)]
        for i, j, w in edges:
            xp = xm.copy()
            xp[i] += (2*alpha-1)*w/4
            xp[j] -= (2*alpha-1)*w/4
            assert sum(xp, F(0)) == v(full)
            assert all(sum((xp[k] for k in range(n) if (s >> k) & 1), F(0)) >= v(s)
                       for s in coalitions(n))
    # Total balancedness witness for each induced subgame.
    for S in coalitions(n):
        vertices = [i for i in range(n) if (S >> i) & 1]
        b = {}
        for j in vertices:
            w_out = [weights[i][j] for i in range(n)
                     if not ((S >> i) & 1) and weights[i][j] is not None]
            b[j] = min(w_out) if w_out else F(0)
        q = {j: sum((weights[i][j] for i in vertices if weights[i][j] is not None), F(0)) + b[j]
             for j in vertices}
        yS = {j: F(0) for j in vertices}
        for i in vertices:
            for j in vertices:
                if i != j and weights[i][j] is not None:
                    yS[i] += weights[i][j]/2
                    yS[j] += weights[i][j]/2
        xS = {j: (1-alpha)*q[j] + (2*alpha-1)*yS[j] for j in vertices}
        assert sum(xS.values(), F(0)) == v(S)
        for T in coalitions(n):
            if (T & S) != T:
                continue
            assert sum((xS[j] for j in vertices if (T >> j) & 1), F(0)) >= v(T), (n, alpha, S, T)


def run():
    r = Random(20260518)
    count = 0
    alpha_values = [F(0), F(1, 4), F(2, 5), F(1, 2), F(3, 5), F(3, 4), F(1)]
    for n in range(2, 7):
        for case in range(73):
            weights = [[None for _ in range(n)] for __ in range(n)]
            if case >= 3:
                for i in range(n):
                    for j in range(n):
                        if i != j and r.randrange(5) != 0:
                            weights[i][j] = F(r.randrange(5), 4)
            elif case == 1:
                weights[0][1] = F(1)
            elif case == 2:
                weights[0][1] = F(0)
                weights[1][0] = F(1)
            for a in alpha_values:
                check_case(weights, a)
                count += 1
    print(f'VERIFY_OK rational_graph_parameter_cases={count} graph_profiles={5*73} parameters={len(alpha_values)}')

if __name__ == '__main__':
    run()
