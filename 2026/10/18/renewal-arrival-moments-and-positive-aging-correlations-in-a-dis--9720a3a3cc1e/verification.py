"""Finite checks of renewal mass and its Hausdorff moment representation.
Analytic arguments, not this script, establish infinite-sequence statements.
"""
import math
import mpmath as mp


def sequence(q, lam, nmax):
    # D(z)=(1-z)^q+lam*(1-z); U(z)-1=lam*z/D(z).
    q, lam = mp.mpf(q), mp.mpf(lam)
    d = [1+lam, -q-lam]
    for k in range(2,nmax+1):
        d.append((-1)**k*mp.binomial(q,k))
    u=[mp.mpf(1)]
    for n in range(1,nmax+1):
        rhs=lam if n==1 else mp.mpf(0)
        rhs-=sum(d[k]*u[n-k] for k in range(1,n))
        u.append(rhs/d[0])
    return u


def spectral_w(q,lam,x):
    q,lam=mp.mpf(q),mp.mpf(lam)
    return (lam*mp.sin(mp.pi*q)/mp.pi)*x**(-q)/(1-2*lam*x**(1-q)*mp.cos(mp.pi*q)+(lam*x**(1-q))**2)


def spectral_u(q,lam,n):
    q,lam=mp.mpf(q),mp.mpf(lam)
    # x=y**(1/(1-q)) cancels the integrable singularity at zero.
    f=lambda y: (lam*mp.sin(mp.pi*q)/(mp.pi*(1-q)))/(1+y**(1/(1-q)))**n/(1-2*lam*y*mp.cos(mp.pi*q)+(lam*y)**2)
    return mp.quad(f,[0,mp.mpf('0.1'),1,10,mp.inf])


def check():
    mp.mp.dps=38
    checks=0
    for q,lam in [('0.25','0.4'),('0.5','0.7'),('0.8','0.9'),('0.35','1.4')]:
        u=sequence(q,lam,14)
        for n in range(1,9):
            sp=spectral_u(q,lam,n)
            assert abs(sp-u[n])<mp.mpf('1e-18'),(q,lam,n,sp,u[n])
            checks+=1
        assert abs(spectral_u(q,lam,0)-1)<mp.mpf('1e-18')
        checks+=1
        for start in range(0,9):
            for k in range(0,5):
                difference=sum((-1)**j*mp.binomial(k,j)*u[start+j] for j in range(k+1))
                assert difference>0,(q,lam,start,k,difference)
                checks+=1
        for s in range(2,12):
            for t in range(1,s):
                cov=u[t]*(u[s-t]-u[s])
                assert cov>0
                checks+=1
    print('PASS',checks,'spectral, recurrence, finite-difference and renewal covariance checks')

if __name__=='__main__':check()
