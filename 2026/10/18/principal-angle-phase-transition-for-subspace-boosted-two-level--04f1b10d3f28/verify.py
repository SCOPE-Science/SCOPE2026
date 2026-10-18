"""Numerical cross-checks of two-level subspace-boost eigenvalues.

Requires numpy as declared in requirements.txt. No external data are needed.
"""
import math
import numpy as np


def extrema(contrast, theta, boost):
    c, s = math.cos(theta), math.sin(theta)
    trace = 1.0 + contrast + (boost-1.0)*(c*c+contrast*s*s)
    delta = math.sqrt(max(0.0, trace*trace-4.0*boost*contrast))
    return (trace-delta)/2.0, (trace+delta)/2.0


def check(contrast, angles):
    k = len(angles)
    d = 2*k
    a = np.diag([1.0]*k+[contrast]*k)
    a_half = np.diag([1.0]*k+[math.sqrt(contrast)]*k)
    basis = np.zeros((d,k))
    for i, theta in enumerate(angles):
        basis[i,i] = math.cos(theta)
        basis[k+i,i] = math.sin(theta)
    theta = max(angles)
    c2, s2 = math.cos(theta)**2, math.sin(theta)**2
    optimum = max(1.0, (contrast*c2+s2)/(c2+contrast*s2))
    lo_star, hi_star = extrema(contrast, theta, optimum)
    for boost in [1.0, optimum, 1.03*optimum, contrast, 5*contrast,
                  max(1.0, 0.95*optimum)]:
        inv_precond = np.eye(d)+(boost-1.0)*(basis@basis.T)
        matrix = a_half@inv_precond@a_half
        eigenvalues = np.linalg.eigvalsh(matrix)
        lo, hi = extrema(contrast, theta, boost)
        assert math.isclose(eigenvalues[0],lo,rel_tol=2e-11,abs_tol=1e-8)
        assert math.isclose(eigenvalues[-1],hi,rel_tol=2e-11,abs_tol=1e-8)
        assert hi/lo >= hi_star/lo_star-1e-9
    return optimum, hi_star/lo_star


def main():
    family = [[0.0],[math.pi/8],[math.pi/4],[math.pi/3],[math.pi/2],
              [0.0,0.15],[0.01,0.8],[0.1,0.2,0.3],
              [0.0,0.0,1.56],[0.2,0.5,0.9,1.2]]
    for contrast in [1.1,2.0,10.0,100.0,10000.0]:
        for angles in family:
            check(contrast, angles)
    print("PASS: 50 principal-angle configurations, 300 boost strengths")
    c = 2.0
    target = (math.sqrt(1.0+c*c)+c)**2
    for contrast in [100.0,1000.0,10000.0,1000000.0]:
        _, cond = check(contrast, [0.0,c/math.sqrt(contrast)])
        assert cond < target
    print("PASS: high-contrast critical-window convergence")


if __name__ == '__main__':
    main()
