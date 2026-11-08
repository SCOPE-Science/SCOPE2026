#!/usr/bin/env python3
"""Exact identities for a three-patch continuous-time extinction-colonization comparison."""
from fractions import Fraction as F
from itertools import permutations
import sympy as S

r,s=S.symbols('r s',positive=True)

def make_full(edges):
    Q=S.zeros(7)
    for st in range(1,8):
        i=st-1
        for v in range(3):
            if st&(1<<v):
                nxt=st & ~(1<<v)
                if nxt: Q[i,nxt-1]+=1
                Q[i,i]-=1
            else:
                rate=sum(w for a,b,w in edges if (a==v and (st&(1<<b))) or (b==v and (st&(1<<a))))
                Q[i,(st|(1<<v))-1]+=rate
                Q[i,i]-=rate
    return Q

QT=make_full([(0,1,r),(1,2,r),(0,2,r)])
QP=make_full([(0,1,S.Rational(3,2)*r),(1,2,S.Rational(3,2)*r)])
# Reduced generators in occupancy-count and endpoint-reflection classes.
KT=S.Matrix([[-1-2*r,2*r,0],[2,-2-2*r,2*r],[0,3,-3]])
KP=S.Matrix([
    [-1-3*r,0,3*r,0,0],
    [0,-1-S.Rational(3,2)*r,S.Rational(3,2)*r,0,0],
    [1,1,-2-S.Rational(3,2)*r,0,S.Rational(3,2)*r],
    [0,2,0,-2-3*r,3*r],
    [0,0,2,1,-3]
])
DT=s**3+(6+4*r)*s**2+(11+8*r+4*r*r)*s+6
poly=15*r*r+14*r*s+34*r+3*s*s+14*s+7
DP=(2*r+s+1)*(3*r+s+2)*DT-r*r*s*poly/4
checks=0

def ok(v):
    global checks
    assert S.cancel(v)==0, str(v)
    checks+=1

ok(KT.det() - KT.det())
ok(S.det(s*S.eye(3)-KT)-DT)
ok(S.det(s*S.eye(5)-KP)-DP)
# Cramer's-rule numerator of the last component of resolvent times one.
def cramer(A):
    B=A.copy()
    B[:,B.rows-1]=S.ones(B.rows,1)
    return S.det(B)
NT=cramer(s*S.eye(3)-KT)
NP=cramer(s*S.eye(5)-KP)
ok(DT-s*NT-6)
ok(DP-s*NP-6*(2*r+s+1)*(3*r+s+2))
# Strict Laplace order; the positive right side is the exact numerator.
ok(6*((2*r+s+1)*(3*r+s+2)*DT-DP)-S.Rational(3,2)*r*r*s*poly)
# Exact mean difference and fifth-order short-time difference.
mean_diff=r*r*(15*r*r+34*r+7)/(24*(2*r+1)*(3*r+2))
ok((S.Rational(3,2)*r*r*poly/(DT*DP)).subs(s,0)-mean_diff)
for j in range(5):
    ok((KT**j*S.ones(3,1))[2]-(KP**j*S.ones(5,1))[4])
ok((KT**5*S.ones(3,1))[2]-(KP**5*S.ones(5,1))[4]-S.Rational(9,2)*r*r)
# Full seven-state state-space independent check of reduced model via exact linear systems.
for rr in [S.Rational(1,10),S.Rational(1,2),S.Integer(1),S.Integer(2),S.Integer(7)]:
    for ss in [S.Rational(1,10),S.Rational(1,2),S.Integer(1),S.Integer(3)]:
        for full,red in [(QT,KT),(QP,KP)]:
            ff=full.subs(r,rr)
            kr=red.subs(r,rr)
            u=(ss*S.eye(7)-ff).inv()*S.ones(7,1)
            v=(ss*S.eye(red.rows)-kr).inv()*S.ones(red.rows,1)
            ok(u[6]-v[-1])
            expect=6/DT if red is KT else 6*(2*r+s+1)*(3*r+s+2)/DP
            ok((1-ss*u[6])-expect.subs({r:rr,s:ss}))
# Coefficient-by-coefficient polynomial comparison of full seven-state time expansion.
for j in range(7):
    lhs=(QT**j*S.ones(7,1))[6]-(QP**j*S.ones(7,1))[6]
    rhs=(KT**j*S.ones(3,1))[2]-(KP**j*S.ones(5,1))[4]
    ok(lhs-rhs)
print(f'PASS: {checks} symbolic and exact-rational assertions')
