"""Reproducible symbolic and numerical checks for critical two-group opinion dynamics.

Run: python -m pip install -r requirements.txt && python verify.py
Numerical tests corroborate but do not establish the global theorem.
"""
from fractions import Fraction
import math
import random
import sympy as sp
from scipy.integrate import solve_ivp

# An exact critical parameter tuple with nonlinear sender reformulation and
# nonzero individual content filtering.
rho = Fraction(1, 2)
alpha = Fraction(2, 1)
tau = Fraction(1, 4)
eta = Fraction(1, 3)
kappa = Fraction(1, 5)
beta = Fraction(32, 55)
a = (1-rho) + rho*alpha
H = tau + (1-tau)*a
assert kappa + beta*H == 1
Q = 1 + beta*(1-tau)*rho*alpha**3
D = beta*(1-tau)*(1-eta)*a
assert Q == Fraction(151, 55)
assert D == Fraction(24, 55)
assert Fraction(3, 2) / Q == Fraction(165, 302)

# The nonlinear cubic coefficient is checked algebraically, before any ODE solve.
x, K, B, C = sp.symbols('x K B C')
# C = beta*(1-tau)*rho*alpha^3; B = beta*H.
r = sp.tanh(B*x - C*x**3/3)
u = sp.tanh(K*x)
f = r+u-x*(1+r*u) # selected response with gamma/2 = 1
coefficient = sp.expand(sp.series(f, x, 0, 4).removeO()).coeff(x, 3)
assert sp.simplify(coefficient.subs(K, 1-B) + (1+C)/3) == 0

rng = random.Random(24680)
for selected in (False, True):
    for _ in range(1200):
        ro = rng.random()
        al = 2*rng.random()+0.15
        ta = .85*rng.random()
        et = rng.random()
        ka = .45*rng.random() if selected else 0.0
        aa = 1-ro+ro*al
        bb = (1-ka)/(ta+(1-ta)*aa)
        x1 = 2*rng.random()-1
        x2 = 2*rng.random()-1
        xx=[x1,x2]
        M=max(abs(x1),abs(x2))
        phi = [(1-ro)*x+ro*math.tanh(al*x) for x in xx]
        zs = [((1+et)*phi[0]+(1-et)*phi[1])/2,
              ((1-et)*phi[0]+(1+et)*phi[1])/2]
        h = [(1-ta)*zs[i]+ta*xx[i] for i in range(2)]
        r = [math.tanh(bb*v) for v in h]
        if selected:
            u = [math.tanh(ka*v) for v in xx]
            dx = [r[i]+u[i]-xx[i]*(1+r[i]*u[i]) for i in range(2)]
        else:
            dx = [r[i]-xx[i] for i in range(2)]
        active = [i for i in range(2) if abs(xx[i]) >= M-1.e-13]
        Mprime = max(math.copysign(1,xx[i])*dx[i] for i in active)
        assert Mprime <= (math.tanh(M)-M)+1e-12

ro=float(rho); al=float(alpha); ta=float(tau); et=float(eta)
be=float(beta); ka=float(kappa)
expected=math.sqrt(float(Fraction(3, 2)/Q))

def rhs(selected):
    b = be if selected else 1/float(H)
    def f(t, xx):
        x,y=xx
        ph1=(1-ro)*x+ro*math.tanh(al*x)
        ph2=(1-ro)*y+ro*math.tanh(al*y)
        h1=(1-ta)*((1+et)*ph1+(1-et)*ph2)/2+ta*x
        h2=(1-ta)*((1-et)*ph1+(1+et)*ph2)/2+ta*y
        r1=math.tanh(b*h1);r2=math.tanh(b*h2)
        if selected:
            u1=math.tanh(ka*x);u2=math.tanh(ka*y)
            return [r1+u1-x*(1+r1*u1),r2+u2-y*(1+r2*u2)]
        return [r1-x,r2-y]
    return f

for selected in (True, False):
    const=expected if selected else math.sqrt(Fraction(33,70))
    for initial in ((.9,-.3),(.7,.6),(-.5,-.2)):
        sol=solve_ivp(rhs(selected),(0.,40000.),initial,t_eval=[10000.,40000.],
                      method='DOP853',rtol=1e-10,atol=1e-12)
        assert sol.success
        mm=(sol.y[0,-1]+sol.y[1,-1])/2
        pp=(sol.y[0,-1]-sol.y[1,-1])/2
        assert abs(abs(mm)*math.sqrt(40000)-const) < .001*const
        assert abs(pp)<1e-8
    anti=solve_ivp(rhs(selected),(0.,1000.),(.2,-.2),method='DOP853',
                   rtol=1e-11,atol=1e-13)
    assert anti.success and abs(sum(anti.y[:,-1]))<1e-10

print('PASS: rational critical identities, symbolic cubic cancellation,')
print('2400 max-norm inward inequalities, long-time amplitudes and fast antisymmetric mode.')
print('These finite checks do not prove asymptotic or uniqueness statements.')
