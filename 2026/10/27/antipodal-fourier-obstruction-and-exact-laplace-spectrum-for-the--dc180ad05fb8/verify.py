"""Independent finite checks for the Fourier calculation on a supremum circle torus.

All computations are diagnostic: the accompanying proof establishes all frequencies.
Run: python3 verify.py
"""
import math

PI = math.pi


def coefficient(a, n, m):
    n, m = abs(n), abs(m)
    E = math.exp(-PI * a)
    if n == 0 and m == 0:
        return 2 * (1 - (1 + PI * a) * E) / (PI**2 * a**2)
    if m == 0:
        z = (-1)**n * E
        return (2 * a*a * (1-z) / ((a*a+n*n)**2)
                - PI*a*z / (a*a+n*n)) / PI**2
    if n == 0:
        return coefficient(a, m, 0)
    return (a*a * (1 - (-1)**(n+m)*E) / (2 * PI**2 * n*m)
            * (1/(a*a+(n-m)**2) - 1/(a*a+(n+m)**2)))


def grid_integral(a, n, m, mesh=800):
    """Composite trapezoid on [0, pi]^2, independent of closed form."""
    dt = PI / mesh
    csn = [math.cos(n*j*dt) for j in range(mesh+1)]
    csm = [math.cos(m*j*dt) for j in range(mesh+1)]
    e = [math.exp(-a*j*dt) for j in range(mesh+1)]
    total = 0.
    for j in range(mesh+1):
        wj = .5 if j==0 or j==mesh else 1.
        term = 0.
        for k in range(mesh+1):
            wk = .5 if k==0 or k==mesh else 1.
            term += wk * e[max(j,k)] * csm[k]
        total += wj * csn[j] * term
    return total * dt**2 / PI**2


def sampled_coeff(a, n, m, side=16):
    """Exact finite-grid DFT evaluated by a direct real cosine sum."""
    cosn = [math.cos(2*PI*n*j/side) for j in range(side)]
    cosm = [math.cos(2*PI*m*j/side) for j in range(side)]
    distances = [2*PI*min(j,side-j)/side for j in range(side)]
    return sum(math.exp(-a*max(distances[j],distances[k])) * cosn[j] * cosm[k]
               for j in range(side) for k in range(side)) / side**2


def run():
    comparisons = 0
    worst = 0.
    for a in (0.4, 1., 2.):
        for n,m in ((0,0),(1,0),(2,0),(4,0),(1,1),(1,2),(2,3),(3,3)):
            diff = abs(grid_integral(a,n,m) - coefficient(a,n,m))
            worst = max(worst,diff)
            assert diff < 0.000018, (a,n,m,diff)
            comparisons += 1
        Q = 2*a*math.expm1(a*PI)/PI - a*a
        for n in range(2,1000,2):
            coeff = coefficient(a,n,0)
            assert (coeff < 0) == (n*n > Q), (a,n,coeff,Q)
            assert coefficient(a,n+1,0) > 0
        for n in range(1,13):
            for m in range(1,13):
                assert coefficient(a,n,m)>0
    a=1.
    for side in (16,32):
        z = sampled_coeff(a,4,0,side)
        assert z<0, (side,z)
        # Character is an eigenvector of any translation-invariant finite-grid Gram matrix.
        # For side 16 or 32 and frequency 4, ||cos(4x)||^2=side^2/2.
        qform = side**4/2 * z
        assert qform < 0
        print('grid',side,'normalized_fourier',f'{z:.14g}', 'negative_quadratic_form',f'{qform:.14g}')
    print('continuous Fourier vs direct quadrature comparisons',comparisons,'max_abs_error',worst)
    print('first negative axial mode for a=1: (4,0); Fourier coefficient',coefficient(1.,4,0))
    print('all checks passed')

if __name__ == '__main__':
    run()
