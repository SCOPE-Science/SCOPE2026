"""Reproducible finite-slab polar-feedback checks (NumPy/SciPy).

This tests algebraic consequences and discretized spectra, not a proof of the
infinite-dimensional spectral or uniqueness statements.
"""
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from scipy.linalg import eigvals

CHECKS = 0


def verify(condition, message):
    global CHECKS
    if not condition:
        raise AssertionError(message)
    CHECKS += 1


def coth(x):
    return 1.0 / math.tanh(x)


def F(q, Dr, Dt, Dc, kappa, H):
    return (Dt + Dr / q**2) * (kappa + Dc * q * coth(H*q))


def t(y):
    return y * coth(y)


def dt(y):
    return coth(y) - y / math.sinh(y)**2 if y < 350 else 1.0


def B(y, u):
    ty = t(y)
    dty = dt(y)
    return u*y**3*dty/(2 + u*(2*ty-y*dty))


def response(s, q, Dc, kappa, H):
    r = np.sqrt(q*q + complex(s)/Dc)
    return 1.0/(kappa+Dc*r/np.tanh(H*r))


def growth_root(q, G, Dr, Dt, Dc, kappa, H):
    a = Dr+Dt*q*q
    fun = lambda s: (s+a-G*q*q*response(s,q,Dc,kappa,H)).real
    return brentq(fun,-0.1, max(10.,G*q*q)) if fun(0.) < 0 else None


def finite_volume_matrix(n, q, G, Dr, Dt, Dc, kappa, H):
    # Choose b=f=q*sqrt(G), so b*f=G*q^2. Both physically positive.
    b = q*math.sqrt(G)
    f = q*math.sqrt(G)
    dz=H/n
    norm = 1 + kappa*dz/(2*Dc)
    L=np.zeros((n+1,n+1),dtype=float)
    L[0,0]=-(Dr+Dt*q*q)+b*f*dz/(2*Dc*norm)
    L[0,1]=b/norm
    L[1,0]=f/(dz*norm)
    L[1,1]=-Dc/dz**2-kappa/(dz*norm)-Dc*q*q
    L[1,2]=Dc/dz**2
    for j in range(2,n):
        L[j,j-1]=Dc/dz**2
        L[j,j]=-2*Dc/dz**2-Dc*q*q
        L[j,j+1]=Dc/dz**2
    L[n,n-1]=Dc/dz**2
    L[n,n]=-3*Dc/dz**2-Dc*q*q
    return L


def main():
    for Dr in [0.02, 0.2, 1., 10.]:
        for Dt, Dc, H, kappa in [(1.,1.,1.,1.),(0.7,3.,2.,0.2),(2.,0.6,0.5,3.)]:
            u=Dc/(kappa*H)
            beta=Dr*H*H/Dt
            y=brentq(lambda z: B(z,u)-beta, 1e-5, max(100.,100*math.sqrt(beta)))
            qstar=y/H
            opt=minimize_scalar(lambda q:F(q,Dr,Dt,Dc,kappa,H),bounds=(qstar/3,3*qstar),method='bounded',options={'xatol':1e-12})
            verify(abs(opt.x-qstar)<1e-5*max(1,qstar),'B equation versus minimization')
            verify(F(qstar*.5,Dr,Dt,Dc,kappa,H)>F(qstar,Dr,Dt,Dc,kappa,H),'left of minimum')
            verify(F(qstar*2,Dr,Dt,Dc,kappa,H)>F(qstar,Dr,Dt,Dc,kappa,H),'right of minimum')
            for alpha in [.2,.5,1.,2.,5.]:
                verify(B(alpha*y,u)>B(alpha*y*.999,u),'B strictly increasing locally')
            q=qstar
            Gc=F(q,Dr,Dt,Dc,kappa,H)
            if Gc*1.2>0:
                root=growth_root(q,1.2*Gc,Dr,Dt,Dc,kappa,H)
                verify(root is not None and root>0,'unstable root exists')
                for s in [0.,root,1+2j,0.5+4j]:
                    z=response(s,q,Dc,kappa,H)
                    verify(z.real>0,'positive real transfer')
                    if complex(s).imag>0:
                        verify(z.imag<0,'Stieltjes imaginary sign')
    # Small angular diffusion: quarter-root mode and square-root threshold.
    for dr in [1e-2,1e-3,1e-4,1e-5,1e-6]:
        q0=brentq(lambda q:B(q,1.)-dr,1e-7,10.)
        quas=(6*dr)**.25
        Gc=F(q0,dr,1.,1.,1.,1.)
        Gas=2+2*math.sqrt(2*dr/3)
        verify(abs(q0/quas-1)<0.2,'quarter-root asymptotics')
        verify(abs((Gc-2)/(Gas-2)-1)<0.2,'square-root threshold')
    # Compare continuous resolvent growth rate to actual 1D bulk finite-volume generator.
    q=1.72
    Gc=F(q,1.,1.,1.,1.,1.)
    for mult in [.7, .95, 1.05, 1.4]:
        G=mult*Gc
        lambdas=[]
        for n in [25,50,100]:
            ev=eigvals(finite_volume_matrix(n,q,G,1.,1.,1.,1.,1.))
            verify(np.max(np.abs(ev.imag))<1e-6,'real eigenvalues of symmetrizable bulk-polar generator')
            lead=ev.real.max()
            lambdas.append(lead)
            verify((lead>0)==(mult>1.),'same threshold sign finite volume')
        verify(abs(lambdas[-1]-lambdas[-2])<0.004,'finite-volume convergence')
        if mult>1.:
            root=growth_root(q,G,1.,1.,1.,1.,1.)
            verify(abs(lambdas[-1]-root)<0.003,'growth root matches finite-volume eigenvalue')
    print('PASS',CHECKS,'deterministic checks')

if __name__=='__main__':
    main()
