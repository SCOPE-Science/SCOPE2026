"""Reproduce finite star stationary correlations and beta-limit moments.
Uses scipy/numpy for finite reduced Markov chains; assertions are executable checks.
"""
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from math import prod


def rates(m,a):
    # i = (h_idx)*(m+1)+k ; h_idx=0 -> -1; 1 -> +1
    n=2*(m+1)
    Q=lil_matrix((n,n), dtype=float)
    for hidx,h in enumerate((-1,1)):
        for k in range(m+1):
            i=hidx*(m+1)+k
            up=(m-k)*(a+(1+h)/2)
            down=k*(a+(1-h)/2)
            cross=a + ((m-k)/m if h==1 else k/m)
            for j,r in ((i+1,up),(i-1,down),((1-hidx)*(m+1)+k,cross)):
                if r: Q[i,j]=r
            Q[i,i]=-(up+down+cross)
    return Q.tocsr()


def stationary(m,a):
    Q=rates(m,a)
    A=Q.transpose().tolil()
    A[-1,:]=1.0
    rhs=np.zeros(2*(m+1));rhs[-1]=1
    pi=spsolve(A.tocsc(), rhs)
    assert pi.min() > -1e-11
    assert abs(pi.sum()-1)<1e-10
    assert np.max(np.abs(Q.transpose() @ pi))<1e-8
    return pi


def moment_target(j,b):
    if j%2: return 0.0
    return prod((2*k-1)/(2*k*b*b-1) for k in range(1,j//2+1))


def run():
    checks=0
    for m in (1,2,3,5,8,15,40,120,400):
      for a in (0.2,0.5,1.4):
        pi=stationary(m,a)
        b=1+2*a
        x=np.array([2*k/m-1 for h in (-1,1) for k in range(m+1)])
        h=np.array([h for h in (-1,1) for k in range(m+1)])
        xx=float(pi @ (x*x)); hx=float(pi @ (h*x))
        # Pair correlations, second moments, finite m exact formula.
        y=(m+1)/(m*(2*b*b-1)+1)
        hubleaf=b*y
        assert abs(hx-hubleaf)<2e-10;checks+=1
        assert abs(xx-(1/m+(m-1)/m*y))<2e-10;checks+=1
        assert abs(pi@x)<2e-11;checks+=1
        assert abs(pi@h)<2e-11;checks+=1
        if m>=40:
            for degree in (2,4,6):
                err=abs(float(pi@(x**degree))-moment_target(degree,b))
                # Bound from direct O(1/m) generator approximation, loose numerical tolerance.
                assert err<8/m, (m,a,degree,err)
                checks+=1
    print(f'PASS {checks} finite generator/stationary/correlation/beta-moment checks')

if __name__=='__main__':run()
