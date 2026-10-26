#!/usr/bin/env python3
"""Independent finite Markov-chain checks for cycle first meetings."""
import numpy as np
from scipy.linalg import solve
from math import atanh,cosh

def analytic(n,a,b,r):
    inv2=pow(2,-1,n)
    u=(a+b)*inv2%n
    v=(a-b)*inv2%n
    z=1-r
    w=[]
    for ell in range(n):
        k=2*np.pi*ell/n
        alpha=np.arccosh(2/z-np.cos(k))
        h=np.cosh((v-n/2)*alpha)/np.cosh(n*alpha/2)
        w.append(h)
    if r==0:phi=1.0;mean=2*v*(n-v)
    else:
        phi=w[0];mean=(1/phi-1)/r
    # omega_ell=E[exp(ik (J-u))], so P_J = ifft(w/phi) shifted u.
    probs=np.fft.fft(np.array(w)/phi).real/n # p[(j-u)] computed with DFT positive inversion negative
    probs=np.roll(probs,u)
    return mean, probs

def direct(n,a,b,r):
    pairs=[(i,j) for i in range(n) for j in range(n) if i!=j]
    index={st:k for k,st in enumerate(pairs)}
    d=len(pairs)
    Q=np.zeros((d,d)); R=np.zeros((d,n))
    for i,(x,y) in enumerate(pairs):
        Q[i,index[(a,b)]]+=r
        for dx in (-1,1):
            for dy in (-1,1):
                xx=(x+dx)%n; yy=(y+dy)%n
                if xx==yy:R[i,xx]+=(1-r)/4
                else:Q[i,index[(xx,yy)]]+=(1-r)/4
    Z=np.eye(d)-Q
    mean=solve(Z,np.ones(d),assume_a='gen')[index[(a,b)]]
    p=solve(Z,R,assume_a='gen')[index[(a,b)]]
    return mean,p

def main():
    checks=0
    for n in (3,5,7,9):
        for a,b in [(0,1),(0,2),(1,n-1)]:
            if a==b:continue
            for r in (0,.015,.14,.49):
                x,p=analytic(n,a,b,r)
                y,q=direct(n,a,b,r)
                assert abs(x-y)<3e-8,(n,a,b,r,x,y)
                assert max(abs(p-q))<3e-9,(n,a,b,r,p,q)
                assert abs(sum(p)-1)<1e-9
                checks+=3
    for n in (5,7,9,11,21,51):
        for v in range(1,n):
            q=v*(n-v)
            mu=2*q
            derivative=(2/3)*q*(5*q-(n*n-2))
            eps=min(2e-7,0.001/n**2)
            am,_=analytic(n,0,(2*v)%n,eps)
            # derivative checked with two-step divided finite difference (O(eps))
            assert abs((am-mu)/eps-derivative)<max(3.0,abs(derivative)*.008),(n,v,(am-mu)/eps,derivative)
            checks+=1
    print('VERIFIED',checks, 'independent exact-state Markov and derivative comparisons')
if __name__=='__main__':main()
