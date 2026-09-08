"""Independent exact verifier (stdlib only) for the exhibited 3x3 game.
Re-derives from payoff entries: non-degeneracy, all 7 NE (indifference equalities
+ strict best-response inequalities), welfare table, and one-sided support census counts."""
from fractions import Fraction
import itertools

A = [[0,1,3],[0,3,0],[2,2,1]]
B = [[0,1,3],[2,3,1],[2,1,0]]

def solve(M, rhs):
    n = len(M)
    Aug = [list(M[i]) + [rhs[i]] for i in range(n)]
    for c in range(n):
        piv = next((r for r in range(c, n) if Aug[r][c] != 0), None)
        assert piv is not None, "singular indifference system"
        Aug[c], Aug[piv] = Aug[piv], Aug[c]
        for r in range(n):
            if r != c and Aug[r][c] != 0:
                f = Aug[r][c] / Aug[c][c]
                for cc in range(c, n + 1):
                    Aug[r][cc] -= f * Aug[c][cc]
    return [Aug[i][n] / Aug[i][i] for i in range(n)]

def enum_NE(A, B):
    out = []
    for ks in (1, 2, 3):
        for I in itertools.combinations(range(3), ks):
            for J in itertools.combinations(range(3), ks):
                k = ks
                M = [[Fraction(A[I[0]][j] - A[I[t]][j]) for j in J] for t in range(1, k)] + [[Fraction(1)] * k]
                rhs = [Fraction(0)] * (k - 1) + [Fraction(1)]
                try: y = solve(M, rhs)
                except AssertionError: continue
                if any(v <= 0 for v in y): continue
                uI = sum(Fraction(A[I[0]][j]) * y[c] for c, j in enumerate(J))
                if any(sum(Fraction(A[I[t]][j]) * y[c] for c, j in enumerate(J)) != uI for t in range(1, k)): continue
                if any(sum(Fraction(A[i][j]) * y[c] for c, j in enumerate(J)) >= uI for i in range(3) if i not in I): continue
                N = [[Fraction(B[i][J[0]] - B[i][J[t]]) for i in I] for t in range(1, k)] + [[Fraction(1)] * k]
                # transpose N to k x k in basis of I
                N = [[Fraction(B[I[r]][J[0]] - B[I[r]][J[t]]) for r in range(k)] for t in range(1, k)] + [[Fraction(1)] * k]
                try: x = solve(N, rhs)
                except AssertionError: continue
                if any(v <= 0 for v in x): continue
                vJ = sum(Fraction(B[I[r]][J[0]]) * x[r] for r in range(k))
                if any(sum(Fraction(B[I[r]][J[t]]) * x[r] for r in range(k)) != vJ for t in range(1, k)): continue
                if any(sum(Fraction(B[I[r]][j]) * x[r] for r in range(k)) >= vJ for j in range(3) if j not in J): continue
                out.append((I, J, tuple(x), tuple(y)))
    return out

# 1. non-degeneracy: pure best responses unique + no edge indifference ties
for i in range(3):
    m = max(B[i]); assert sum(1 for j in range(3) if B[i][j] == m) == 1, f"row {i} pure tie"
for j in range(3):
    m = max(A[i][j] for i in range(3)); assert sum(1 for i in range(3) if A[i][j] == m) == 1, f"col {j} pure tie"
for I in itertools.combinations(range(3), 2):
    k = [i for i in range(3) if i not in I][0]
    for J in itertools.combinations(range(3), 2):
        kk = [j for j in range(3) if j not in J][0]
        d0, d1 = B[I[0]][J[0]] - B[I[0]][J[1]], B[I[1]][J[0]] - B[I[1]][J[1]]
        if d0 == 0 and d1 == 0:
            g0, g1 = B[I[0]][kk] - B[I[0]][J[0]], B[I[1]][kk] - B[I[1]][J[0]]
            assert not (g0 == 0 or g1 == 0 or (g0 > 0) != (g1 > 0)), "degenerate col edge"
        elif (d0 == 0) != (d1 == 0):
            tv = B[I[0]][J[0]] if d0 == 0 else B[I[1]][J[0]]
            mm = max(B[I[0]]) if d0 == 0 else max(B[I[1]])
            assert tv < mm, "degenerate pure tie"
        elif (d0 > 0) != (d1 > 0):
            t = Fraction(abs(d1), abs(d0) + abs(d1)); u = 1 - t
            assert t * B[I[0]][kk] + u * B[I[1]][kk] != t * B[I[0]][J[0]] + u * B[I[1]][J[0]], "degenerate 3rd best"
for J in itertools.combinations(range(3), 2):
    k = [j for j in range(3) if j not in J][0]
    for I in itertools.combinations(range(3), 2):
        kk = [i for i in range(3) if i not in I][0]
        d0, d1 = A[I[0]][J[0]] - A[I[1]][J[0]], A[I[0]][J[1]] - A[I[1]][J[1]]
        if d0 == 0 and d1 == 0:
            h0, h1 = A[kk][J[0]] - A[I[0]][J[0]], A[kk][J[1]] - A[I[0]][J[1]]
            assert not (h0 == 0 or h1 == 0 or (h0 > 0) != (h1 > 0)), "degenerate row edge"
        elif (d0 == 0) != (d1 == 0):
            tv = A[I[0]][J[0]] if d0 == 0 else A[I[0]][J[1]]
            mm = max(A[i][J[0]] for i in range(3)) if d0 == 0 else max(A[i][J[1]] for i in range(3))
            assert tv < mm, "degenerate pure tie"
        elif (d0 > 0) != (d1 > 0):
            t = Fraction(abs(d1), abs(d0) + abs(d1)); u = 1 - t
            assert t * A[kk][J[0]] + u * A[kk][J[1]] != t * A[I[0]][J[0]] + u * A[I[0]][J[1]], "degenerate 3rd best"
print("non-degeneracy: PASS")

ne = enum_NE(A, B)
assert len(ne) == 7, f"expected 7 NE, got {len(ne)}"
assert len(ne) % 2 == 1
print(f"NE count: {len(ne)} (odd: PASS)")
for (I, J, x, y) in ne:
    u = sum(Fraction(A[i][j]) * x[r] * y[c] for r, i in enumerate(I) for c, j in enumerate(J))
    v = sum(Fraction(B[i][j]) * x[r] * y[c] for r, i in enumerate(I) for c, j in enumerate(J))
    print(f"  support {I}x{J}: x={[str(t) for t in x]} y={[str(t) for t in y]} welfare=({u},{v}) sum={u+v}")
assert any(len(I) == 3 for I, J, x, y in ne), "fully-mixed NE required"
wel = []
for (I, J, x, y) in ne:
    u = sum(Fraction(A[i][j]) * x[r] * y[c] for r, i in enumerate(I) for c, j in enumerate(J))
    v = sum(Fraction(B[i][j]) * x[r] * y[c] for r, i in enumerate(I) for c, j in enumerate(J))
    wel.append(u + v)
assert max(wel) == 6 and max(v for v in wel if v != 6) == 4, "welfare gap"
print(f"max welfare 6 (two co-maximal pure NE), next distinct 4, gap 2: PASS")

# 2. one-sided census recounts (exact integer arithmetic)
n1 = sum(1 for a in range(4) for c1 in range(4) for c2 in range(4)
         if a > c1 and a > c2)
assert n1 == 14, n1  # sum_a a^2 = 0+1+4+9; one-sided col/row factor
NA1 = n1 * 4**6  # per fixed pure support (i,j): strict col x free entries
assert NA1 == 57344, NA1
print(f"1x1 strict: core(col)={n1}, NA1={NA1} of 262144; pairs/support={NA1 * NA1}")
n2 = 0
for tup in itertools.product(range(4), repeat=6):
    a, b, c, d, e, f = tup
    p, q = a - c, b - d
    if p == 0 or q == 0 or (p > 0) == (q > 0): continue
    num = (e - a) * q + (f - b) * (-p); den = q - p
    if (num < 0 < den) or (num > 0 > den): n2 += 1
assert n2 == 486, n2
print(f"2x2 strict core={n2}, NA2={n2 * 64}")
def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1]) - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
n3 = 0
for e in itertools.product(range(4), repeat=9):
    R = [e[0:3], e[3:6], e[6:9]]
    M = [[R[0][0]-R[1][0], R[0][1]-R[1][1], R[0][2]-R[1][2]],
         [R[0][0]-R[2][0], R[0][1]-R[2][1], R[0][2]-R[2][2]], [1, 1, 1]]
    D = det3(M)
    if D == 0: continue
    ns = []
    for k in range(3):
        Mk = [row[:] for row in M]
        for r in range(3): Mk[r][k] = 1 if r == 2 else 0
        ns.append(det3(Mk))
    if all(v > 0 for v in ns) or all(v < 0 for v in ns): n3 += 1
assert n3 == 34032, n3
print(f"3x3 strict fully-mixed matrices={n3}")
print("ALL CHECKS PASS")
