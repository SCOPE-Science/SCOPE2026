from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal
s2 = D(2).sqrt()
s3 = D(3).sqrt()
s6 = D(6).sqrt()
a = D(1) / s2.sqrt()
P = (s3 - s2) / D(2)
c = (a*a + D(4)*P).sqrt()
r = (c-a)/D(2)
d = (c+a)/D(2)

def p4norm(x):
    return sum(t**4 for t in x) ** (D(1)/D(4))

x = (a,a)
y = (-r,d)
w = (d,-r)
A = p4norm((x[0]+y[0],x[1]+y[1]))
B = p4norm((D(2)*x[0]-y[0],D(2)*x[1]-y[1]))
R = y[0]**2*w[0]**2 + y[1]**2*w[1]**2
R0 = D(5)/D(2)-s6
target4 = D(6)*s6-D(3)
M1 = target4 ** (D(1)/D(4))
M2 = target4.sqrt()

def close(z,t,tol=D('1e-60')):
    return abs(z-t) < tol

assert close(p4norm(x),D(1))
assert close(p4norm(y),D(1))
assert close(p4norm(w),D(1))
assert close(R,R0)
assert close(A,B)
assert close(A**4,target4)
assert close(A,M1)
assert close((A*A+B*B)/D(2),M2)
assert close(D(4)*R0*R0-D(20)*R0+D(1),D(0))
print('M1 =', M1)
print('M2 =', M2)
print('R0 =', R0)
print('VERIFY_OK')
