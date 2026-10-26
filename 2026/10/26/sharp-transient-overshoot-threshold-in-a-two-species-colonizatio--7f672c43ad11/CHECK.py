"""Reproduce numerical examples of a two-species competition-colonization transient peak.

Standard-library computation; the analytic theorem is proved separately.
"""
import math

c1, m1, c2, m2, x0 = 2.0, 1.5, 2.0, 0.75, 0.125
r = c1 - m1
K = r / c1
B, C = c1 + c2, c2
lam = c2 - m2 - B*K
q = K/x0 - 1
beta = B*K/r
d = B*K*q
zeta = (1+q)**beta

def simpson(f, left, right, n=8000):
    assert n % 2 == 0
    step = (right-left)/n
    total = f(left)+f(right)
    for j in range(1,n):
        total += (4 if j % 2 else 2)*f(left+j*step)
    return total*step/3

# With these parameters, lambda/r=1/2, so u=v^2 removes the endpoint singularity.
coefficient = d/r*zeta
kernel = lambda v: 2.0/(1+v*v)**3
I_inf = coefficient*simpson(kernel,0.0,1.0)
assert abs(I_inf-(4+1.5*math.pi)) < 2e-10
critical = lam/(C*(1+I_inf))
assert abs(critical-1/(40+12*math.pi)) < 2e-12

def F(t):
    return lam*t + beta*math.log((1+q)/(1+q*math.exp(-r*t)))

def delta(t):
    u=math.exp(-r*t)
    return d*u/(1+q*u)

def G(t):
    v=math.exp(-0.5*r*t)
    tail = coefficient*simpson(kernel,0.0,v)
    return C/lam*(tail+math.exp(F(t))*delta(t)/(lam+delta(t)))

def peak(y0):
    L = 1/critical-1/y0
    if not 0 < L < G(0):
        raise ValueError('parameter outside interior-peak domain')
    lo,hi=0.0,100.0
    for _ in range(90):
        mid=(lo+hi)/2
        if G(mid)>L:
            lo=mid
        else:
            hi=mid
    t=(lo+hi)/2
    return t, (lam+delta(t))/C

p, yp = peak(0.02)
assert abs(p-8.6955699347) < 2e-5
assert yp > lam/C
assert 0.01 < critical < 0.02
A0=C*zeta*d*r/(lam*lam*(r-lam))
for fraction in (0.01,0.001):
    y0=critical*(1+fraction)
    t,ymax=peak(y0)
    L=1/critical-1/y0
    t_approx=math.log(A0/L)/(r-lam)
    height_approx=d/C*(L/A0)**(r/(r-lam))
    assert abs(t-t_approx) < 2e-4
    assert abs((ymax-lam/C)/height_approx-1)<3e-4
print('VERIFY_OK', 'critical=',format(critical,'.12f'),
      'peak_t=',format(p,'.9f'),'peak_y=',format(yp,'.9f'),
      'A0=',format(A0,'.2f'))
