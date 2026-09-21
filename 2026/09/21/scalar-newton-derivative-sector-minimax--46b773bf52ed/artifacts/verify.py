import math
import random

SEED = 20260921
rng = random.Random(SEED)

def trap_average(v):
    n = len(v) - 1
    return (0.5*v[0] + sum(v[1:-1]) + 0.5*v[-1]) / n

max_violation = -1e300
for kappa in (1.2, 1.5, 2.0, 3.0, 10.0):
    m, L = 1.0, kappa
    gamma = 2.0*kappa/(kappa*kappa + 1.0)
    theory = (kappa*kappa - 1.0)/(kappa*kappa + 1.0)
    for _ in range(5000):
        vals = [rng.uniform(m,L) for _ in range(101)]
        a = trap_average(vals)
        d = vals[-1]
        ratio = abs(1.0 - gamma*a/d)
        max_violation = max(max_violation, ratio-theory)
print('seed', SEED)
print('random_constant_damping_max_violation', format(max_violation,'.17g'))

for kappa in (1.5,2.0,3.0,10.0):
    gamma = 2.0*kappa/(kappa*kappa+1.0)
    theory = (kappa*kappa-1.0)/(kappa*kappa+1.0)
    eps=1e-8
    upper_avg=kappa-(kappa-1.0)*eps/2.0
    lower_avg=1.0+(kappa-1.0)*eps/2.0
    upper=abs(1.0-gamma*upper_avg)
    lower=abs(1.0-gamma*lower_avg/kappa)
    print('boundary', kappa, 'theory', format(theory,'.17g'),
          'upper', format(upper,'.17g'), 'lower', format(lower,'.17g'))

for kappa in (2.01,2.1,3.0,10.0):
    eps=min(0.1,(kappa-2.0)/(2.0*(kappa-1.0)))
    C=(4.0-eps)/(2.0-eps)
    avg=C*(1.0-eps)+(C+1.0)*eps/2.0
    N1=1.0-avg
    Nm1=-1.0+avg
    print('two_cycle', kappa, 'C', format(C,'.17g'), 'C_lt_L', C<kappa,
          'N1', format(N1,'.17g'), 'Nm1', format(Nm1,'.17g'))

for kappa in (1.2,2.0,5.0,20.0):
    m,L=1.0,kappa
    theory=(L-m)/(L+m)
    worst=0.0
    for j in range(1001):
        d=m+(L-m)*j/1000.0
        gamma=2.0*d/(m+L)
        for a in (m,L):
            worst=max(worst,abs(1.0-gamma*a/d))
    print('derivative_aware',kappa,'computed',format(worst,'.17g'),'theory',format(theory,'.17g'))
