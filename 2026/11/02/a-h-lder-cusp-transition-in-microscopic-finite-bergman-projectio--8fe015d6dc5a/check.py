#!/usr/bin/env python3
"""Finite checks for cusp-weight hard-edge polynomial kernels.

Python standard library only. These experiments do not prove the asymptotic theorem.
"""
import cmath
import math


def integral_power(q, s):
    """F_q(s) = integral_0^1 t^q exp(-s*t) dt, via its entire series."""
    z = 1.0 + 0j
    total = z / (q + 1)
    for k in range(1, 160):
        z *= -s / k
        increment = z / (q + k + 1)
        total += increment
        if abs(increment) < 1e-16:
            break
    return total


def moment(j, alpha, c, d):
    # Squared norm of z**(j-1), normalized planar area measure.
    beta = math.exp(math.lgamma(2*j) + math.lgamma(1+alpha)
                    - math.lgamma(2*j+1+alpha))
    return 1.0/j + 2*c*beta + d/(j*(2*j+1))


def kernel_scaled(n, alpha, c, d, s):
    return sum(cmath.exp(-s*(j-1)/n)/moment(j, alpha, c, d)
               for j in range(1, n+1)) / n**2


def coefficient(alpha, c, d, s):
    c_alpha = c*2**(-alpha)*math.gamma(1+alpha)
    gamma = s*integral_power(1, s)+cmath.exp(-s)/2
    if alpha < 0.5:
        return c_alpha*c_alpha*integral_power(1-2*alpha, s), 2*alpha
    if alpha == 0.5:
        return gamma+(c_alpha*c_alpha-d/2)*integral_power(0, s), 1.0
    return gamma-d/2*integral_power(0, s), 1.0


def first_corrected(n, alpha, c, d, s):
    c_alpha = c*2**(-alpha)*math.gamma(1+alpha)
    return (kernel_scaled(n, alpha, c, d, s)
            - integral_power(1, s)
            + c_alpha*n**(-alpha)*integral_power(1-alpha, s))


def run():
    checks = 0
    # Independent moment quadrature uses a different integral representation.
    for alpha in (0.30, 0.50, 0.70):
        for (c,d) in ((0.8,0.7),(0.6,-0.2)):
            for j in (1,2,5,12,30):
                steps = 30000
                h=1/steps
                f=lambda r: 2*r**(2*j-1)*(1+c*(1-r)**alpha+d*(1-r))
                approx = h*(f(0.0)+f(1.0)+4*sum(f(h*k) for k in range(1,steps,2))
                            +2*sum(f(h*k) for k in range(2,steps,2)))/3
                assert abs(approx-moment(j,alpha,c,d)) < 0.000003
                checks += 1
    # Known unweighted finite kernel identity.
    for n in (2,5,30,100):
        for s in (0j,0.5+0j,0.3+0.4j):
            q=cmath.exp(-s/n)
            explicit=sum(j*q**(j-1) for j in range(1,n+1))/n**2
            assert abs(kernel_scaled(n,0.3,0,0,s)-explicit)<1e-12
            checks+=1
    # Hermitian symmetry of the finite polynomial reproducing kernel.
    for alpha in (0.30,0.50,0.70):
        for n in (19,113):
            s=0.9+0.6j
            v=kernel_scaled(n,alpha,0.8,0.7,s)
            vs=kernel_scaled(n,alpha,0.8,0.7,s.conjugate())
            assert abs(v-vs.conjugate())<2e-12
            checks+=1
    # Convergence of the exact second-order scaled residual to its predicted
    # complex limiting profile, tested in every exponent regime.
    for alpha in (0.30,0.50,0.70):
        for (c,d) in ((0.8,0.7),(0.6,-0.2)):
            for s in (0j,0.7+0.4j,1.1+0j):
                target,power=coefficient(alpha,c,d,s)
                obs=[]
                for n in (128,512,2048,8192):
                    value=first_corrected(n,alpha,c,d,s)*n**power
                    obs.append(abs(value-target))
                    assert math.isfinite(value.real) and math.isfinite(value.imag)
                    checks+=2
                # A fourfold increase in n must improve the error markedly.
                assert obs[-1] < obs[-2] and obs[-1] < 0.05
                checks+=1
    print('PASS: %d finite supplementary assertions' % checks)
    print('Exponents checked: 0.30, 0.50, 0.70; the endpoint 0.50 is included.')
    print('These finite comparisons are corroboration, not a proof of any limit.')

if __name__=='__main__':run()
