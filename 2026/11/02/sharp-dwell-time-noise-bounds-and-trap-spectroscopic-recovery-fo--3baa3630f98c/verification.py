"""Reproduce formulas for a stationary alternating-renewal harmonic particle.

All distribution parameters and checks are explicit. No external dependencies.
The regenerative-reward computation is independent of the stationary
correlation/linear-filter derivation in the accompanying mathematical proof.
Numerical tests are supporting evidence and cannot certify general identities.
"""
import math
import random


def laplace(kind, k, mean):
    z = k * mean
    if kind == "deterministic":
        return math.exp(-z), math.exp(-2*z)
    if kind == "exponential":
        return 1/(1+z), 1/(1+2*z)
    if kind == "erlang2":
        return (1+z/2)**-2, (1+z)**-2
    if kind == "two_point":
        # Equal masses at mean/2 and 3*mean/2.
        return ((math.exp(-z/2)+math.exp(-3*z/2))/2,
                (math.exp(-z)+math.exp(-3*z))/2)
    raise ValueError(kind)


def variance_by_correlation(k, speed, mean, phi):
    return speed**2/k**2 * (1 - 2*(1-phi)/(k*mean*(1+phi)))


def variance_by_reward(k, speed, mean, a, b):
    # Starting position relative to the current force sign at run beginnings:
    # Y_next = -exp(-k*L)*Y - (speed/k)*(1-exp(-k*L)).
    # a=E exp(-kL), b=E exp(-2kL).
    c = speed/k
    m = -c*(1-a)/(1+a)
    M = (2*c*(a-b)*m+c*c*(1-2*a+b))/(1-b)
    integral = c*c*mean + 2*c*(m-c)*(1-a)/k
    integral += (M-2*c*m+c*c)*(1-b)/(2*k)
    return integral/mean


def draw(kind, rng, mean):
    if kind == "deterministic": return mean
    if kind == "exponential": return rng.expovariate(1/mean)
    if kind == "erlang2": return (rng.expovariate(2/mean)
                                  + rng.expovariate(2/mean))
    if kind == "two_point": return mean*(0.5 if rng.random()<0.5 else 1.5)
    raise ValueError(kind)


def independent_time_average(kind, k, speed, mean, n=120000):
    rng = random.Random(0x415152)
    c = speed/k
    y = 0.0
    total_reward = 0.0
    total_duration = 0.0
    for i in range(n+3000):
        L = draw(kind, rng, mean)
        a = math.exp(-k*L)
        reward = c*c*L+2*c*(y-c)*(-math.expm1(-k*L))/k
        reward += ((y-c)**2)*(-math.expm1(-2*k*L))/(2*k)
        y = -a*y-c*(1-a)
        if i>=3000:
            total_duration += L
            total_reward += reward
    return total_reward/total_duration


def run():
    kinds = ("deterministic", "exponential", "erlang2", "two_point")
    count = 0
    for mean in (0.7, 1.7, 3.0):
        for k in (0.16, 0.43, 1.1, 2.3):
            for kind in kinds:
                a,b=laplace(kind,k,mean)
                x=variance_by_correlation(k,1.31,mean,a)
                y=variance_by_reward(k,1.31,mean,a,b)
                assert x > 0 and abs(x-y)<max(1e-9,abs(x)*1e-10), (kind,k,mean,x,y)
                count+=1
    print('Independent correlation/reward identities:',count,'PASS')
    for mean in (.6,1.0,2.5):
        for k in (.1,.4,1.0,4.0):
            d=variance_by_correlation(k,1.31,mean,laplace('deterministic',k,mean)[0])
            for kind in kinds[1:]:
                v=variance_by_correlation(k,1.31,mean,laplace(kind,k,mean)[0])
                assert v>d, (kind,k,mean,d,v)
    print('Strict deterministic optimum over nondegenerate examples: PASS')
    for k in (0.2, .6, 1.5):
        for kind in kinds:
            mean = 1.2
            a,b=laplace(kind,k,mean)
            theory=variance_by_reward(k,1.3,mean,a,b)
            independent=independent_time_average(kind,k,1.3,mean)
            rel=abs(theory-independent)/theory
            assert rel < .08, (kind,k,theory,independent,rel)
            print('Independent event-driven time integration',kind,'k=',k,
                  'relative discrepancy=',round(rel,5))
    # At arbitrarily weak confinement, strictly positive run-time variance
    # forces a positive k*Var(X), whereas deterministic timing stays bounded.
    for k in (1e-2, 5e-3, 1e-3):
        for kind, varL in (('exponential',1.),('erlang2',0.5),('two_point',0.25)):
            a,_=laplace(kind,k,1.0)
            val=variance_by_correlation(k,1.0,1.0,a)
            assert abs(k*val-varL/2)/(varL/2) < .02
        z=k/2
        v_det = (1 - math.tanh(z)/z)/k**2
        assert abs(v_det-1/12)/(1/12)<.01
    print('Weak-trap singularity and deterministic finite limit: PASS')
    for eps in (1e-2,1e-3,1e-4):
        # Increasingly heterogeneous two-point law of fixed mean 1.
        a=(1-eps)*math.exp(-2*eps)+eps*math.exp(-2*(1-eps+eps**2)/eps)
        vmax=variance_by_correlation(2.0,1.0,1.0,a)
        if eps==1e-4:
            assert vmax/(1/4)>.999
    print('Unattained upper envelope approached: PASS')

if __name__ == '__main__':
    run()
