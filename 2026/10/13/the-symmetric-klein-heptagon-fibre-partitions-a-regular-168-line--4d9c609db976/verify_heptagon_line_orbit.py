#!/usr/bin/env python3
"""Exact verification for the Klein-quartic symmetric-heptagon line orbit.

The computation uses exact arithmetic in Q(zeta_7,a), where
zeta_7 is a primitive seventh root of unity and a^7=-(b+1)/b^3 with
b=zeta_7^3+zeta_7^4.  It reconstructs the explicit heptagon, the
168-element projective automorphism group, and the stabilizer of one
constituent line.
"""
from itertools import combinations
import sympy as sp
from sympy import QQ

# Cyclotomic coefficient field K=Q(zeta_7).
zeta_expr = sp.exp(2 * sp.pi * sp.I / 7)
K = QQ.algebraic_field(zeta_expr)
zeta = K.convert(zeta_expr)
k0, k1 = K.zero, K.one
b = zeta**3 + zeta**4
rhs = -(b + k1) / (b**3)

# Certify that adjoining a with a^7=rhs gives a degree-seven field extension.
u = sp.symbols("u")
poly = sp.Poly(u**7 - K.to_sympy(rhs), u, extension=zeta_expr)
fac = poly.factor_list()[1]
assert len(fac) == 1 and fac[0][0].degree() == 7 and fac[0][1] == 1

# Elements of L=K[a]/(a^7-rhs) as coefficient tuples of length seven.
def lzero():
    return (k0,) * 7

def lconst(c):
    return (c, k0, k0, k0, k0, k0, k0)

def ladd(x, y):
    return tuple(x[i] + y[i] for i in range(7))

def lneg(x):
    return tuple(-c for c in x)

def lsub(x, y):
    return ladd(x, lneg(y))

def lmul(x, y):
    tmp = [k0] * 13
    for i, xi in enumerate(x):
        if xi == k0:
            continue
        for j, yj in enumerate(y):
            if yj != k0:
                tmp[i+j] += xi * yj
    # max degree is 12, so one use of a^7=rhs per high term suffices.
    for d in range(12, 6, -1):
        if tmp[d] != k0:
            tmp[d-7] += tmp[d] * rhs
            tmp[d] = k0
    return tuple(tmp[:7])

def lpow(x, n):
    out = lconst(k1)
    base = x
    while n:
        if n & 1:
            out = lmul(out, base)
        base = lmul(base, base)
        n >>= 1
    return out

def lscale(c, x):
    return tuple(c * xi for xi in x)

def liszero(x):
    return all(c == k0 for c in x)

a = (k0, k1, k0, k0, k0, k0, k0)
assert lsub(lpow(a, 7), lconst(rhs)) == lzero()

# Projective/vector operations over L.
def vcross(P, Q):
    return (
        lsub(lmul(P[1], Q[2]), lmul(P[2], Q[1])),
        lsub(lmul(P[2], Q[0]), lmul(P[0], Q[2])),
        lsub(lmul(P[0], Q[1]), lmul(P[1], Q[0])),
    )

def vdet(P, Q, R):
    return ladd(
        lsub(lmul(P[0], lsub(lmul(Q[1], R[2]), lmul(Q[2], R[1]))),
             lmul(P[1], lsub(lmul(Q[0], R[2]), lmul(Q[2], R[0])))),
        lmul(P[2], lsub(lmul(Q[0], R[1]), lmul(Q[1], R[0])))
    )

def projectively_equal(P, Q):
    return (liszero(lsub(lmul(P[0], Q[1]), lmul(P[1], Q[0]))) and
            liszero(lsub(lmul(P[0], Q[2]), lmul(P[2], Q[0]))) and
            liszero(lsub(lmul(P[1], Q[2]), lmul(P[2], Q[1]))))

def quartic(P):
    x, y, zc = P
    return ladd(ladd(lmul(lpow(x,3), y), lmul(lpow(y,3), zc)), lmul(lpow(zc,3), x))

# Explicit seven points from the heptagon construction.
points = []
for i in range(7):
    ai = lscale(zeta**i, a)
    points.append((lscale(b, lpow(ai,3)), ai, lconst(k1)))
assert all(liszero(quartic(P)) for P in points)

# Lines L_i join R_{i-2} to R_i, matching (R6,R1),(R7,R2),... in 1-based labels.
lines = [vcross(points[(i-2) % 7], points[i]) for i in range(7)]
for i, j in combinations(range(7), 2):
    assert not projectively_equal(lines[i], lines[j])
for i, j, k in combinations(range(7), 3):
    assert not liszero(vdet(lines[i], lines[j], lines[k]))

# The fourteen intersections of nonadjacent sides lie on the quartic.
residual = 0
for i, j in combinations(range(7), 2):
    d = (j-i) % 7
    if d not in (1,6):
        Q = vcross(lines[i], lines[j])
        assert not all(liszero(c) for c in Q)
        assert liszero(quartic(Q))
        residual += 1
assert residual == 14

# Exact projective automorphism group, from standard Klein-quartic generators.
A = ((k0,k0,k1),(k1,k0,k0),(k0,k1,k0))
B = ((k0,k0,zeta**6),(k1,k0,k0),(k0,zeta**4,k0))
C = (
    (k1, zeta**2+zeta, -(zeta**5+zeta**4+zeta**3)),
    (-(zeta**4+zeta**3+zeta**2+zeta+k1), zeta**5+zeta**4+zeta**3+zeta**2,
     -(zeta**5+zeta**4+zeta**3+zeta**2+zeta+k1)),
    (-(zeta**4+zeta**3+zeta**2), zeta, zeta**4+zeta**3),
)
I3 = ((k1,k0,k0),(k0,k1,k0),(k0,k0,k1))

def mm(X,Y):
    return tuple(tuple(sum((X[i][r]*Y[r][j] for r in range(3)), k0)
                       for j in range(3)) for i in range(3))

def mcanon(M):
    for i in range(3):
        for j in range(3):
            if M[i][j] != k0:
                s = k1 / M[i][j]
                return tuple(tuple(M[r][c]*s for c in range(3)) for r in range(3))
    raise AssertionError("zero matrix")

def detK(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def cofactor(M, i, j):
    rr=[r for r in range(3) if r!=i]
    cc=[c for c in range(3) if c!=j]
    val=M[rr[0]][cc[0]]*M[rr[1]][cc[1]]-M[rr[0]][cc[1]]*M[rr[1]][cc[0]]
    return val if (i+j)%2==0 else -val

def dual_action(M, ell):
    # cofactor(M)=det(M) M^{-T}; projectively this is the line action.
    return tuple(
        ladd(ladd(lscale(cofactor(M,i,0),ell[0]), lscale(cofactor(M,i,1),ell[1])),
             lscale(cofactor(M,i,2),ell[2]))
        for i in range(3)
    )

# Check generators really preserve C by substitution on coefficient monomials via sample symbolic identity.
x,y,zz=sp.symbols('x y zz')
F=x**3*y+y**3*zz+zz**3*x
for M in (A,B,C):
    ex=[sum(K.to_sympy(M[i][j])*v for j,v in enumerate((x,y,zz))) for i in range(3)]
    transformed=sp.Poly(sp.expand(ex[0]**3*ex[1]+ex[1]**3*ex[2]+ex[2]**3*ex[0]),x,y,zz,extension=zeta_expr)
    base=sp.Poly(F,x,y,zz,extension=zeta_expr)
    # A projective automorphism need only preserve F up to a nonzero scalar.
    coeffT=transformed.coeff_monomial(x**3*y)
    coeffF=base.coeff_monomial(x**3*y)
    lam=coeffT/coeffF
    assert transformed == base.mul_ground(lam)

G={mcanon(I3):I3}
queue=[I3]
while queue:
    X=queue.pop()
    for gen in (A,B,C):
        Y=mcanon(mm(X,gen))
        if Y not in G:
            G[Y]=Y
            queue.append(Y)
assert len(G)==168
assert all(detK(M)!=k0 for M in G.values())

phi=((zeta**4,k0,k0),(k0,zeta**2,k0),(k0,k0,zeta))
assert mcanon(phi) in G
for i in range(7):
    assert projectively_equal(dual_action(phi, lines[i]), lines[(i+1)%7])

# The order-seven subgroup generated by phi has 24 left cosets in G.
H=set()
powphi=I3
for _ in range(7):
    H.add(mcanon(powphi))
    powphi=mm(powphi,phi)
assert len(H)==7 and mcanon(powphi)==mcanon(I3)
cosets={frozenset(mcanon(mm(g,h)) for h in H) for g in G.values()}
assert len(cosets)==24 and all(len(c)==7 for c in cosets)

# The line-level check: one constituent line has trivial stabilizer in G.
base_line=lines[0]
stab=[M for M in G.values() if projectively_equal(dual_action(M,base_line),base_line)]
assert len(stab)==1
line_orbit=len(G)//len(stab)
assert line_orbit==168

print("VERIFY_OK field_degree=42 group=168 residual_points=14 line_stabilizer=1 line_orbit=168 heptagon_partition=24x7")
