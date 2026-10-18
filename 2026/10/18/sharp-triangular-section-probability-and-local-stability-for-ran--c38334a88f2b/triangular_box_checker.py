"""Deterministic numerical cross-checks for affine box section probabilities.
The general theorem is proved analytically; finite grids are not a proof.
"""
from math import pi, sqrt, atan, cos, sin


def radical_inverse_base2(n):
    f = 0.5
    ans = 0.0
    while n:
        if n & 1:
            ans += f
        n >>= 1
        f *= 0.5
    return ans


def measure(a, b, c, power=18):
    n = 1 << power
    summation = 0.0
    for k in range(n):
        z = 2.0 * (k + 0.5) / n - 1.0
        radius = sqrt(1-z*z)
        azimuth = 2*pi*radical_inverse_base2(k)
        x, y = abs(radius*cos(azimuth)), abs(radius*sin(azimuth))
        summation += min(a*x, b*y, c*abs(z))
    return 4*summation/(n*(a+b+c))


if __name__ == '__main__':
    phi = atan(sqrt(2))
    maximum = 2.0-4.0*sqrt(2)*phi/pi
    hessian = phi/(pi*sqrt(2))-1.0/(3*pi)
    p = measure(1.,1.,1.)
    assert abs(p-maximum)<3e-5, (p,maximum)
    for dims in [(0.8,1.,1.2),(.2,1.,1.8),(.4,.5,2.1)]:
        assert measure(*dims)<maximum-1e-5
    for delta in [0.1, 0.06]:
        approx = (maximum-measure(1+delta,1-delta,1))/(2*delta**2)
        assert abs(approx-hessian)<0.003, (delta,approx,hessian)
    print('PASS: cube exact value, strict examples, Hessian limit; n=2^18 quasi-uniform normals')
    print('cube probability:',format(maximum,'.15g'))
    print('isotropic Hessian coefficient:',format(hessian,'.15g'))
