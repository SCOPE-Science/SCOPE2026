from fractions import Fraction as F

def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def mode_matrix(a, b, rho, alpha):
    p = rho / (a + rho)
    q = rho / (b + rho)
    hz = alpha*p + 1 - alpha
    hu = 1 - alpha*p
    return [[q*hz, q*hu], [(1-q)*hz, (1-q)*hu]]

def zeta(a, b, rho, alpha):
    return 1 - alpha*rho*(a+b)/((rho+a)*(rho+b))

rho, alpha, tau = F(4), F(15,8), F(7,2)
pairs = [(F(1),F(5)), (F(2),F(6))]
for a,b in pairs:
    assert a*b == tau*(a+b) - rho*rho
    assert zeta(a,b,rho,alpha) == 0
    M = mode_matrix(a,b,rho,alpha)
    assert mm(M,M) == [[F(0),F(0)],[F(0),F(0)]]

assert mode_matrix(F(1),F(5),rho,alpha) == [[F(5,18),F(-2,9)],[F(25,72),F(-5,18)]]
assert mode_matrix(F(2),F(6),rho,alpha) == [[F(3,20),F(-1,10)],[F(9,40),F(-3,20)]]

A=[F(1),F(2)]; B=[F(5),F(6)]; c=[F(-6),F(-8)]
def step(z,u):
    x=[(-c[i]+rho*(z[i]-u[i]))/(A[i]+rho) for i in range(2)]
    hat=[alpha*x[i]+(1-alpha)*z[i] for i in range(2)]
    z2=[rho*(hat[i]+u[i])/(B[i]+rho) for i in range(2)]
    u2=[u[i]+hat[i]-z2[i] for i in range(2)]
    return x,z2,u2

z=[F(0),F(0)]; u=[F(0),F(0)]
x1,z1,u1=step(z,u)
assert x1 == [F(6,5),F(4,3)]
assert z1 == [F(1),F(1)]
assert u1 == [F(5,4),F(3,2)]
x2,z2,u2=step(z1,u1)
assert x2 == [F(1),F(1)] and z2==z1 and u2==u1

z=[F(7,3),F(-5,4)]; u=[F(-2,5),F(11,6)]
_,z1,u1=step(z,u)
_,z2,u2=step(z1,u1)
assert z2 == [F(1),F(1)] and u2 == [F(5,4),F(3,2)]
x3,_,_=step(z2,u2)
assert x3 == [F(1),F(1)]
print("VERIFY_OK")
