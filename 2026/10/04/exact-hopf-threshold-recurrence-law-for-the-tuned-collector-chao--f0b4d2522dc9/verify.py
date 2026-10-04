from fractions import Fraction as F

M=F(49,100)
Y=F(33,10)
alpha=F(-10,1)
beta=F(15,1)
d=1-M*M
K=Y*Y*(beta-M*Y)/(-alpha)
assert K == F(14574087,1000000)

# At beta=M*Y, reconstruct the characteristic coefficients exactly.
beta_h=M*Y
a=F(1,1)/(Y*d)
a2=(Y-M*beta_h)/(Y*d)
a3=F(1,1)/(Y*d)
assert a2 == F(1,1) and a3 == a
# Hence p(lambda)=lambda^3+a lambda^2+lambda+a=(lambda^2+1)(lambda+a).

def check_state(x,y,z):
    xdot=-y+alpha*z**3/Y**3+beta*z/Y
    ydot=(x-M*z/Y)/d
    zdot=(M*x-z/Y)/d
    q=y-M*z
    qdot=ydot-M*zdot
    assert qdot == x
    # G and its derivative.
    G=alpha*z**4/(4*Y**3)+beta*z**2/(2*Y)
    Gp=alpha*z**3/Y**3+beta*z/Y
    # H partial derivatives: H=(x^2+q^2)/2+d z^2/2-d G/M.
    Hx=x
    Hy=q
    Hz=-M*q+d*z-d*Gp/M
    Hdot=Hx*xdot+Hy*ydot+Hz*zdot
    target=(beta-M*Y)*z*z/(M*Y**2)+alpha*z**4/(M*Y**4)
    assert Hdot == target

for state in [(F(1),F(2),F(3)),(F(-2,3),F(5,7),F(-11,5)),(F(0),F(4),F(1,9)),(F(7,4),F(-3,8),F(0))]:
    check_state(*state)

print('VERIFY_OK')
