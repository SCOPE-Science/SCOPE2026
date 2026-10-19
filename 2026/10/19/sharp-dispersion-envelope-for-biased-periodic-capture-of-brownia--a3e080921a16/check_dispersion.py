"""Independent numerical cross-checks for a periodized Brownian capture model.

Run with Python 3, NumPy and mpmath. The analytic proof is in RESULT.md.
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 50
checks = 0

def confirm(ok, message):
    global checks
    assert ok, message
    checks += 1

def statistics(z,theta):
    delta = mp.mpf('0.5')-theta
    s = mp.sinh(z/2)
    m = mp.sinh(delta*z)/(2*s)
    b = mp.cosh(delta*z)*mp.cosh(z/2)/(2*s*s)
    dm = delta*mp.cosh(delta*z)/(2*s)-mp.sinh(delta*z)*mp.cosh(z/2)/(4*s*s)
    R = z*z/2*(b+z*m*dm)
    return m,b,R

# Compare the two-sided Laplace-tail enumeration to hyperbolic closed forms.
for z0 in [0.35,0.8,1.7,3.9,7.3]:
    z=mp.mpf(str(z0))
    q=mp.exp(-z)
    for th0 in [0,0.13,0.3,0.5,0.72,0.91,1]:
        th=mp.mpf(str(th0)); delta=mp.mpf('0.5')-th
        u=mp.exp(-th*z); w=mp.exp(-(1-th)*z)
        m1=(u-w)/(2*(1-q))
        b1=(u+w)*(1+q)/(2*(1-q)**2)
        m,b,R=statistics(z,th)
        confirm(abs(m-m1)<mp.mpf('1e-42'),"first-moment tail identity")
        confirm(abs(b-b1)<mp.mpf('1e-42'),"second-moment tail identity")
        confirm(R>0,"positive dispersion")
        # Analytic r-derivative and independent differentiated expression.
        dmdz=mp.diff(lambda x: statistics(x,th)[0],z)
        confirm(abs(R-z*z/2*(b+z*m*dmdz))<mp.mpf('1e-38'),"cycle-time correlation")

# The sharp asymmetry envelope is strict away from its equality classes.
for z0 in [0.13,0.5,1.0,1.7,3,6,12,25]:
    z=mp.mpf(str(z0))
    prev=statistics(z,mp.mpf('0.5'))[2]
    low=prev
    upper=z*z*mp.coth(z/2)**2/4
    confirm(abs(upper-statistics(z,mp.mpf('0'))[2])<mp.mpf('1e-40'),"boundary identity")
    for d0 in [.03,.09,.14,.21,.27,.33,.40,.47,.5]:
        delta=mp.mpf(str(d0))
        val=statistics(z,mp.mpf('0.5')-delta)[2]
        confirm(val>prev and val<=upper*(1+mp.mpf('1e-40')),"strict capture-asymmetry ordering")
        prev=val
    confirm(low<=upper,"envelope consistency")

# Weak-rate enhancement and large-rate quenching in the nondegenerate model.
for theta0 in [.04,.17,.31,.5,.67,.93]:
    th=mp.mpf(str(theta0)); delta=mp.mpf('0.5')-th
    z=mp.mpf('0.001')
    approximant=1+z*z*(mp.mpf(1)/24+delta*delta/2)
    confirm(abs(statistics(z,th)[2]-approximant)<mp.mpf('2e-10'),"weak-rate expansion")
    confirm(statistics(mp.mpf('1000'),th)[2]<mp.mpf('1e-5'),"strong-rate quenching")

# Seeded independent cycle simulation checks the covariance correction.
rng=np.random.default_rng(29071)
for rate,theta in [(3.0,0.3),(1.0,0.5),(6.0,0.2)]:
    n=450000
    ages=rng.exponential(scale=1/rate,size=n)
    excursion=rng.standard_normal(n)*np.sqrt(2*ages)
    moves=np.floor(excursion+(1-theta)).astype(np.int64)
    sample_speed=moves.mean()/ages.mean()
    sample_dispersion=np.mean((moves-sample_speed*ages)**2)/(2*ages.mean())
    z=mp.sqrt(rate)
    m,b,R=statistics(z,mp.mpf(str(theta)))
    exact_speed=float(rate*m)
    confirm(abs(sample_speed-exact_speed)<0.025,"independent renewal-cycle speed simulation")
    confirm(abs(sample_dispersion-float(R))<0.055,"independent renewal-cycle dispersion simulation")

print('PASSED',checks,'checks')
