"""Reproduce numerical consistency checks for the analytic fluence--loss frontier.

Run with Python 3.11+ and the standard library only: python verify.py.
This finite numerical suite supplements, and does not replace, the proof.
"""
import cmath
import math

PI = math.pi
checks = 0


def check(statement, message):
    global checks
    assert statement, message
    checks += 1


def bisect(fn, left, right, count=85):
    yl = fn(left)
    yr = fn(right)
    check(yl * yr < 0, 'root is not bracketed')
    for _ in range(count):
        middle = (left + right) / 2
        ym = fn(middle)
        if yl * ym <= 0:
            right, yr = middle, ym
        else:
            left, yl = middle, ym
    return (left + right) / 2


def solution(q):
    check(0 < q < 1, 'q outside range')
    if q < 1 / 3 - 1e-9:
        def qfun(z):
            return 1 / (2 * z * math.tanh(z)) - 1 / (2 * math.sinh(z) ** 2)
        z = bisect(lambda z: qfun(z) - q, 1e-3, 150)
        den = math.sinh(z)
        f = lambda s: math.sinh(z * s) / den
        d = lambda s: z * math.cosh(z * s) / den
        h = z / (2 * math.tanh(z)) + z*z / (2 * den*den)
        branch = 'hyperbolic'
    elif q <= 1 / 3 + 1e-9:
        f, d, h, branch = (lambda s: s), (lambda s: 1), 1, 'linear'
    elif q < .5 - 1e-9:
        def qfun(z):
            return 1 / (2 * math.sin(z)**2) - math.cos(z)/(2*z*math.sin(z))
        z = bisect(lambda z: qfun(z) - q, 1e-3, PI/2)
        den = math.sin(z)
        f = lambda s: math.sin(z*s) / den
        d = lambda s: z*math.cos(z*s)/den
        h = z/(2*math.tan(z)) + z*z/(2*den*den)
        branch = 'sine'
    else:
        t0 = 2*(1-q)
        k = PI/(2*t0)
        f = lambda s: math.sin(k*s) if s<=t0 else 1.
        d = lambda s: k*math.cos(k*s) if s<=t0 else 0.
        h = PI**2/(16*(1-q))
        branch = 'sine-plateau'
    return f, d, h, branch


def simpson(fn, n=12000):
    assert n%2==0
    v=fn(0)+fn(1)
    for i in range(1,n):
        v+=(4 if i%2 else 2)*fn(i/n)
    return v/(3*n)


for q in [0.03, 0.08, 0.15, .21, .29, 1/3, .355, .375, .43, .48, .5, .51, .56, .63, .72, .86, .96]:
    f,d,h,branch=solution(q)
    check(abs(f(0))<2e-12 and abs(f(1)-1)<2e-12, 'endpoints')
    check(all(-1e-12<=f(j/100)<=1+1e-12 for j in range(101)), 'bounds')
    check(all(d(j/100)>=-1e-11 for j in range(101)), 'monotonicity')
    # When the plateau kink falls inside a Simpson panel, quadrature is O(h),
    # still well within the explicit 0.0003 numerical check tolerance.
    check(abs(simpson(lambda s:f(s)**2)-q)<3e-4, 'quadratic budget')
    check(abs(simpson(lambda s:d(s)**2)-h)<3e-4, 'Dirichlet cost')
    if q < .5:
        p = (1/q - 1)/2
        e_comp = p*p/(2*p-1)
    else:
        e_comp = 2/(3*(1-q))
    check(h <= e_comp + 1e-10, 'simple admissible competitor is cheaper')

q=3/8
_,_,h,_=solution(q)
check(abs(h-1.0179548427248712)<2e-10, 'specified illustrative value')
check(math.pi**2/8-h>0.2157, 'strict comparison with sin-squared ramp')

# Check the full two-quadrature drive, including its mixed term.
a, omega, A, T, coupling = .6,1.3,.8,2.0,1.2
G2 = a*a + omega*omega
gamma=complex(a,omega)
for q in [.1,.375,.65]:
    f,d,h,_=solution(q)
    uf=lambda t: A*f(t/T)+A*d(t/T)/(T*gamma)
    der=lambda t: A*d(t/T)/T
    # Trapezoid with subintervals aligned with possible plateau time.
    n=12000; dt=T/n
    sumflu=0.; sumref=0.; sumder=0.; alpha=0j
    for j in range(n):
        tm=(j+.5)*dt
        ut=uf(tm)
        sumflu+=abs(ut)**2*dt
        sumref+=(A*f(tm/T))**2*dt
        sumder+=der(tm)**2*dt
        def rhs(t,z):return -gamma*z + 1j*coupling*uf(t)
        t=j*dt
        k1=rhs(t,alpha)
        k2=rhs(t+.5*dt,alpha+.5*dt*k1)
        k3=rhs(t+.5*dt,alpha+.5*dt*k2)
        k4=rhs(t+dt,alpha+dt*k3)
        alpha+=dt*(k1+2*k2+2*k3+k4)/6
    predicted=A*A*T*q + A*A*h/(T*G2)+a*A*A/G2
    check(abs(sumref-A*A*T*q)<2e-4, 'loss constraint normalization')
    check(abs(sumder-A*A*h/T)<2e-4, 'derivative cost normalization')
    check(abs(sumflu-predicted)<2e-4, 'mixed drive fluence')
    check(abs(alpha-1j*coupling*A/gamma)<2e-6, 'final coherent state tracking')

print('PASS:',checks,'deterministic checks; universal claims use the analytical proof.')
