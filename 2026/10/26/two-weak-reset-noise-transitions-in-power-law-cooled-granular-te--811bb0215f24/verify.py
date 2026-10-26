"""Independent quadrature checks for a Poisson-reset power-law cooling temperature.
Dependencies: Python 3, scipy.  Execute: python verify.py
"""
from math import exp, log1p, expm1, gamma, pi
from scipy.integrate import quad


def experiment(alpha, r, tau=1., scale=1.):
    def f(x):
        return scale * (1+x/tau)**(-alpha)
    def F(x):
        z = log1p(x/tau)
        return scale*tau*(z if alpha == 1 else expm1((1-alpha)*z)/(1-alpha))
    def expect(g):
        return quad(lambda u: exp(-u)*g(u/r), 0., 50.,
                    epsabs=1e-11, epsrel=1e-11, limit=500)[0]
    mean = expect(f)
    var = expect(lambda x: f(x)**2)-mean**2
    sigma_regen = r*expect(lambda x: (F(x)-mean*x)**2)
    def C(t):
        e = expect(lambda x: f(x+t))
        return exp(-r*t)*(expect(lambda x: f(x)*f(x+t))-mean*e)
    sigma_corr = (2/r)*quad(lambda u: C(u/r), 0., 48.,
                             epsabs=1e-11, epsrel=1e-11, limit=500)[0]
    return var, sigma_regen, sigma_corr, C(.4)


def main():
    cases = [(2., .5), (2., 2.), (5/3, .3), (.4, 1.),
             (.75, .6), (1., .8), (.5, 2.)]
    for alpha, r in cases:
        v, s1, s2, c = experiment(alpha, r)
        assert v > 0 and s1 > 0 and c > 0
        assert abs(s1-s2) <= 2e-8*max(1., abs(s1),abs(s2)), (alpha,r,s1,s2)
        print(f'alpha={alpha:.6g} rate={r:.6g} stationary_var={v:.12g} '
              f'CLT_variance={s1:.12g} 2*integrated_cov={s2:.12g}')
    assert abs((gamma(2)/(.5**2) - 2*(.5)*gamma(.5)**2)-(4-pi)) < 1e-12
    for a in (.25, .5, .75):
        b = gamma(3-2*a)/(1-a)**2-2*(1-a)*gamma(1-a)**2
        assert b > 0
    # Far below the reset clock scale, independently check the predicted
    # singular noise exponent for a subcritical and a supercritical example.
    for alpha in (.25, 2.):
        r = .01
        _, sig, _, _ = experiment(alpha, r)
        if alpha < 1:
            B = gamma(3-2*alpha)/(1-alpha)**2 - 2*(1-alpha)*gamma(1-alpha)**2
            approx = B*r**(2*alpha-1)
            assert .8 < sig/approx < 1.2, (alpha,sig,approx)
        else:
            approx = r/(alpha-1)**2
            assert .8 < sig/approx < 1.2, (alpha,sig,approx)
    print('All 7 regenerative/Green-Kubo checks and 2 limit-regime checks passed.')

if __name__=='__main__':
    main()
