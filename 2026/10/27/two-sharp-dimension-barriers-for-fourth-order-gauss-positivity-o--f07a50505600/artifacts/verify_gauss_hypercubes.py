#!/usr/bin/env python3
"""Exact independent checks for Padé [2/2] positivity on Boolean cubes."""
from math import comb
import sympy as S

h,z=S.symbols('h z', real=True)
R=(12+6*z+z*z)/(12-6*z+z*z)
coeffs=[S.expand(S.series(R,z,0,10).removeO()).coeff(z,k) for k in range(10)]
assert coeffs[:9]==[1,1,S.Rational(1,2),S.Rational(1,6),S.Rational(1,24),S.Rational(1,144),0,-S.Rational(1,1728),-S.Rational(1,3456)]

def orbit(d,j):
    return S.factor(sum(sum((-1)**a*comb(j,a)*comb(d-j,k-a) for a in range(max(0,k-(d-j)),min(j,k)+1)) * R.subs(z,-2*k*h) for k in range(d+1))/2**d)

u3=(h*h+3*h+3)*(3*h*h+3*h+1)*(4*h*h+6*h+3)
q=h**4-6*h**3-20*h**2-18*h-6
assert S.factor(orbit(3,1) + 3*h*q/(2*u3))==0
assert S.factor(orbit(3,2) - 3*h*h*(7*h**3+18*h*h+18*h+6)/(2*u3))==0
assert S.factor(orbit(3,3) - 3*h**3*(11*h*h+18*h+6)/(2*u3))==0
assert S.factor(orbit(2,1) - 3*h/(4*h*h+6*h+3))==0
assert S.factor(orbit(2,2) - 9*h*h*(h+1)/((h*h+3*h+3)*(4*h*h+6*h+3)))==0

# All off-diagonal leading coefficients for Q_1,...,Q_7.
# Krawtchouk expansion is independent of matrix-inverse implementations.
for d in range(1,8):
    for j in range(1,d+1):
        first=None
        for m in range(j,10):
            km=sum(sum((-1)**a*comb(j,a)*comb(d-j,k-a) for a in range(max(0,k-d+j),min(j,k)+1))*(-2*k)**m for k in range(d+1))
            c=S.factor(coeffs[m]*S.Rational(km,2**d))
            if c!=0:
                first=(m,c)
                break
        assert first is not None
        if j<=4: assert first==(j,S.Integer(1)), (d,j,first)
        elif j==5: assert first==(5,S.Rational(5,6)),(d,j,first)
        elif j==6: assert first==(7,S.Rational(35*d,12)),(d,j,first)
        elif j==7: assert first==(7,-S.Rational(35,12)),(d,j,first)

# Exact Green edge formula via the heat kernel and spectral binomial sums.
# Ldagger_{0,e_1} = 2^(-d-1) integral_0^1 ((1-u)(1+u)^(d-1)-1)/u du.
u=S.symbols('u')
for d in range(1,9):
    integrand=S.cancel(((1-u)*(1+u)**(d-1)-1)/u)
    green=S.integrate(integrand,(u,0,1))/2**(d+1)
    spectral=sum(S.Rational(comb(d-1,k)-comb(d-1,k-1) if k>0 else 1,2*k) for k in range(1,d+1))/2**d
    # For k>=1, Walsh sum over subsets of size k, pair sign: C(d-1,k)-C(d-1,k-1).
    spectral=sum(S.Rational(comb(d-1,k) if k<=d-1 else 0,2*k)-S.Rational(comb(d-1,k-1),2*k) for k in range(1,d+1))/2**d
    assert S.simplify(green-spectral)==0,(d,green,spectral)
    if d>=3: assert green>0
    if d==2: assert green==-S.Rational(1,16)

# Independent dense symbolic matrix rational identity for Q_3 at rational h.
for step in (S.Rational(1,7),S.Rational(1,1),S.Rational(8,1),S.Rational(9,1),S.Rational(40,1)):
    d=3; nn=1<<d
    adjacency=S.zeros(nn)
    for x in range(nn):
        for bit in range(d): adjacency[x,x^(1<<bit)]=1
    L=d*S.eye(nn)-adjacency
    B=12*S.eye(nn)+6*step*L+step**2*L**2
    P=(12*S.eye(nn)-6*step*L+step**2*L**2)*B.inv()
    assert all(P[0,y]==orbit(d,int(y).bit_count()).subs(h,step) for y in range(nn))
    assert all(sum(P[x,y] for y in range(nn))==1 for x in range(nn))
    for x in range(nn):
        for y in range(nn):
            if x!=y:
                if step<9: assert P[x,y]>0
                else:
                    if int(x^y).bit_count()==1: assert P[x,y]<0
                    else:assert P[x,y]>0
root=S.nroots(q,maxsteps=100)
positive=[S.re(t) for t in root if abs(float(S.im(t)))<1e-9 and t>0]
assert len(positive)==1
print('VERIFY_OK', 'cube_cutoff=',positive[0], 'small_dim_boundary=7', 'large_dim_boundary=3', 'exact_cube_matrices=5', 'green_edge_checks=8')
