"""Finite consistency tests for the ultraspherical quadratic projector.
Requires Python 3.10+ and mpmath. Running this file does not certify the asymptotic theorem.
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 55
checks = 0


def require(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def moments(a, k):
    val = Fraction(1)
    for j in range(k):
        val *= Fraction(2*j+1, 2*a+2*j+1)
    return val


# Exact rational reproduction of 1, y and y^2 at rational evaluation points.
for a in (1, 2, 3, 5, 8):
    s = Fraction(1, 2*a+1)
    v = moments(a,2)-s*s
    for x in (Fraction(0), Fraction(1,4), Fraction(2,3), Fraction(1)):
        # K(x,y)=A+B*y+C*y^2.
        A=1-(x*x-s)*s/v
        B=x/s
        C=(x*x-s)/v
        require(A + C*moments(a,1) == 1, 'mass')
        require(B*moments(a,1) == x, 'linear reproduction')
        require(A*moments(a,1)+C*moments(a,2) == x*x, 'quadratic reproduction')


def endpoint_value(a):
    a=mp.mpf(a)
    lo=(-1-mp.sqrt(2*a+4))/(2*a+3)
    hi=(-1+mp.sqrt(2*a+4))/(2*a+3)
    const=mp.gamma(a+mp.mpf('.5'))/(mp.sqrt(mp.pi)*mp.gamma(a))
    def integrand(y):
        return (2*a+1)/2*((2*a+3)*y*y+2*y-1) * const*(1-y*y)**(a-1)
    negative=mp.quad(integrand,[lo,0,hi])
    return 1-2*negative

phi=mp.exp(-mp.mpf('.5'))/mp.sqrt(2*mp.pi)
Q=mp.erfc(1/mp.sqrt(2))/2
leading=4*phi
constant=7*phi+4*Q-1

for a in (10, 20, 50, 100, 250, 500):
    val=endpoint_value(a)
    require(abs(val-leading*a-constant) < mp.mpf('.4')/a, 'endpoint two-term error')
    require(val > leading*a, 'positive lower-order offset')

# Exact finite-parameter kernel at scaled evaluations converges to the Hermite kernel.
for a in (10, 25, 100):
    aa=mp.mpf(a)
    for z in ('-2', '-1', '0', '.5', '1.3', '3'):
        zz=mp.mpf(z)
        for t in ('-3','-.75','0','.6','2'):
            tt=mp.mpf(t)
            K=1+zz*tt+(2*aa+3)/(4*aa)*(zz*zz-1)*(tt*tt-1)
            H=1+zz*tt+(zz*zz-1)*(tt*tt-1)/2
            require(abs(K-H) < 2/aa*(abs(zz*zz-1)*abs(tt*tt-1)+1), 'scaled kernel convergence')

# Check numerical central convergence on a compact set using a finite integral.
for a in (40, 100):
    a=mp.mpf(a)
    const=mp.gamma(a+mp.mpf('.5'))/(mp.sqrt(mp.pi)*mp.gamma(a)*mp.sqrt(2*a+1))
    bound=mp.sqrt(2*a+1)
    def dens(t):
        return const*max(mp.mpf(0),1-t*t/(2*a+1))**(a-1) if abs(t)<bound else mp.mpf(0)
    for z in ('0','1','2'):
        z=mp.mpf(z)
        def func(t):
            K=1+z*t+(2*a+3)/(4*a)*(z*z-1)*(t*t-1)
            return abs(K)*dens(t)
        val=mp.quad(func,[-10,-3,-1,0,1,3,10])
        def gauss(t):
            K=1+z*t+(z*z-1)*(t*t-1)/2
            return abs(K)*mp.exp(-t*t/2)/mp.sqrt(2*mp.pi)
        limit=mp.quad(gauss,[-10,-3,-1,0,1,3,10])
        require(abs(val-limit)<mp.mpf('.07'), 'central gaussian profile')

print('PASS', checks, 'assertions; leading=', mp.nstr(leading,18), 'constant=', mp.nstr(constant,18))
