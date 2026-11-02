"""Numerical supplementary validation for a weighted-distance negative-type threshold."""
import math
import numpy as np
from collections import deque

def analytic(m,n):
    U=m/(2*(m-1))
    beta=(n-1)/(2*n)
    A=2*(1-U*beta+math.sqrt(U/n+U*U*beta*beta))
    s=(A-2)/(2*U)
    return A,math.log2(A),s

def distances(m,n):
    N=m+n
    adj=[set() for _ in range(N)]
    for i in range(m):
      for j in range(i):adj[i].add(j); adj[j].add(i)
    for j in range(m,m+n):adj[0].add(j);adj[j].add(0)
    d=np.zeros((N,N),int)
    for i in range(N):
      todo=deque([i]); reached={i};
      while todo:
        u=todo.popleft()
        for v in adj[u]:
          if v not in reached:
            d[i,v]=d[i,u]+1;reached.add(v);todo.append(v)
    return d

def eig(m,n,p):
    D=distances(m,n).astype(float)**p
    # orthonormal zero-sum basis via QR
    N=m+n
    E=np.zeros((N,N-1)); E[:N-1,:]=np.eye(N-1); E[N-1,:]=-1
    Q,_=np.linalg.qr(E)
    return np.linalg.eigvalsh(Q.T@D@Q)

def main():
    checks=0
    for m in [3,4,5,7,15,31]:
      for n in [2,3,4,8,16,50]:
        A,p,s=analytic(m,n)
        assert 2<A<2*n/(n-1)
        e0=eig(m,n,p-1e-5)
        e1=eig(m,n,p)
        e2=eig(m,n,p+1e-5)
        assert e0[-1]<-1e-7,(m,n,p,e0[-1])
        assert abs(e1[-1])<1e-9,(m,n,p,e1[-1])
        assert e1[-2]<-0.00001,(m,n,p,e1[-2])
        assert e2[-1]>1e-7,(m,n,p,e2[-1])
        z=np.array([-s-1]+[s/(m-1)]*(m-1)+[1/n]*n)
        assert abs(z.sum())<1e-12
        d=distances(m,n).astype(float)**p
        assert abs(z@d@z)<1e-9
        # At the endpoint the equality vector is a null vector of the centered form.
        f=d@z
        assert max(f)-min(f)<1e-8
        checks+=7
    for m in [3,4,8,31]:
      previous=100
      for n in [2,3,4,5,10,20,40,80,160]:
        A,p,_=analytic(m,n)
        assert p<previous;previous=p;checks+=1
    for n in [2,3,4,10,40]:
      previous=100
      for m in [3,4,6,10,50,100]:
        A,p,_=analytic(m,n)
        assert p<previous;previous=p;checks+=1
    print('PASS',checks,'analytical comparison assertions')
    for m,n in [(3,2),(3,5),(5,5),(20,5),(3,50)]:
      print(m,n,*analytic(m,n)[:2])
if __name__=='__main__':main()
