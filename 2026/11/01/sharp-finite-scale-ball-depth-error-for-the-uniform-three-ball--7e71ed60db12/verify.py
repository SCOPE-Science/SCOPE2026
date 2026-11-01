"""Standalone arithmetic diagnostics for the exact 3D ball-depth discrepancy.

Requires Python 3 standard library only. Symbolic proof is supplied in RESULT.md;
finite checks here supplement rather than replace it.
"""
from decimal import Decimal, getcontext
from fractions import Fraction as F

getcontext().prec = 65
checks = 0

def check(test, label):
    global checks
    if not test:
        raise AssertionError(label)
    checks += 1


def lens_fraction(t, r):
    # Intersection volume of radii 1,t and center distance D=t-r,
    # divided by the volume of the unit 3-ball.
    D = t-r
    return (1+r)**2 * (D*D+2*D*(t+1)-3*(t-1)**2)/(16*D)


def lens_from_slices(t, r):
    # Independent integration of the minimum of the two circular
    # cross-sectional area polynomials, normalized by 4/3.
    D = t-r
    x0 = (t*t-1-D*D)/(2*D)
    def f1(x): return x-x**3/F(3)
    def f2(x): return (t*t-D*D)*x-D*x*x-x**3/F(3)
    return F(3,4)*((f1(x0)-f1(-1))+(f2(r)-f2(x0)))


def hd(r):
    return (2-3*r+r**3)/4


def depth(t,r):
    return 1-lens_fraction(t,r)


def gap(t,r):
    return F(3,16)*(1-r*r)**2/(t-r)

for t in [F(1),F(6,5),F(3,2),F(2),F(7,3),F(4),F(10),F(41,2)]:
    for k in range(1,39):
        r=F(k,40)
        check(lens_fraction(t,r)==lens_from_slices(t,r),f'slice-to-lens t={t} r={r}')
        check(depth(t,r)-hd(r)==gap(t,r),f'exact-gap t={t} r={r}')
        check(gap(t,r)>0,f'positivity t={t} r={r}')
        check(F(-1)<= (t*t-1-(t-r)**2)/(2*(t-r)) <= r,'radical-plane bounds')

for t in [F(1),F(3,2),F(2),F(4),F(10),F(40)]:
    tt = Decimal(t.numerator)/Decimal(t.denominator)
    rt = (2*tt-(4*tt*tt-3).sqrt())/3
    rt2=1/(2*tt+(4*tt*tt-3).sqrt())
    check(abs(rt-rt2)<Decimal('1e-58'), 'root rationalization')
    check(0<rt<1, 'unique optimizer interior')
    check(abs(3*rt**2-4*tt*rt+1)<Decimal('1e-58'), 'stationarity')
    def dec_gap(rr):return Decimal(3)*(1-rr*rr)**2/(Decimal(16)*(tt-rr))
    E=Decimal(3)*rt*(1-rt*rt)/4
    check(abs(dec_gap(rt)-E)<Decimal('1e-58'),'optimal formula')
    for k in range(101):
        rk=Decimal(k)/100
        if tt==1 and rk==1: continue
        check(dec_gap(rk)<=E+Decimal('1e-56'),'global supremum sample')

# Endpoint t=1,r=1 is interpreted by continuity; outer points have zero depth.
check(gap(F(1),F(1,3))==F(2,9),'t=1 exact sharp constant')
check(hd(F(0))==F(1,2),'center halfspace depth')
for t in [F(10),F(100),F(1000)]:
    tt=Decimal(t.numerator)/Decimal(t.denominator)
    rr=1/(2*tt+(4*tt*tt-3).sqrt())
    E=Decimal(3)*rr*(1-rr*rr)/4
    err=abs(E-(Decimal(3)/(16*tt)+Decimal(3)/(128*tt**3)))
    check(err<Decimal(1)/(tt**5),'asymptotic expansion remainder')

print('PASS:',checks,'exact rational and high-precision diagnostic checks')
