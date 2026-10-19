#!/usr/bin/env python3
"""Independent finite-size checks of bipartite torus resonance formulas."""
import math
import numpy as np
from math import gcd

def predict(m,n,fx,fy):
    g=gcd(m,n)
    hit=lambda z:abs(z/g-round(z/g))<1e-9
    hplus=hit(n*fx-m*fy)
    hminus=hit(n*fx+m*fy)
    return g*(int(hplus)+int(hminus))//2 - int(abs(fx)<1e-10 and abs(fy)<1e-10)

def hamiltonian(m,n,fx,fy):
    assert min(m,n)>=4 and m%2==n%2==0
    H=np.zeros((m*n,m*n),complex)
    def idx(x,y):return (x%m)*n+(y%n)
    for x in range(m):
        for y in range(n):
            a=idx(x,y)
            for (xx,yy,v) in ((x+1,y,np.exp(2j*np.pi*fx/m)),(x,y+1,np.exp(2j*np.pi*fy/n))):
                b=idx(xx,yy);H[a,b]+=v;H[b,a]+=v.conjugate()
    return H

def run():
    checked=0
    for m,n in ((4,4),(4,6),(6,6),(4,8),(6,8),(8,8)):
        for fx,fy in ((0.,0.),(.5,.5),(.5,0.),(0.,.5),(.25,.25),(.137,.289)):
            H=hamiltonian(m,n,fx,fy)
            eva=np.linalg.eigvalsh(H)
            nz=int(np.sum(np.abs(eva)<1e-8))
            d=predict(m,n,fx,fy)
            assert nz==2*d, (m,n,fx,fy,nz,d)
            ev=[];od=[]
            for x in range(m):
                for y in range(n):
                    (ev if (x+y)%2==0 else od).append(x*n+y)
            B=H[np.ix_(ev,od)]
            vals=np.linalg.svd(B,compute_uv=False)
            kd=int(np.sum(vals<1e-8))
            assert kd==d,(m,n,fx,fy,kd,d)
            H2=(H@H)[np.ix_(ev,ev)]
            seen={0}; stack=[0]
            while stack:
                j=stack.pop()
                for k in range(len(ev)):
                    if k!=j and abs(H2[j,k])>1e-8 and k not in seen:
                        seen.add(k);stack.append(k)
            assert len(seen)==len(ev),(m,n,fx,fy,len(seen))
            checked+=1
    for m,n,fx,fy in ((4,4,0,0),(4,4,.5,.5),(4,6,0,0),(4,6,.137,.289),(6,6,.5,.5)):
        H=hamiltonian(m,n,fx,fy)
        ev=[];od=[]
        for x in range(m):
            for y in range(n):
                (ev if (x+y)%2==0 else od).append(x*n+y)
        U,s,Vh=np.linalg.svd(H[np.ix_(ev,od)],full_matrices=True)
        d=predict(m,n,fx,fy)
        D=np.zeros((m*n,m*n),complex)
        if d:
            Q=Vh[-d:,:].conj().T
            D[np.ix_(od,od)]=Q@Q.conj().T
        assert np.linalg.norm(H@D)<1e-8
        assert np.linalg.norm(D@D-D)<1e-8
        assert abs(np.trace(D).real-d)<1e-8
        if d:
            for v in od:
                assert abs(D[v,v].real-2*d/(m*n))<1e-8
        for v in (od[0],ev[0]):
            rho=np.zeros((m*n,m*n),complex);rho[v,v]=1
            p=float(np.trace(D@rho).real)
            R=D@rho@D+(1-p)/(m*n-d)*(np.eye(m*n)-D)
            assert abs(np.trace(R).real-1)<1e-8
            assert np.linalg.norm(H@R-R@H)<1e-8
            for e in ev:
                P=np.zeros((m*n,m*n));P[e,e]=1
                assert np.linalg.norm(P@R-R@P)<1e-8
            ret_formula=(2*d/(m*n))**2+(1-2*d/(m*n))**2/(m*n-d) if v==od[0] else 1/(m*n-d)
            assert abs(R[v,v].real-ret_formula)<1e-8
    print('PASS:',checked,'independent Fourier/physical zero-mode and length-two connectivity comparisons; ten stationary-state tests.')

if __name__=='__main__':run()
