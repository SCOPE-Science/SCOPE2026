"""Minimal generator counts of Ann(G0) in low degrees (Betti head)."""
from sympy import Matrix, Rational
from audit_target import catalecticant, monomials_4

a = Rational(0); b = Rational(0)
# Ann3 basis monomials (fixed span)
A3 = [(3,0,0,0),(2,1,0,0),(1,2,0,0),(0,3,0,0),(0,2,1,0),(2,0,0,1)]
R1 = monomials_4(1); R4 = monomials_4(4)
idx4 = {m:i for i,m in enumerate(R4)}
prods = []
for g in A3:
    for l in R1:
        prods.append(tuple(g[i]+l[i] for i in range(4)))
# rank of span of products inside R4
M = Matrix.zeros(len(R4), len(prods))
for j,p in enumerate(prods):
    M[idx4[p], j] = 1
r = M.rank()
print("rank(R1*Ann3 in R4) =", r, " nprods=", len(prods))
_, _, C4 = catalecticant(a,b,4)
h4 = C4.rank()
print("h4 =", h4, "dimAnn4 =", len(R4)-h4)
print("mu4 = dimAnn4 - rank(R1 Ann3) =", (len(R4)-h4) - r)
# mu3 = 6 (Ann1=Ann2=0 so all 6 cubics minimal)
_, _, C1 = catalecticant(a,b,1); _, _, C2 = catalecticant(a,b,2)
print("dimAnn1 =", len(R1)-C1.rank(), "dimAnn2 =", 10-C2.rank())
# which products are dependent / Ann4 complement basis
print("distinct products:", len(set(prods)))
