"""Independent finite-dimensional diagnostics for endpoint-weighted shifts.
Requires NumPy and SciPy. Infinite asymptotics are proved analytically, not by this code.
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import minimize_scalar


def largest_norm(n, weights, t):
    diagonal = np.concatenate(([t*t], t*t + weights**2))
    eig = eigh_tridiagonal(diagonal, t*weights, select='i',
                           select_range=(n-1, n-1), check_finite=False)[0][0]
    return math.sqrt(eig)


def qradius(n, weights, c):
    if c == 0:
        return eigh_tridiagonal(np.zeros(n), weights/2, select='i',
              select_range=(n-1,n-1), check_finite=False)[0][0]
    q = 1-c/n**2
    if not (0 <= q <= 1):
        raise ValueError('parameter outside q range')
    f = lambda t: largest_norm(n,weights,t)-q*t
    solution = minimize_scalar(f,method='bounded',bounds=(0,math.pi**2/c),
                               options={'xatol':1e-11})
    return min(1.0,solution.fun)


def run():
    assertions=0
    for k in (0,1,2,3):
        for n in (32,64,128):
            weights = np.ones(n-1)
            if k:
                weights[:k] = [.07,.36,.9][:k]
                weights[-k:] = [.2,.68,.1][:k]
            for t in (0, .125,1,4,16):
                lower = math.sqrt(1+t*t+2*t*math.cos(math.pi/(n-2*k)))
                upper = math.sqrt(1+t*t+2*t*math.cos(math.pi/(n+1)))
                actual = largest_norm(n,weights,t)
                assert lower-1e-11 <= actual <=upper+1e-11
                assertions+=1
            for c in (0,.3,1,2,3,4,4.93,5,6):
                radius=qradius(n,weights,c)
                scaled=n*n*(1-radius)
                target=max(math.pi/math.sqrt(2)-math.sqrt(c),0)**2
                assert -.00001 <= scaled <= 5.0+4*(k+1)
                assert abs(scaled-target) <= 50*(k+1)/n
                assertions+=2
    print('PASS: %d finite numerical assertions' % assertions)

if __name__=='__main__':run()
