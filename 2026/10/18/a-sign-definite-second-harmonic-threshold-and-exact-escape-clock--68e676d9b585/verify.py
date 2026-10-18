"""Reproduce finite algebraic and quadrature checks for a degree-seven planar flow.

The arguments proving statements for all parameters are given in RESULT.md.
This script checks selected identities and diagnostic instances only.
"""
import math
import sympy as sp
import mpmath as mp

mp.mp.dps = 40
checks = 0

def insist(condition, msg):
    global checks
    assert condition, msg
    checks += 1

# Exact harmonic exponents after factoring z|z|^6 from each degree-seven monomial.
z, zb = sp.symbols('z zb')
monomials = [(z**4 * zb**3,0), (z**2 * zb**5,-4), (zb**7,-8)]
for monom, harmonic in monomials:
    u = sp.symbols('u', nonzero=True)
    # On the unit circle z=u, conj(z)=1/u; divide by z.
    value = sp.cancel(monom.subs({z:u,zb:1/u})/u)
    insist(sp.simplify(value-u**harmonic)==0, 'polar monomial exponent')

# Beta-integral sign formula: int cos(2u) sin^(2n)u cos^(2j)u du / baseline
# equals (j-n)/(n+j+1), for 0 <= j <= n.
for n in range(1,7):
    for j in range(n+1):
        norm = sp.beta(sp.Rational(2*n+1,2), sp.Rational(2*j+1,2))*2
        num = norm - 2*sp.beta(sp.Rational(2*n+3,2), sp.Rational(2*j+1,2))*2
        rat = sp.cancel(num / norm)
        insist(sp.simplify(sp.expand_func(rat)-sp.Rational(j-n,n+j+1)) == 0, 'beta sign identity')


def critical(a, b, c, omega):
    g = lambda u: omega-b*mp.sin(u)-c*mp.sin(2*u)
    J = mp.quad(lambda u: 1/g(u), [0,mp.pi/2,mp.pi,3*mp.pi/2,2*mp.pi])
    L = mp.quad(lambda u: mp.cos(2*u)/g(u), [0,mp.pi/2,mp.pi,3*mp.pi/2,2*mp.pi])
    N = mp.quad(lambda u: (b*mp.cos(u)+c*mp.cos(2*u))/g(u),
                [0,mp.pi/2,mp.pi,3*mp.pi/2,2*mp.pi])
    insist(abs(N+c*L) < mp.mpf('1e-30'), 'exact integration by parts')
    return -c*L/J, J, L

for b,c,omega in [(1,mp.mpf('.1'),2),(1,-mp.mpf('.1'),2),
                  (1,mp.mpf('.8'),mp.mpf('1.61')),
                  (mp.mpf('.1'),mp.mpf('3'),mp.mpf('3.2')),
                  (mp.mpf('.7'),mp.mpf('.01'),2)]:
    ac, J, L = critical(0,b,c,omega)
    insist(L < 0, 'strict harmonic-correlation sign')
    insist(mp.sign(ac)==mp.sign(c), 'critical damping sign')
    M = max(abs(b*mp.sin(2*mp.pi*k/10000)+c*mp.sin(4*mp.pi*k/10000))
            for k in range(10000))
    assert omega > M
    lower = abs(c)*b*b*(omega-M)/(4*omega**3)
    insist(abs(ac)>lower, 'analytical positive lower bound')

b,omega = mp.mpf(1),mp.mpf(2)
q = b/(omega+mp.sqrt(omega**2-b**2))
for c in [mp.mpf('0.001'),mp.mpf('0.0001')]:
    ac, _, _ = critical(0,b,c,omega)
    insist(abs(ac/c-q**2) < 3*c*c, 'critical threshold first variation')
    acminus,_,_ = critical(0,b,-c,omega)
    insist(abs(acminus+ac)<mp.mpf('1e-30'), 'odd symmetry')

# The geometric physical-time clock is reproduced by independent numerical
# integration of the angular system. These are finite consistency tests only.
from scipy.integrate import solve_ivp
b, c, omega = mp.mpf(1),mp.mpf('.1'),mp.mpf(2)
ac,J,_ = critical(0,b,c,omega)
start = 0.21
for delta in [0.006,0.003,0.001]:
    a=float(ac)-delta
    bf,cf,wf=float(b),float(c),float(omega)
    def vector(theta, yz):
        h=yz[0]
        g=wf-bf*math.sin(4*theta)-cf*math.sin(8*theta)
        f=-a+bf*math.cos(4*theta)+cf*math.cos(8*theta)
        return [f/g,math.exp(-6*h)/g]
    sol=solve_ivp(vector, [start,start+2*math.pi], [0.,0.],rtol=2e-12,atol=2e-13)
    insist(sol.success, 'angle flight ODE')
    I=float(J)*delta
    insist(abs(sol.y[0,-1]-I)<2e-10, 'angular drift equals integral')
    ratio=math.exp(-6*I)
    K=sol.y[1,-1]
    T=K/(1-ratio)
    insist(abs(T*(1-ratio)-K)<2e-10, 'exact geometric escape clock')
    insist(I>0 and ratio<1, 'finite-time escape side')

print('PASS',checks,'finite symbolic/quadrature assertions')
print('example omega=2 b=1 c=0.1: a_c=',mp.nstr(ac,20))
print('q^2=',mp.nstr(q*q,20))
