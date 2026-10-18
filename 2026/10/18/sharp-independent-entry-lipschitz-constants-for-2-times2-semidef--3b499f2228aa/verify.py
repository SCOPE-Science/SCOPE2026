#!/usr/bin/env python3
"""Independent-entry coordinate sensitivity of real 2-by-2 PSD projection.

This checks algebraic formulas on exact rational samples and numerically tests
projection identities, Jacobians, finite-difference sharpness, and norm bounds.
It does not replace the proof of uniform bounds over continuous parameters.
Only the Python 3 standard library is required.
"""
import math
import random
from fractions import Fraction

ROOT2 = math.sqrt(2.0)
EPS = 1e-8
rng = random.Random(470902)
checks = 0

def test(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

def norm(x, p):
    if p == 1:
        return sum(abs(t) for t in x)
    if p == 2:
        return math.sqrt(sum(t*t for t in x))
    if p == math.inf:
        return max(abs(t) for t in x)
    raise ValueError(p)

def positive_part_spectral(x):
    a, c, b = x
    mid = (a+c)/2.0
    rad = math.hypot((a-c)/2.0, b)
    if rad == 0.0:
        return (max(a, 0.0), max(c, 0.0), 0.0)
    lp, lm = mid+rad, mid-rad
    fp, fm = max(lp, 0.0), max(lm, 0.0)
    alpha = (fp-fm)/(2*rad)
    beta = (fm*lp-fp*lm)/(2*rad)
    return (alpha*a+beta, alpha*c+beta, alpha*b)

def positive_part_lorentz(x):
    a,c,b = x
    T = (a+c)/ROOT2
    Z = (a-c)/ROOT2
    W = ROOT2*b
    r = math.hypot(Z,W)
    if T >= r:
        return x
    if T <= -r:
        return (0.0,0.0,0.0)
    s = (T+r)/2.0
    Zp,Wp = s*Z/r, s*W/r
    return ((s+Zp)/ROOT2,(s-Zp)/ROOT2,Wp/ROOT2)

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def transpose(A):
    return [list(row) for row in zip(*A)]

def mv(A,x):
    return [sum(a*b for a,b in zip(row,x)) for row in A]

def deriv(u,v,s):
    # Jacobian in Lorentz coordinates; s=T/|Z| in the mixed-eigenvalue sector.
    U = [u,v]
    J = [[0.5,0.5*u,0.5*v]]
    for i in range(2):
        row = [0.5*U[i]]
        for j in range(2):
            row.append(0.5*((1+s)*(1.0 if i==j else 0.0)-s*U[i]*U[j]))
        J.append(row)
    M = [[1/ROOT2,1/ROOT2,0],[1/ROOT2,-1/ROOT2,0],[0,0,ROOT2]]
    Mi = [[1/ROOT2,1/ROOT2,0],[1/ROOT2,-1/ROOT2,0],[0,0,1/ROOT2]]
    return mm(mm(Mi,J),M)

def endpoint(t,sign):
    q = math.sqrt(t*(1-t))
    v = [t,1-t,sign*q]
    f = [t,1-t,sign*2*q]
    P = [[v[i]*f[j] for j in range(3)] for i in range(3)]
    return P, [[(1.0 if i==j else 0.0)-P[i][j] for j in range(3)] for i in range(3)]

def induced_1(A):
    return max(sum(abs(A[i][j]) for i in range(3)) for j in range(3))

def induced_inf(A):
    return max(sum(abs(z) for z in row) for row in A)

def induced_2(A):
    # Stable power method on A^T A. Seeds span independent directions.
    C=mm(transpose(A),A)
    best=0.0
    for seed in ([1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0],[1.0,1.0,1.0]):
        x=list(seed)
        for _ in range(85):
            y=mv(C,x)
            n=norm(y,2)
            if n<1e-15:
                break
            x=[z/n for z in y]
        best=max(best,math.sqrt(max(0.0,sum(z*w for z,w in zip(x,mv(C,x))))/sum(z*z for z in x)))
    return best

# Exact rational algebra for the endpoint oblique projectors.
for aa,bb in ((3,4),(5,12),(8,15),(7,24),(20,21),(9,40)):
    den=aa*aa+bb*bb
    t=Fraction(aa*aa,den); q=Fraction(aa*bb,den)
    v=(t,1-t,q); f=(t,1-t,2*q)
    test(sum(a*b for a,b in zip(v,f))==1,'dual normalization')
    test(sum(z*z for z in v)==1-q*q,'primal Euclidean norm')
    test(sum(z*z for z in f)==1+2*q*q,'dual Euclidean norm')
    test((1-q*q)*(1+2*q*q)==1+q*q-2*q**4,'squared norm factorization')

# Compare spectral and Lorentz constructions across all sign regimes.
for _ in range(2500):
    x=tuple(rng.uniform(-4,4) for i in range(3))
    a=positive_part_spectral(x)
    b=positive_part_lorentz(x)
    test(norm([aa-bb for aa,bb in zip(a,b)],math.inf)<3e-14,
         'projection representations')

# Jacobian from geometric coordinates against finite differences.
for _ in range(900):
    theta=rng.uniform(0,2*math.pi)
    u,v=math.cos(theta),math.sin(theta)
    s=rng.uniform(-.90,.90)
    radius=rng.uniform(.8,2.0)
    a=(s+u)*radius/ROOT2
    c=(s-u)*radius/ROOT2
    b=v*radius/ROOT2
    J=deriv(u,v,s)
    for k in range(3):
        h=2e-6
        e=[0.0,0.0,0.0];e[k]=h
        plus=positive_part_lorentz(tuple(x+y for x,y in zip((a,c,b),e)))
        minus=positive_part_lorentz(tuple(x-y for x,y in zip((a,c,b),e)))
        fd=[(x-y)/(2*h) for x,y in zip(plus,minus)]
        test(norm([fd[j]-J[j][k] for j in range(3)],math.inf)<3e-8,
             'Jacobian finite difference')

# Endpoint derivative formulas and interpolation along the mixed sector.
for _ in range(1200):
    theta=rng.uniform(0,2*math.pi)
    u,v=math.cos(theta),math.sin(theta)
    tplus=(1+u)/2
    tminus=(1-u)/2
    orientation=(1 if v>=0 else -1)
    lo,_=endpoint(tplus,orientation)
    _,hi=endpoint(tminus,-orientation)
    for s,J in ((-1,lo),(1,hi)):
        K=deriv(u,v,s)
        test(max(abs(K[i][j]-J[i][j]) for i in range(3) for j in range(3))<2e-14,
             'endpoint formula')
    s=rng.uniform(-1,1)
    J=deriv(u,v,s)
    B=[[(1-s)*lo[i][j]/2+(1+s)*hi[i][j]/2 for j in range(3)] for i in range(3)]
    test(max(abs(J[i][j]-B[i][j]) for i in range(3) for j in range(3))<2e-14,
         'Jacobian interpolation')
    test(induced_1(J)<=1.5+3e-13, 'l1 upper')
    test(induced_inf(J)<=1.5+3e-13, 'linfty upper')
    test(induced_2(J)<=3/(2*ROOT2)+4e-12, 'l2 upper')

# Global inequality on sampled input pairs (not a substitute for proof).
for _ in range(1100):
    x=tuple(rng.uniform(-3,3) for i in range(3))
    y=tuple(rng.uniform(-3,3) for i in range(3))
    dx=tuple(a-b for a,b in zip(x,y))
    px,py=positive_part_lorentz(x),positive_part_lorentz(y)
    dp=tuple(a-b for a,b in zip(px,py))
    for p,L in ((1,1.5),(2,3/(2*ROOT2)),(math.inf,1.5)):
        test(norm(dp,p)<=L*norm(dx,p)+1e-12,'global random pair')

# Exact finite-pair attainment in coordinate l1.
x=(0.,0.,1.); y=(0.,0.,2.)
d=tuple(aa-bb for aa,bb in zip(positive_part_lorentz(y),positive_part_lorentz(x)))
test(abs(norm(d,1)/norm(tuple(aa-bb for aa,bb in zip(y,x)),1)-1.5)<1e-14,
     'l1 equality pair')

# The other endpoint norms are approached by ordinary smooth points.
for eps in (1e-3, 1e-5, 1e-7):
    J=deriv(0,1,1-eps)
    test(induced_inf(J)>1.5-2*eps,'linfty sharp boundary direction')
    test(induced_2(J)>3/(2*ROOT2)-2*eps,'l2 sharp boundary direction')

print('CHECKS_OK',checks)
print('SHARP_CONSTANTS',1.5,3/(2*ROOT2),1.5)
