"""R5: degree-<=2 polynomial Poisson-cocycle classification (exact, lane-1099).

nu^{ij}(x) = a^{ij} + b^{ij}_k x^k + c^{ij}_{kl} x^k x^l, symmetric c in (k,l).
E_abc = [pi0,nu]^{abc} polynomial of degree <= 3; impose all coefficients = 0.
Exact linear algebra over QQ. Compares null space against:
  - constants span{d01, d23} (dim 2)
  - coboundaries [pi0, X], X polynomial vector field deg <= 2.
A surviving essential direction with nu^{01}(0) != 0 and nontrivial x-dependence
would revive TARGET (localization route); absence strengthens the rigidity case.
"""
import itertools
import sympy as sp

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
# unknowns
A_ = {(i,j): sp.symbols(f'a{i}{j}') for (i,j) in pairs}
B_ = {(i,j,k): sp.symbols(f'b{i}{j}_{k}') for (i,j) in pairs for k in range(4)}
C_ = {(i,j,k,l): sp.symbols(f'c{i}{j}_{k}{l}')
      for (i,j) in pairs for k in range(4) for l in range(k,4)}
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
E = {}
for (a,b,c) in trips:
    ex = 0
    for l in range(4):
        ex += Pi[l,a]*sp.diff(Nu[b,c],X[l]) + Nu[l,a]*sp.diff(Pi[b,c],X[l])
        ex += Pi[l,b]*sp.diff(Nu[c,a],X[l]) + Nu[l,b]*sp.diff(Pi[c,a],X[l])
        ex += Pi[l,c]*sp.diff(Nu[a,b],X[l]) + Nu[l,c]*sp.diff(Pi[a,b],X[l])
    E[(a,b,c)] = sp.expand(ex)

unks = list(A_.values()) + list(B_.values()) + list(C_.values())
print("n unknowns:", len(unks))
# collect monomial-coefficient equations: E cubic max
from sympy import Poly
rows = []
for k in trips:
    P = Poly(E[k], X)
    for mon, coeff in P.as_dict().items():
        if sum(mon) > 3:
            print("UNEXPECTED DEGREE", mon)
        row = [sp.Rational(0)]*len(unks)
        cc = sp.expand(coeff)
        for j,u in enumerate(unks):
            row[j] = cc.coeff(u) or 0
        const = cc.subs({u:0 for u in unks})
        assert const == 0, const
        rows.append([sp.Rational(t) for t in row])
M = sp.Matrix(rows)
print("system:", M.shape)
ns = M.nullspace()
print("null dim (deg<=2 poly cocycles):", len(ns))
# evaluate each basis vector at origin component nu01
idx_a01 = unks.index(A_[(0,1)])
vals = [(w[idx_a01], w) for w in ns]
for v, w in vals:
    print("nu01(0) =", v)
print("R5 DONE")
