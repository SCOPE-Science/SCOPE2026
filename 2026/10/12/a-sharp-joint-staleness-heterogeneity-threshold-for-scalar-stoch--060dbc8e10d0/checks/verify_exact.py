#!/usr/bin/env python3
"""Reproduce polynomial identities for iid one-step-stale scalar SGD.
Requires SymPy; all algebra and finite test cases use exact arithmetic.
"""
from fractions import Fraction as F
from itertools import product
import sympy as S

s,p,theta,x,y=S.symbols('s p theta x y',real=True)
# First/second conditional moments of z = x - s A*(x or y), E A=1.
z2=(1-p)*(1-2*s+theta*s*s)*x*x+p*(x*x-2*s*x*y+theta*s*s*y*y)
zx=(1-(1-p)*s)*x*x-p*s*x*y
v=lambda u,w:(1+p*s)*u*u-2*p*s*u*w+p*theta*s*s*(1+p*s)*w*w
mean_next_v=(1+p*s)*z2-2*p*s*zx+p*theta*s*s*(1+p*s)*x*x
drift=S.expand(mean_next_v-v(x,y))
assert S.simplify(drift-s*(theta*(s+p*s*s)-2)*x*x)==0
T=S.Matrix([
[1-2*(1-p)*s+(1-p)*theta*s*s,-2*p*s,p*theta*s*s],
[1-(1-p)*s,-p*s,0],
[1,0,0]])
assert S.simplify((S.eye(3)-T).det()-s*(2-theta*s-p*theta*s*s))==0
# Positive definiteness of the quadratic form: V11>0 and determinant.
G=S.Matrix([[1+p*s,-p*s],[-p*s,p*theta*s*s*(1+p*s)]])
assert S.simplify(G.det()-p*s*s*(theta*(1+p*s)**2-p))==0
pp,tt=S.symbols('pp tt',positive=True)
root=4/(tt+S.sqrt(tt*tt+8*pp*tt))
assert S.simplify(tt*(root+pp*root*root)-2)==0
assert S.simplify(S.limit(root,pp,0)-2/tt)==0



def V(z,w,step,prob,second):
    return (1+prob*step)*z*z-2*prob*step*z*w+prob*second*step*step*(1+prob*step)*w*w

cases=0
for prob,d,step,xx,yy in product(
    [F(0),F(1,7),F(1,2),F(5,7),F(1)],
    [F(0),F(1,5),F(2,5),F(3,5),F(4,5)],
    [F(1,3),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(2)],
    [F(-2),F(0),F(1),F(3)],
    [F(-2),F(0),F(1),F(3)],
):
    second=1+d*d
    actual=F(0)
    for a in [1-d,1+d]:
        for lag,lagp in [(0,1-prob),(1,prob)]:
            nxt=xx-step*a*(yy if lag else xx)
            actual+=F(1,2)*lagp*V(nxt,xx,step,prob,second)
    expected=V(xx,yy,step,prob,second)+step*(second*(step+prob*step*step)-2)*xx*xx
    assert actual==expected,(prob,d,step,xx,yy)
    cases+=1
assert cases==2800
# Stability / instability at rational points with strictly positive samples.
assert F(5,4)*(F(1)+F(1,2)*F(1)**2)<2
assert F(5,4)*(F(6,5)+F(1,2)*F(6,5)**2)>2
print('VERIFY_OK symbolic_drift=1 symbolic_moment_matrix=1 exact_cases='+str(cases))
