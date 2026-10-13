"""Independent finite-dimensional checks for two discord-rounding families.

This script is corroborative; the theorem is established by the analytic proof.
"""
import math
import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1., -1.]).astype(complex)
P = [X, Y, Z]


def rho(kind, a, b, eps, t):
    q = math.exp(-t)
    if kind == 'local':
        mat = (np.kron(I,I)+a*q*q*np.kron(X,X)+b*np.kron(Z,Z)
               +eps*q*np.kron(X,I)+eps*np.kron(Z,I))/4
    elif kind == 'correlation':
        mat = (np.kron(I,I)+a*q*q*np.kron(X,X)+b*np.kron(Z,Z)
               +eps*q*(np.kron(X,Z)+np.kron(Z,X)))/4
    else:
        raise ValueError(kind)
    return mat


def exact(kind,a,b,eps,t):
    q = math.exp(-t)
    delta = a*a*q**4-b*b
    if kind == 'local':
        s = a*a*q**4+b*b+eps*eps*(q*q+1)
        gap=math.hypot(delta+eps*eps*(q*q-1), 2*eps*eps*q)
    else:
        s=a*a*q**4+b*b+2*eps*eps*q*q
        gap=math.hypot(delta, 2*eps*q*(a*q*q+b))
    return (s-gap)/8


def direct(kind,a,b,eps,t):
    m=rho(kind,a,b,eps,t)
    assert abs(np.trace(m)-1)<1e-12
    assert np.linalg.eigvalsh(m).min()>0, 'not a state'
    assert np.linalg.norm(m.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)-m)<1e-12, 'not PPT invariant'
    x=np.array([np.trace(m@np.kron(p,I)).real for p in P])
    T=np.array([[np.trace(m@np.kron(p,r)).real for r in P] for p in P])
    K=np.outer(x,x)+T@T.T
    return (np.dot(x,x)+np.sum(T*T)-np.linalg.eigvalsh(K)[-1])/4


def scaled_value(kind,a,b,eps,z):
    r=math.sqrt(b/a)
    t0=0.5*math.log(a/b)
    if kind=='local':
        tc=t0 +eps**2*(r*r-1)/(4*b*b)
        width=eps**2*r/(2*b*b)
    else:
        tc=t0
        width=eps*r/b
    t=tc+width*z
    return t, exact(kind,a,b,eps,t)


def derivative(kind,a,b,eps,t):
    h=min(1e-6, eps*eps/100) if kind=='local' else min(1e-6, eps/15)
    return (exact(kind,a,b,eps,t+h)-exact(kind,a,b,eps,t-h))/(2*h)


def main():
    a,b=0.31,0.13
    comparisons=0
    for kind in ('local','correlation'):
        for eps in (0.005,0.019,0.041):
            for t in (0,.10,.27,.435,.55,.91,1.8):
                d=direct(kind,a,b,eps,t)
                e=exact(kind,a,b,eps,t)
                assert abs(d-e)<2e-14, (kind,eps,t,d,e)
                comparisons+=1
        for eps in (0.0002,0.0005,0.001) if kind=='local' else (0.000002,0.000005,0.00001):
            for z in (-3.,-1.,0.,1.,3.):
                t,d=scaled_value(kind,a,b,eps,z)
                normalized=derivative(kind,a,b,eps,t)/(-b*b)
                predicted=(1+z/math.sqrt(1+z*z))/2
                tol=(1e-3 if kind=='local' else 2e-3)
                assert abs(normalized-predicted)<max(tol,6e-4), (kind,eps,z,normalized,predicted)
    print('VERIFY_OK direct_state_matrix='+str(comparisons)+' PPT_invariant=passed local_quadratic=passed correlation_linear=passed universal_slope=passed')

if __name__=='__main__':
    main()
