"""High-precision reference (mpmath 80 digits)."""
from mpmath import mp, mpf, sin, log, pi, sqrt

mp.dps = 80

def build(m):
    js = [j for j in range(1, m // 2, 2)]
    As = [a for a in js if a != 1]
    M = [[log(abs(sin(pi * a * j / m))) - log(abs(sin(pi * j / m)))
          for a in As] for j in js]
    n = len(As)
    G = [[sum(row[a] * row[b] for row in M) for b in range(n)]
         for a in range(n)]
    return js, As, M, G

for m in [16, 32]:
    js, As, M, G = build(m)
    n = len(As)
    print("m=%d" % m)
    for i, row in enumerate(G):
        print("  G[%d]=" % i, [mp.nstr(x, 15) for x in row])
    # LDL
    L = [[mpf(0)] * n for _ in range(n)]
    D = [mpf(0)] * n
    for i in range(n):
        for j in range(i):
            L[i][j] = (G[i][j] - sum(L[i][k] * L[j][k] * D[k]
                                     for k in range(j))) / D[j]
        D[i] = G[i][i] - sum(L[i][k] ** 2 * D[k] for k in range(i))
        L[i][i] = 1
    print("  GS D:", [mp.nstr(x, 12) for x in D])
    print("  GS bound:", mp.nstr(sqrt(sum(D)) / 2, 12),
          " norm:", mp.nstr(sqrt(sum(D)) / 2 / sqrt(n), 12))
    # det via LDL
    det = mpf(1)
    for d in D:
        det *= d
    print("  det:", mp.nstr(det, 15), " covol:", mp.nstr(sqrt(det), 15))
    # regulator minor (drop last row)
    rows = M[:-1]
    # det of square matrix via LU
    A = [r[:] for r in rows]
    detm = mpf(1)
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[p], A[i] = A[i], A[p]
        if p != i:
            detm = -detm
        detm *= A[i][i]
        for r in range(i + 1, n):
            f = A[r][i] / A[i][i]
            for c in range(i, n):
                A[r][c] -= f * A[i][c]
    print("  regulator:", mp.nstr(abs(detm), 15))

# exact hole values
G16 = build(16)[3]
x16 = [mpf(1) / 4, mpf(1) / 4, mpf(-3) / 4]
q16 = sum(G16[i][j] * x16[i] * x16[j] for i in range(3) for j in range(3))
print("mu16 vertex q:", mp.nstr(q16, 15), " depth:", mp.nstr(sqrt(q16), 15),
      " norm:", mp.nstr(sqrt(q16 / 3), 15))
G32 = build(32)[3]
t = [mpf(1) / 2, mpf(0), mpf(1) / 2, mpf(1) / 2, mpf(0), mpf(1) / 2,
     mpf(1) / 2]
z = [1, 0, 0, 0, 1, 1, 0]
x = [t[i] - z[i] for i in range(7)]
q32 = sum(G32[i][j] * x[i] * x[j] for i in range(7) for j in range(7))
print("mu32 hole q:", mp.nstr(q32, 15), " depth:", mp.nstr(sqrt(q32), 15),
      " norm:", mp.nstr(sqrt(q32 / 7), 15))
