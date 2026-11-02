"""Supplementary exact algebra and numerical checks for modified Bessel edge constants.

The universal conclusions rely on the analytic proof; finite checks are not a proof.
Requires sympy, scipy.
"""
import sympy as s
from scipy import special, optimize

z, p = s.symbols('z p', positive=True)
R = 1 + z**2
checks = 0

def check(statement):
    global checks
    assert statement
    checks += 1

# NIST DLMF 10.41.9, with U0=1.
u = [s.S.One]
t = s.symbols('t')
for k in range(4):
    f = u[-1]
    u.append(s.factor(p**2*(1-p**2)*s.diff(f, p)/2
        + s.integrate((1-5*t**2)*f.subs(p,t), (t,0,p))/8))
A = s.factor(2*u[2] - u[1]**2)
B = s.factor(2*u[4] - 2*u[1]*u[3] + u[2]**2)
check(s.simplify(A - p**2*(p**2-1)*(5*p**2-1)/8)==0)
check(s.simplify(B - p**4*(p**2-1)*(1155*p**6-1617*p**4+553*p**2-27)/128)==0)
Az = s.factor(A.subs(p,1/s.sqrt(R)))
Bz = s.factor(B.subs(p,1/s.sqrt(R)))
h0 = s.factor(-2*R*Az)
h2 = s.factor(R*(3*Az**2-2*Bz))
base = -z/R
ap = s.diff(Az,z)
bp = s.diff(Bz,z)-Az*ap
H0 = s.factor(z*ap/base**2)
H2 = s.factor(z*(bp/base**2-ap**2/base**3))
check(s.simplify(h0 - z**2*(4-z**2)/(4*R**2))==0)
check(s.simplify(h2 + z**2*(3*z**6-56*z**4+68*z**2-8)/(8*R**5))==0)
check(s.simplify(H0 + (z**4-10*z**2+4)/(4*R**2))==0)
check(s.simplify(H2 + 3*z**2*(2*z**6-59*z**4+136*z**2-48)/(8*R**5))==0)
zh, zH = s.sqrt(s.Rational(2,3)), s.sqrt(s.Rational(3,2))
for ff, aa, val, dd, shift in [
    (h0,zh,s.Rational(1,5),-s.Rational(108,125),None),
    (H0,zH,s.Rational(7,20),-s.Rational(144,125),None)]:
    check(s.simplify(ff.subs(z,aa)-val)==0)
    check(s.simplify(s.diff(ff,z).subs(z,aa))==0)
    check(s.simplify(s.diff(ff,z,2).subs(z,aa)-dd)==0)
check(s.simplify(h2.subs(z,zh)+s.Rational(54,625))==0)
check(s.simplify(H2.subs(z,zH)+s.Rational(108,625))==0)
check(s.simplify(-s.diff(h2,z).subs(z,zh)/s.diff(h0,z,2).subs(z,zh)-17*s.sqrt(6)/150)==0)
check(s.simplify(-s.diff(H2,z).subs(z,zH)/s.diff(H0,z,2).subs(z,zH)-27*s.sqrt(6)/80)==0)
# Exact local-max inequalities used to trap every global maximizer.
w = s.symbols('w',real=True)
check(s.expand(w-s.Rational(5,4)*w**2 -(s.Rational(1,5)-s.Rational(5,4)*(w-s.Rational(2,5))**2))==0)
check(s.expand(-1+s.Rational(9,2)*w-s.Rational(15,4)*w**2 -(s.Rational(7,20)-s.Rational(15,4)*(w-s.Rational(3,5))**2))==0)

# Supplementary numerical consistency of fixed-order maxima; cancellation limits accuracy.
def fvals(n, zz):
    x=n*zz
    I = special.ive(n,x)
    K = special.kve(n,x)
    product=I*K
    logder = special.ive(n+1,x)/I - special.kve(n-1,x)/K
    return 1/(4*product*product)-x*x-n*n, -x/logder-x*x-n*n
for n in (10,30,60):
    opt1=optimize.minimize_scalar(lambda zz: -fvals(n,zz)[0], bounds=(.7,1.0), method='bounded', options={'xatol':1e-8})
    opt2=optimize.minimize_scalar(lambda zz: -fvals(n,zz)[1], bounds=(1.1,1.4), method='bounded', options={'xatol':1e-8})
    c=-opt1.fun; d=-opt2.fun
    check(abs(n*n*(.2-c)-54/625)<.004)
    check(abs(n*n*(.35-d)-108/625)<.008)
    check(abs(opt1.x-(float(zh)+float(17*s.sqrt(6)/150)/n**2))<.0005)
    check(abs(opt2.x-(float(zH)+float(27*s.sqrt(6)/80)/n**2))<.002)
    check(c<.2 and d<.35)
print('CHECK_OK',checks)
