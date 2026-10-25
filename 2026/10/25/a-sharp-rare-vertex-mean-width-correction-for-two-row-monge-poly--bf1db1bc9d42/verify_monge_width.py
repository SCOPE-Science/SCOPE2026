"""Numerical support tests and one-dimensional extreme-value Laplace integrals.
These finite checks corroborate, but do not prove, an asymptotic theorem.
"""
import math
import numpy as np
from scipy.optimize import linprog
from scipy.integrate import quad
from scipy.special import ndtr, log_ndtr, ndtri


def support_vertex(g):
    n=g.shape[1]
    avg=(g[0]+g[1])/2
    suffix=np.cumsum(g[0,::-1])/np.arange(1,n+1)
    prefix=np.cumsum(g[1])/np.arange(1,n+1)
    return max(avg.max(),suffix.max(),prefix.max())


def support_lp(g):
    n=g.shape[1]
    a=[]
    for j in range(n-1):
        h=np.zeros(2*n)
        h[j]=1;h[n+j+1]=1;h[j+1]=-1;h[n+j]=-1
        a.append(h)
    ans=linprog(-g.reshape(-1),A_ub=np.array(a),b_ub=np.zeros(n-1),A_eq=np.ones((1,2*n)),b_eq=[1],bounds=[(0,None)]*(2*n),method='highs')
    assert ans.success
    return -ans.fun


def singleton_integral(n):
    b=ndtri(1-1/n)/math.sqrt(2)
    # I_n = int Phi(sqrt(2)t)^(n-2)*barPhi(t) dt; integrate positive t.
    def f(t):
        return math.exp((n-2)*log_ndtr(math.sqrt(2)*t))*ndtr(-t)
    integral=quad(f,0,max(10,b+12),epsabs=1e-12,epsrel=2e-9,limit=250)[0]
    target=0.5*math.pi**0.25
    scaled=integral*math.sqrt(n)*b**1.5
    return b,scaled,target


def main():
    rng=np.random.default_rng(182717)
    ct=0
    for n in range(3,13):
        for _ in range(30):
            g=rng.standard_normal((2,n))
            assert abs(support_vertex(g)-support_lp(g))<2e-9
            ct+=1
    checks=[]
    for n in [1000,10000,100000,1000000,10000000]:
        b,ratio,target=singleton_integral(n)
        checks.append((n,round(b,5),round(ratio,6)))
    print('VERIFY_OK supports',ct,'LP comparisons; normalized singleton rare-boundary integral',checks,'limit',round(target,6))

if __name__=='__main__':main()
