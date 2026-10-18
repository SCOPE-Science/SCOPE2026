"""Independent numerical/symbolic spot checks for an exact weighted-composition theorem.

This is a finite consistency checker, not a substitute for the analytic proof.
"""
import math
import random

random.seed(823617)
checks=0

def verify(condition, note):
    global checks
    assert condition, note
    checks+=1


def tstar(n,a,b,eta):
    # Cancellation-safe positive root of t(t+n*b)=eta*b/a.
    return (2*eta*b/a)/(math.sqrt((n*b)**2+4*eta*b/a)+n*b)


def log_formula(n,a,b,eta):
    if a*b == 0: return 0.0
    t=tstar(n,a,b,eta)
    return -a*b*n*(n-1)/2-a*n*t+eta*math.log(t/(t+n*b))


def log_at(n,a,b,eta,t):
    return -a*b*n*(n-1)/2-a*n*t+eta*math.log(t/(t+n*b))


def log_asym(n,a,b,eta):
    return -a*b*n*(n-1)/2-2*eta*math.log(n)+eta*(math.log(eta/(a*b))-1)

for eta in (0.08,0.35,0.5,1.,1.7,3.1):
    for a,b in ((0.2,0.1),(0.7,1.3),(2.3,0.25)):
        for n in (1,2,3,5,11,30,120):
            t=tstar(n,a,b,eta)
            verify(t>0, 'positive optimizer')
            verify(abs(t*(t+n*b)-eta*b/a)<1e-9*(1+eta*b/a), 'critical equation')
            main=log_formula(n,a,b,eta)
            for factor in (0.1,0.45,0.85,1.15,3,10):
                verify(log_at(n,a,b,eta,t*factor)<main+1e-12,'unique maximum')
            # n^2-corrected logarithmic remainder is uniformly controlled at large n.
            if n>=30:
                verify(abs(main-log_asym(n,a,b,eta))<50*(1+eta*eta/(a*b))/n**2, 'asymptotic remainder')

# Direct L2 input ratios on compact intervals approach the exact norm.
for eta in (0.2,0.5,1.5):
    for a,b in ((0.6,0.4),(1.8,0.8)):
        for n in (1,2,4):
            t=tstar(n,a,b,eta)
            target=log_formula(n,a,b,eta)
            for delta in (1e-2,1e-3,1e-4):
                # Input density t^{-2eta}; right-shifted output is exact.
                m=200
                h=delta/m
                sums=0.; su=0.
                for j in range(m):
                    x=t+(j+0.5)*h
                    mass=x**(-2*eta)
                    su+=mass
                    sums+=math.exp(-2*a*n*x-a*b*n*(n-1))*((x)/(x+n*b))**(2*eta)*mass
                ratio=.5*math.log(sums/su)
                verify(ratio<=target+1e-8,'test-vector upper bound')
                if delta<=1e-3:
                    verify(abs(ratio-target)<1e-4,'near optimizer lower bound')

# Boundary faces have operator norm exactly one at every positive power.
for eta in (0.1,0.7,2.0):
    for n in (1,2,9,100):
        verify(log_formula(n,0,1,eta)==0,'no horizontal shift')
        verify(log_formula(n,1,0,eta)==0,'no exponential weight')

print('PASS: ', checks, ' independent finite checks')
