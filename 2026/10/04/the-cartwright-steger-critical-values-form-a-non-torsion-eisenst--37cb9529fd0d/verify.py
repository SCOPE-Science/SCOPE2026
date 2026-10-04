from fractions import Fraction
from math import gcd

q=Fraction(6267859,1459**2)
ystar=Fraction(487135434066,1459**3)
assert ystar*ystar == q**3*1116 - 3888

def modfrac(a,p):
    assert a.denominator % p != 0
    return (a.numerator * pow(a.denominator,-1,p)) % p

def add(P,Q,p):
    if P is None: return Q
    if Q is None: return P
    x1,y1=P; x2,y2=Q
    if x1==x2 and (y1+y2)%p==0:
        return None
    if P != Q:
        m=((y2-y1)*pow((x2-x1)%p,-1,p))%p
    else:
        if y1%p==0: return None
        m=(3*x1*x1*pow((2*y1)%p,-1,p))%p
    x3=(m*m-x1-x2)%p
    y3=(m*(x1-x3)-y1)%p
    return (x3,y3)

def mul(n,P,p):
    R=None
    Q=P
    while n:
        if n&1: R=add(R,Q,p)
        Q=add(Q,Q,p)
        n//=2
    return R

def order(P,p,limit=200):
    R=None
    for n in range(1,limit+1):
        R=add(R,P,p)
        if R is None:
            return n
    raise RuntimeError("order bound too small")

disc_E = -16 * 27 * (-3888)**2
disc_cubic = -27 * 1116**2

data=[]
for p,theta_bar,expected_point,expected_order in [
    (17,12,(2,8),9),
    (23,13,(17,17),4),
]:
    assert 1459 % p != 0
    assert disc_E % p != 0
    assert disc_cubic % p != 0
    assert pow(theta_bar,3,p) == 1116 % p
    x=(modfrac(q,p)*theta_bar)%p
    y=modfrac(ystar,p)
    P=(x,y)
    assert P == expected_point
    assert (y*y - (x*x*x-3888)) % p == 0
    o=order(P,p)
    assert o == expected_order
    assert mul(o,P,p) is None
    for d in range(1,o):
        if o%d==0:
            assert mul(d,P,p) is not None
    data.append((p,theta_bar,P,o))

# A torsion order would have to be simultaneously 9*17^a and 4*23^b.
for a in range(12):
    for b in range(12):
        assert 9*(17**a) != 4*(23**b)

print("point_equation_exact=OK")
for p,t,P,o in data:
    print(f"p={p} theta={t} point={P} exact_order={o}")
print("torsion_order_forms=9*17^a versus 4*23^b: incompatible")
print("VERIFY_OK")
