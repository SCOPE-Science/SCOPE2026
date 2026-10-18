"""Exact local algebra and independent quadrature checks for a two-matrix RJD model.

This verifier does not establish the asymptotic theorem; its proof is in RESULT.md.
Run with Python 3 (standard library only): python verify.py
"""
from fractions import Fraction as F
from math import acos, atan, cos, hypot, isclose, log, pi, sin, tan


def candidate(e, a, b):
    """Squared Frobenius off-diagonal loss of an eigenbasis of a A+b B."""
    # The eigengap direction is (a,e*b) in the traceless symmetric 2x2 plane.
    denom = a*a + e*e*b*b
    assert denom
    p = 2 * (e*b)**2 / denom  # loss for diagonal A
    q = 2 * e*e * a*a / denom  # loss for offdiagonal B
    return p+q


def closed(e, a, b):
    return 2*e*e*(a*a+b*b)/(a*a+e*e*b*b)


count = 0
for e in [F(1,2), F(1,3), F(2,3), F(3,4), F(1,17)]:
    for a in list(range(-10,0))+list(range(1,11)):
        for b in range(-10,11):
            assert candidate(e,F(a),F(b)) == closed(e,F(a),F(b))
            count += 1
    trials = [(F(5),F(9)), (F(-3),F(2)), (F(4),F(-7)), (F(9),F(1))]
    assert min(trials,key=lambda ab: ab[1]**2/ab[0]**2) == min(trials,key=lambda ab: candidate(e,*ab))


# Independent reconstruction of the eigenbasis of the actual 2x2 pencil.
# Its off-diagonal entries are measured by explicit conjugation, not by the
# angle-derived closed loss used above.
float_checks = 0
for e in (0.05,0.3,0.71):
    for ia in range(-12,13):
        for ib in range(-12,13):
            if ia == 0 and ib == 0:
                continue
            a, b = ia/7, e*ib/9
            rad = hypot(a,b)
            if abs(b)>1e-14:
                vx,vy=(a+rad,b) if a >= 0 else (b,rad-a)
            else:
                vx,vy=(1.,0.) if a>0 else (0.,1.)
            nv=hypot(vx,vy)
            x,y=vx/nv,vy/nv
            off_a=-2*x*y
            off_b=e*(x*x-y*y)
            measured=2*(off_a*off_a+off_b*off_b)
            predicted=float(closed(F(e), F(a),F(ib,9)))
            assert isclose(measured,predicted,rel_tol=4e-12,abs_tol=1e-12), (e,ia,ib,measured,predicted)
            float_checks += 1

def simpson(f,a,b,n=200000):
    """Independent deterministic composite Simpson quadrature, even n."""
    assert n>0 and n%2==0
    h=(b-a)/n
    total=f(a)+f(b)
    for j in range(1,n):
        total+=(4 if j%2 else 2)*f(a+j*h)
    return total*h/3


def expected(e,L):
    def f(u):
        return (4*L*e*e/pi)*(2*u/pi)**(L-1)/(sin(u)**2+e*e*cos(u)**2)
    return simpson(f,0,pi/2,200000)

for e in [0.5,0.1,0.03,0.01]:
    assert isclose(expected(e,1),2*e,rel_tol=2e-10,abs_tol=1e-12)
    assert expected(e,3)<expected(e,2)<expected(e,1)

# The limiting triple-trial constant has a non-singular integrand.
def c3_integrand(u):
    return 1.0 if u==0.0 else (u/sin(u))**2

c3 = 48/pi**3 * simpson(c3_integrand,0,pi/2,50000)
assert isclose(c3,48*log(2)/pi**2,rel_tol=4e-12)
assert abs(expected(1e-3,2)/(1e-6*log(1e3))-16/pi**2)<0.4
print('VERIFY_OK exact_rational_cases=',count, 'explicit_eigenbasis_cases=',float_checks, 'C3=',repr(c3))
