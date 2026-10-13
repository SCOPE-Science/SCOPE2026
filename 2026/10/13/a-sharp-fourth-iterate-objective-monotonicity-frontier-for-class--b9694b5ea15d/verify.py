from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal

t1 = D(1)
t2 = (D(1) + D(5).sqrt()) / D(2)
t3 = (D(1) + (D(1) + D(4)*t2*t2).sqrt()) / D(2)
t4 = (D(1) + (D(1) + D(4)*t3*t3).sqrt()) / D(2)
b2 = (t2-D(1))/t3
b3 = (t3-D(1))/t4
a = D(1) + b2
c = a*(D(1)+b3)
qplus = (D(1)+c-a)/c
disc = (a+c+D(1))**2 - D(8)*c
qminus = ((a+c+D(1))-disc.sqrt())/(D(2)*c)
kappa = D(1)/qplus

assert D('1.2817535251253208') < a < D('1.2817535251253209')
assert D('1.8380893920091768') < c < D('1.8380893920091769')
assert D('0.7109896908853096') < qminus < D('0.7109896908853097')
assert D('0.8467139159008246') < qplus < D('0.8467139159008247')
assert D('1.1810364530693856') < kappa < D('1.1810364530693857')
assert D(0) < qminus < qplus < D(1)
assert D(1) < a < D(2)
assert c > a

# Check the exact factorization numerically at representative points.
def D4(q):
    return (D(1)-q)**2*(D(1)-c*q)**2 - (D(1)-a*q)**2

def fact(q):
    return q*(a+c*q-c-D(1))*(c*q*q-(a+c+D(1))*q+D(2))

for q in [D('0.2'), D('0.70'), D('0.75'), D('0.84'), D('0.90')]:
    assert abs(D4(q)-fact(q)) < D('1e-70')
assert D4(D('0.70')) < 0
assert D4(D('0.75')) > 0
assert D4(D('0.84')) > 0
assert D4(D('0.90')) < 0

# Direct scalar FISTA replay for q=3/4.
q = D(3)/D(4)
x0 = D(1)
y1 = x0
x1 = (D(1)-q)*y1
# beta_1 = 0
y2 = x1
x2 = (D(1)-q)*y2
y3 = x2 + b2*(x2-x1)
x3 = (D(1)-q)*y3
y4 = x3 + b3*(x3-x2)
x4 = (D(1)-q)*y4
assert abs(x3 - (D(4)-D(3)*a)/D(64)) < D('1e-70')
assert abs(x4 - (D(4)-D(3)*c)/D(256)) < D('1e-70')
ratio = (x4/x3)**2
assert D('5.9852687051217626') < ratio < D('5.9852687051217628')
assert abs(x1) < abs(x0)
assert abs(x2) < abs(x1)
assert abs(x3) < abs(x2)
assert abs(x4) > abs(x3)

# Frontier logic: below the threshold the entire allowed spectrum begins
# at or above qplus; above it an admissible point lies in the violation band.
for kap in [D('1.01'), D('1.10'), D('1.18')]:
    assert D(1)/kap > qplus
for kap in [D('1.19'), D('1.333333333333333333333333333')]:
    assert D(1)/kap < qplus
    lo = max(D(1)/kap, qminus)
    qtest = (lo + qplus)/D(2)
    assert lo < qtest < qplus
    assert D4(qtest) > 0

print('VERIFY_OK')
