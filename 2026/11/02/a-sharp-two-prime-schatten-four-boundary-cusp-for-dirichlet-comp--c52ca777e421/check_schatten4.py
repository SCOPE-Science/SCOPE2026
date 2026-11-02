"""Supplementary checks for the two-index Schatten-four boundary law.

The asymptotic and operator statements require the accompanying analytic proof;
these finite calculations do not constitute proof of the infinite tail.
"""
import math
from scipy.special import i0, i0e
from scipy.integrate import quad


def kernel(m, n, amplitudes, gap):
    t, u = math.log(m), math.log(n)
    A = sum(amplitudes)
    v = math.exp(-(0.5 + A + gap) * (t + u))
    for a in amplitudes:
        v *= i0(2 * a * math.sqrt(t * u))
    return v


def direct_kernel(m, n, amplitudes, gap, cutoff=32):
    t, u = math.log(m), math.log(n)
    A = sum(amplitudes)
    v = math.exp(-(0.5 + A + gap) * (t + u))
    for a in amplitudes:
        x = a * a * t * u
        series = sum((x**k) / math.factorial(k)**2 for k in range(cutoff + 1))
        v *= series
    return v


def profile(x, amplitudes):
    root = math.sqrt(x)
    A = sum(amplitudes)

    def integrand(v):
        t = x + 0.5 * v * root
        u = x - 0.5 * v * root
        if min(t, u) < 0:
            return 0.0
        z = math.sqrt(t * u)
        result = root * math.exp(-2 * A * (math.sqrt(t) - math.sqrt(u))**2)
        for a in amplitudes:
            result *= i0e(2 * a * z)**2
        return result

    return quad(integrand, -2 * root, 2 * root, epsabs=2e-12, epsrel=5e-10, limit=350)[0]


def asymptotic_coefficient(amplitudes):
    A = sum(amplitudes)
    return (4*math.pi)**(-len(amplitudes)) * math.prod(1/a for a in amplitudes) * math.sqrt(2*math.pi/A)


def main():
    count = 0
    for amplitudes in ([0.4], [0.4, 0.7], [0.4, 0.7, 1.2]):
        for gap in (0.0, 0.1, 0.7):
            for m in (1, 2, 3, 7, 12):
                for n in (1, 3, 5, 11):
                    x = kernel(m, n, amplitudes, gap)
                    y = direct_kernel(m, n, amplitudes, gap)
                    assert abs(x-y) <= 3e-12 * max(1.0, abs(x)), (amplitudes,gap,m,n,x,y)
                    assert abs(kernel(n,m,amplitudes,gap)-x) <= 1e-13
                    count += 2

    for amplitudes in ([1.0], [1.0, 1.0], [0.4, 0.7], [0.4, 0.7, 1.2]):
        k = asymptotic_coefficient(amplitudes)
        for x in (200, 1000, 4000):
            ratio = profile(x,amplitudes) / (k*x**(0.5-len(amplitudes)))
            assert abs(ratio-1) < 2.5/x, (amplitudes,x,ratio)
            count += 1

    # At a_1=a_2=1 the predicted square-root cusp coefficient is 1/(4*pi).
    a = [1.0, 1.0]
    coeff = 4 * math.sqrt(math.pi) * asymptotic_coefficient(a)
    assert abs(coeff-1/(4*math.pi)) < 1e-14
    count += 1
    print('PASS:',count,'supplementary assertions')
    print('equal-amplitude two-prime cusp coefficient:', format(coeff,'.16g'))
    print('scope: finite Gram and independent asymptotic-profile checks, not an infinite proof')


if __name__ == '__main__':
    main()
