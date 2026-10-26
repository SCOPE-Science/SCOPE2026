"""Exact algebra and independent moment-propagation checks for the two-node lognormal heat splitting theorem.

Run: python check.py. Requires SymPy. Universal conclusions are established in RESULT.md.
"""
from fractions import Fraction
from math import exp, log, sqrt
import sympy as S

y,m=S.symbols('y m', positive=True)
u=(y+y**3)/2
v=(y-y**3)/2
K=S.Matrix([[m*u,v],[m*v,u]])
assert S.factor((S.eye(2)-K).det() - (1-u-m*(u-y**4)))==0
mc=S.factor((1-u)/(u-y**4))
assert S.simplify(mc-(2+y+y**2)/(y*(1+y+2*y**2)))==0
R=(2+y+y**2)/(1+y+2*y**2)
gp=S.factor(-2*y*S.diff(S.log(R),y))
gpp=S.factor(-2*y*S.diff(gp,y))
assert S.simplify(gp-2*y*(y*y+6*y+1)/((y*y+y+2)*(2*y*y+y+1)))==0
assert S.simplify(gpp-8*y*(y-1)*(y+1)*(y**4+12*y**3+10*y*y+12*y+1)/((y*y+y+2)**2*(2*y*y+y+1)**2))==0
assert S.limit(gp,y,1)==1
assert S.limit(R,y,0,dir='+')==2

# Cross-check the exact covariance map on a non-symmetric rank-one covariance.
z1,z2=S.symbols('z1 z2',real=True)
p=(S.sqrt(y)+y**S.Rational(3,2))/2
q=(S.sqrt(y)-y**S.Rational(3,2))/2
B=S.Matrix([[p,q],[q,p]])
X=S.Matrix([[z1*z1,z1*z2],[z1*z2,z2*z2]])
Q=S.Matrix([[m*z1*z1,z1*z2],[z1*z2,m*z2*z2]])
Y=S.simplify(B*Q*B)
s=(X[0,0]+X[1,1])/2
t=X[0,1]
d=(X[0,0]-X[1,1])/2
assert S.simplify((Y[0,0]+Y[1,1])/2-(m*u*s+v*t))==0
assert S.simplify(Y[0,1]-(m*v*s+u*t))==0
assert S.simplify((Y[0,0]-Y[1,1])/2-m*y*y*d)==0

# Exact sample at h=1/3, sigma^2=15/2.
assert mc.subs(y,S.Rational(1,4))==S.Rational(74,11)
assert mc.subs(y,S.Rational(1,16))==S.Rational(4232,137)
assert 4*S.sqrt(2) < S.Rational(74,11)
assert S.Integer(32)>S.Rational(4232,137)

# Independent full 3-dimensional second-moment map tested against reduced K,
# with exact rational heat eigenvalues, multipliers and initial vectors.
count=0
for yy in [S.Rational(1,2),S.Rational(1,3),S.Rational(1,4),S.Rational(1,5),S.Rational(1,8),S.Rational(1,16),S.Rational(2,3)]:
    a=S.sqrt(yy); b=yy**S.Rational(3,2)
    BB=S.Matrix([[(a+b)/2,(a-b)/2],[(a-b)/2,(a+b)/2]])
    uu=(yy+yy**3)/2; vv=(yy-yy**3)/2
    for mm in [S.Rational(1),S.Rational(3,2),S.Rational(2),S.Rational(4),S.Rational(11),S.Rational(37)]:
        KK=S.Matrix([[mm*uu,vv],[mm*vv,uu]])
        for z in [(1,0),(0,1),(1,1),(1,-1),(2,3),(-3,2)]:
            vec=S.Matrix(z); XX=vec*vec.T
            ss=(XX[0,0]+XX[1,1])/2; tt=XX[0,1]
            for it in range(3):
                v_expected=KK**it*S.Matrix([ss,tt]);
                assert S.simplify(v_expected[0]-(XX[0,0]+XX[1,1])/2)==0
                assert S.simplify(v_expected[1]-XX[0,1])==0
                XX=BB*S.Matrix([[mm*XX[0,0],XX[0,1]],[XX[1,0],mm*XX[1,1]]])*BB
                count+=2

# Numeric inequalities independently exercise both sides of the exact cutoff.
for x in [0.05,0.2,0.7,1,1.5,2,4]:
    yy=exp(-2*x); uu=(yy+yy**3)/2; vv=(yy-yy**3)/2
    cutoff=log((2+yy+yy**2)/(yy*(1+yy+2*yy**2)))/x
    for eta in [cutoff-0.1,cutoff+0.1]:
        mm=exp(eta*x)
        discr=uu*uu*(mm-1)**2+4*mm*vv*vv
        rho=(uu*(mm+1)+sqrt(discr))/2
        assert (rho<1) == (eta<cutoff)
        count+=1
print('PASS: symbolic covariance identities, exact cutoff and strict curvature; %d independent moment/threshold assertions' % count)
