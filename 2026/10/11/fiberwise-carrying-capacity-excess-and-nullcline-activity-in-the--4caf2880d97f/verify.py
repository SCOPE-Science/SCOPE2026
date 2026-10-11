from fractions import Fraction as F

r=F(3,2); K=F(5); c=F(4,3); h=F(2,5); s=F(7,10); gamma=F(3,2)
x=F(7,4); y=F(9,5)
H=(r/c)*(x+h)*(1-x/K)
perx=r*(1-x/K)-c*y/(x+h)
xdot=x*perx
assert y-H == -(x+h)/c*(xdot/x)

pery=s*(1-y/(gamma*x))
ydot=y*pery
assert F(1,x)-gamma/y == -gamma/s*(ydot/(y*y))

a=y/gamma
lhs=(x-a)**2/x
assert lhs == x-2*a+a*a/x
assert lhs == x/s**2*(ydot/y)**2

# Positive-equilibrium quadratic for r(x+h)(1-x/K)-c gamma x.
A=-r/K
B=r-r*h/K-c*gamma
C=r*h
assert A<0 and C>0
assert C/A<0  # roots have opposite signs
f0=C
fK=r*(K+h)*(1-K/K)-c*gamma*K
assert f0>0 and fK<0

# Abstract Pythagorean variance checks.
varH=F(5,11); eres=F(7,13)
varY=varH+eres
assert varY-varH==eres
varInvY=F(3,17); eres2=F(2,19)
varInvX=gamma*gamma*varInvY+eres2
assert varInvX-gamma*gamma*varInvY==eres2

print('VERIFY_OK')
