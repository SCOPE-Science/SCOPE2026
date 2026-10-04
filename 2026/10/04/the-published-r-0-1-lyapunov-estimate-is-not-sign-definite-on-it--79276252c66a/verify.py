from fractions import Fraction as F

pi=mu=omega=phi=varphi=vartheta=varsigma=F(1)
rho=F(1)
beta=F(9)
S0=pi/(omega+mu)
R0=beta*vartheta*varphi*phi*S0/((phi+mu)*(mu+varsigma+rho))
assert S0 == F(1,2)
assert R0 == F(3,4)
assert mu/(omega+mu) == F(1,2) < R0 < 1
S=F(4,5)
A=F(1,10)
E=R=Q=F(0)
assert S+E+A+R+Q <= pi/mu
direct = varphi*phi*(beta*vartheta*A*S-(phi+mu)*E) + (phi+mu)*(varphi*phi*E-(mu+varsigma+rho)*A)
factored = (phi+mu)*(mu+varsigma+rho)*A*(R0*S/S0-1)
assert direct == factored == F(3,25)
max_ratio=(pi/mu)/S0
assert max_ratio == (omega+mu)/mu
assert 1/max_ratio == mu/(omega+mu)
print("VERIFY_OK")
