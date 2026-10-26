"""Numerical checks for the conditional killing-time decomposition of a killed telegraph motion.

Requires Python 3 and SciPy. Execute: python telegraph_posterior_check.py
"""
import math
from scipy.integrate import quad
from scipy.special import ive


def weighted_bessel_i(n, z, exponential_factor):
    # Exponential factor is <= -z, preventing overflow in the Bessel tail.
    return math.exp(exponential_factor + z) * float(ive(n, z))


def posterior_transform(gamma, alpha, speed, x, u):
    s = gamma + u
    root = math.sqrt(s * (s + 2 * alpha))
    root0 = math.sqrt(gamma * (gamma + 2 * alpha))
    return (gamma / s) * (root / root0) * math.exp(-(root - root0) * abs(x) / speed)


def joint_transform_from_paper(gamma, alpha, speed, x, u):
    # Integrate the boundary atom and interior Bessel density in Eq. (48).
    t0 = abs(x) / speed
    boundary = gamma / (2 * speed) * math.exp(-(gamma + alpha + u) * t0)

    def density(t):
        radius2 = (speed*t)**2 - x*x
        radius = math.sqrt(max(0.0, radius2))
        z = (alpha / speed) * radius
        expo = -(gamma + alpha + u) * t
        term0 = alpha * weighted_bessel_i(0, z, expo)
        d_i0 = alpha*alpha*t/2 * math.exp(expo) if radius < 1.e-10 else alpha*speed*t/radius*weighted_bessel_i(1, z, expo)
        return gamma * (term0 + d_i0) / (2 * speed)

    # Integrate the positive half-line, splitting close to the ballistic frontier.
    return boundary + quad(density, t0, math.inf, epsabs=3e-10, epsrel=3e-10, limit=300)[0]


def levy_laplace_from_integrals(gamma, alpha, speed, x, u):
    # Both jump measures are finite; use directly their Laplace-exponent integrals.
    def part0(t):
        if t == 0: return 0.
        return (1-math.exp(-u*t))*math.exp(-gamma*t)*(-math.expm1(-2*alpha*t))/(2*t)

    def part1(t):
        if t == 0: return 0.
        z = alpha * t
        return (-math.expm1(-u*t))*(alpha / speed)*weighted_bessel_i(1,z,-(gamma+alpha)*t)/t

    exponent = quad(part0, 0, math.inf, epsabs=3e-10, epsrel=3e-10)[0]
    exponent += abs(x)*quad(part1, 0, math.inf, epsabs=3e-10, epsrel=3e-10)[0]
    return math.exp(-u*abs(x)/speed-exponent)


def test():
    n = 0
    for gamma, alpha, speed in [(0.35,0.65,1.7),(1.2,0.3,0.8),(0.1,0.9,2.1), (2.0,0.7,0.5)]:
        r0 = 0.5*math.log((gamma+2*alpha)/gamma)
        r1 = (gamma+alpha-math.sqrt(gamma*(gamma+2*alpha)))/speed
        assert r0 > 0 and r1 > 0
        for x in [0.0, 0.4, 1.5]:
            f0 = joint_transform_from_paper(gamma,alpha,speed,x,0.)
            exact_dens = math.sqrt(gamma*(gamma+2*alpha))/(2*speed)*math.exp(-math.sqrt(gamma*(gamma+2*alpha))*abs(x)/speed)
            assert abs(f0/exact_dens-1) < 1.e-8, ('marginal',gamma,alpha,speed,x,f0,exact_dens)
            for u in [0.2,0.75,1.5]:
                F = posterior_transform(gamma,alpha,speed,x,u)
                G = joint_transform_from_paper(gamma,alpha,speed,x,u)/f0
                H = levy_laplace_from_integrals(gamma,alpha,speed,x,u)
                assert abs(F-G)<2.e-8, ('source joint',gamma,alpha,speed,x,u,F,G)
                assert abs(F-H)<2.e-8, ('Levy',gamma,alpha,speed,x,u,F,H)
                n += 1
        # Verify both finite Levy masses and their first two moments directly.
        def levy0(t):
            return math.exp(-gamma*t)*(-math.expm1(-2*alpha*t))/(2*t) if t>0 else alpha
        def levy1(t):
            return (alpha/speed)*weighted_bessel_i(1,alpha*t,-(gamma+alpha)*t)/t if t>0 else alpha*alpha/(2*speed)
        zroot = math.sqrt(gamma*(gamma+2*alpha))
        expected = [
            (r0, r1),
            (alpha/(gamma*(gamma+2*alpha)),(gamma+alpha)/(speed*zroot)-1/speed),
            (0.5*(1/gamma**2-1/(gamma+2*alpha)**2),alpha**2/(speed*zroot**3)),
        ]
        for k,(target0,target1) in enumerate(expected):
            a0=quad(lambda t: t**k*levy0(t),0,math.inf,epsabs=3e-10,epsrel=3e-10)[0]
            a1=quad(lambda t: t**k*levy1(t),0,math.inf,epsabs=3e-10,epsrel=3e-10)[0]
            assert abs(a0-target0)<2e-8,('levy0 moment',k,a0,target0)
            assert abs(a1-target1)<2e-8,('levy1 moment',k,a1,target1)
            n+=2
        # Check posterior-moment identity against the unconditional Exp(gamma) law.
        root = math.sqrt(gamma*(gamma+2*alpha))
        mu0 = alpha/(gamma*(gamma+2*alpha))
        mu1 = (gamma+alpha)/(speed*root)
        assert abs(mu0+mu1*speed/root-1/gamma)<1.e-11
        # The sum of no-flip endpoint joint intensities is gamma/(2*speed)exp(-(gamma+alpha)|x|/speed).
        for x in [0.,.4,1.5]:
            ballistic_bayes = (gamma/root)*math.exp(-((gamma+alpha)-root)*abs(x)/speed)
            compound_zero = math.exp(-r0-abs(x)*r1)
            assert abs(ballistic_bayes-compound_zero)<1.e-11
            n += 1
    print('PASS:',n,'numerical comparisons; joint-density, compound-Poisson, moments, ballistic atoms')

if __name__ == '__main__':
    test()
