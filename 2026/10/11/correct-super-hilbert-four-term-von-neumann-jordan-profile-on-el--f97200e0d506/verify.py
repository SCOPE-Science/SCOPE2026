from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal

def fourth_root(z):
    return z.sqrt().sqrt()

def norm4(v):
    return fourth_root(sum(abs(z) ** 4 for z in v))

def add(a,b,sa=D(1),sb=D(1)):
    return [sa*x + sb*y for x,y in zip(a,b)]

lam = D(1) / D(4)
c = fourth_root(D(1) / D(2))
x = [c,c]
y = [c,-c]
assert abs(norm4(x)-D(1)) < D('1e-70')
assert abs(norm4(y)-D(1)) < D('1e-70')

A = norm4(add(x,y,lam,D(1)-lam))
B = norm4(add(x,y,lam,-(D(1)-lam)))
C = norm4(add(x,y))
E = norm4(add(x,y,D(1),D(-1)))
F = (A*A + B*B + lam*(D(1)-lam)*(C*C+E*E)) / D(2)

sqrt17 = D(17).sqrt()
sqrt2 = D(2).sqrt()
sharp = (sqrt17 + D(3)) / (D(4)*sqrt2)
source_value = D(7).sqrt() / D(2)
assert abs(F-sharp) < D('1e-65')
assert sharp < source_value
# Exact sign reduction for the squared comparison: sqrt(17) < 5 because 17 < 25.
assert D(17) < D(25)
assert abs(sharp*sharp - (D(13)+D(3)*sqrt17)/D(16)) < D('1e-65')
assert abs(source_value*source_value - D(7)/D(4)) < D('1e-65')
print('VERIFY_OK')
