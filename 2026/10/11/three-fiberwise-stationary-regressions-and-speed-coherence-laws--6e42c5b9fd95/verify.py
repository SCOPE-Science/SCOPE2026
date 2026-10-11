from fractions import Fraction as F

# Generic pointwise residual checks.
a=F(7,3)
b=F(5,2)
c=F(11,4)
x=F(13,7)
y=F(17,9)
z=F(19,10)

xdot=a*(y-x)
ydot=(c-a)*x-x*z+c*y
zdot=x*y-b*z

assert y-x == xdot/a
assert x*(z+a-c)-c*y == -ydot
assert x*y-b*z == zdot

# Abstract orthogonal-regression algebra.
# Predictor B and residual R: E[R]=0, Cov(B,R)=0.
EB=F(2,5)
EB2=F(17,13)
ER=F(0)
ER2=F(7,11)
EBR=F(0)
varB=EB2-EB*EB
varBR=(EB2+2*EBR+ER2)-(EB+ER)**2
cov_B_BR=(EB2+EBR)-EB*(EB+ER)
assert varBR == varB+ER2
assert cov_B_BR == varB

# Scaling check for a predictor kB.
k=F(11,6)
EkB=k*EB
EkB2=k*k*EB2
var_kB=EkB2-EkB*EkB
assert var_kB == k*k*varB

# Classical Chen parameters and equilibrium algebra.
a0=F(35)
b0=F(3)
c0=F(28)
h=2*c0-a0
q2=b0*h
assert h == 21
assert q2 == 63
# At x=y, z=h, x^2=q2:
assert a0*(F(1)-F(1)) == 0
# ydot/x = (c-a)-z+c = 2c-a-z.
assert (c0-a0)-h+c0 == 0
# zdot = x^2-bz.
assert q2-b0*h == 0

print("VERIFY_OK")
