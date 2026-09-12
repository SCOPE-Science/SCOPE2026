"""R5b: decompose the 34-dim deg<=2 polynomial cocycle space (lane-1099).

Coboundary map d: X (affine vector field, 20 params) -> deg<=2 bivector coeffs.
Essential quotient Z/B in degree<=2: is d01 isolated from all essential
deformations? Report dimensions, image of d01 in quotient, and whether any
essential class has nu01(0) != 0.
"""
import itertools
import sympy as sp
from sympy import Poly

x0, x1, x2, x3 = sp.symbols('x0 x1 x2 x3')
X = [x0, x1, x2, x3]
C1 = x0*x1; C2 = x2*x3
d1 = [sp.diff(C1, x) for x in X]; d2 = [sp.diff(C2, x) for x in X]

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
A_ = {(i,j): sp.symbols(f'a{i}{j}') for (i,j) in pairs}
B_ = {(i,j,k): sp.symbols(f'b{i}{j}_{k}') for (i,j) in pairs for k in range(4)}
C_ = {(i,j,k,l): sp.symbols(f'c{i}{j}_{k}{l}')
      for (i,j) in pairs for k in range(4) for l in range(k,4)}
unks = list(A_.values()) + list(B_.values()) + list(C_.values())

def biv_to_vec(expr_dict):
    """expr_dict: (i,j)->poly for i<j. Returns coeff vector in unks basis."""
    v = [sp.Rational(0)]*len(unks)
    for (i,j) in pairs:
        P0 = Poly(sp.expand(expr_dict[(i,j)]), X)
        for mon, cf in P0.as_dict().items():
            if mon == (0,0,0,0):
                v[unks.index(A_[(i,j)])] += cf
            elif sum(mon) == 1:
                k = mon.index(1)
                v[unks.index(B_[(i,j,k)])] += cf
            elif sum(mon) == 2:
                ks = []
                for d, e_ in enumerate(mon):
                    ks += [d]*e_
                k, l = ks
                v[unks.index(C_[(i,j,k,l)])] += cf
            else:
                raise ValueError(mon)
    return sp.Matrix(v)

# coboundary columns from affine X: X^i = p^i + q^i_k x^k
p = sp.symbols('p0:4'); q = sp.symbols('q0:16')
params = list(p)+list(q)
Xf = [p[i]+sum(q[4*i+k]*X[k] for k in range(4)) for i in range(4)]
Bcols = []
for pr in params:
    ed = {}
    for (i,j) in pairs:
        e = 0
        for l in range(4):
            e += Xf[l]*sp.diff(Pi[i,j],X[l]) - Pi[l,j]*sp.diff(Xf[i],X[l]) - Pi[i,l]*sp.diff(Xf[j],X[l])
        ed[(i,j)] = sp.expand(e).coeff(pr) or 0
    Bcols.append(biv_to_vec(ed))
Bm = sp.Matrix.hstack(*Bcols)
print("coboundary image rank (affine X):", Bm.rank(), " / 20 params")

# cocycle null space (rebuild system)
Nu = sp.zeros(4,4)
for (i,j) in pairs:
    e = A_[(i,j)]
    for k in range(4):
        e += B_[(i,j,k)]*X[k]
    for k in range(4):
        for l in range(k,4):
            e += C_[(i,j,k,l)]*X[k]*X[l]
    Nu[i,j] = sp.expand(e); Nu[j,i] = sp.expand(-e)
trips = list(itertools.combinations(range(4),3))
rows = []
for (a,b,c) in trips:
    ex = 0
    for l in range(4):
        ex += Pi[l,a]*sp.diff(Nu[b,c],X[l]) + Nu[l,a]*sp.diff(Pi[b,c],X[l])
        ex += Pi[l,b]*sp.diff(Nu[c,a],X[l]) + Nu[l,b]*sp.diff(Pi[c,a],X[l])
        ex += Pi[l,c]*sp.diff(Nu[a,b],X[l]) + Nu[l,c]*sp.diff(Pi[a,b],X[l])
    P0 = Poly(sp.expand(ex), X)
    for mon, coeff in P0.as_dict().items():
        cc = sp.expand(coeff)
        rows.append([sp.Rational(cc.coeff(u) or 0) for u in unks])
M = sp.Matrix(rows)
Z = M.nullspace()
print("cocycle dim:", len(Z))
Zmat = sp.Matrix.hstack(*Z)
aug = Zmat.row_join(Bm)
# quotient dim = dim Z - dim(Z cap B)
capdim = Zmat.rank() + Bm.rank() - aug.rank()
print("dim(Z cap B) =", capdim, "=> essential dim =", Zmat.rank()-capdim)
# d01 in quotient?
e_d01 = sp.zeros(len(unks), 1); e_d01[unks.index(A_[(0,1)])] = 1
print("rank(Bm) =", Bm.rank(), "rank(Bm|d01) =", Bm.row_join(e_d01).rank(),
      "=> d01 essential:", Bm.row_join(e_d01).rank() > Bm.rank())
# essential classes with nu01(0)!=0: project: solve for combo with a01=1 mod B
sys = Bm.row_join(e_d01)
print("R5b DONE")
