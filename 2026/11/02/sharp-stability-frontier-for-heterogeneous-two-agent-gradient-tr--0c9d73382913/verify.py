#!/usr/bin/env python3
"""Exact algebra and rational checks for a two-agent gradient-tracking stability frontier."""
from fractions import Fraction as F
from random import Random
import sympy as s

B,L,E,U,Z = s.symbols('B L E U Z')
M=s.Matrix([[1-B,B*E*(L-1),-B*E*L],
            [0,L,-L],
            [-B*E,B*(L-1),(1-B)*L]])
a=B*(1+L)-2*L-1
b=B**2*L*(1-E**2)-4*B*L+L**2+2*L
c=-B**2*L*(1-E**2)+B*L*(1+L)-L**2
p=Z**3+a*Z**2+b*Z+c
Q=2*L*(1-E**2)*B**2-(L**2+6*L+1)*B+2*(1+L)**2
S=1-b+a*c-c**2
H=(1-L)**2+2*B*L*(1-L)+B**2*L*(1+L-B)
K=B**2*L*(1+L)**2+B*L*(1-L)*(2*L+3)+(1-L)**2*(1+L)
checks=[
    ('determinant',s.det(Z*s.eye(3)-M)-p),
    ('unit positive',p.subs(Z,1)-B*(1-L)**2),
    ('unit negative',p.subs(Z,-1)+Q),
    ('Schur eta zero',S.subs(E,0)-(1-L**2+B*L)*H),
    ('Schur eta one',S.subs(E,1)-(1-L)*K),
    ('concavity coefficient',s.expand(S.subs(E,s.sqrt(U))).coeff(U,2)+B**4*L**2),
    ('quadratic discriminant',(1+6*L+L**2)**2-16*L*(1-E**2)*(1+L)**2-((1-L)**4+16*E**2*L*(1+L)**2)),
    ('upper minus',Q.subs(B,2)+8*L*E**2),
    ('H endpoint',H.subs(B,2)-(1-L)**2),
]
for name,x in checks:
    assert s.cancel(s.expand(x))==0,name
W=s.Matrix([-E,-B*(1-E**2),1])
assert s.simplify(M.T*W-s.Matrix([-E,-B*(1-E**2),L]))==s.zeros(3,1)
assert s.simplify(s.diff(H,B,2)-2*L*(1+L-3*B))==0
print('Exact polynomial identities:',len(checks)+2)

rng=Random(3456789)
for i in range(5400):
    lam=F(rng.randrange(1,100),100)
    eta=F(rng.randrange(0,100),100)
    beta=F(rng.randrange(1,200),100)
    aa=beta*(1+lam)-2*lam-1
    bb=beta*beta*lam*(1-eta*eta)-4*beta*lam+lam*lam+2*lam
    cc=-beta*beta*lam*(1-eta*eta)+beta*lam*(1+lam)-lam*lam
    q=2*lam*(1-eta*eta)*beta*beta-(lam*lam+6*lam+1)*beta+2*(1+lam)**2
    ss=1-bb+aa*cc-cc*cc
    assert ss>0 and 1+aa+bb+cc>0
    schur=(-1<cc<1) and (1+aa+bb+cc>0) and (1-aa+bb-cc>0) and (ss>0)
    assert schur == (q>0),(i,lam,eta,beta)
print('Exact-rational Schur classifications:',5400)

# Direct exact example: lambda=eta=1/2, beta=3/2 has a root below -1.
example={L:s.Rational(1,2),E:s.Rational(1,2),B:s.Rational(3,2)}
assert s.factor(p.subs(example)-(Z**3+Z**2/4-s.Rational(29,32)*Z+s.Rational(1,32)))==0
assert s.factor(Q.subs(example))==-s.Rational(3,16)
print('Exact instability witness: Q(3/2)=-3/16')
print('All checks passed')
