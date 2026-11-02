"""Supplementary finite-dimensional checks for a separated-interval sinc concentration theorem.

These numerical checks do not constitute a proof of the infinite-dimensional claims.
Run: python CHECK.py
"""
from math import pi
import numpy as np
from numpy.polynomial.legendre import leggauss


def data(a, n=100):
    x, w = leggauss(n)
    x, w = a*x/2, a*w/2
    sw=np.sqrt(w)
    K=np.sinc(x[:, None]-x[None, :])*sw[:, None]*sw[None, :]
    ev, U=np.linalg.eigh(K)
    lam, second, psi=ev[-1],ev[-2],U[:,-1]
    if np.dot(psi, sw*np.cos(pi*x))<0:psi=-psi
    c=np.dot(psi,sw*np.cos(pi*x))
    d=np.dot(psi,sw*x*np.sin(pi*x))
    Q=c*d/pi
    C=c*c
    assert lam>second>0 and C>0 and Q>0
    assert abs(np.linalg.norm(psi)-1.0)<1.e-12
    assert abs(np.dot(psi,sw*np.sin(pi*x)))<1.e-12
    assert np.linalg.norm(K@psi-lam*psi)<1.e-12
    assert np.linalg.norm(K-K.T)<1.e-12
    comm=(lam*np.eye(n)-K)@(x*psi)-(c/pi)*sw*np.sin(pi*x)
    assert np.linalg.norm(comm)<1.e-12,(a,np.linalg.norm(comm))
    return x,w,lam,psi,C,Q

def top_two(a,m,t,dat):
    x,w,lam,psi,C,Q=dat
    sw=np.sqrt(w)
    K=np.sinc(x[:,None]-x[None,:])*sw[:,None]*sw[None,:]
    R=m+t/m
    B=np.sinc(x[:,None]-x[None,:]-R)*sw[:,None]*sw[None,:]
    A=np.block([[K,B],[B.T,K]])
    e=np.linalg.eigvalsh(A)
    return e[-1],e[-2],e[-3]

def main():
    checks=0
    for a in [0.5,1.5,3.0]:
        D=data(a,90)
        x,w,lam,psi,C,Q=D
        checks+=6
        threshold=2*Q/C
        for m in [20,21,40,41,80]:
            for t in [0.0, threshold/2, threshold, 2*threshold, -threshold]:
                hi,lo,third=top_two(a,m,t,D)
                assert lo>third,(a,m,t,lo,third)
                ph=lam+(Q+abs(C*t-2*Q))/m**2
                pl=lam+(Q-abs(C*t-2*Q))/m**2
                assert abs(hi-ph)*m*m < 3.0/m, (a,m,t,hi,ph,(hi-ph)*m*m)
                assert abs(lo-pl)*m*m < 3.0/m, (a,m,t,lo,pl,(lo-pl)*m*m)
                checks+=3
        for R in [14.5,15.5,26.5,27.5,51.5,52.5]:
            hi,lo,third=top_two(a,int(R),int(R)*(R-int(R)),D)
            lead=C*abs(np.sin(pi*R))/(pi*R)
            assert abs(hi-(lam+lead))*R<1.0/R,(a,R,hi,lam+lead)
            assert abs(lo-(lam-lead))*R<1.0/R,(a,R,lo,lam-lead)
            checks+=2
        print(f'a={a:g}: top={lam:.10f}, C={C:.10f}, Q={Q:.10f}, tcrit={threshold:.10f}')
    print('CHECK_OK',checks)

if __name__=='__main__':main()
