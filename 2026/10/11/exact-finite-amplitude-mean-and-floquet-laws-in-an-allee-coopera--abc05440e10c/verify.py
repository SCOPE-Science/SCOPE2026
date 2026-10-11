from fractions import Fraction as F

# Example 4 exact constants.
a,b,c,e,m,alpha,beta,eps = F(3),F(9,10),F(2),F(1),F(23,10),F(1),F(2),F(9,10)
xs=e/(eps*c)
ys=(a-b*xs-m/(xs+alpha))/c
coef=m/(c*(xs+alpha)**2)
assert xs == F(5,9)
assert ys == F(143,280)
assert coef == F(1863,3920)

# Reciprocal centering identity, tested exactly at several rational values.
for x in [F(1,7), F(2,3), F(5,4), F(9,2)]:
    s=F(5,9); al=F(1)
    u=x+al; u0=s+al
    lhs=1/u-1/u0
    rhs=-(u-u0)/(u0*u0)+(u-u0)*(u-u0)/(u*u0*u0)
    assert lhs == rhs

# Transformed predator coboundary and divergence cancellation at exact rational states.
for x,y in [(F(2,5),F(3,7)), (F(5,9),F(7,5)), (F(4,3),F(11,6))]:
    q=-e+eps*c*x
    ydot=y*q/(y+beta)
    Hdot=(1+beta/y)*ydot
    assert Hdot == q

    prey_percap=a-b*x-m/(x+alpha)-c*y
    xdot=x*prey_percap
    # Direct divergence.
    dfdx=prey_percap+x*(-b+m/(x+alpha)**2)
    dgdy=beta*q/(y+beta)**2
    div_direct=dfdx+dgdy
    # Coboundary decomposition.
    dlogx=xdot/x
    dlogyfrac=beta*ydot/(y*(y+beta))
    div_decomp=dlogx+dlogyfrac+x*(-b+m/(x+alpha)**2)
    assert div_direct == div_decomp

print('VERIFY_OK')
