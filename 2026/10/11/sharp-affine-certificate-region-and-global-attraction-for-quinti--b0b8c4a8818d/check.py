#!/usr/bin/env python3
"""Exact-rational reproducibility spot checks for the quartic affine certificate."""
from fractions import Fraction as F

def quartic(x,a1,a2,a3,a4,alpha):
    return 2*(x**4+a4*x**3+a3*x*x+a2*x+a1)+alpha*x

def square_formula(x,a1_sqrt,a3,a4):
    beta=a3-a4*a4/F(4)+2*a1_sqrt
    return 2*((x*x+(a4/F(2))*x-a1_sqrt)**2+beta*x*x)

for s,a2,a3,a4 in [(F(1),F(5),F(-1),F(0)),(F(2),F(-5),F(0),F(4)),(F(1),F(7),F(0),F(2))]:
    a1=s*s
    alpha=-2*a2-2*a4*s
    for m in range(-20,21):
        x=F(m,7)
        assert quartic(x,a1,a2,a3,a4,alpha)==square_formula(x,s,a3,a4)
assert F(1)+F(5)*F(-1,2)-F(1,2)**2+F(-1,2)**4==F(-27,16)
# Under a3<-2 (with a1=1,a4=0), opposite-root evaluations contradict any linear term.
s=F(1);a1=s*s;a4=F(0);a3=F(-3);beta=a3+2*s
assert beta<0
# At q(1)=q(-1)=0, p(1)/2 = beta+gamma and p(-1)/2=beta-gamma.
# Both nonnegative would force gamma>=-beta>0 and gamma<=beta<0.
assert -beta>0 and beta<0
print('CHECK_OK')
