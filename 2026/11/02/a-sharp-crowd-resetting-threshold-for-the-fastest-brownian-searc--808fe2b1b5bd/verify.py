"""Checks for Brownian first arrival under log-squared resetting.
Only numerical consistency checks; the asymptotic theorem is analytical.
"""
import math

def success_probability(a, length):
    return math.exp(-2.0 * math.sqrt(a) * length)

def success_by(a, length, y):
    # t0=1, r=a L^2, t=y/L. Integration of Levy density weighted by Exp(-rt).
    u=math.sqrt(length/y)
    v=math.sqrt(a*y*length)
    w=math.sqrt(a)*length
    return (math.exp(-2*w)*math.erfc(u-v) + math.exp(2*w)*math.erfc(u+v))/2

def saddle_rate(a,y):
    if a==0: return 1/y
    z=min(y,1/math.sqrt(a))
    return 1/z+a*z

def small_root(a):
    if a==0: return 1
    return 2/(1+math.sqrt(1-4*a))

count=0
for L in (12,20,35,60):
    for a in (0,0.08,0.15,0.24,0.25,0.4,0.8):
        for y in (0.5,0.8,1.1,1.5,2.0,2.5,3.5):
            if a==0:  continue
            q=success_probability(a,L)
            qt=success_by(a,L,y)
            assert -1e-14 <= qt <= q*(1+1e-9)
            count+=1
        if a>0:
            y=1/math.sqrt(a)+1
            q=success_probability(a,L)
            # Finite-cutoff fractions eventually approach one as L grows.
            assert 0 < success_by(a,L,y)/q <= 1.00000001
            count+=1
for a in (0,0.05,0.12,0.2,0.24):
    y=small_root(a)
    assert abs(saddle_rate(a,y)-1)<2e-14
    if a>0: assert y < 1/math.sqrt(a)
    count+=1
# Numerical evaluation of exact reset-success identity by quadrature.
def simpson_success(r, intervals=16000):
    # u = 1/sqrt(time), giving a rapidly decaying smooth integral.
    upper=20.0
    step=upper/intervals
    def f(u):
        return 0.0 if u == 0 else math.exp(-u*u-r/(u*u))
    total=f(0)+f(upper)
    for k in range(1,intervals):
        total+=(4 if k%2 else 2)*f(k*step)
    return 2/math.sqrt(math.pi)*total*step/3
for a in (0.1,0.25,0.5,1.):
  for L in (2.,5.,10.):
    r=a*L*L
    integral=simpson_success(r)
    assert abs(integral-math.exp(-2*math.sqrt(r)))<2e-11
    count+=1
print('PASS',count,'checks')
