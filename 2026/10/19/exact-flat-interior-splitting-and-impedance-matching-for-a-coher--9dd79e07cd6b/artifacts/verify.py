#!/usr/bin/env python3
"""Independent finite-dimensional checks for the two-terminal coherent absorption theorem."""
from fractions import Fraction
import numpy as np
from scipy.linalg import solve_continuous_lyapunov


def expected(n, hopping, left, right):
    j, a, b = hopping, left, right
    denom = (a + b) * (a*b + 4*j*j)
    d0 = a*(a*b + b*b + 4*j*j)/denom
    di = a*(b*b + 4*j*j)/denom
    dn = 4*a*j*j/denom
    c = 2*a*b*j/denom
    e = np.diag(np.array([d0] + [di]*(n-2) + [dn], dtype=complex))
    for k in range(n-1):
        e[k,k+1] = -1j*c
        e[k+1,k] = 1j*c
    return e


def direct(n, hopping, left, right):
    h = hopping*(np.diag(np.ones(n-1),1) + np.diag(np.ones(n-1),-1))
    a = -1j*h
    a[0,0] -= left/2
    a[-1,-1] -= right/2
    qleft = np.zeros((n,n),complex)
    qright = np.zeros((n,n),complex)
    qleft[0,0] = left
    qright[-1,-1] = right
    el = solve_continuous_lyapunov(a.conj().T,-qleft)
    er = solve_continuous_lyapunov(a.conj().T,-qright)
    return a,el,er,qleft,qright


def exact_boundary_relations(j,a,b):
    """Use exact Fraction arithmetic, independent of numerical matrix solvers."""
    den=(a+b)*(a*b+4*j*j)
    di=a*(b*b+4*j*j)/den
    d0=a*(a*b+b*b+4*j*j)/den
    dn=4*a*j*j/den
    c=2*a*b*j/den
    checks=[a*d0+2*j*c==a, b*dn==2*j*c,
            j*(di-d0)+a*c/2==0,
            j*(dn-di)+b*c/2==0,
            j*(dn-d0)+(a+b)*c/2==0]
    assert all(checks), (j,a,b,checks)
    p=di
    optimum=(b*b+4*j*j)/(b+2*j)**2
    at=2*j
    assert at*(b*b+4*j*j)/((at+b)*(at*b+4*j*j))==optimum
    return len(checks)+1


def main():
    numerical=0
    rational=0
    for n in range(2,12):
        for hop,left,right in [(1.,1.,3.),(2.,.5,4.),(.75,7.,.4),
                               (1.,2.,2.),(1.,.17,.29),(.5,3.,.9)]:
            g,el,er,ql,qr=direct(n,hop,left,right)
            ex=expected(n,hop,left,right)
            assert np.max(abs(el-ex))<3e-10,(n,hop,left,right,'effect')
            assert np.max(abs(g.conj().T@ex+ex@g+ql))<3e-10
            assert np.max(abs(el+er-np.eye(n)))<3e-10
            assert np.min(np.linalg.eigvalsh(el))>-3e-10
            assert np.min(np.linalg.eigvalsh(er))>-3e-10
            if n>=3 and left==right:
                assert np.max(abs(np.diag(el)[1:-1]-.5))<3e-10
            numerical+=5+(n>=3 and left==right)
    for j,a,b in [(Fraction(1),Fraction(2),Fraction(3)),
                  (Fraction(2,3),Fraction(3,2),Fraction(7,5)),
                  (Fraction(5,4),Fraction(1,7),Fraction(23,11)),
                  (Fraction(3,5),Fraction(11,13),Fraction(31,2))]:
        rational+=exact_boundary_relations(j,a,b)
    print(f'VERIFY_OK {numerical} matrix/effect checks + {rational} exact rational identities')

if __name__=='__main__':
    main()
