"""Supplementary numerical tests for the Bergman localization shape expansion.

Run: python verify.py  (requires numpy and scipy).
The analytical theorem is not inferred from finite-dimensional tests.
"""
import math
import numpy as np
from scipy.special import gammaln, betainc, betaln
from scipy.linalg import eigvalsh


def w(n, c):
    return math.exp(math.lgamma(c+n+1)-math.lgamma(c+1)-math.lgamma(n+1))


def v(j, c):
    return math.exp(math.lgamma(c+j)-math.lgamma(c)-math.lgamma(j+1))


def S(n, c, T):
    return sum(v(j, c)*T**j for j in range(1, n+1))


def B(n, c, T):
    return c*(c+1)*(1-T)**(c+2)*(1-c*w(n,c)*T**n/((c+1)*S(n,c,T)))


def disk_eval(n, c, T):
    return float(betainc(n+1,c,T))


def top_eig(N, c, T, eps, mode, nt=1024):
    angle=2*np.pi*np.arange(nt)/nt
    x=T/(1-T)+eps*np.cos(mode*angle)
    t=x/(1+x)
    ns=np.arange(N)
    wn=np.exp(gammaln(c+ns+1)-gammaln(c+1)-gammaln(ns+1))
    a=np.empty((N,N), dtype=complex)
    for m in range(N):
        for n in range(m,N):
            p=(m+n)/2
            row=c*math.sqrt(wn[m]*wn[n])*math.exp(betaln(p+1,c))*betainc(p+1,c,t)
            z=np.mean(row*np.exp(1j*(n-m)*angle))
            a[m,n]=z
            a[n,m]=np.conj(z)
    return eigvalsh(a,subset_by_index=[N-1,N-1])[0]


def main():
    tests=0
    for c in (0.3,1.,2.5,5.):
        for T in (0.16,0.5,0.82):
            # Independent regularized-beta check of the negative-binomial identity.
            for n in range(13):
                v1=1-(1-T)**c*(1+S(n,c,T) if n else 1)
                assert abs(disk_eval(n,c,T)-v1)<2e-12
                tests+=1
            arr=[B(n,c,T) for n in range(1,13)]
            assert abs(arr[0]) < 2e-12
            assert min(np.diff(arr))>1e-10
            tests+=2
            exact=c*(c+1)*(1-T)**(c+2)*(2-T)/(2+(c+1)*T)
            assert abs(arr[1]-exact)<3e-13
            tests+=1
    for c,T in ((1.,.4),(.5,.7),(3.,.2)):
        for mode in (1,2,3,4):
            eps=0.004
            # Central second difference of the largest finite-section eigenvalue.
            base=disk_eval(0,c,T)
            plus=top_eig(14,c,T,eps,mode)
            minus=top_eig(14,c,T,-eps,mode)
            measured=(2*base-plus-minus)/(2*eps*eps)
            target=B(mode,c,T)/4.
            assert abs(measured-target)<3.5e-5, (c,T,mode,measured,target)
            tests+=1
    # Exactly area-preserving variable x=t/(1-t): area = pi X.
    for mode in (1,2,3,4):
        for eps in (.07,.1):
            theta=2*np.pi*np.arange(4096)/4096
            X=2./3.
            radialX=X+eps*np.cos(mode*theta)
            area=np.pi*radialX.mean()
            assert abs(area-np.pi*X)<3e-14
            tests+=1
    print('PASS:',tests,'supplementary checks')
    print('Example alpha=0, T=1/2, h=cos(2 theta): coefficient =',B(2,1,.5)/4)

if __name__=='__main__':
    main()
