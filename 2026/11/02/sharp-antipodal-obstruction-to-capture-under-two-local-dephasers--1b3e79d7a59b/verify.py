#!/usr/bin/env python3
"""Separate finite checks of a three-monitor hypercube quantum transport law.
The exact theorem for all dimensions is proved separately; these tests are finite.
"""
import math
import numpy as np
from scipy.linalg import expm


def krawtchouk(d, k, h):
    return sum((-1)**j * math.comb(h,j) * math.comb(d-h,k-j)
               for j in range(max(0,k-d+h), min(k,h)+1))


def rank3_gram(d, k, u, v):
    m = math.comb(d,k)
    x, y, z = (krawtchouk(d,k,(w).bit_count()) for w in (u,v,u^v))
    # Symmetric 3x3: [m,x,y; x,m,z; y,z,m].
    det = m**3 + 2*x*y*z - m*(x*x+y*y+z*z)
    if det != 0: return 3
    if abs(x) != m or abs(y) != m or abs(z) != m: return 2
    return 1


def exhaustive():
    checks=0
    for d in range(3,8):
        mask=(1<<d)-1
        counts={"antipodal":0,"nonantipodal":0}
        for u in range(1,mask+1):
            for v in range(u+1,mask+1):
                anti = (u==mask or v==mask or (u^v)==mask)
                expect=2 if anti else 3
                count=sum(rank3_gram(d,k,u,v) for k in range(d+1))
                assert count==(2*d if anti else 3*d-1),(d,u,v,count)
                for k in range(1,d):
                    assert rank3_gram(d,k,u,v)==expect,(d,k,u,v)
                    checks+=1
                counts['antipodal' if anti else 'nonantipodal']+=1
        print(f'd={d} all anchored unordered distinct monitor pairs: {counts}')
    return checks


def hcube(d):
    n=1<<d
    H=np.zeros((n,n),float)
    for x in range(n):
        for j in range(d):H[x,x^(1<<j)]=1.0
    return H


def generator(H,a,b,c,kappa=1.0,gamma=1.0):
    n=H.shape[0]; I=np.eye(n)
    L=-1j*(np.kron(I,H)-np.kron(H.T,I))
    Pa=np.diag([int(i==a) for i in range(n)])
    L-=kappa/2*(np.kron(I,Pa)+np.kron(Pa.T,I))
    for w in (b,c):
        P=np.diag([int(i==w) for i in range(n)])
        L+=gamma*(np.kron(P.T,P)-0.5*np.kron(I,P)-0.5*np.kron(P.T,I))
    return L


def check_lindblad(d, triples, t=200):
    H=hcube(d); n=1<<d
    for a,b,c in triples:
        mask=n-1
        anti=((a^b)==mask or (a^c)==mask or (b^c)==mask)
        target=(2*d if anti else 3*d-1)/n
        L=generator(H,a,b,c)
        rho=(np.eye(n)/n).reshape(n*n,order='F')
        survival=np.trace(expm(L*t).dot(rho).reshape((n,n),order='F')).real
        err=abs(1-survival-target)
        assert err<1e-5,(d,(a,b,c),err,1-survival,target)
        print('Lindblad', d,(a,b,c),'capture at t=',t,round(1-survival,9),'infinite-time=',round(target,9),'err=',round(err,10))
    return len(triples)


def main():
    n=exhaustive()
    check_lindblad(3,[(0,1,2),(0,1,7)],t=1000)
    check_lindblad(4,[(0,1,2),(0,1,15)],t=2000)
    print('PASS exact finite rank checks:',n,'and four direct Lindblad dynamics tests')

if __name__=='__main__':main()
