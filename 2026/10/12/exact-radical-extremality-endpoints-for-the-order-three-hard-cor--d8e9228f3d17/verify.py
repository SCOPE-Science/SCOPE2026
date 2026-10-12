from decimal import Decimal, getcontext
from fractions import Fraction

# Exact arithmetic in Q(sqrt(3)): a + b*s, with s^2 = 3.
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def sub(x,y): return (x[0]-y[0], x[1]-y[1])
def mul(x,y): return (x[0]*y[0]+3*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def inv(x):
    d=x[0]*x[0]-3*x[1]*x[1]
    return (x[0]/d, -x[1]/d)
def div(x,y): return mul(x,inv(y))
def powq(x,n):
    r=(Fraction(1),Fraction(0))
    for _ in range(n): r=mul(r,x)
    return r

def lam(z):
    one=(Fraction(1),Fraction(0))
    return div((8*powq(z,4)[0],8*powq(z,4)[1]),powq(add(one,z),3))

s=(Fraction(0),Fraction(1))
one=(Fraction(1),Fraction(0))
zlo=sub(s,one)
zhi=(Fraction(1,2),Fraction(1,2))
lo=lam(zlo)
hi=lam(zhi)
want_lo=(Fraction(-128,3),Fraction(224,9))
want_hi=(Fraction(4,3),Fraction(4,9))
assert lo==want_lo, (lo,want_lo)
assert hi==want_hi, (hi,want_hi)

getcontext().prec=50
sd=Decimal(3).sqrt()
lo_d=Decimal(32)*(Decimal(7)*sd-Decimal(12))/Decimal(9)
hi_d=Decimal(4)*(Decimal(3)+sd)/Decimal(9)
assert Decimal('0.44215343282539') < lo_d < Decimal('0.44215343282540')
assert Decimal('2.10313369225283') < hi_d < Decimal('2.10313369225284')
# The actual monotonicity proof is symbolic: d log Lambda/dz=(z+4)/(z(1+z))>0 for z>0.
# This finite loop is only a smoke test of the sign expression.
for n in range(1,101):
    z=Fraction(n,17)
    assert (z+4)/(z*(1+z)) > 0
print('VERIFY_OK exact_Qsqrt3=2 decimal_brackets=2 monotonic_smoke=100')
