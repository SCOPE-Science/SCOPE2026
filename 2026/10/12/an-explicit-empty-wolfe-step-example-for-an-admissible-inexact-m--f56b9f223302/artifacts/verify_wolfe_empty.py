from fractions import Fraction as F
x0=F(1,10); eps0=F(1,4); eps1=F(1,5); delta=F(1,4); sigma=F(1,2)
e0=-F(9,20)
# q_x(z)=F(x)+(z-x/2)^2 for f(z)=z^2/2, lambda=1.
g0=x0/F(2)-e0
d0=-g0
Fa0=x0*x0/F(4)+e0*e0
assert e0*e0 <= eps0
assert g0==F(1,2) and d0==-F(1,2) and Fa0==F(41,200)
# Trial oracle at eps1 uses e=-2/5 for y>-1/5 and +2/5 otherwise.
for j in range(1,4001):
    a=F(j,1000)
    y=x0+a*d0
    e=-F(2,5) if y>-F(1,5) else F(2,5)
    assert e*e <= eps1
    g1=y/F(2)-e
    Fa1=y*y/F(4)+e*e
    armijo=(Fa1-Fa0 <= delta*a*g0*d0)
    curvature=(g1*d0 >= sigma*g0*d0)
    assert not (armijo and curvature), (a, y, e, g1, Fa1)
# Exact symbolic branch checks.
# For 0<a<3/5, g1=9/20-a/4 >3/10>1/4, so curvature fails.
assert F(3,10) > F(1,4)
# For a>=3/5, Armijo is equivalent to 25a^2+15a-17<=0; polynomial is increasing on a>0.
a=F(3,5)
assert 25*a*a+15*a-17 == 1 > 0
print('VERIFY_OK')
