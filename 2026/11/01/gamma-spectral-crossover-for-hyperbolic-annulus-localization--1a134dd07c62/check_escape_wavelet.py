"""Reproducibility checks for sharp escaping-annulus Bergman localization laws."""
import math
import numpy as np
from scipy.special import betainc, gammaln, gammainc, gamma

def beta_eigs(p,S,L,nmax):
    u=S/(1+S);v=(S+L)/(1+S+L)
    ks=np.arange(nmax+1,dtype=np.float64)
    if p==1:
        return v**(ks+1)-u**(ks+1)
    return betainc(ks+1,p,v)-betainc(ks+1,p,u)

def peak_index(p,S,L):
    logratio=math.log1p(L/(1+S))
    logbase=math.log1p(L/(S*(1+S+L)))
    H=p*logratio/logbase
    return H,math.floor(H)

def gamma_profile(p,c,rho):
    return gammainc(p,c)-gammainc(p,c/(1+rho))

N=0
for p in (.6,1.,2.,3.):
    for S,L in ((25,2),(75,2),(200,2),(40,40),(100,100),(250,250)):
        kmax=round(max(50*S, p*50*S))+200
        lam=beta_eigs(p,S,L,kmax)
        assert min(lam)>-3e-13
        H,k=peak_index(p,S,L)
        assert abs(np.argmax(lam)-k)<=1, (p,S,L,H,k,np.argmax(lam))
        N+=1
        assert abs(np.sum(lam)-p*L) < 4e-6, (p,S,L,np.sum(lam),p*L)
        N+=1
        if L/S<.1:
            lead=L/S * p**p*math.exp(-p)/gamma(p)
            assert abs(lam.max()/lead-1)<.30, (p,S,L,lam.max(),lead)
            N+=1
            hscoef=gamma(2*p+1)/(2**(2*p+1)*gamma(p)**2)
            assert abs(sum(lam*lam)/(L*L/S*hscoef)-1)<.40
            N+=1
        elif L==S:
            rho=1; cm=2*p*math.log(2)
            pred=gamma_profile(p,cm,rho)
            assert abs(lam.max()-pred)<.030, (p,S,lam.max(),pred)
            N+=1
            assert abs(k/S-cm)<.15, (p,S,k,cm)
            N+=1
# exact closed form p=1 and trace identity independent of quadrature
for S in (3.,10.,50.,300.):
    for L in (.5, 3., S):
        u=S/(1+S);v=(S+L)/(1+S+L)
        lam=beta_eigs(1,S,L,30000)
        assert abs(sum(lam)-L)<1e-9
        H,k=peak_index(1,S,L)
        assert k==int(np.argmax(lam))
        N+=2
print('PASS',N,'tests')

# Fractional Schatten powers and the macroscopic gamma-profile crossover.
from scipy.integrate import quad
for p in (1.,2.):
    for q in (.5,1.5,2.,3.):
        coeff=gamma(p*q+1)/(q**(p*q+1)*gamma(p)**q)
        for S in (150.,400.):
            L=2.
            lam=beta_eigs(p,S,L,int(45*S))
            est=np.sum(lam**q)*S**(q-1)/L**q
            assert abs(est/coeff-1)<.07, (p,q,S,est,coeff)
            N+=1
        def f(c):
            return gamma_profile(p,c,1.)**q
        integ=quad(f,0,100,epsabs=1e-10)[0]
        for S in (150.,400.):
            lam=beta_eigs(p,S,S,int(45*S))
            est=np.sum(lam**q)/S
            assert abs(est/integ-1)<.05, (p,q,S,est,integ)
            N+=1
print('PASS',N,'total assertions including Schatten tests')
