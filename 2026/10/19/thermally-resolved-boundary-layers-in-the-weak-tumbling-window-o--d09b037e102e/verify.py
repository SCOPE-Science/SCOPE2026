"""Independent finite-generator checks of reflecting two-orientation lattice transport.

Requires numpy and scipy. Prints numerical comparisons, and exits on mismatch.
"""
import numpy as np
from scipy.linalg import solve


def density_exact(L, u, v, alpha):
    assert L >= 1 and u > v > 0 and alpha > 0
    delta, w = u-v, u+v
    s = (u*u+v*v+alpha*w)/(u*v)
    k = np.arccosh(s/2)
    z = np.exp(k)
    H = (delta/w)*(z+1)/(z-1)
    t = np.exp(-(2*L+1)*k)
    i = np.arange(-L, L+1)
    boundary = (np.exp((i-L-1)*k)+np.exp((-i-L-1)*k))/2
    den = H*(1-t)+(2*L+1)*(alpha/delta)*(1+t)
    return ((z-1)*H*boundary+(alpha/delta)*(1+t))/den


def density_ctmc(L, u, v, alpha):
    n = 2*L+1
    G = np.zeros((2*n,2*n))
    for k in range(n):
        for sig in range(2):
            col=2*k+sig
            outward = u if sig==0 else v
            inward = v if sig==0 else u
            for j, rate in ((k+1,outward),(k-1,inward)):
                if 0<=j<n:
                    G[2*j+sig,col] += rate
                    G[col,col] -= rate
            G[2*k+1-sig,col] += alpha
            G[col,col] -= alpha
    G[-1,:] = 1.0
    h=np.zeros(2*n);h[-1]=1
    pi=solve(G,h)
    return pi.reshape(n,2).sum(axis=1)


def check():
    comparisons=0
    maxerr=0.0
    for L in (1,2,4,6,12):
        for u,v,a in ((3.,1.,.02),(2.,.6,1.5),(1.12,.95,.8)):
            rho=density_exact(L,u,v,a)
            q=density_ctmc(L,u,v,a)
            err=np.max(np.abs(rho-q))
            maxerr=max(err,maxerr)
            assert err < 2e-12, (L,u,v,a,err)
            assert np.all(np.diff(rho[L:])>0)
            assert np.all(np.diff(np.diff(rho))>0)
            assert abs(rho.sum()-1)<5e-12
            comparisons += 1
    u,v,c=2.5,1.,1.7
    delta=u-v
    edge=delta*delta/(2*u*(delta+2*c))
    bulk=c/(delta+2*c)
    print('15 independent full Markov-generator checks; max absolute error:',format(maxerr,'.3g'))
    print('L    wall density   target         bulk L*rho(0)   target')
    for L in (20,80,300,1000):
        rho=density_exact(L,u,v,c/L)
        print('%d  %.9f  %.9f  %.9f  %.9f' %(L,rho[-1],edge,L*rho[L],bulk))
    assert abs(density_exact(1000,u,v,c/1000)[-1]-edge) < 4e-4
    assert abs(1000*density_exact(1000,u,v,c/1000)[1000]-bulk) < 5e-5
    print('All independent checks passed.')


if __name__=='__main__':
    check()
