"""Standalone finite checks for the radial polyanalytic Bergman boundary-layer formula.
Scientific tests only: numerical tests are not proofs of the limiting statement.
Requires numpy. Run: python checker.py
"""
import math
import numpy as np


def jacobi_x(beta, alpha, width):
    """Multiplication by x=1-t in the orthonormal Jacobi polynomial basis.
    Scalar measure proportional to x**alpha*(1-x)**beta dx on (0,1).
    Polynomial basis has positive value at x=0.
    """
    M = np.zeros((width, width))
    for j in range(width):
        if j == 0:
            M[j, j] = (alpha+1)/(alpha+beta+2)
        else:
            den = (2*j+alpha+beta)*(2*j+alpha+beta+2)
            M[j,j] = 0.5*(1+(alpha**2-beta**2)/den)
        if j+1 < width:
            t = (j+1)*(j+alpha+1)*(j+beta+1)*(j+alpha+beta+1)
            den = (2*j+alpha+beta+2)*math.sqrt(
                (2*j+alpha+beta+1)*(2*j+alpha+beta+3))
            M[j,j+1] = M[j+1,j] = -math.sqrt(t)/den
    return M


def laguerre_x(alpha, width):
    """Multiplication by x in the Laguerre ONB of x**alpha exp(-x) dx."""
    M = np.zeros((width, width))
    for j in range(width):
        M[j,j] = 2*j+alpha+1
        if j+1 < width:
            M[j,j+1] = M[j+1,j] = -math.sqrt((j+1)*(j+alpha+1))
    return M


def g2(alpha, power):
    """Closed form of limiting 2-by-2 Gram matrix for a power-law symbol."""
    A = math.gamma(alpha+power+1)/math.gamma(alpha+1)
    return A*np.array([[1, -power/math.sqrt(alpha+1)],
                       [-power/math.sqrt(alpha+1), 1+power*(power+1)/(alpha+1)]])


def run():
    tests=0
    for alpha in [0.0,0.5,1.0,2.5]:
      for q in [1,2,3,4]:
        for power in [1,2,3]:
          width=q+power+1
          target=(np.linalg.matrix_power(laguerre_x(alpha,width),power))[:q,:q]
          ev=np.linalg.eigvalsh(target)
          assert min(ev)>0
          tests+=1
          for beta in [300,1200,4000]:
            finite=(np.linalg.matrix_power(beta*jacobi_x(beta,alpha,width),power))[:q,:q]
            dev=np.max(np.abs(finite-target))
            bound=500*(1+alpha+q+power)**(power+2)/beta
            assert dev < bound, (alpha,q,power,beta,dev,bound)
            tests+=1
          if power==1:
            target_trace=q*(q+alpha)
            assert abs(np.trace(target)-target_trace)<1e-10
            tests+=1
          if q==2:
            assert np.max(np.abs(target-g2(alpha,power)))<1e-8
            tests+=1
    # q=2 first-order Laguerre zeros: trace and determinant of the 2x2 Jacobi matrix.
    for alpha in [0.0,0.3,1.0,2.0,5.0]:
       J=laguerre_x(alpha,2)
       eig=np.linalg.eigvalsh(J)
       assert abs(sum(eig)-2*(alpha+2))<1e-12
       assert abs(np.prod(eig)-(alpha+1)*(alpha+2))<1e-12
       tests+=2
    print(f"PASS: {tests} numerical checks; limits follow from the analytic proof, not these samples")


if __name__ == '__main__':
    run()
