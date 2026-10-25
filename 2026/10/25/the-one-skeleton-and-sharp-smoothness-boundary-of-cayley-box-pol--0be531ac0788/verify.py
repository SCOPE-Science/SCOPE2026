"""Exact, independent small-instance checks for Cayley sums of coordinate boxes.

Run: python3 verify.py (Python 3 standard library only).
The finite checks corroborate but do not replace the proof for all dimensions.
"""
from fractions import Fraction
from itertools import product
from math import gcd
from random import Random


def rank(rows):
    if not rows:
        return 0
    B = [[Fraction(x) for x in row] for row in rows]
    h, w, p = len(B), len(B[0]), 0
    for col in range(w):
        k = next((i for i in range(p, h) if B[i][col]), None)
        if k is None:
            continue
        B[p], B[k] = B[k], B[p]
        z = B[p][col]
        for j in range(col, w):
            B[p][j] /= z
        for i in range(p + 1, h):
            z = B[i][col]
            if z:
                for j in range(col, w):
                    B[i][j] -= z * B[p][j]
        p += 1
        if p == h:
            break
    return p


def determinant(rows):
    N = len(rows)
    M = [[Fraction(v) for v in row] for row in rows]
    ans = Fraction(1)
    for c in range(N):
        piv = next((k for k in range(c, N) if M[k][c]), None)
        if piv is None:
            return 0
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            ans = -ans
        z = M[c][c]
        ans *= z
        for k in range(c + 1, N):
            m = M[k][c] / z
            if m:
                for j in range(c + 1, N):
                    M[k][j] -= m * M[c][j]
                M[k][c] = 0
    assert ans.denominator == 1
    return int(ans)


def vertices(A):
    n, d = len(A), len(A[0]) - 1
    out = []
    for j in range(d + 1):
        S = [i for i in range(n) if A[i][j] > 0]
        for bits in product((0, 1), repeat=len(S)):
            b = dict(zip(S, bits))
            x = tuple(A[i][j] * b.get(i, 0) for i in range(n))
            y = tuple(int(j == k) for k in range(1, d + 1))
            out.append((j, b, x + y))
    return out


def active(A, v):
    n, d = len(A), len(A[0]) - 1
    x = v[:n]
    y = v[n:]
    lam = (1 - sum(y),) + tuple(y)
    out = set()
    for j in range(d + 1):
        if lam[j] == 0:
            out.add(j)
    for i in range(n):
        if x[i] == 0:
            out.add(d + 1 + i)
        if x[i] == sum(A[i][j] * lam[j] for j in range(d + 1)):
            out.add(d + 1 + n + i)
    return out


def normals(A):
    n, d = len(A), len(A[0]) - 1
    rows = []
    for j in range(d + 1):
        rows.append(tuple([0] * n + ([int(j == k) for k in range(1, d + 1)] if j else [-1] * d)))
    for i in range(n):
        rows.append(tuple(int(i == k) for k in range(n)) + tuple([0] * d))
    for i in range(n):
        rows.append(tuple(-int(i == k) for k in range(n)) + tuple(A[i][k] - A[i][0] for k in range(1, d + 1)))
    return rows


def predicted(A):
    n, d = len(A), len(A[0]) - 1
    supp = [frozenset(j for j in range(d + 1) if A[i][j] > 0) for i in range(n)]
    singleton = [next(iter(s)) for s in supp if len(s) == 1]
    simple = all(len(s) in (1, d + 1) for s in supp) and len(singleton) == len(set(singleton))
    smooth = simple and all(A[i][next(iter(s))] == 1 for i, s in enumerate(supp) if len(s) == 1)
    return simple, smooth


def check(A):
    n, d = len(A), len(A[0]) - 1
    D = n + d
    V = vertices(A)
    h = [active(A, v[2]) for v in V]
    normals_matrix = normals(A)
    assert rank([tuple(b - a for a, b in zip(V[0][2], v[2])) for v in V[1:]]) == D
    neighbours = [[] for _ in V]
    within, between = 0, 0
    for u in range(len(V)):
        j, bu, xu = V[u]
        for v in range(u + 1, len(V)):
            l, bv, xv = V[v]
            shared = h[u] & h[v]
            actual = rank([normals_matrix[i] for i in sorted(shared)]) == D - 1
            expected = (sum(x != y for x, y in zip(xu[:n], xv[:n])) == 1 if j == l else
                        all(bu[i] == bv[i] for i in bu.keys() & bv.keys()))
            # Same-layer vertices differ in one positive coordinate; between layers they
            # must select the same lower/upper face on every common positive row.
            assert actual == expected, (A, u, v, actual, expected)
            if actual:
                neighbours[u].append(v)
                neighbours[v].append(u)
                if j == l:
                    within += 1
                else:
                    between += 1
    supports = [frozenset(i for i in range(n) if A[i][j] > 0) for j in range(d + 1)]
    formula_within = sum(len(s) * (2 ** (len(s) - 1)) for s in supports)
    formula_between = sum(2 ** len(supports[j] | supports[l]) for j in range(d + 1) for l in range(j + 1, d + 1))
    assert (within, between) == (formula_within, formula_between)
    for u, (j, bu, xu) in enumerate(V):
        degree = len(supports[j]) + sum(2 ** len(supports[l] - supports[j]) for l in range(d + 1) if l != j)
        assert len(neighbours[u]) == degree
    Psimple, Psmooth = predicted(A)
    assert all(len(L) == D for L in neighbours) == Psimple
    if Psimple:
        smooth = True
        for u, (_, _, xu) in enumerate(V):
            directions = []
            for v in neighbours[u]:
                delta = [v - u for u, v in zip(xu, V[v][2])]
                g = gcd(*delta)
                directions.append([x // g for x in delta])
            if abs(determinant(directions)) != 1:
                smooth = False
        assert smooth == Psmooth
    return len(V), within + between


def main():
    total = 0
    for n, d in [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1)]:
        for flat in product(range(3), repeat=n * (d + 1)):
            A = [flat[i * (d + 1):(i + 1) * (d + 1)] for i in range(n)]
            if not all(any(row) for row in A):
                continue
            check(A)
            total += 1
    rng = Random(71)
    for n, d in [(3, 2), (2, 3), (3, 3), (4, 2)]:
        for _ in range(100):
            while True:
                A = [[rng.randrange(4) for _ in range(d + 1)] for _ in range(n)]
                if all(any(row) for row in A):
                    break
            check(A)
            total += 1
    # Source-motivated sparse-support family: one large cube layer plus d 1-cubes.
    for d in range(2, 51):
        S = [frozenset(range(d))] + [frozenset({i}) for i in range(d)]
        degree0 = len(S[0]) + sum(2 ** len(S[j] - S[0]) for j in range(1, d + 1))
        degreel = len(S[1]) + sum(2 ** len(S[j] - S[1]) for j in range(d + 1) if j != 1)
        assert degree0 == 2*d and degreel == 2**(d-1) + 2*d - 1
        assert degreel > 2*d
    print(f"EXACT_OK matrices={total} graph_edge_count_simplicity_smoothness=verified sparse_family_d=2..50")


if __name__ == '__main__':
    main()
