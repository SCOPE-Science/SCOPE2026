"""Small-graph computational checks for bipartite fourth-order diffusion.

Requires Python 3, numpy, scipy. Finite checks supplement the general proof.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

def kernel_entries(m,n,t):
    N=m+n
    z=math.exp(-N*N*t); a=math.exp(-n*n*t); b=math.exp(-m*m*t)
    off_a=(m+n*z-N*a)/(m*N)
    off_b=(n+m*z-N*b)/(n*N)
    cross=(1-z)/N
    return off_a,off_b,cross,off_a+a,off_b+b

def excess(m,n,t):
    A,B,_,_,_=kernel_entries(m,n,t)
    return 2*max(0,-(m-1)*A,-(n-1)*B)

def peaks(m,n):
    N=m+n
    ta=math.log(N/n)/(N*N-n*n)
    tb=math.log(N/m)/(N*N-m*m)
    aa,bb,*_=kernel_entries(m,n,ta)
    aaa,bbb,*_=kernel_entries(m,n,tb)
    return ta,tb,2*(m-1)*max(0,-aa),2*(n-1)*max(0,-bbb)

def positive_root(m,n,branch):
    N=m+n
    if branch=='A':
        def f(t):return N*math.exp(-n*n*t)-m-n*math.exp(-N*N*t)
        tp=math.log(N/n)/(N*N-n*n)
    else:
        def f(t):return N*math.exp(-m*m*t)-n-m*math.exp(-N*N*t)
        tp=math.log(N/m)/(N*N-m*m)
    return brentq(f,tp,100/(m*m),xtol=5e-15)

def run():
    nchecks=0
    # Independently exponentiate actual graph matrices and compare every entry.
    for m in range(2,9):
        for n in range(m,15):
            N=m+n
            A=np.zeros((N,N)); A[:m,m:]=1; A[m:,:m]=1
            L=np.diag(A.sum(axis=1))-A
            for t in [0,0.01/N**2,0.1/N**2,1/N**2,3/N**2,20/N**2]:
                H=expm(-t*(L@L))
                oa,ob,c,da,db=kernel_entries(m,n,t)
                T=np.full((N,N),c)
                T[:m,:m]=oa;T[m:,m:]=ob
                np.fill_diagonal(T,np.r_[np.full(m,da),np.full(n,db)])
                assert np.max(abs(H-T))<3e-12,(m,n,t)
                assert abs(np.linalg.norm(H,np.inf)-(1+excess(m,n,t)))<4e-12,(m,n,t)
                nchecks+=2
    # Test the proved cutoff, unique peak and recovery ordering.
    for m in [2,3,4,5,7,10,20,70]:
        for ratio in [32,33,48,64,100,250]:
            n=m*ratio
            ta,tb,am,bm=peaks(m,n)
            assert bm>am,(m,n,am,bm)
            assert ta<tb,(m,n,ta,tb)
            assert (m-1)*max(0,-kernel_entries(m,n,2/n**2)[0])<1e-12
            assert (n-1)*max(0,-kernel_entries(m,n,2/n**2)[1])>0
            assert abs(excess(m,n,tb)-bm)<1e-12
            nchecks+=5
    # Test finite root implications and sampled temporal maximum.
    for m,n in [(2,64),(3,96),(5,160),(10,320),(2,400),(8,500)]:
        ra=positive_root(m,n,'A'); rb=positive_root(m,n,'B')
        ta,tb,am,bm=peaks(m,n)
        assert ta<ra<2/n**2<rb
        assert tb<rb
        nchecks+=2
        for j in range(251):
            t=j*3*rb/250
            assert excess(m,n,t)<=bm+2e-10
            nchecks+=1
            if t>rb+1e-12:
                assert excess(m,n,t)<1e-10
                nchecks+=1
    # Asymptotics at strong imbalance: no finite computation is used as proof.
    for m in [2,5,11]:
        for k in [1000,10000]:
            n=m*k
            theta=peaks(m,n)[1]
            tau=positive_root(m,n,'B')
            assert abs(m*n*tau-1)<0.025
            assert abs(excess(m,n,theta)/(2*m/n)-1)<0.025
            assert abs((tau/theta)/(k/math.log(k))-1)<0.1
            nchecks+=3
    return nchecks
if __name__=='__main__':print('CHECKS_OK',run())
