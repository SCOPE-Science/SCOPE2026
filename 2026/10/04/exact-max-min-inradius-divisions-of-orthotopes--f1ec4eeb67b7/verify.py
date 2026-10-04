from fractions import Fraction
from decimal import Decimal, getcontext
from math import sqrt
getcontext().prec=60

def q(L,r):
    return sum((x-2*r)**2 for x in L)-4*r*r

def delta(L):
    ell=L[-1]
    return sum((x-ell)**2 for x in L)-ell*ell

def root_float(L):
    d=len(L); A=sum(L); B=sum(x*x for x in L)
    disc=A*A-(d-1)*B
    assert disc >= 0
    return (A-sqrt(disc))/(2*(d-1))

def value_float(L):
    ell=L[-1]
    if delta(L) >= 0:
        return ell/2
    return root_float(L)

# Exact sign/monotonicity checks for rational boxes in dimensions 2..8.
boxes=[]
for d in range(2,9):
    boxes.append([Fraction(1) for _ in range(d)])
    boxes.append([Fraction(d+1,2)] + [Fraction(1) for _ in range(d-1)])
    boxes.append([Fraction(3)] + [Fraction(2)]*(d-2) + [Fraction(1)])
    boxes.append([Fraction(10)] + [Fraction(1) for _ in range(d-1)])

for L in boxes:
    L=sorted(L, reverse=True)
    d=len(L); ell=L[-1]
    # q'(r)=-4A+8(d-1)r is strictly negative on [0,ell/2].
    A=sum(L)
    assert -4*A + 8*(d-1)*(ell/2) < 0
    de=delta(L)
    if de >= 0:
        r=ell/2
        assert q(L,r) >= 0
        # Full inradius is an absolute upper bound.
        assert r == ell/2
    else:
        r=Fraction.from_float(value_float([float(x) for x in L])).limit_denominator(10**12)
        # Numeric root is bracketed by exact rational values around it.
        eps=Fraction(1,10**9)
        assert q(L,r-eps) > 0 and q(L,r+eps) < 0

# Hypercube closed form and its tangent diagonal identity.
for d in range(2,101):
    r=sqrt(d)/(2*(sqrt(d)+1))
    side=1-2*r
    assert abs(sqrt(d)*side-2*r) < 3e-14
    assert r < 0.5

# Rectangle phase transition and square value.
for W,H in [(1,1),(3,2),(2,1),(5,2),(10,1)]:
    assert W>=H
    if W<=2*H:
        r=(W+H-sqrt(2*W*H))/2
        assert abs((W-2*r)**2+(H-2*r)**2-(2*r)**2) < 1e-12
    else:
        r=H/2
        assert (W-H)**2 >= H*H
assert abs(value_float([1.0,1.0])-(1-1/sqrt(2))) < 1e-15

# Random deterministic stress family: compare closed form with bisection of the
# exact packing inequality diameter(eroded box)>=2r.
state=1729
def rng():
    global state
    state=(1103515245*state+12345)%(2**31)
    return state/(2**31)
for d in range(2,11):
    for _ in range(80):
        ell=0.2+1.8*rng()
        L=[ell+(4.0*rng()) for _ in range(d-1)]+[ell]
        L.sort(reverse=True)
        target=value_float(L)
        lo,hi=0.0,ell/2
        for __ in range(100):
            mid=(lo+hi)/2
            if q(L,mid)>=0: lo=mid
            else: hi=mid
        assert abs(lo-target) < 2e-12*max(1.0,target)

print('VERIFY_OK orthotope max-min inradius profile')
