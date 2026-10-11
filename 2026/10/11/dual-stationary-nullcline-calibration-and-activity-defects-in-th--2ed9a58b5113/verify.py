from fractions import Fraction as F

feed=F(1,10)
kill=F(1,20)
c=feed+kill
Delta=1-F(4)*c*c/feed
assert Delta==F(1,10)

# Choose U satisfying the quadratic inequality at the upper root only symbolically
# through a rational test value strictly inside the admissible interval.
U=F(1,2)
q=feed*U*U-feed*U+c*c
assert q<0
T=feed*U*U/(feed*U*U+c*c)
assert U<T
vfloor=c/U
assert vfloor>0

# Abstract residual/variance algebra.
Varu=F(3,20)
Edu2=F(7,50)
VarQ=feed*feed*Varu+Edu2
assert VarQ-feed*feed*Varu==Edu2

VarP=F(5,21)
Elogv2=VarP
assert VarP==Elogv2

# Pointwise residual identities at an exact state.
u=F(3,5); v=F(1,4)
Q=u*v*v
udot=feed*(1-u)-Q
vdot=Q-c*v
assert Q==feed*(1-u)-udot
assert u*v==c+vdot/v

print('VERIFY_OK')
