#!/usr/bin/env python3
"""Reproduce exact algebra and independent finite-cycle tests for a two-periodic hat-spline projector.
Requires Python 3, SymPy, and NumPy. No network, external data, or nonstandard solvers.
"""
import math
import sympy as sp
import numpy as np

checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

# Prove that the geometric Green-row integral and the stated rational function
# agree whenever the characteristic quadratic for the decay root is satisfied.
a, b, r = sp.symbols('a b r', positive=True)
D = 2 * (a + b)
u = (a + b*r)/D
v = (b + a*r)/D
q = a*b*r**2 + (a*a + b*b - D*D)*r + a*b
A = 6/(D-a*u-b*v)
L = A/(2*(1-r))*(a*(1+v)*(1+u*u)/(1+u) + b*(1+u)*(1+v*v)/(1+v))
F = (5*a*a + 22*a*b + 5*b*b)/(3*a*a + 10*a*b + 3*b*b)
num,den = sp.fraction(sp.cancel(L-F))
check(sp.rem(num,q,r)==0,'symbolic characteristic polynomial reduction')
check(sp.simplify(F-(2-(a-b)**2/(3*a*a+10*a*b+3*b*b)))==0,
      'strict norm deficit identity')
check(sp.simplify(F-(sp.Rational(5,3)+(16*a*b)/(3*(3*a*a+10*a*b+3*b*b))))==0,
      'lower endpoint identity')
check(sp.simplify(sp.factor(u*v-r).as_numer_denom()[0]/q).is_constant(r),
      'identity uv=r follows from the characteristic quadratic')

# Exact arithmetic at rational parameter pairs. The root is algebraic, so
# numerical evaluation is used here independently of the polynomial reduction.
def infinite_norm(aa,bb):
    d=2*(aa+bb)
    Q=(d*d-aa*aa-bb*bb)/(aa*bb)
    rr=2/(Q+math.sqrt(Q*Q-4))
    uu=(aa+bb*rr)/d
    vv=(bb+aa*rr)/d
    AA=6/(d-aa*uu-bb*vv)
    expression=AA/(2*(1-rr))*(aa*(1+vv)*(1+uu*uu)/(1+uu)+bb*(1+uu)*(1+vv*vv)/(1+vv))
    return expression,rr,uu,vv,AA

pairs=[(1,1),(1,2),(2,1),(1,10),(10,1),(1,100),(100,1),
       (4,7),(5,3),(9,11),(13,17),(17,13),(1,3),(3,1)]
for aa,bb in pairs:
    measured,rr,uu,vv,AA=infinite_norm(aa,bb)
    expected=(5*aa**2+22*aa*bb+5*bb**2)/(3*aa**2+10*aa*bb+3*bb**2)
    check(0<rr<1 and 0<uu<1 and 0<vv<1 and AA>0,
          f'positive Green parameters for {aa},{bb}')
    check(abs(uu*vv-rr)<1e-13, f'Green product for {aa},{bb}')
    check(abs(measured-expected)<3e-12, f'Green sum for {aa},{bb}')
    check(expected>5/3 and expected<=2+1e-14, f'sharp range for {aa},{bb}')

# Completely independent matrix assembly and integration on a cyclic mesh.
# Periodic finite-domain inverses approximate the bi-infinite Green kernel.
def cyclic_norm(aa,bb,n):
    hs=np.array([aa if k%2==0 else bb for k in range(n)],dtype=float)
    G=np.diag((hs+np.roll(hs,1))/3.)
    for k in range(n):
        G[k,(k+1)%n]+=hs[k]/6.
        G[(k+1)%n,k]+=hs[k]/6.
    columns=np.linalg.solve(G, np.eye(n)[:,0:2])
    row0, row1=columns[:,0], columns[:,1]
    vals=[]
    for row in (row0,row1):
        absrow=np.abs(row)
        check(all((-1)**k*row[k]>0 for k in range(n)) if row is row0 else
              all((-1)**(k+1)*row[k]>0 for k in range(n)),
              f'alternating inverse Gram signs n={n}, {aa},{bb}')
        vals.append(float(sum(hs[k]*(absrow[k]**2+absrow[(k+1)%n]**2)/
                              (2*(absrow[k]+absrow[(k+1)%n])) for k in range(n))))
    check(abs(vals[0]-vals[1])<4e-11,f'reflection symmetry {aa},{bb},{n}')
    return vals[0]

for aa,bb in [(1.,1.),(1.,2.),(1.,10.),(4.,7.)]:
    target=(5*aa**2+22*aa*bb+5*bb**2)/(3*aa**2+10*aa*bb+3*bb**2)
    errors=[]
    for n in (8,16,32,64):
        vnum=cyclic_norm(aa,bb,n)
        errors.append(abs(vnum-target))
        check(1<=vnum<=target+1e-10,f'cycle is bounded by full-line norm {aa},{bb},{n}')
    check(errors[-1]<2e-9,f'large-cycle limit {aa},{bb}')
    check(errors[-1]<errors[0]+1e-15,f'finite-size convergence {aa},{bb}')

# Exact cycle test with rational linear algebra (a separate calculation).
for aa,bb in [(sp.S(1),sp.S(2)),(sp.S(1),sp.S(1))]:
    n=8
    h=[aa if i%2==0 else bb for i in range(n)]
    G=sp.zeros(n)
    for i in range(n):
        G[i,i]=(h[i-1]+h[i])/3
        G[i,(i+1)%n]=h[i]/6
        G[(i+1)%n,i]=h[i]/6
    vec=G.inv()[:,0]
    check(all((-1)**i*vec[i]>0 for i in range(n)),f'exact signed inverse {aa},{bb}')
    Lcyc=sp.simplify(sum(h[i]*(vec[i]**2+vec[(i+1)%n]**2)/
                            (2*(abs(vec[i])+abs(vec[(i+1)%n]))) for i in range(n)))
    check(Lcyc< F.subs({a:aa,b:bb}),f'exact cycle below infinite {aa},{bb}')
    check(abs(float(Lcyc)-cyclic_norm(float(aa),float(bb),n))<1e-12,
          f'exact versus floating independent cycle {aa},{bb}')

print(f'PASS: {checks} independent symbolic, exact rational, and finite-cycle checks')
