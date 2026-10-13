#!/usr/bin/env python3
"""Exact algebraic checks for SAG with uniform replacement and identical quadratics.

All calculations are scientific and use symbolic or rational arithmetic; no simulation.
"""
import sympy as sp

n, s = sp.symbols('n s', positive=True)
one = sp.Integer(1)
# Moment columns represent x*x, x*u, u*u, q, with u=mean stored gradient / lambda.
row_x2 = sp.Matrix([[1, 0, 0, 0]])
row_xu_p = sp.Matrix([[1/n, (n-1)/n, 0, 0]])
row_u2_p = sp.Matrix([[1/n**2, 2*(n-1)/n**2, (n-2)/n, 1/n**2]])
row_q_p = sp.Matrix([[1/n, 0, 0, (n-1)/n]])
T = sp.Matrix.vstack(
    row_x2-2*s*row_xu_p+s**2*row_u2_p,
    row_xu_p-s*row_u2_p,
    row_u2_p, row_q_p
)
A = n-1+1/s
B = (n-1)*(s-2)
C = s*(n-2)*(2*n-1)/2
D = s*(2*n-1)/2
E = sp.Matrix([[A,B,C,D]])
assert all(sp.factor(z)==0 for z in (E*T-E-sp.Matrix([[s-2,0,0,0]])))
assert sp.factor((sp.eye(4)-T).det()+2*s*(s-2)/n**3)==0
minor = sp.factor(A*(C+D)-B**2/4)
assert sp.factor(minor-(n-1)*(2+(n-1)*s*(4*n+2-s))/4)==0
# Rational hand-construction of each sample's full scalar state update.
from fractions import Fraction as F
for N in (2,3,4,6):
    for S in (F(1,3),F(3,2),F(2),F(5,2)):
        xn=F(7,5)
        tab=[F(2*i-N,3) for i in range(N)]
        mean=sum(tab)/N; q=sum(v*v for v in tab)/N
        def energy(xx,bb):
            uu=sum(bb)/N; qq=sum(v*v for v in bb)/N
            return (N-1+1/S)*xx*xx+(N-1)*(S-2)*xx*uu + S*(N-2)*(2*N-1)*uu*uu/F(2)+S*(2*N-1)*qq/F(2)
        v0=energy(xn,tab)
        vals=[]
        for i in range(N):
            b=tab.copy(); b[i]=xn
            xnew=xn-S*sum(b)/N
            vals.append(energy(xnew,b))
        assert sum(vals)/N-v0 == (S-2)*xn*xn
        M=T.subs({n:N,s:sp.Rational(S.numerator,S.denominator)})
        assert sp.factor((sp.eye(4)-M).det()+2*sp.Rational(S.numerator,S.denominator)*(sp.Rational(S.numerator,S.denominator)-2)/N**3)==0
print('VERIFY_OK')
