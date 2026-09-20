from itertools import product
from math import prod, sqrt, comb, log, exp, erf, pi, fsum


def mirror_tv(a):
    m = len(a)
    tv = 0.0
    for eps in product((-1.0, 1.0), repeat=m):
        fp = prod(1.0 + ai*ei for ai, ei in zip(a, eps))
        fm = prod(1.0 - ai*ei for ai, ei in zip(a, eps))
        tv += abs(fp-fm)
    return tv / (2.0**(m+1))


def delta(a):
    return sqrt(1.0 - prod(1.0-ai*ai for ai in a))


def homogeneous_tv(m, t):
    a = t/sqrt(m)
    p = (1.0+a)/2.0
    # Exact binomial probabilities evaluated through log-PMFs.
    gt = []
    k0 = m//2 + 1
    for k in range(k0, m+1):
        lp = (log(comb(m,k)) + k*log(p) + (m-k)*log(1.0-p))
        gt.append(exp(lp))
    pgt = fsum(gt)
    tie = 0.0
    if m % 2 == 0:
        k = m//2
        tie = exp(log(comb(m,k)) + k*log(p) + (m-k)*log(1.0-p))
    return 2.0*pgt + tie - 1.0, sqrt(1.0-(1.0-a*a)**m)


def Phi(x):
    return 0.5*(1.0+erf(x/sqrt(2.0)))


def efficiency_curve(v):
    return (2.0*Phi(sqrt(v))-1.0)/sqrt(1.0-exp(-v))


print('Two-coordinate sharp local endpoint check')
for e in (1e-1, 1e-2, 1e-3):
    a=[e,e]
    tv=mirror_tv(a)
    de=delta(a)
    print(f'e={e:.0e} tv={tv:.15g} delta={de:.15g} ratio={tv/de:.15g}')
print('limit 1/sqrt(2)=', 1.0/sqrt(2.0))

print('\nOne-coordinate upper endpoint check')
for e in (0.1, 0.7):
    tv=mirror_tv([e])
    de=delta([e])
    print(f'a={e} tv={tv:.15g} delta={de:.15g} ratio={tv/de:.15g}')

print('\nHomogeneous diffuse finite-signal convergence')
for t in (0.3,0.7,1.0,2.0):
    v=t*t
    lim_tv=2.0*Phi(t)-1.0
    lim_de=sqrt(1.0-exp(-v))
    lim_ratio=lim_tv/lim_de
    print(f't={t} limit_tv={lim_tv:.15g} limit_delta={lim_de:.15g} limit_ratio={lim_ratio:.15g}')
    for m in (100,1000,10000):
        tv,de=homogeneous_tv(m,t)
        print(f'  m={m:5d} tv={tv:.15g} delta={de:.15g} ratio={tv/de:.15g}')

print('\nEfficiency curve monotonic sample')
last=0.0
for v in (1e-6,1e-3,1e-2,0.1,0.5,1.0,2.0,4.0,10.0):
    r=efficiency_curve(v)
    assert r > last
    last=r
    print(f'v={v:g} R(v)={r:.15g}')
print('sqrt(2/pi)=',sqrt(2.0/pi))
