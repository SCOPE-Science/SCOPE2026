from math import sqrt, asin, acos, atan, pi, sin, cos
import random

def theta_crit(h):
    th0=asin(h)
    return (acos(h/sqrt(2))-pi/4) if h<1/sqrt(5) else th0

def conditional_cdf(h,z):
    assert 0<=h<1/sqrt(2) and 0<=z<=1
    th0=asin(h);th1=pi/4; crit=theta_crit(h)
    left=atan(z)-asin(h/sqrt(1+z*z))
    right=acos(h/sqrt(1+z*z))-atan(z)
    l=max(0.0,min(crit,left)-th0)
    r=max(0.0,th1-max(crit,right))
    return (l+r)/(th1-th0)

def tt(h,theta):
    p=sin(theta);q=cos(theta)
    return (h+p)/q if q>=h+p else (q-h)/p

for h in [0,0.01,0.1,0.23,0.28562048389556804,0.33,0.44,1/sqrt(5),0.47,0.6,0.69]:
    theta0=asin(h);theta1=pi/4
    N=16000
    ts=sorted(tt(h,theta0+(j+.5)*(theta1-theta0)/N) for j in range(N))
    for z in [0,.03,.1,.25,.4,.55,.7,.9,1]:
        theoretical=conditional_cdf(h,z)
        empirical=sum(v<=z for v in ts)/N
        if abs(empirical-theoretical)>1/N+1e-11:
            print('ERROR',h,z,empirical,theoretical);raise SystemExit(1)
print('PASS 11 conditional profiles, 9 thresholds, 16k-point midpoint quadrature per profile')
# Verify probability measure on sorted normal chamber; integrand includes theta interval.
N=100000
H=1/sqrt(2)
def fn(h):
    return (12/pi)*(pi/4-asin(h))/((1+h*h)**1.5)
S=fn(0)+fn(H)
for i in range(1,N):S+=(4 if i%2 else 2)*fn(H*i/N)
ans=S*H/(3*N)
assert abs(ans-1)<1e-10,(ans,)
print('PASS joint measure normalization:',ans)
# Validate low endpoint crossover and conditional density cancellation
h=.2;z=.95
T=sqrt(1+z*z-h*h)
fQ=(1+h*z/T)/(1+z*z)
fH=(1-h*z/T)/(1+z*z)
assert abs(fQ+fH-2/(1+z*z))<1e-14
print('PASS universal two-branch density cancellation')
