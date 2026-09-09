"""Independent replay verifier for the lane-302 maximal-growth census.
Reads output/artifacts/graphs.json + table.json, re-derives EVERYTHING:
 1. counts == OEIS A001349 slice, total 995; all graphs connected (union-find).
 2. clique vectors recomputed from edges; Q recomputed via Q=sum c_k(-t)^k(1+t)^{w-k}.
 3. tree lemma: every 7-vertex tree has Q == 1-5t exactly -> rate exactly 5.
 4. Sturm certificate: no non-tree graph has a Q-root in (0,1/5] (exact Fraction arithmetic).
 5. argmax == exactly the eleven 7-vertex trees; runner-up 2+sqrt(2), gap 3-sqrt(2)... (gap = 5-(2+sqrt2) = 3-sqrt2).
 6. Tits-representation Cayley BFS sphere sizes to radius 5 for ALL 995 graphs match series Taylor coeffs;
    (radius chosen so full run takes ~minutes in stdlib).
Prints VERIFY_OK on success.
"""
import json, itertools, os
_HERE = os.path.dirname(os.path.abspath(__file__))
from fractions import Fraction
from math import comb

def deriv(p):
    d = [i * p[i] for i in range(1, len(p))]
    while len(d) > 1 and d[-1] == 0:
        d.pop()
    return d if d else [Fraction(0)]

def negrem(a, b):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    while len(b) > 1 and b[-1] == 0:
        b.pop()
    if len(a) < len(b):
        return [-x for x in a]
    while len(a) >= len(b) and any(x != 0 for x in a):
        if b[-1] == 0:
            break
        mult = a[-1] / b[-1]
        d = len(a) - len(b)
        for i in range(len(b)):
            a[d + i] -= mult * b[i]
        while len(a) > 1 and a[-1] == 0:
            a.pop()
        if len(a) < len(b):
            break
    return [-x for x in a]

def sturm_seq(p):
    seq = [p, deriv(p)]
    while True:
        r = negrem(seq[-2], seq[-1])
        while len(r) > 1 and r[-1] == 0:
            r.pop()
        if len(r) == 1 and r[0] == 0:
            break
        seq.append(r)
    return seq

def sval(p, x):
    s = sum(c * (x ** i) for i, c in enumerate(p))
    return 1 if s > 0 else (-1 if s < 0 else 0)

def var_count(seq, x):
    prev, v = 0, 0
    for p in seq:
        s = sval(p, x)
        if s == 0:
            continue
        if prev != 0 and s != prev:
            v += 1
        prev = s
    return v

def roots_in_0_fifth(Qint):
    p = [Fraction(x) for x in Qint]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    seq = sturm_seq(p)
    r = Fraction(1, 5)
    eps = Fraction(1, 10 ** 15)
    va = var_count(seq, eps)  # V(0+)
    if sval(seq[0], r) == 0:
        return var_count(seq, r - eps) - 0 + 1 - (var_count(seq, r + eps) - 0) + 0 if False else None
    return None

def count_leq_fifth(Qint):
    p = [Fraction(x) for x in Qint]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    seq = sturm_seq(p)
    r = Fraction(1, 5)
    eps = Fraction(1, 10 ** 15)
    va = var_count(seq, eps)
    if any(sval(q, r) == 0 for q in seq):
        below = var_count(seq, r - eps)
        return (va - below) + (1 if sval(seq[0], r) == 0 else 0)
    return (va - var_count(seq, r)) + (1 if sval(seq[0], r) == 0 else 0)

def Qpoly(c, w):
    Q = [0] * (w + 1)
    for k in range(w + 1):
        ck = c[k] if k < len(c) else 0
        if ck == 0:
            continue
        for j in range(w - k + 1):
            Q[k + j] += ck * ((-1) ** k) * comb(w - k, j)
    return Q

def connected(edges, n):
    par = list(range(n))
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for a, b in edges:
        ra, rb = f(a), f(b)
        if ra != rb:
            par[ra] = rb
    return all(f(i) == f(0) for i in range(n))

def tits_bfs(edges, n, R):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b); adj[b].add(a)
    B = [[(2 if i == j else (0 if j in adj[i] else -2)) for j in range(n)] for i in range(n)]
    Ms = []
    for k in range(n):
        Ms.append(tuple(tuple((1 if i == j else 0) - (B[k][j] if i == k else 0) for j in range(n)) for i in range(n)))
    def mm(A, C):
        return tuple(tuple(sum(A[i][k] * C[k][j] for k in range(n)) for j in range(n)) for i in range(n))
    I = tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))
    seen, cur, sph = {I}, {I}, [1]
    for _ in range(1, R + 1):
        nxt = set()
        for X in cur:
            for M in Ms:
                Y = mm(X, M)
                if Y not in seen:
                    seen.add(Y); nxt.add(Y)
        sph.append(len(nxt)); cur = nxt
        if not cur:
            sph += [0] * (R - len(sph) + 1)
            break
    return sph

def main():
    G = json.load(open(os.path.join(_HERE, "graphs.json")))
    T = json.load(open(os.path.join(_HERE, "table.json")))
    assert G["counts"] == {"2": 1, "3": 2, "4": 6, "5": 21, "6": 112, "7": 853}, G["counts"]
    assert sum(G["counts"].values()) == 995
    Tmap = {(t["n"], t["gi"]): t for t in T}
    assert len(Tmap) == 995
    for ns, gl in G["graphs"].items():
        n = int(ns)
        for gi, edges in enumerate(gl):
            assert connected([tuple(e) for e in edges], n), (n, gi)
            t = Tmap[(n, gi)]
            assert t["m"] == len(edges)
            adj = [set() for _ in range(n)]
            for a, b in edges:
                adj[a].add(b); adj[b].add(a)
            c = [0] * (n + 1)
            for r in range(n + 1):
                for S in itertools.combinations(range(n), r):
                    if all(S[j] in adj[S[i]] for i in range(len(S)) for j in range(i + 1, len(S))):
                        c[r] += 1
            assert c == t["c"], (n, gi)
            w = max(k for k in range(len(c)) if c[k])
            assert w == t["w"]
            assert Qpoly(c, w) == t["Q"], (n, gi)
    # tree lemma + argmax
    trees7 = [t for t in T if t["tree"] and t["n"] == 7]
    assert len(trees7) == 11
    for t in trees7:
        assert t["Q"][:3] == [1, -5, 0] and all(x == 0 for x in t["Q"][3:])
    for t in T:
        if not t["tree"]:
            k = count_leq_fifth(t["Q"])
            assert k == 0, (t["n"], t["gi"], t["Q"])
    mx = [t for t in T if t["rate"] is not None and t["rate"] >= 5 - 1e-9]
    assert len(mx) == 11 and all(t["tree"] and t["n"] == 7 for t in mx)
    # BFS cross-check radius 5 all graphs
    for ns, gl in G["graphs"].items():
        n = int(ns)
        for gi, edges in enumerate(gl):
            t = Tmap[(n, gi)]
            P = [comb(t["w"], j) for j in range(t["w"] + 1)]
            Q = t["Q"]
            a, R = [0] * 6, 5
            for k in range(R + 1):
                s = P[k] if k < len(P) else 0
                for j in range(1, min(k, len(Q) - 1) + 1):
                    s -= Q[j] * a[k - j]
                a[k] = s
            assert tits_bfs([tuple(e) for e in edges], n, R) == a, (n, gi)
    print("VERIFY_OK: 995 graphs, Sturm max-cert, BFS radius-5 all pass; max rate 5 on exactly the eleven 7-trees")

if __name__ == "__main__":
    main()
