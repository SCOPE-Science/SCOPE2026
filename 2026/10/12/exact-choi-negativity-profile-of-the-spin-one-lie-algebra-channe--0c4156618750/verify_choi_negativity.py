#!/usr/bin/env python3
from fractions import Fraction as F

D=3
N=D*D

def zmat(): return [[F(0) for _ in range(N)] for _ in range(N)]
def eye():
    M=zmat()
    for i in range(N): M[i][i]=F(1)
    return M

def add(A,B): return [[A[i][j]+B[i][j] for j in range(N)] for i in range(N)]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(N)] for i in range(N)]
def scale(c,A): return [[c*A[i][j] for j in range(N)] for i in range(N)]
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(N)),F(0)) for j in range(N)] for i in range(N)]
def tr(A): return sum((A[i][i] for i in range(N)),F(0))
def eq(A,B): return A==B

def idx(a,b): return D*a+b

I=eye()
SW=zmat()
for a in range(D):
    for b in range(D):
        SW[idx(a,b)][idx(b,a)] = F(1)
P=zmat()
for a in range(D):
    for b in range(D):
        P[idx(a,a)][idx(b,b)] = F(1,D)

A=scale(F(1,2),sub(I,SW))
Q=P
S=sub(scale(F(1,2),add(I,SW)),P)

# Orthogonal spectral projectors.
assert eq(mm(A,A),A) and eq(mm(Q,Q),Q) and eq(mm(S,S),S)
assert mm(A,Q)==zmat() and mm(A,S)==zmat() and mm(Q,S)==zmat()
assert add(add(A,Q),S)==I
assert (tr(A),tr(Q),tr(S))==(F(3),F(1),F(5))

# Polynomial matrix entries a+b p represented as pairs.
def pz(): return (F(0),F(0))
def pa(x,y): return (x[0]+y[0],x[1]+y[1])
def ps(c,x): return (c*x[0],c*x[1])
def pmat(): return [[pz() for _ in range(N)] for _ in range(N)]
def padd(Ap,Bp): return [[pa(Ap[i][j],Bp[i][j]) for j in range(N)] for i in range(N)]
def pscale(c0,c1,A0): return [[(c0*A0[i][j],c1*A0[i][j]) for j in range(N)] for i in range(N)]
def pt_second(Mp):
    R=pmat()
    for a in range(D):
      for b in range(D):
       for c in range(D):
        for d in range(D):
          R[idx(a,d)][idx(c,b)] = Mp[idx(a,b)][idx(c,d)]
    return R

# Direct normalized Choi matrix of E_p(X)=(1-p)X+p/2(Tr(X)I-X^T).
J=pmat()
for i in range(D):
  for j in range(D):
    # block E_p(|i><j|)/3
    for a in range(D):
      for b in range(D):
        const = F(1,3) if (a==i and b==j) else F(0)
        coeff = -const
        if i==j and a==b:
            coeff += F(1,6)
        if a==j and b==i:
            coeff -= F(1,6)
        J[idx(i,a)][idx(j,b)] = (const,coeff)
Jpt=pt_second(J)
formula=padd(pscale(F(1,3),F(-1,3),SW),
             padd(pscale(F(0),F(1,6),I), pscale(F(0),F(-1,2),P)))
assert Jpt==formula

# Exact spectral decomposition of J_p^{T_2}.
lamA=(F(-1,3),F(1,2))   # (3p-2)/6, multiplicity 3
lamQ=(F(1,3),F(-2,3))   # (1-2p)/3, multiplicity 1
lamS=(F(1,3),F(-1,6))   # (2-p)/6, multiplicity 5
recomp=padd(padd(pscale(*lamA,A),pscale(*lamQ,Q)),pscale(*lamS,S))
assert recomp==formula

# Exact negativity checks at rational points across all three regimes.
def ev(lam,p): return lam[0]+lam[1]*p
def neg_direct(p):
    vals=[(lamA,3),(lamQ,1),(lamS,5)]
    return sum((m*max(F(0),-ev(l,p)) for l,m in vals),F(0))
def neg_formula(p):
    if p <= F(1,2): return F(1)-F(3,2)*p
    if p <= F(2,3): return F(4,6)-F(5,6)*p
    return (F(2)*p-F(1))/F(3)
pts=[F(0),F(1,7),F(1,2),F(7,12),F(2,3),F(5,6),F(1)]
for p in pts:
    assert neg_direct(p)==neg_formula(p)

# Endpoint and unique-minimum data from piecewise slopes.
assert neg_formula(F(0))==F(1)
assert neg_formula(F(1,2))==F(1,4)
assert neg_formula(F(2,3))==F(1,9)
assert neg_formula(F(1))==F(1,3)
assert F(-3,2)<0 and F(-5,6)<0 and F(2,3)>0

print('VERIFY_OK')
print('projector_ranks = 3,1,5')
print('exact_direct_choi_partial_transpose = yes')
print('exact_spectral_decomposition = yes')
print('rational_negativity_points =', len(pts))
print('minimum_parameter = 2/3')
print('minimum_negativity = 1/9')
