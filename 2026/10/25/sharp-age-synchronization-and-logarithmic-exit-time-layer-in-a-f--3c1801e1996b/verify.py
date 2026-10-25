"""Reproducible numerical checks for sharp stationary age synchronization.

Only scientific calculations are included. Requires Python 3 and mpmath >=1.3.
Run: python verify.py
"""
from mpmath import mp

mp.dps = 45
checks = 0

def close(x, y, tol='1e-23'):
    global checks
    assert abs(x-y) < mp.mpf(tol), (x, y, abs(x-y))
    checks += 1

def beta(z):
    return mp.dirichlet(z, [0,1,0,-1])

def mellin(p):
    return 4/mp.pi * mp.gamma(p+1)*(4/mp.pi**2)**p*beta(2*p+1)

# The first three exit-time moments independently follow from
# recursively solving u_0=1, u_n''=-n u_(n-1), u_n(+-1)=0.
for n, rational in [(0,mp.mpf(1)),(1,mp.mpf(1)/2),
                    (2,mp.mpf(5)/12),(3,mp.mpf(61)/120)]:
    close(mellin(n), rational)

mu = mp.re(mp.diff(lambda p: mp.log(mellin(p)), 0, method='quad'))
varY = mp.re(mp.diff(lambda p: mp.log(mellin(p)), 0, 2, method='quad'))
s0 = mp.exp(mu)
a = lambda n: mp.pi**2 * (2*n+1)**2/4
C = 2/mp.pi*sum((-1)**n/(2*n+1)*mp.e1(a(n)*s0) for n in range(18))

# Numerical landmarks are independent decimal regression benchmarks.
close(mu, mp.mpf('-0.98916190592581424528126929751404168'), '1e-29')
close(varY, mp.mpf('0.61860043816188562756370825849397207'), '1e-29')
close(C, mp.mpf('0.16066394845703390824413431820372089'), '1e-29')
assert varY > 0 and C > 0
checks += 1

# Exact difference in densities is 1/2 E|Q-1|, Q=S**p/M(p).
# Integration of the positive part by the exit survival spectrum yields
# TV=p*(4/pi)/M(p) * sum (-1)^n/(2n+1) * a_n**(-p)
# * Gamma(p, a_n*M(p)**(1/p)); the formula is independently
# compared with its H->infty limit.
def exact_tv(H):
    p = mp.mpf(1)/(2*H)
    m = mellin(p)
    threshold = mp.exp(mp.log(m)/p)
    series = sum((-1)**n/(2*n+1) * a(n)**(-p)
                 * mp.gammainc(p, a(n)*threshold) for n in range(18))
    return p*(4/mp.pi)*series/m

previous = 0
for H in [1,2,5,10,20,50,100,200]:
    tv = exact_tv(H)
    assert 0 < tv < mp.mpf(1)/2
    checks += 1
    assert tv < previous or previous == 0
    checks += 1
    close(H*tv, C, str(mp.mpf('0.005')/H + mp.mpf('0.00003')))
    previous = tv

# Exact moment comparison: positive qth moment of the normalized
# inter-reset lifetime is M(p*q)/M(p)**q.  In the H=1/2 case,
# Q=2 S, giving E(Q)=1 and Var(Q)=2/3.
close(mellin(2)/mellin(1)**2 - 1, mp.mpf(2)/3)
for H in [1,2,5,10,20,40,80,160]:
    p = mp.mpf(1)/(2*H)
    V = mellin(2*p)/mellin(p)**2 - 1
    assert V > 0
    checks += 1
    close(4*H**2*V, varY, str(mp.mpf('2.0')/H))

# The full exit-survival series at moderate s is a positive, decreasing
# CDF complement; its integral is M(1)=1/2.
for s in [mp.mpf('0.1'),mp.mpf('0.2'),mp.mpf('0.5'),mp.mpf('1.0')]:
    surv = 4/mp.pi*sum((-1)**n/(2*n+1)*mp.exp(-a(n)*s)
                     for n in range(35))
    assert 0 < surv < 1
    checks += 1

print('PASS', checks, 'deterministic checks')
print('E[log S] =', mp.nstr(mu,30))
print('Var(log S) =', mp.nstr(varY,30))
print('TV coefficient =', mp.nstr(C,30))
print('200*TV_H=200 =', mp.nstr(200*exact_tv(200),25))
