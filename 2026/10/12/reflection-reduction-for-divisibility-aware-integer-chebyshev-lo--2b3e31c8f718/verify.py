#!/usr/bin/env python3
from fractions import Fraction
from math import log, isclose

# Coefficients are ascending: a_0 + a_1 x + ...
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a

def reflect_poly(a):
    # (-1)^d Q(1-x), exact integer binomial expansion.
    a=trim(a); d=len(a)-1
    out=[0]*(d+1)
    from math import comb
    for k,ak in enumerate(a):
        for j in range(k+1):
            out[j] += ((-1)**d)*ak*comb(k,j)*((-1)**j)
    return trim(out)

def peval(a,x):
    s=0.0
    for v in reversed(a): s=s*x+v
    return s

polys=[[1,1],[-1,2],[3,-4,1],[2,3,0,1],[-5,1,2,1,1]]
for q in polys:
    qr=reflect_poly(q)
    assert reflect_poly(qr)==trim(q)
    assert len(qr)==len(trim(q))
    assert qr[-1]==trim(q)[-1]

# Exact w identity on a rational grid.
w_cases=0
for i in range(1,10):
    x=Fraction(i,11)
    for j in range(1,10):
        t=Fraction(j,13)
        assert (x-t)*(1-x-t) == x*(1-x)-t*(1-t)
        w_cases += 1

# Reflection-closed test library: x+1 <-> x-2, and 2x-1 fixed.
Q=[[1,1],[-2,1],[-1,2]]
perm=[1,0,2]
deg=[1,1,1]
lead=[1,1,2]
roots=[-1.0,2.0,0.5]
# nonsingular measure and its reflection
pts=[0.20,0.35,0.65,0.80]
mass=[0.10,0.40,0.40,0.10]
c=[0.07,0.13,0.05]
cr=[c[perm[i]] for i in range(3)]
ptsr=[1-p for p in pts]

# Potential of atomic measure.
def U(z, P=pts, M=mass):
    return sum(m*log(abs(z-t)) for t,m in zip(P,M))
def Ur(z):
    return sum(m*log(abs(z-t)) for t,m in zip(ptsr,mass))
def Avec(x,P=pts,M=mass,C=c):
    u=sum(m*log(abs(x-t)) for t,m in zip(P,M))
    return u-sum(ci*log(abs(peval(q,x))) for ci,q in zip(C,Q))
def Aref(x):
    u=sum(m*log(abs(x-t)) for t,m in zip(ptsr,mass))
    return u-sum(ci*log(abs(peval(q,x))) for ci,q in zip(cr,Q))

def G(i,P,M,C):
    B=sum(C[k]*deg[k] for k in range(3))
    Li=log(lead[i])/deg[i]
    ui=sum(m*log(abs(roots[i]-t)) for t,m in zip(P,M))
    cross=0.0
    for j in range(3):
        if j==i: continue
        cross += C[j]*log(abs(peval(Q[j],roots[i])))
    return Li*(1-B+C[i]*deg[i])+ui-cross

reflection_grid=0
for x in [0.07,0.11,0.27,0.43,0.58,0.74,0.91]:
    if all(abs(x-t)>1e-12 for t in pts):
        assert isclose(Aref(x),Avec(1-x),rel_tol=0,abs_tol=2e-13)
        reflection_grid += 1
for i in range(3):
    assert isclose(G(perm[i],ptsr,mass,cr),G(i,pts,mass,c),rel_tol=0,abs_tol=2e-13)

# Symmetric pushforward potential identity.
potential_cases=0
for x in [0.09,0.18,0.29,0.47,0.72,0.93]:
    ux=U(x)
    wx=x*(1-x)
    ueta=sum(m*log(abs(wx-t*(1-t))) for t,m in zip(pts,mass))
    assert isclose(ux,0.5*ueta,rel_tol=0,abs_tol=3e-13)
    potential_cases += 1

print(f"VERIFY_OK polynomial_cases={len(polys)} w_identity_cases={w_cases} reflection_grid={reflection_grid} G_pairs=3 potential_cases={potential_cases}")
