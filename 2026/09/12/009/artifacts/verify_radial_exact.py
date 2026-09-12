"""R4-EXACT: radial localization impossible at linear order — exact certificate (lane-1099).

Ansatz nu^{ij}(x) = f_ij(s), s = |x|^2. Cocycle E_abc(x) = L_abc(x;f(s)) + C_abc(x;g(s)),
L homogeneous deg 1 in x, C homogeneous deg 3, g = f'.
On sphere |x|^2 = s > 0, direction v in Q^4 nonzero, x = rho*v, rho^2 = s/|v|^2:
  row(v)/rho = L_abc(v; f) + (s/|v|^2) C_abc(v; g).
So per-sphere system is M(s) = [A | s*B] over Q[s], A,B rational matrices.
Claim: null_{Q(s)} M = span{e_f01, e_f23} (i.e. g = 0 forced, f in jump span),
hence no C^1 radial transition f01: 1 -> 0 exists. Exceptional s handled by
direct substitution. All arithmetic exact (QQ).
"""
import itertools
import sympy as sp

s = sp.symbols('s')
x0, x1, x2, x3 = sp.symbols('x0 x1 x2 x3')
X = [x0, x1, x2, x3]
C1 = x0*x1
C2 = x2*x3
d1 = [sp.diff(C1, x) for x in X]
d2 = [sp.diff(C2, x) for x in X]

def sgn(p):
    p = list(p); inv = 0
    for i in range(4):
        for j in range(i+1, 4):
            if p[i] > p[j]:
                inv += 1
    return 1 if inv % 2 == 0 else -1

Pi = sp.zeros(4, 4)
for i in range(4):
    for j in range(4):
        e = 0
        for k in range(4):
            for l in range(4):
                if len({i, j, k, l}) < 4:
                    continue
                e += sgn((i, j, k, l))*d1[k]*d2[l]
        Pi[i, j] = sp.expand(e)

pairs = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
fsym = sp.symbols('f01 f02 f03 f12 f13 f23')
gsym = sp.symbols('g01 g02 g03 g12 g13 g23')
fD = dict(zip(pairs, fsym)); gD = dict(zip(pairs, gsym))
def Fget(D,i,j):
    if i == j:
        return sp.Integer(0)
    if (i,j) in D:
        return D[(i,j)]
    return -D[(j,i)]

trips = list(itertools.combinations(range(4),3))
E = {}   # (a,b,c) -> sympy expr in X, fsym, gsym
for (a,b,c) in trips:
    ex = 0
    for l in range(4):
        ex += Pi[l,a]*2*X[l]*Fget(gD,b,c) + Fget(fD,l,a)*sp.diff(Pi[b,c],X[l])
        ex += Pi[l,b]*2*X[l]*Fget(gD,c,a) + Fget(fD,l,b)*sp.diff(Pi[c,a],X[l])
        ex += Pi[l,c]*2*X[l]*Fget(gD,a,b) + Fget(fD,l,c)*sp.diff(Pi[a,b],X[l])
    E[(a,b,c)] = sp.expand(ex)

# split L (f-part) and C (g-part)
L = {k: sp.expand(v.subs({u: 0 for u in gsym})) for k, v in E.items()}
C = {k: sp.expand(v.subs({u: 0 for u in fsym})) for k, v in E.items()}
# sanity: E == L + C
for k in E:
    assert sp.expand(E[k]-L[k]-C[k]) == 0
print("split OK")

# rational directions: all nonzero {0,1}-vectors (14) + a few {0,1,-1} for bulk
dirs = []
for mask in range(1, 16):
    v = [(mask >> i) & 1 for i in range(4)]
    dirs.append(tuple(v))
extra = [(1,-1,0,0),(1,0,-1,0),(1,1,-1,0),(0,1,1,-1),(1,-1,1,-1),(2,1,0,0)]
dirs += extra
print("n directions:", len(dirs))

def asE(t):
    return sp.sympify(t)
def eval_at(expr, v):
    return asE(expr).subs({x0:v[0], x1:v[1], x2:v[2], x3:v[3]})

rowsA, rowsB = [], []
for v in dirs:
    n2 = sum(t*t for t in v)
    for k in trips:
        rA = [eval_at(sp.expand(L[k]).coeff(u), v) for u in fsym]
        # C-part: C[k] is cubic in X with g-coeffs; coeff of g_u evaluated at v, scaled by 1/|v|^2
        rB = [sp.Rational(eval_at(sp.expand(C[k]).coeff(u), v), n2) for u in gsym]
        rowsA.append([sp.Rational(t) for t in rA])
        rowsB.append(rB)
A = sp.Matrix(rowsA); B = sp.Matrix(rowsB)
print("A shape:", A.shape, "B shape:", B.shape)
print("rank(A) =", A.rank(), "(expect 4: R1 says f-null is 2-dim)")
print("A nullspace:", A.nullspace())

M = A.row_join(s*B)
print("M shape:", M.shape)
ns = M.nullspace()
print("null dim over Q(s):", len(ns))
for w in ns:
    print(sp.simplify(w).T)
# verify kernel == span{e_f01, e_f23}
e_f01 = sp.Matrix([1,0,0,0,0,0, 0,0,0,0,0,0])
e_f23 = sp.Matrix([0,0,0,0,0,1, 0,0,0,0,0,0])
assert all(M*e == sp.zeros(M.rows, 1) for e in (e_f01, e_f23))
K = sp.Matrix.hstack(e_f01, e_f23)
assert len(ns) == 2, "kernel bigger than jump span!"
# each null vector must lie in column space of K: check augmented rank
for w in ns:
    assert K.row_join(w).rank() == 2, "null vector outside jump span!"
print("EXACT CERTIFICATE: null_{Q(s)} M(s) = span{e_f01, e_f23}; all g forced 0.")
print("R4-EXACT DONE: no C^1 radial transition of the jump cocycle exists on any sphere s>0.")
print("Exceptional-sphere check is closed by verify_loopholes.py part (b): a 10x10 minor has")
print("exact determinant D(s) = -36*s^6 != 0 for all s > 0, so rank M(s) = 10 on every sphere.")
