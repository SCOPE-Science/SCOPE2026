"""Independent numerical tests of the stated Euclidean random-line chord asymptotic.

Requires numpy and scipy. Uses actual intersections with the l_p unit disk,
not the leading-order chord-deficit approximation, in the planar tests.
The analytical proof in RESULT.md, not these finite tests, is the certificate
for all dimensions and all real exponents in the stated open interval.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma
from scipy.stats import qmc


def perimeter_lp(p):
    assert 1 < p < 2
    def integrand(x):
        if x >= 1: return float('inf')
        t = x**(p-1) * (1-x**p)**(1/p-1)
        return math.hypot(1.0, t)
    return 4 * quad(integrand, 0, 1, epsabs=1e-11,
                    epsrel=1e-11, limit=400)[0]


def predicted_coefficient(p, d, surface_area):
    q = d-1
    kappa_q = math.pi**(q/2) / gamma(1+q/2)
    return (d * 2**(q+1) * p**(2*q/p) * gamma(1+1/p)**(2*q)
            / (kappa_q * surface_area * gamma(1+2*q/p)))


def exact_chord_lengths(theta, offset, p):
    """Actual intersection chord lengths, lines x=s(cos t,sin t)+r(-sin t,cos t)."""
    c, s = np.cos(theta), np.sin(theta)
    roots=[]
    for side in (+1., -1.):
        v=np.full_like(theta, side)
        for _ in range(12):
            a=v*c-offset*s
            b=v*s+offset*c
            F=np.abs(a)**p+np.abs(b)**p-1
            deriv=p*(np.sign(a)*np.abs(a)**(p-1)*c
                     + np.sign(b)*np.abs(b)**(p-1)*s)
            v-=F/deriv
        residual=np.max(np.abs(np.abs(v*c-offset*s)**p+
                               np.abs(v*s+offset*c)**p-1))
        assert residual < 2e-13, residual
        roots.append(v)
    return roots[0]-roots[1]


def run():
    # Endpoint-to-line tangent Jacobian in each transverse dimension q.
    for q in range(1,6):
        I=np.eye(q)
        J=np.block([[I/2,-I/2],[I/2,I/2]])
        assert abs(abs(np.linalg.det(J))-2**(-q))<1e-12

    xy=qmc.Sobol(d=2,scramble=False).random_base2(19)
    for p, max_rel in ((1.25,.01),(1.5,.013),(1.75,.06)):
        surface=perimeter_lp(p)
        C=predicted_coefficient(p,2,surface)
        ratios=[]
        for eps in (1e-4,1e-8):
            t=(p*eps)**(1/p)
            B=1.1*t
            theta=(2*xy[:,0]-1)*B
            offset=(2*xy[:,1]-1)*B
            L=exact_chord_lengths(theta,offset,p)
            accept=L>2-eps
            # Two diameter lines; the square area is (2B)^2 at each.
            actual=2*(2*B)**2*np.count_nonzero(accept)/len(xy)/surface
            ratio=actual/(C*eps**(2/p))
            ratios.append(ratio)
            if eps==1e-8 and p==1.5:
                U=offset[accept]+theta[accept]
                V=offset[accept]-theta[accept]
                T=np.abs(U)**p/(p*eps)
                rem=1-(np.abs(U)**p+np.abs(V)**p)/(p*eps)
                assert abs(np.mean(T)-1/(p+2))<.004
                assert abs(np.mean(rem)-p/(p+2))<.007
        assert abs(ratios[-1]-1)<max_rel, (p,ratios)
        assert ratios[-1]<ratios[0], (p,ratios)
        print('d=2, p=%.2f, perimeter=%.10f, C=%.10f, '
              'ratios at 1e-4 and 1e-8 = %s' % (p,surface,C,ratios))

    # With p=2 the maximizing diameters are no longer isolated:
    # the exact Euclidean-ball formula has exponent (d-1)/2,
    # whereas the theorem has exponent 2(d-1)/p for every p<2.
    for d in range(2,7):
        q=d-1
        for eps in (1e-2,1e-4):
            exact=(eps-eps**2/4)**(q/2)
            assert abs(exact/eps**(q/2)-(1-eps/4)**(q/2))<1e-12
    print('dimension-specific Jacobians, planar chord probabilities, '
          'conditional Dirichlet means, and ball endpoint: PASS')


if __name__=='__main__':
    run()
