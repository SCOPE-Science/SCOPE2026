"""Independent elementary checks for a three-population payoff specialization.

This verifies finite algebra and numerical consistency, not infinite-time claims.
"""
from fractions import Fraction as Q
from math import exp

rho = Q(1, 20)
eps = Q(1, 100)
Cg, theta, S, F = Q(1), Q(1), Q(2), Q(1)
lw, ls = Q(1, 4), Q(1, 4) + eps
delta, B, E, alpha = Q(1), Q(1), Q(1, 2), Q(1)
c = Q(3, 4) + rho + eps
a, cu, q, r = Q(1, 2), Q(1, 2) + rho + eps, Q(1), eps
assert -Cg + theta*S == 1
assert (ls-lw)*F == eps
assert -c+delta*B-E+lw*F == -rho-eps
assert alpha == 1 and (ls-lw)*F == eps
assert a-cu == -rho-eps and q == 1 and r == eps
assert Q(0)<lw<ls<1 and 0<rho<1 and 0<eps<min(Q(3,4),1-rho)

s = rho + eps
b = s*(1-s)
L = 1 + eps*(1-s)
kappa = b/L
assert kappa == Q(282,5047), (kappa,Q(282,5047))
assert 0<kappa<1
ac = rho*(1-rho)
L1 = 1+eps*(1-rho)
K = ac*eps/(L1+ac)
assert 0<K<eps

# Exact tests for the two strict invariant growth signs.
checks = 0
for ix in range(1,50):
    x=Q(ix,50)
    for iy in range(1,20):
        y=rho*Q(iy,20)
        for iz in range(1,20):
            z=rho*Q(iz,20)
            assert z-rho-eps*(1-x)<0 and y-rho-eps*(1-x)<0
            checks += 1
for ix in range(1,50):
    x=Q(ix,50)
    for iy in range(1,20):
        y=s+(1-s)*Q(iy,20)
        for iz in range(1,20):
            z=s+(1-s)*Q(iz,20)
            assert z-rho-eps*(1-x)>0 and y-rho-eps*(1-x)>0
            checks += 1
assert rho*rho == Q(1,400)
for j in range(1,10):
    p=Q(j,10)
    assert p>s

def ode(x, w, de=float(eps)):
    return w*(1-w)*(w-float(rho)-de*(1-x))/(x*(1-x)*(1+de*(1-w)))

def rk4_step(x,w,h,de=float(eps)):
    k1=ode(x,w,de)
    k2=ode(x+h/2,w+h*k1/2,de)
    k3=ode(x+h/2,w+h*k2/2,de)
    k4=ode(x+h,w+h*k3,de)
    return w+h*(k1+2*k2+2*k3+k4)/6

def threshold_at(x_target,de=float(eps),steps=45000):
    x=1-1.e-7
    aa=float(rho)*(1-float(rho))
    K1=aa*de/(aa+1+de*(1-float(rho)))
    w=float(rho)+K1*(1-x)
    h=(x_target-x)/steps
    for _ in range(steps):
        w=rk4_step(x,w,h,de)
        x+=h
    return w

wth=threshold_at(0.1)
assert 0.05100 < wth < 0.05102, wth
assert float(rho)<wth<float(rho+eps*(1-Q(1,10)))

# Midpoint quadrature for first variation (numerical sanity only).
def response_at(x):
    aa=float(rho)*(1-float(rho))
    T=350.0; n=100000; dt=T/n
    summ=0.0
    for i in range(n):
        t=(i+0.5)*dt
        one_minus_X=(1-x)/(1-x+x*exp(t))
        summ+=exp(-aa*t)*one_minus_X
    return aa*dt*summ

R=response_at(0.1)
smalleps=0.0001
ws=threshold_at(0.1,de=smalleps)
assert 0 < (ws-float(rho))/smalleps < 1
assert abs((ws-float(rho))/smalleps-R)<0.00005, (ws,R)

print('PASS: exact payoff substitutions, basin sign checks:', checks)
print('PASS: kappa=',str(kappa), 'saddle slope=',str(-K))
print('PASS: numerical threshold x=0.1:',f'{wth:.12f}')
print('PASS: first-variation integral:',f'{R:.9f}', 'finite-difference:',f'{(ws-float(rho))/smalleps:.9f}')
print('Finite tests only; proof establishes infinite-time and cusp claims.')
