"""Reproducible quadrature tests for eccentric Fock annulus spectral cusp.
Only scientific computations; independent mathematical reasoning is in RESULT.md.
"""
import math
import numpy as np
from scipy.special import gammainc, gamma, gammaln


def radii(k, width):
    a = width / np.expm1(width / k)
    return a, a + width


def prediction(k, width, tau, delta):
    a, b = radii(k, width)
    C = a**k * np.exp(-a)
    alpha = C * (1/b - 1/a) / math.factorial(k-1)
    gam = C/math.sqrt(math.factorial(k-1)*math.factorial(k))
    from scipy.special import gammainc
    lam = gammainc(k,b)-gammainc(k,a)
    return lam + alpha*tau/2 + np.sqrt((alpha*tau/2)**2+(gam*abs(delta))**2), (lam,alpha,gam)


def matrix(k, width, tau, delta, dim=12, ntheta=2048):
    a,b=radii(k,width);a+=tau;b+=tau
    if abs(delta) >= (math.sqrt(b)-math.sqrt(a)):
        raise ValueError('outer circle does not contain inner circle')
    t=np.arange(ntheta)*2*np.pi/ntheta
    outer_t = (delta*np.cos(t)+np.sqrt(b-delta**2*np.sin(t)**2))**2
    mat=np.zeros((dim,dim), dtype=np.complex128)
    for m in range(dim):
        for n in range(m,dim):
            s=1+(m+n)/2
            # lower incomplete gamma difference
            d=gamma(s)*(gammainc(s,outer_t)-gammainc(s,a))
            z=np.mean(d*np.exp(1j*(n-m)*t)) /math.sqrt(math.factorial(m)*math.factorial(n))
            mat[m,n]=z;mat[n,m]=z.conjugate()
    return mat


def run():
    count=0
    for k in [1,2,3,4]:
        for width in [0.7, 1.3, 2.0]:
            a,b=radii(k,width)
            m=matrix(k,width,0,0,dim=max(14,k+6),ntheta=128)
            diag=np.real(np.diag(m))
            assert abs(diag[k]-diag[k-1])<5e-13
            assert all(diag[k]>diag[j]+1e-8 for j in range(len(diag)) if j not in [k-1,k])
            count+=2
            # Conical law is verified by convergent errors, not taken as proof.
            errs=[]
            for eps in [0.05,0.025,0.0125]:
                tau=0.4*eps;delta=0.5*eps
                pred,_=prediction(k,width,tau,delta)
                actual=np.linalg.eigvalsh(matrix(k,width,tau,delta,dim=max(14,k+6),ntheta=512))[-1]
                errs.append(abs(actual-pred))
                assert abs(actual-pred)<10*eps*eps
                count+=1
            assert errs[-1]<errs[0]/8, (k,width,errs)
            count+=1
    # Directly differentiate off-diagonal matrix elements: independent of
    # eigenvalue perturbation tests and sensitive to boundary normalization.
    for k in range(1,6):
        for width in [0.8, 1.5]:
            eps=1e-5
            plus=matrix(k,width,0,eps,dim=k+4,ntheta=768)
            minus=matrix(k,width,0,-eps,dim=k+4,ntheta=768)
            derivative=(plus[k-1,k]-minus[k-1,k])/(2*eps)
            _,(_,_,g)=prediction(k,width,0,0)
            assert abs(derivative.real-g)<2e-8, (k,width,derivative,g)
            assert abs(derivative.imag)<1e-9
            count+=2
    print('PASS',count,'checks')
    for k in [1,2,3]:
        a,b=radii(k,1)
        _,(lam,alpha,gam)=prediction(k,1,0,0)
        print('k=',k,'a=',a,'b=',b,'lambda=',lam,'alpha=',alpha,'gamma=',gam)

if __name__=='__main__': run()
