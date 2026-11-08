"""Exact symbolic and geometric checks for a diagonally corner-clipped cube.
Requires Python 3, sympy, numpy and scipy. Run: python check.py.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import product
from math import factorial
import sympy as S
from scipy.spatial import ConvexHull
import numpy as np

D,t,q,k,z=S.symbols('D t q k z')
u=12*t*t/((D+1)*(D+2))
delta=(D+1-2*t)/(2*(D+1))
F=(1-q)*(1-q*u/(D+1))-12*D*q*delta**2
T=lambda x:S.expand(t*S.diff(x,t)+D*q*S.diff(x,q))
N=S.factor(T(F)*(1-q*u)*(1-q)-(D-1)*T(q*u)*F*(1-q)+(D+3)*D*q*F*(1-q*u))
assert S.simplify(N/(D*q) - S.factor(N/(D*q)))==0
B=S.cancel(N/(D*q))
c=[S.factor(S.expand(B).coeff(q,i)) for i in range(3)]
assert S.simplify(B-sum(c[i]*q**i for i in range(3)))==0
# Certificate that c1+c2/120<0 for D>=5 and 0<=t<=1.
P=S.cancel(-(c[1]+c[2]/120)*(D+1)**3*(D+2)).subs(D,k+5).expand()
assert S.Poly(P,t).degree()<=4
bern=[]
for i in range(5):
    b=S.factor(sum(P.coeff(t,j)*S.Rational(S.binomial(i,j),S.binomial(4,j)) for j in range(i+1)))
    assert S.Poly(b,k).degree()>=0
    assert all(v>0 for v in S.Poly(b,k).all_coeffs()), (i,b)
    bern.append(str(b))
# For D=2,3,4 use the one-sign-change certificate in z=t/(1-t).
unique_roots={}
for d in (2,3,4):
    nd=S.factor(N.subs({D:d,q:t**d/S.factorial(d)}))
    p=S.cancel(nd/t**d)
    if d==2: p=S.cancel(p/(t-1))
    poly=S.Poly(p,t)
    h=S.Poly(S.expand(sum(co*z**j*(1+z)**(poly.degree()-j) for (j,),co in poly.terms())),z)
    signs=[S.sign(v) for v in reversed(h.all_coeffs())]
    nonzero=[i for i in signs if i]
    assert sum(a!=b for a,b in zip(nonzero,nonzero[1:]))==1
    assert S.sign(poly.eval(0)) != S.sign(poly.eval(1))
    unique_roots[d]=(str(S.factor(p)), ''.join('+' if v>0 else '-' for v in signs))
    intervals={2:(S.Rational(295,1000),S.Rational(297,1000)),3:(S.Rational(526,1000),S.Rational(528,1000)),4:(S.Rational(810,1000),S.Rational(811,1000))}
    lo,hi=intervals[d]
    assert S.sign(poly.eval(lo))*S.sign(poly.eval(hi))==-1
# Geometric integral check. Qhull triangulates boundary, exact rational integration
# over d-simplices with common interior point, without using deleted-cap formulas.
def polytope_moments(d:int, r:Q):
    points=[tuple(Q(i) for i in v) for v in product((0,1),repeat=d) if not all(i==1 for i in v)]
    points.extend(tuple(Q(1)-r if i==j else Q(1) for i in range(d)) for j in range(d))
    points=list(dict.fromkeys(points))
    hull=ConvexHull(np.array([[float(v) for v in a] for a in points]),qhull_options='Qx')
    origin=tuple(Q(1,10+j) for j in range(d))
    total=S.Rational(0)
    first=[S.Rational(0) for _ in range(d)]
    second=[[S.Rational(0) for _ in range(d)] for __ in range(d)]
    for face in hull.simplices:
        vertices=[origin]+[points[int(i)] for i in face]
        mat=S.Matrix([[S.Rational(vertices[i+1][j]-vertices[0][j]) for i in range(d)] for j in range(d)])
        vol=abs(mat.det())/S.factorial(d)
        if not vol:
            continue
        ss=[sum(S.Rational(v[j]) for v in vertices) for j in range(d)]
        for i in range(d):
            first[i]+=vol*ss[i]/(d+1)
            for j in range(d):
                second[i][j]+=vol*(ss[i]*ss[j]+sum(S.Rational(v[i]*v[j]) for v in vertices))/((d+1)*(d+2))
        total+=vol
    mu=[v/total for v in first]
    cov=[[second[i][j]/total-mu[i]*mu[j] for j in range(d)] for i in range(d)]
    return total,mu,cov,len(hull.simplices)

cases=0; simplices=0
for d in (2,3,4,5):
    for r in (Q(1,5),Q(1,2),Q(1)):
        vol,mu,cov,nfaces=polytope_moments(d,r)
        simplices+=nfaces;cases+=1
        Qq=S.Rational(r.numerator,r.denominator)**d/S.factorial(d)
        tt=S.Rational(r.numerator,r.denominator)
        cv=1-Qq
        mc=1-tt/(d+1)
        expected_mu=(S.Rational(1,2)-Qq*mc)/cv
        cr=tt**2/((d+1)*(d+2))
        dd=S.Rational(1,2)-tt/(d+1)
        orth=(S.Rational(1,12)-Qq*cr)/cv
        para=(S.Rational(1,12)-Qq*cr/(d+1))/cv-d*Qq*dd**2/cv**2
        expected_off=(para-orth)/d
        expected_diag=orth+expected_off
        assert vol==cv,(d,r,vol,cv)
        for i in range(d):
            assert mu[i]==expected_mu,(d,r,'centroid')
            for j in range(d):
                assert cov[i][j]==(expected_diag if i==j else expected_off),(d,r,i,j,cov[i][j])
print('CORNER_CUBE_ISOTROPY_CHECKS_PASSED',cases,simplices)
print('BERNSTEIN_POSITIVE_CERTIFICATE',len(bern),'LOW_DIMENSION_DESCARTES', {d:v[1] for d,v in unique_roots.items()})
