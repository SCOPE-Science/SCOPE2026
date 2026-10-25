"""Self-contained numerical spot checks of a planar width-constrained support-function estimate.

This is not a substitute for the universal analytic proof.
"""
import math

PI = math.pi


def phi_root(nmax):
    def even_sum(angle):
        return sum(math.cos(n * angle) / (n*n-1)
                   for n in range(2, nmax+1, 2))
    left, right = 0.0, PI/2
    assert even_sum(left) > 0 and even_sum(right) < 0
    for _ in range(65):
        mid = (left+right)/2
        if even_sum(mid) > 0:
            left = mid
        else:
            right = mid
    return (left+right)/2


def check(nmax, ngrid=65536):
    r, ell = 1.0, 2.0
    phi = phi_root(nmax)
    eps = 0.001
    harmonics = [(n, 1/(n*n-1)) for n in range(2, nmax+1)]
    t = sum(c for n,c in harmonics)
    # Minkowski curvature measure has density r - eps*sum(cos n(theta-phi))
    # and two point atoms of mass ell at normals 0 and pi.
    integral = 0.0
    min_density = 1e10
    minwidth = float('inf')
    max_dh = 0.0
    for j in range(ngrid):
        theta = 2*PI*j/ngrid
        s = math.sin(theta)
        q = sum(c*math.cos(n*(theta-phi)) for n,c in harmonics)
        density = r-eps*sum(math.cos(n*(theta-phi)) for n,c in harmonics)
        h = r + ell*abs(s)/2 + eps*q
        integral += h*density
        min_density = min(min_density,density)
        max_dh = max(max_dh,abs(eps*q))
        if j < ngrid//2:
            q_pi = sum(c*math.cos(n*(theta+PI-phi)) for n,c in harmonics)
            minwidth = min(minwidth,2*r + ell*abs(s) + eps*(q+q_pi))
    integral *= 2*PI/ngrid
    q0 = sum(c*math.cos(n*(0-phi)) for n,c in harmonics)
    qp = sum(c*math.cos(n*(PI-phi)) for n,c in harmonics)
    area = (integral+ell*(2*r+eps*(q0+qp)))/2
    stadium_area=PI*r*r+2*r*ell
    gap = stadium_area-area
    predicted_gap=eps*eps*PI*t/2
    predicted_distance=eps*t
    sharp_ratio = predicted_distance**2 / predicted_gap
    assert min_density>0
    assert abs(minwidth-2*r)<1e-10
    assert abs(gap-predicted_gap)<1e-7, (nmax,gap,predicted_gap)
    assert abs(max_dh-predicted_distance)<5e-7
    assert sharp_ratio < 3/(2*PI)
    return nmax,phi,gap,predicted_gap,sharp_ratio,min_density


def main():
    print('N / root / measured area deficit / predicted / sharpness ratio / min curvature density')
    for n in (4,8,16,32,64,128):
        result = check(n)
        print('%3d %.9f %.10f %.10f %.10f %.6f' % result)
    print('limiting sharp constant',3/(2*PI))
    print('PASS: six distinct smooth Fourier perturbations of a stadium; '
          'numerical integration agrees with the exact defect identity.')

if __name__ == '__main__':
    main()
