#!/usr/bin/env python3
import math
from statistics import NormalDist

N = NormalDist()
SQRT2PI = math.sqrt(2.0 * math.pi)

def phi(x):
    return math.exp(-0.5*x*x) / SQRT2PI

def Phi(x):
    return N.cdf(x)

def h(x):
    return phi(x) / Phi(x)

def deriv(theta, mu, alpha):
    z = N.inv_cdf(1.0-alpha)
    return mu*(-math.sin(theta)*h(mu*math.cos(theta)) + math.cos(theta)*h(mu*math.sin(theta)-z))

def optimum(mu, alpha):
    lo, hi = 0.0, math.pi/2
    assert deriv(lo, mu, alpha) > 0
    assert deriv(hi, mu, alpha) < 0
    for _ in range(120):
        mid = (lo+hi)/2
        if deriv(mid, mu, alpha) > 0:
            lo = mid
        else:
            hi = mid
    theta=(lo+hi)/2
    tau=math.tan(theta)
    z=N.inv_cdf(1.0-alpha)
    D=Phi(mu*math.cos(theta))*Phi(mu*math.sin(theta)-z)
    return theta,tau,D

def D_tau(mu, alpha, tau):
    z=N.inv_cdf(1.0-alpha)
    return Phi(mu/math.sqrt(1+tau*tau))*Phi(mu/math.sqrt(1+tau**-2)-z)

# Algebra of the split, represented by coefficients on independent X,Z.
for tau in [0.2, 0.7, 1.0, 2.3, 10.0]:
    var_u=1+tau*tau
    var_v=1+tau**-2
    cov=1 + tau*(-1/tau)
    assert abs(cov) < 1e-15
    assert abs(1/var_u + 1/var_v - 1) < 1e-14

# Unique numerical roots and strict inference-heavy allocation for conventional levels.
for alpha in [0.01,0.05,0.10,0.25,0.49]:
    for mu in [0.05,0.2,1.0,3.0,8.0]:
        th,tau,D=optimum(mu,alpha)
        assert tau > 1.0
        assert abs(deriv(th,mu,alpha)) < 2e-12
        assert D > D_tau(mu,alpha,1.0)

# Reported benchmark.
th,tau,D=optimum(1.0,0.05)
info_sel=1/(1+tau*tau)
D_equal=D_tau(1.0,0.05,1.0)
assert abs(tau-2.32247756096945) < 5e-13
assert abs(info_sel-0.156399018421506) < 5e-13
assert abs(D-0.152850177804114) < 5e-13
assert abs(D_equal-0.132425855003328) < 5e-13

# Weak-signal limit.
alpha=0.05
z=N.inv_cdf(1-alpha)
tau_lim=math.exp(-0.5*z*z)/(2*alpha)
info_lim=1/(1+tau_lim*tau_lim)
_,tau_small,_=optimum(1e-5,alpha)
assert abs(tau_small-tau_lim) < 3e-5
assert abs(tau_lim-2.58522712287081) < 5e-13
assert abs(info_lim-0.130150726777404) < 5e-13

# Boundary-null invariance.
for alpha in [0.01,0.05,0.2,0.49]:
    for tau in [0.1,0.5,1.0,2.0,10.0]:
        assert abs(D_tau(0.0,alpha,tau)-alpha/2) < 2e-15

print(f"tau_star(alpha=.05,mu=1)={tau:.14f}" if False else f"tau_star(alpha=.05,mu=1)={optimum(1.0,0.05)[1]:.14f}")
print(f"discovery_star={optimum(1.0,0.05)[2]:.15f}")
print(f"weak_signal_tau_limit={tau_lim:.14f}")
print(f"weak_signal_selection_information={info_lim:.15f}")
print("VERIFY_OK")
