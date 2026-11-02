#!/usr/bin/env python3
"""Finite independent reconstruction checks for subdivided biclique distances."""
import math
from collections import deque
import numpy as np
from scipy.optimize import brentq

def distance_matrix(m,n):
    size=m+n+m*n
    adj=[[] for _ in range(size)]
    for i in range(m):
        for j in range(n):
            k=m+n+i*n+j
            adj[i].append(k);adj[k].append(i)
            adj[m+j].append(k);adj[k].append(m+j)
    D=np.empty((size,size),dtype=np.int64)
    for start in range(size):
        d=[-1]*size;d[start]=0;q=deque([start])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==-1:d[v]=d[u]+1;q.append(v)
        assert min(d)>=0
        D[start,:]=d
    return D

def mass_matrix(m,n,p):
    a,b,c=2**p,3**p,4**p
    return np.array([[c*(m-1)/m,a,(1+(m-1)*b)/m],
      [a,c*(n-1)/n,(1+(n-1)*b)/n],
      [(1+(m-1)*b)/m,(1+(n-1)*b)/n,
         ((m+n-2)*a+(m-1)*(n-1)*c)/(m*n)]],float)

def H(m,n,p):
    T=np.array([[1.,0.],[0.,1.],[-1.,-1.]])
    return T.T@mass_matrix(m,n,p)@T

def threshold(m,n):
    alpha0=math.log2(2*m*n/(2*m*n-m-n))
    return brentq(lambda p:np.linalg.det(H(m,n,p)),0.,alpha0,xtol=1e-14),alpha0

def direct_Q(D,m,n,p):
    N=m+n+m*n
    mass=np.zeros((N,3),float)
    mass[:m,0]=1/m;mass[m:m+n,1]=1/n;mass[m+n:,2]=1/(m*n)
    X=D.astype(float)**p
    np.fill_diagonal(X,0.)
    return mass.T@X@mass

def main():
    cases=0
    for m in range(2,7):
      for n in range(m+1,10):
        D=distance_matrix(m,n)
        assert D.shape==(m+n+m*n,)*2
        p,alpha0=threshold(m,n)
        assert 0<p<alpha0<1
        for pp in [0.,p/3.,p,alpha0]:
            Q=direct_Q(D,m,n,pp)
            assert np.max(np.abs(Q-mass_matrix(m,n,pp)))<2e-12,(m,n,pp)
            a,b,c=2**pp,3**pp,4**pp
            # Check all pair distances and the analytic row/column blocks.
            for i in range(m+n+m*n):
              for j in range(i+1,m+n+m*n):
                if i<m and j<m or m<=i<m+n and m<=j<m+n: expected=4
                elif i<m+n and j<m+n:expected=2
                elif i>=m+n:
                    x,y=divmod(i-m-n,n);u,v=divmod(j-m-n,n)
                    expected=2 if x==u or y==v else 4
                else:
                    x,y=divmod(j-m-n,n)
                    expected=1 if (i==x if i<m else i-m==y) else 3
                assert D[i,j]==expected,(m,n,i,j,D[i,j],expected)
        P=np.eye(D.shape[0])-np.ones(D.shape)/D.shape[0]
        for pp,positivity in [(p/2,False),(p,False),((p+alpha0)/2,True)]:
            eig=np.linalg.eigvalsh(P@(D.astype(float)**pp)@P)
            nonzero=eig[np.abs(eig)>2e-7]
            assert (np.max(nonzero)>0)==positivity,(m,n,pp)
            if pp==p:
                assert np.sum(abs(eig)<2e-7)==2,(m,n,eig)
        assert np.linalg.det(H(m,n,alpha0))<0
        cases+=1
        if m==2 and n in [3,9]:
            print('EXAMPLE',m,n,'critical',format(p,'.12f'),'original',format(alpha0,'.12f'))
    for m in [2,3,4,6]:
        c=(m+1)/((4*m-1)*math.log(2)-2*m*math.log(3))
        p,_=threshold(m,5000)
        assert abs(p*5000/c-1)<.025,(m,p,c)
        print('ASYMPTOTIC',m,'n=5000','n_times_p=',format(p*5000,'.8f'),'limit=',format(c,'.8f'))
    print('CHECK_OK:',cases,'full finite graph cases and four asymptotic probes')
if __name__=='__main__':main()
