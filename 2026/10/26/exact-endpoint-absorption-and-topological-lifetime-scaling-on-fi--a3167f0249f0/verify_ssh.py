"""Independent finite-matrix checks for the lossy alternating chain result.

Run: python verify_ssh.py
Dependencies: numpy >= 1.23, scipy >= 1.9, sympy >= 1.11
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import solve_continuous_lyapunov


def chain(m, a, b):
    n = 2 * m
    h = np.zeros((n, n), dtype=float)
    for k in range(n - 1):
        h[k, k+1] = h[k+1, k] = a if k % 2 == 0 else b
    return h


def predicted(m, a, b, gamma):
    B = (m - 1) / b**2 + (b / a)**(2*(m-1)) / (2*a**2)
    return m/gamma + gamma*B


def independent_gramian(m, a, b, gamma):
    h=chain(m,a,b)
    A=-1j*h
    A[0,0] -= gamma
    q=solve_continuous_lyapunov(A.conj().T, -np.eye(2*m))
    residual=np.linalg.norm(A.conj().T@q + q@A + np.eye(2*m),ord=np.inf)
    return q[-1,-1].real, residual


def exact_lyapunov_check(m):
    a,b,g=sp.symbols('a b g', positive=True)
    n=2*m
    h=sp.zeros(n)
    for k in range(n-1):
        h[k,k+1]=h[k+1,k]=a if k%2==0 else b
    A=-sp.I*h-sp.diag(g,*([0]*(n-1)))
    x=sp.symbols('x:'+str(n*(n+1)//2), real=True)
    q=sp.zeros(n);z=0
    for i in range(n): q[i,i]=x[z];z+=1
    for i in range(n):
        for j in range(i+1,n):
            fac=sp.I if (j-i)%2 else 1
            q[i,j]=fac*x[z];q[j,i]=sp.conjugate(fac)*x[z];z+=1
    eq=A.conjugate().T*q+q*A+sp.eye(n)
    equations=[eq[i,i] for i in range(n)]+[eq[i,j]/(sp.I if (j-i)%2 else 1) for i in range(n) for j in range(i+1,n)]
    M,y=sp.linear_eq_to_matrix(equations,x)
    sol=M.inv()*y
    actual=sp.factor(sol[n-1]); expected=sp.Rational(m,1)/g+g*(sp.Rational(m-1,1)/b**2+b**(2*m-2)/(2*a**(2*m)))
    assert sp.cancel(actual-expected)==0,(m,actual,expected)


def run():
    checks=0; worst=0.0
    for m in range(1,11):
        for a,b in ((0.6,1.4),(1.3,0.7),(1.0,1.0),(1.8,1.2)):
            for gamma in (0.2, 0.8, 2.5):
                actual,residual=independent_gramian(m,a,b,gamma)
                expected=predicted(m,a,b,gamma)
                err=abs(actual-expected)/expected
                worst=max(worst,err)
                assert err<3e-7,(m,a,b,gamma,err)
                assert residual < 1e-7,(m,a,b,gamma,residual)
                checks+=2
    for m in (1,2,3):
        exact_lyapunov_check(m)
        checks+=1
    for m in range(1,12):
        for a,b in ((.7,1.4),(1.4,.7),(1.,1.)):
            h=chain(m,a,b)
            energies,u=np.linalg.eigh(h)
            assert np.all(np.diff(energies)>1e-10)
            alpha=sum((u[-1,j]/u[0,j])**2 for j in range(2*m))/2
            assert abs(alpha-m)<1e-6,(m,a,b,alpha)
            checks+=1
    print(f'PASS {checks} checks; worst relative numerical error {worst:.3g}')

if __name__=='__main__': run()
