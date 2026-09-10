"""Exact QQ apolar / Hilbert / Lefschetz-rank audit for G_{a,b}.
R = QQ[x,y,u,v] acts by differentiation on S = QQ[X,Y,U,V].
F = X^2 U^4 + X Y U^2 V^2 + Y^2 V^4 + a U^5 V + b U V^5.
Computes catalecticant ranks h_e, Ann bases, and rank of xL0: A2->A3.
Stdlib + sympy only, exact QQ.
"""
import itertools
from sympy import Matrix, Rational, symbols

vars_R = ['x','y','u','v']
vars_S = ['X','Y','U','V']

def monomials_4(deg):
    out=[]
    for e0 in range(deg+1):
        for e1 in range(deg+1-e0):
            for e2 in range(deg+1-e0-e1):
                e3 = deg-e0-e1-e2
                out.append((e0,e1,e2,e3))
    return sorted(out)

def diff_action(e, f):
    # D=x^e on M=X^f -> coeff * X^{f-e} or 0
    import math
    for i in range(4):
        if e[i] > f[i]:
            return (None, 0)
    c = 1
    g = []
    for i in range(4):
        c *= math.factorial(f[i]) // math.factorial(f[i]-e[i]) if e[i]<=f[i] else 0
        g.append(f[i]-e[i])
    return (tuple(g), c)

# F as dict f -> coeff (coeff may be symbolic in a,b or rational)
def build_F(a, b):
    F = {}
    F[(2,0,4,0)] = Rational(1)
    F[(1,1,2,2)] = Rational(1)
    F[(0,2,0,4)] = Rational(1)
    F[(0,0,5,1)] = a
    F[(0,0,1,5)] = b
    return F

def catalecticant(a, b, e):
    d = 6
    Rmons = monomials_4(e)
    Smons = monomials_4(d-e)
    Sindex = {m:i for i,m in enumerate(Smons)}
    F = build_F(a, b)
    M = [[Rational(0)]*len(Smons) for _ in Rmons]
    for i,em in enumerate(Rmons):
        row = [Rational(0)]*len(Smons)
        for fm, c in F.items():
            g, k = diff_action(em, fm)
            if g is None:
                continue
            j = Sindex[g]
            row[j] += c*k
        M[i] = row
    return Rmons, Smons, Matrix(M)

def hilbert(a, b):
    hs = []
    for e in range(7):
        Rmons, Smons, M = catalecticant(a, b, e)
        r = M.rank()
        hs.append(r)
    return hs

def ann_basis(a, b, e):
    Rmons, Smons, M = catalecticant(a, b, e)
    ns = M.nullspace()
    return Rmons, M, ns

def lef_rank(a, b):
    # rank of xL0 : A2 -> A3, L0 = x+y+u+v
    Rmons2 = monomials_4(2)
    Rmons3 = monomials_4(3)
    idx3 = {m:i for i,m in enumerate(Rmons3)}
    # multiplication by L0 matrix: 20 x 10
    import sympy
    Mult = [[Rational(0)]*len(Rmons2) for _ in range(len(Rmons3))]
    L = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    for j, em in enumerate(Rmons2):
        for l in L:
            g = tuple(em[i]+l[i] for i in range(4))
            i = idx3[g]
            Mult[i][j] += Rational(1)
    Mult = Matrix(Mult)
    # Ann3 row space: kernel of catalecticant C (10? no: C is 20x20)
    Rmons, Smons, C = catalecticant(a, b, 3)
    assert Rmons == Rmons3
    # Ann3 = nullspace of C (as row vectors D with D*C... careful orientation)
    # C rows = D in R3, cols = S3 basis; D in Ann iff row(D) of C is zero vector.
    # So Ann3 = ker of linear map R3 -> S3 given by C. Compute nullspace of C^T? No:
    # vector v (20 coeffs on R3 basis) maps to v^T C (row combination). Ann = {v : v^T C = 0} = ker(C^T).
    Ct = C.T
    ker = Ct.nullspace()  # each is 20-vector of coeffs in Rmons3 basis
    dimAnn3 = len(ker)
    h3 = len(Rmons3) - dimAnn3
    # quotient projection: complete to basis; rank of (L0*R2 mod Ann3)
    # image space S = colspace(Mult) + Ann3 inside QQ^20. rank = dim(S) - dimAnn3.
    # Build matrix whose columns span S: [Mult columns | ker vectors]
    import sympy
    cols = []
    for j in range(Mult.cols):
        cols.append(Mult.col(j))
    for v in ker:
        cols.append(v)
    S = Matrix.hstack(*cols)
    dimS = S.rank()
    rank = dimS - dimAnn3
    # also h2
    _, _, C2 = catalecticant(a, b, 2)
    h2 = C2.rank()
    return h2, h3, dimAnn3, rank, Mult, C, ker

if __name__ == "__main__":
    for (a,b) in [(Rational(0),Rational(0)),(Rational(1),Rational(2)),(Rational(2),Rational(3)),(Rational(1),Rational(0)),(Rational(3),Rational(-1)),(Rational(7),Rational(11))]:
        hs = hilbert(a,b)
        h2,h3,dA,r,_,_,_ = lef_rank(a,b)
        print(f"(a,b)=({a},{b}) hilbert={hs} sum={sum(hs)} h2={h2} h3={h3} dimAnn3={dA} rank(L0:A2->A3)={r} max={min(h2,h3)}")
    # show Ann3 always contains (x,y)^3 monomials: check rows of C3 for those
    Rmons, Smons, C = catalecticant(Rational(1),Rational(2),3)
    for m in [(3,0,0,0),(2,1,0,0),(1,2,0,0),(0,3,0,0)]:
        i = Rmons.index(m)
        print(m, "rowzero?", all(v==0 for v in C.row(i).tolist()[0]))
    # Ann2 check at (0,0) and (1,2): nullspace dim
    for (a,b) in [(Rational(0),Rational(0)),(Rational(1),Rational(2))]:
        Rmons2,_,C2 = catalecticant(a,b,2)
        print(f"Ann2 dim at {(a,b)}:", C2.cols - C2.rank(), "h2=", C2.rank(), "nullspace=", C2.T.nullspace())
