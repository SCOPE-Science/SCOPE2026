#!/usr/bin/env python3
"""Numerical checks for exact graph-Gram spectral-equivalence theorem.
The mathematical argument in RESULT.md is independent of these checks.
"""
import numpy as np


def rho_bound(epsilon, tau):
    phi = (np.sqrt(4.0 + epsilon*epsilon) + epsilon)/2.0
    return max(abs(1.0-tau*phi**2), abs(1.0-tau/phi**2))


def main():
    rng=np.random.default_rng(1199027)
    checks=0
    for n in (1,2,3,5):
        for k in (1,3,6):
            for epsilon in (0.01,0.1,0.5,1.0,2.0,4.0):
                phi=(np.sqrt(epsilon**2+4)+epsilon)/2
                for _ in range(70):
                    Y=rng.standard_normal((k,n))*rng.choice([0.2,1.0,4.0])
                    E=rng.standard_normal((k,n))
                    E*=epsilon/np.linalg.norm(E,ord=2)
                    W=Y+E
                    C=np.eye(n)+Y.T@Y
                    M=np.eye(n)+W.T@W
                    lambdas=np.linalg.eigvalsh(np.linalg.solve(np.linalg.cholesky(M),C)@np.linalg.inv(np.linalg.cholesky(M).T))
                    assert lambdas.min() >=phi**-2-1e-10,(lambdas,epsilon)
                    assert lambdas.max() <=phi**2+1e-10,(lambdas,epsilon)
                    opttau=2/(epsilon**2+2)
                    contraction=np.max(np.abs(1-opttau*lambdas))
                    assert contraction <=rho_bound(epsilon,opttau)+1e-10
                    checks+=3
    for epsilon in (0.01,0.1,0.5,1.0,2.0,4.0):
        phi=(np.sqrt(epsilon**2+4)+epsilon)/2
        Y=np.diag([phi,1/phi]);W=np.diag([1/phi,phi])
        assert abs(np.linalg.norm(Y-W,2)-epsilon)<1e-12
        C=np.eye(2)+Y.T@Y;M=np.eye(2)+W.T@W
        vals=np.linalg.eigvalsh(np.linalg.solve(M,C))
        assert np.allclose(vals,[phi**-2,phi**2],atol=1e-12)
        assert abs(vals[-1]/vals[0]-phi**4)<1e-10
        tau=2/(epsilon*epsilon+2)
        assert np.allclose(np.abs(1-tau*vals),[rho_bound(epsilon,tau)]*2,atol=1e-12)
        checks+=4
    for a in (0.5,1.0,3.0):
        for delta in (-0.3,0.01,0.2):
            w=a+delta
            assert w>0
            R=2.0
            ystar=0.0
            def residual(y):return np.array([-a*R-y,R-a*y])
            def corrected(y):
                r=residual(y)
                z=r[0]+a*r[1]
                return z/(1+w*w)
            def original(y):
                r=residual(y)
                return (r[0]+w*r[1])/(1+w*w)
            assert abs(corrected(ystar))<1e-13
            assert abs(original(ystar)-delta*R/(1+w*w))<1e-13
            e=np.sign(delta)*abs(delta*R)/(2*(1+a*w))
            r=residual(e)
            z=r[0]+a*r[1]
            h=original(e)
            assert z*h<0
            f=lambda y:0.5*sum(residual(y)**2)
            assert f(e+h)>f(e)
            ybias=delta*R/(1+a*w)
            assert abs(original(ybias))<1e-12
            assert abs(f(ybias)-f(0.0)-0.5*(1+a*a)*ybias**2)<1e-11
            checks+=6
    print('PASSED',checks,'checks')

if __name__=='__main__': main()
