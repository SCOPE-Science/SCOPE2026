"""Finite numerical checks for the exact q numerical annuli of 2D antiunitaries.

Independent of any external paper or dataset. It checks witnesses and upper/lower
inequalities for representative parameters; the universal theorem uses a proof.
"""
import cmath
import math
import numpy as np

rng = np.random.default_rng(20261026)
J = np.array([[0., 1.], [-1., 0.]], dtype=complex)
K = np.eye(2, dtype=complex)
checks = 0

def alpha_beta(U, x):
    Ax = U @ x.conj()
    v = np.array([-x[1].conjugate(), x[0].conjugate()])
    return np.vdot(x, Ax), np.vdot(v, Ax), Ax, v

for b in (0, 0.13, 0.4, 1/math.sqrt(2), 0.88, 1.0):
    a = math.sqrt(1-b*b)
    U = a*K+b*J
    for q in (0., 0.07, 0.25, 0.55, 1/math.sqrt(2), 0.94, 1.):
        t = math.sqrt(max(0., 1-q*q))
        inner = max(0., b*t-a*q)
        outer = 1.0 if q<=a else a*q+b*t
        assert inner<=outer+1e-12
        # Search the two continuously-variable exact extremal witnesses.
        for target,kind in ((min(a,q),'outer'),(min(a,t),'inner')):
            u = 0.5*math.acos(min(1., max(-1.,target/a))) if a>0 else 0.
            x = np.array([math.cos(u),1j*math.sin(u)])
            al,be,Ax,v=alpha_beta(U,x)
            assert abs(abs(al)-target)<1e-12
            theta = cmath.phase(be)-cmath.phase(al)
            if kind=='inner':
                theta += math.pi
            y = q*x+t*cmath.exp(1j*theta)*v
            attained = abs(np.vdot(y,Ax))
            expected = outer if kind=='outer' else inner
            assert abs(attained-expected)<1e-10, (b,q,kind,attained,expected)
            assert abs(np.vdot(x,y)-q)<1e-12
            checks+=2
        for _ in range(300):
            x = rng.normal(size=2)+1j*rng.normal(size=2)
            x /= np.linalg.norm(x)
            al,be,Ax,v=alpha_beta(U,x)
            assert abs(np.vdot(x,v))<1e-12
            phi=rng.uniform(0,2*math.pi)
            y=q*x+t*cmath.exp(1j*phi)*v
            assert abs(np.linalg.norm(y)-1)<1e-12
            assert abs(np.vdot(x,y)-q)<1e-12
            z=np.vdot(y,Ax)
            assert inner-1e-10<=abs(z)<=outer+1e-10, (b,q,z,inner,outer)
            checks+=1
        # Check invariant trace(A^2)=2-4b^2.
        assert abs(np.trace(U@U.conj()).real-(2-4*b*b))<1e-12
        checks+=1
        # Verify unitary conjugacy leaves the range unchanged in selected samples.
        Z=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
        Q,R=np.linalg.qr(Z)
        Q=Q@np.diag(np.exp(-1j*np.angle(np.diag(R))))
        U2=Q@U@Q.T
        for _ in range(4):
            x=rng.normal(size=2)+1j*rng.normal(size=2)
            x/=np.linalg.norm(x)
            _,_,Ax,v=alpha_beta(U,x)
            phi=rng.uniform(0,2*math.pi)
            y=q*x+t*cmath.exp(1j*phi)*v
            z=np.vdot(y,Ax)
            assert abs(z-np.vdot(Q@y,U2@(Q@x).conj()))<1e-11
            checks+=1
print(f'PASS: {checks} deterministic finite checks over 42 parameter pairs; analytic proof required for universality.')
