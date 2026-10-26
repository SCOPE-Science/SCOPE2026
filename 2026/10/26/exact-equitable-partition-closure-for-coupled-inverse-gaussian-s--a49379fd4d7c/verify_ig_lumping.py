"""Exact rational checks of aggregated multitype inverse-Gaussian Laplace equations."""
import sympy as s
from itertools import product

def check():
    B=s.Matrix([[3,-1,-s.Rational(1,2),0],[-1,3,0,-s.Rational(1,2)],[-s.Rational(1,4),0,2,-s.Rational(1,2)],[0,-s.Rational(1,4),-s.Rational(1,2),2]])
    P=s.Matrix([[1,0],[1,0],[0,1],[0,1]])
    C=s.Matrix([[2,-s.Rational(1,2)],[-s.Rational(1,4),s.Rational(3,2)]])
    assert B.T*P==P*C.T
    assert all(x >= 0 for x in B.inv())
    assert all(x >= 0 for x in C.inv())
    for a,b in product([s.Rational(k,3) for k in range(4)], repeat=2):
        w=s.Matrix([a,b]);u=C.T*w+s.Matrix([w[0]**2,w[1]**2])/2
        q=P*w
        assert B.T*q+s.Matrix([v*v for v in q])/2 == P*u
    T=s.Matrix([[2,-1],[-1,2]])
    A=T.inv(); eta=s.Matrix([1,1]); mean=A*eta
    v=A.row(0).T
    k1=mean[0]
    k2=sum(mean[i]*v[i]**2 for i in range(2))
    w=A.T*s.Matrix([v[i]**2 for i in range(2)])
    k3=3*sum(mean[i]*v[i]*w[i] for i in range(2))
    assert (k1,k2,k3)==(1,s.Rational(5,9),s.Rational(8,9))
    assert k3 != 3*k2*k2/k1
    covariance=A*s.diag(*mean)*A.T
    assert covariance[0,1]==s.Rational(4,9)
    assert T.T*s.ones(2,1)==s.ones(2,1)
    print('PASS 16 rational quadratic checks; exact equitable identities; nonnegative inverses; cumulant separation and covariance')
if __name__=='__main__':check()
