"""Optional positive-kernel diagnostics for the Bloch Hilbert essential-norm limit.

Requires scipy. Analytic proof is in RESULT.md; this finite check is not a certificate.
"""
from scipy.integrate import quad
from scipy.special import gamma, hyp2f1

for alpha in (1.2, 1.5, 1.8):
    constant = gamma(alpha-1) * gamma(2-alpha)
    for r in (0.9, 0.99, 0.999):
        def F(t):
            return t * hyp2f1(0.5, alpha, 1.5, t*t)
        integral = quad(lambda t: t*F(t)/(1-t*r)**2,
                        0, 1, epsabs=1e-6, epsrel=1e-7,
                        limit=350, points=[.8, .95, .99, .999])[0]
        value = (1-r*r)**alpha * integral
        print(f'alpha={alpha:.1f} r={r:.3f} integral={value:.8f} '
              f'Beta={constant:.8f} ratio={value/constant:.8f}')
