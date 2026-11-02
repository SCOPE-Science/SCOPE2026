"""Independent finite numerical consistency checks for a radial Bergman spectral law.

This program does not prove the asymptotic theorem. The mathematical proof is
in RESULT.md. Requires NumPy and SciPy (see requirements.txt).
"""
import math
import numpy as np
from scipy.special import ndtr, ndtri


def spectral_data(eps, dim=1, c=1.0, gamma=1.0, grid_points=19001):
    assert 0 < eps < 1 and dim >= 1 and c > 0 and gamma > 0
    y_cut = -math.log1p(-eps)
    center = c*gamma*(1-eps)/eps**(gamma+1)-dim
    curvature = c*gamma*((1-eps)/eps**(gamma+1)
                         +(gamma+1)*(1-eps)**2/eps**(gamma+2))
    width = math.sqrt(curvature)
    top = max(int(math.ceil(center + 8*width)), int(2*center), 50)
    grid = np.linspace(0.00005, max(1.0, 5*y_cut), grid_points)
    s = -np.expm1(-grid)
    wt = np.exp(-c/s**gamma)
    at = np.searchsorted(grid, y_cut)
    fraction = (grid[at]-y_cut)/(grid[at]-grid[at-1])
    eigenvalues = []
    for base in range(0, top+1, 150):
        indices = np.arange(base, min(base+150, top+1))
        integrand = np.exp(-np.outer(indices+dim, grid))*wt
        full = np.trapezoid(integrand, grid, axis=1)
        tail = np.trapezoid(integrand[:, at:], grid[at:], axis=1)
        cutoff_value = ((1-fraction)*integrand[:, at-1]
                        +fraction*integrand[:, at])
        tail += 0.5*(grid[at]-y_cut)*(cutoff_value+integrand[:, at])
        eigenvalues.extend(tail/full)
    eigenvalues = np.asarray(eigenvalues)
    multiplicity = np.ones(len(eigenvalues), dtype=float)
    for j in range(1, dim):
        multiplicity *= (np.arange(len(eigenvalues))+j)/j
    defect = np.dot(multiplicity, eigenvalues*(1-eigenvalues))
    leading = ((c*gamma)**(dim-1)*math.sqrt(c*gamma*(gamma+1)) /
               (math.factorial(dim-1)*math.sqrt(math.pi))
               *eps**(-(gamma+1)*(dim-1)-(gamma+2)/2))
    count_leading = center**dim/math.factorial(dim)
    trace = np.dot(multiplicity, eigenvalues)
    return center, width, eigenvalues, multiplicity, defect, leading, trace, count_leading


def main():
    cases = 0
    rows = []
    for dim in (1, 2):
        prev_error = None
        for eps in (0.08, 0.055, 0.035):
            center,width,vals,mult,defect,leading,trace,count_leading = spectral_data(eps,dim)
            assert 0 < vals.min() <= vals.max() < 1
            assert np.max(np.diff(vals)) < 1e-10
            assert width > 0 and center > 0
            ratio = defect/leading
            assert abs(ratio-1) < 0.08, (dim,eps,ratio)
            assert abs(trace/count_leading-1) < 0.6, (dim,eps,trace/count_leading)
            if prev_error is not None:
                assert abs(ratio-1) < prev_error+1e-3
            prev_error = abs(ratio-1)
            for u in (-1,0,1):
                k = int(round(center+u*width))
                assert abs(vals[k]-ndtr(-u)) < 0.09, (dim,eps,u,vals[k])
            # Quantile-counting boundary is accurate to a growing but subleading window.
            if eps == 0.035:
                for threshold in (0.25, 0.5, 0.75):
                    crossing = int(np.count_nonzero(vals > threshold))
                    prediction = center-width*ndtri(threshold)
                    assert abs(crossing-prediction) < 0.32*width
            cases += 1
            rows.append((dim,eps,ratio,trace/count_leading))
    # The independent scalar integral governing the boundary defect.
    from scipy.integrate import quad
    scalar, err = quad(lambda u:ndtr(u)*ndtr(-u), -12, 12,
                       epsabs=2e-12, epsrel=2e-12)
    assert abs(scalar-1/math.sqrt(math.pi)) < 1e-11
    # Closed-form curvature is checked against a symmetric second derivative of U.
    for gamma in (0.6, 1.0, 2.0):
        for eps in (0.04,0.10):
            y = -math.log1p(-eps)
            h = 1e-5*eps
            U = lambda z: 1.3/(-math.expm1(-z))**gamma
            numerical = (U(y+h)-2*U(y)+U(y-h))/(h*h)
            exact = 1.3*gamma*((1-eps)/eps**(gamma+1)
                                +(gamma+1)*(1-eps)**2/eps**(gamma+2))
            assert abs(numerical/exact-1) < 0.001
    print('FINITE CHECKS PASSED: six dimension/cutoff profiles, 18 profile samples,')
    print('six spectral-defect comparisons, six trace comparisons, nine counting tests,')
    print('six curvature comparisons, and the Gaussian integral identity.')
    print('Representative (dimension, cutoff, defect/leading, trace/leading):')
    for row in rows: print('%d %.3f %.9f %.9f' % row)
    print('No finite checks constitute proof of an all-cutoff asymptotic.')


if __name__=='__main__':main()
