"""Reproduce the rank-nesting covariance counterexample using analytical jets.

Python 3, NumPy, SciPy, and SymPy. The sufficiently-small-time conclusions are proved in RESULT.md, not inferred from finite tests.
"""
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp


def symbolic_checks():
    a, b = s.symbols('a b', positive=True)
    q11, q22, q33, q12, q13, q23 = s.symbols(
        'q11 q22 q33 q12 q13 q23', real=True)
    Q = s.Matrix([[q11, q12, q13], [q12, q22, q23], [q13, q23, q33]])
    P1, P2 = s.diag(1, 0, 0), s.diag(1, 1, 0)
    dP1 = s.Matrix([[0, q12/a, q13/a],
                    [q12/a, 0, 0], [q13/a, 0, 0]])
    dP2 = s.Matrix([[0, 0, q13/a],
                    [0, 0, q23/b], [q13/a, q23/b, 0]])
    def field(P):
        return P*Q+Q*P-P*Q*P
    def accel(P,dP):
        return s.simplify(dP*Q+Q*dP-dP*Q*P-P*Q*dP)
    D0 = s.diag(0,b,0)
    D1 = s.simplify(field(P2)-field(P1))
    D2 = s.simplify((accel(P2,dP2)-accel(P1,dP1))/2)
    assert D1 == s.Matrix([[0,0,0],[0,q22,q23],[0,q23,0]])
    assert s.simplify(D2[0,0]) == 0
    assert s.simplify(D2[0,2]+q12*q23/(2*a)) == 0
    assert s.simplify(D2[2,2]-q23**2/b) == 0
    z = s.Matrix([1,0,b*q12/(2*a*q23)])
    assert s.simplify((z.T*D0*z)[0]) == 0
    assert s.simplify((z.T*D1*z)[0]) == 0
    assert s.simplify((z.T*D2*z)[0]+b*q12**2/(4*a**2)) == 0
    assert s.simplify((z.T*D2*z)[0].subs({a:3,b:2,q12:1,q23:1})+s.Rational(1,18)) == 0
    # For symmetric Q and P=P^T=P^2, this residual is PSD for Q PSD.
    I = s.eye(3)
    assert s.simplify(Q-field(P1)-(I-P1)*Q*(I-P1)) == s.zeros(3)
    assert s.simplify(Q-field(P2)-(I-P2)*Q*(I-P2)) == s.zeros(3)
    return 11


def rhs(t, x, rank, Q):
    Y=x.reshape((3,3));Y=(Y+Y.T)/2
    eig,U=np.linalg.eigh(Y)
    P=U[:,-rank:]@U[:,-rank:].T
    return (P@Q+Q@P-P@Q@P).reshape(-1)


def numerical_checks():
    Q=np.ones((3,3)); X0=np.diag([3.,2.,1.]);z=np.array([1.,0.,1/3]); checks=0
    for h in (.002, .005, .01, .02, .05, .1):
        pred=[]
        for rank in (1,2):
            Y0=np.diag([3.,2. if rank==2 else 0.,0.])
            result=solve_ivp(rhs, (0.,h), Y0.reshape(-1), args=(rank,Q),
                             rtol=2e-11, atol=3e-13, method='DOP853')
            assert result.success
            Y=result.y[:,-1].reshape((3,3));Y=(Y+Y.T)/2
            vals=np.linalg.eigvalsh(Y)
            assert vals[0] > -1e-9
            assert np.linalg.eigvalsh(X0+h*Q-Y)[0] > -1e-9
            assert np.trace(Y0)-1e-10 <= np.trace(Y) <= np.trace(Y0)+h*np.trace(Q)+1e-9
            checks += 3
            pred.append(Y)
        D=pred[1]-pred[0]
        eig=np.linalg.eigvalsh(D)
        assert eig[0] < 0. and eig[-1] > 0.
        assert z@D@z < 0.
        assert abs((z@D@z)/h**2+1/18) < 2e-3
        checks += 3
    return checks

if __name__=='__main__':
    nc=symbolic_checks();nn=numerical_checks()
    print(f'PASS: {nc} symbolic identities; {nn} numerical assertions')
