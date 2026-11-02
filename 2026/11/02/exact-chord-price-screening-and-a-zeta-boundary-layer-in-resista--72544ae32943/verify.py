"""Independent finite checks for a priced path and one optional chord."""
import math
import random
import numpy as np


def profile(n):
    return np.concatenate(([0.0], np.cumsum([1.0 / math.sqrt(k*(n-k)) for k in range(1,n)])))


def threshold(n,i,j):
    h=profile(n)
    z=np.clip(h,h[i-1],h[j-1])
    return float(n*np.sum((z-z.mean())**2))


def continuum(x,y):
    a=2.0*math.asin(math.sqrt(x))
    b=2.0*math.asin(math.sqrt(y))
    m=(a+b+math.sin(b)-math.sin(a))/2.0
    return (a*a+b*b)/2.0+b*math.sin(b)-a*math.sin(a)+math.cos(b)-math.cos(a)-m*m


def kirchhoff(n,weights,chord=None):
    L=np.zeros((n,n),dtype=float)
    for k,v in enumerate(weights):
        L[k,k]+=v;L[k+1,k+1]+=v;L[k,k+1]-=v;L[k+1,k]-=v
    if chord is not None:
        i,j,t=chord;i-=1;j-=1
        L[i,i]+=t;L[j,j]+=t;L[i,j]-=t;L[j,i]-=t
    M=np.linalg.inv(L[1:,1:])
    return float(n*np.trace(M)-np.sum(M))


def main():
    rng=random.Random(79131)
    checks=0
    for n in range(3,15):
        B=2.6
        A=[k*(n-k) for k in range(1,n)]
        H=sum(math.sqrt(v) for v in A)
        c=np.array([B*math.sqrt(v)/H for v in A])
        J0=kirchhoff(n,c)
        assert abs(J0-H*H/B)<1e-8*max(1,J0)
        checks+=1
        for _ in range(16):
            i=rng.randrange(1,n-1);j=rng.randrange(i+2,n+1)
            q=threshold(n,i,j)
            # Equality of the clipped variance with an independent pair sum.
            h=profile(n); z=np.clip(h,h[i-1],h[j-1]); pair=0.0
            for u in range(n):
                for v in range(u+1,n): pair+=(z[v]-z[u])**2
            assert abs(pair-q)<1e-9*max(1,q)
            checks+=1
            for ratio in (0.60,1.00,1.35):
                price=ratio*q; eps=3e-5*B/(1+q)
                new=(1-price*eps/B)*c
                J1=kirchhoff(n,new,(i,j,eps))
                J2=kirchhoff(n,(1-2*price*eps/B)*c,(i,j,2*eps))
                analytic=(H/B)**2*(price-q)
                richardson=(4*J1-J2-3*J0)/(2*eps)
                relative=abs(richardson-analytic)/(1+abs(analytic))
                assert relative<0.01,(n,i,j,ratio,relative)
                checks+=1
        for a in range(1,n-1):
            for b in range(a+2,n+1):
                for i in range(a,b-1):
                    for j in range(i+2,b+1):
                        if (i,j)!=(a,b):
                            assert threshold(n,i,j)<threshold(n,a,b)+1e-11
                            checks+=1
    for x,y in ((0,1),(.1,.7),(.2,.8),(.4,.9),(.02,.98)):
        n=2400;i=max(1,round(x*n));j=min(n,round(y*n))
        assert j-i>=2
        err=abs(threshold(n,i,j)/n**2-continuum(x,y))
        assert err<0.008,(x,y,err)
        checks+=1
    zeta_half=-0.207886224977354566
    leading=math.pi**2/4-2
    sub=2*math.pi*zeta_half
    errs=[]
    for n in (250,1000,4000,16000):
        q=threshold(n,1,n)
        err=q-leading*n*n-sub*math.sqrt(n)
        errs.append(abs(err))
        assert abs(err)<2.0*math.log(n), (n,err)
        checks+=1
    print('PASS',checks,'assertions;', 'endpoint remainder magnitudes:',errs)


if __name__=='__main__': main()
