"""Independent numerical checks for Poisson-reset power-law cooling.

External inputs: none.  Requires numpy and scipy.  This tests finite
quadrature identities and asymptotic convergence, not the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_genlaguerre, gamma


def integrate_age(fun, rate):
    return quad(lambda a: rate * math.exp(-rate * a) * fun(a), 0,
                150 / rate, epsabs=2.e-13, epsrel=2.e-12, limit=300)[0]


def direct_cov(rate, cool, p, initial, lag):
    f = lambda a: initial * (1 + cool * a) ** (-p)
    mu = integrate_age(f, rate)
    mean_shift = integrate_age(lambda a: f(a + lag), rate)
    ef_product = integrate_age(lambda a: f(a) * f(a + lag), rate)
    return math.exp(-rate * lag) * (ef_product - mu * mean_shift)


def gamma_quadrature_cov(rate, cool, p, initial, lag, order=100):
    # Laplace mixture f(a) = T0*E[e^{-c G a}], G~Gamma(p,1).
    x, weights = roots_genlaguerre(order, p - 1)
    weights = weights / gamma(p)
    u = cool * x[:, None]
    v = cool * x[None, :]
    positive_kernel = rate * u * v / (
        (rate + u + v) * (rate + u) * (rate + v))
    return float(initial**2 * math.exp(-rate * lag) *
                 np.sum(weights[:, None] * weights[None, :] *
                        np.exp(-v * lag) * positive_kernel))


def mean(rate, cool, p, initial):
    return integrate_age(lambda a: initial * (1 + cool * a) ** (-p), rate)


def susceptibility(rate, cool, p, initial):
    # +d(mean)/d(rate), not the negative derivative.
    return quad(lambda a: math.exp(-rate*a) * (1-rate*a) *
                initial * (1 + cool*a)**(-p), 0, 150/rate,
                epsabs=2.e-13, epsrel=2.e-12, limit=300)[0]


def edge_weight_normalized(rate, cool, p, initial, v):
    # w(v)/v^p from a gamma-mixture, with no subtractions.
    coeff = initial * math.exp(-v/cool) / (gamma(p)*cool**p)
    def integrand(u):
        mu = initial * (u/cool)**(p-1) * math.exp(-u/cool) / (gamma(p)*cool)
        return mu * rate * u / ((rate+u+v)*(rate+u)*(rate+v))
    return coeff*quad(integrand, 0, 100*cool,
                      epsabs=3.e-13, epsrel=3.e-12, limit=300)[0]


def run():
    n = 0
    max_relative_quadrature = 0.0
    max_relative_edge = 0.0
    for p in (0.7, 5/3, 2.0, 3.1):
        for rate in (0.7, 1.3):
            for cool in (0.55, 1.15):
                initial=1.7
                mu=mean(rate,cool,p,initial)
                Q=susceptibility(rate,cool,p,initial)
                assert mu>0 and Q>0
                eps=2.e-5*rate
                numerical=(mean(rate+eps,cool,p,initial)-mean(rate-eps,cool,p,initial))/(2*eps)
                assert abs(numerical/Q-1)<1.e-8, (p,rate,cool,Q,numerical)
                n+=1
                for lag in (0.0, .15, .75, 2.5, 10.0):
                    exact=direct_cov(rate,cool,p,initial,lag)
                    mixture=gamma_quadrature_cov(rate,cool,p,initial,lag)
                    assert exact>0 and mixture>0
                    rel=abs(exact/mixture-1)
                    max_relative_quadrature=max(rel,max_relative_quadrature)
                    assert rel<2.e-6, (p,rate,cool,lag,exact,mixture,rel)
                    n+=1
                predicted_edge=initial*Q/(gamma(p)*cool**p)
                for v in (1.e-5,1.e-4,1.e-3):
                    ratio=edge_weight_normalized(rate,cool,p,initial,v)/predicted_edge
                    assert ratio>0
                    max_relative_edge=max(max_relative_edge,abs(1-ratio))
                    assert abs(ratio-1) < max(0.01,25*v/cool)
                    n+=1
                amplitude=p*initial*Q/(cool**p)
                for lag in (40,100,180):
                    exact=direct_cov(rate,cool,p,initial,lag)
                    scaled=exact*math.exp(rate*lag)*lag**(p+1)
                    assert 0 < scaled < amplitude*1.2, (p,rate,cool,lag,scaled,amplitude)
                    assert abs(scaled/amplitude-1)<(15.0/lag), (p,rate,cool,lag,scaled,amplitude)
                    n+=1
                # Stationary jump carré-du-champ: -C'(0+) = r/2 E[(T0-T)^2].
                jump_m2=integrate_age(lambda a: (initial - initial*(1+cool*a)**(-p))**2, rate)
                predicted_slope=-.5*rate*jump_m2
                step=1.e-4
                measured_slope=(-3*direct_cov(rate,cool,p,initial,0) +
                    4*direct_cov(rate,cool,p,initial,step) -
                    direct_cov(rate,cool,p,initial,2*step))/(2*step)
                assert abs(measured_slope/predicted_slope-1)<1.e-6, (p,rate,cool,measured_slope,predicted_slope)
                n+=1
                # Expected shape of the strict log-convex covariance.
                for h in (.25, .5, 1.0, 2.0, 4.0):
                    c0=direct_cov(rate,cool,p,initial,h)
                    cm=direct_cov(rate,cool,p,initial,h-.1)
                    cp=direct_cov(rate,cool,p,initial,h+.1)
                    assert cm*cp > c0*c0, (p,rate,cool,h)
                    n+=1
    print('PASS:',n,'independent quadrature/edge/response/asymptotic/log-convexity checks')
    print('worst quadrature relative error:',max_relative_quadrature)
    print('worst small-v edge relative error:',max_relative_edge)
    print('physical Haff benchmark: r=1.3, cool=0.8, p=2, T0=2')
    rate,cool,p,initial=1.3,.8,2.,2.
    print('stationary mean:',mean(rate,cool,p,initial))
    print('mean response:',susceptibility(rate,cool,p,initial))
    print('long-time covariance prefactor:',p*initial*susceptibility(rate,cool,p,initial)/cool**p)

if __name__ == '__main__':
    run()
