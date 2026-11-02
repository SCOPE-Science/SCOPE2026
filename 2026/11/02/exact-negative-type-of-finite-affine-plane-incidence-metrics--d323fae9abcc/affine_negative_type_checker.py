"""Independent numerical and combinatorial tests for affine-plane incidence negative type.

Run: python3 affine_negative_type_checker.py (requires NumPy).
The analytic proof, not this finite test, covers arbitrary affine planes and all orders.
"""
import math
from collections import deque
import numpy as np


def instance(q):
    # Prime-field affine plane, with q+1 parallel classes of q lines.
    points = [(x,y) for x in range(q) for y in range(q)]
    lines = [(m,b) for m in range(q) for b in range(q)] + [('v',b) for b in range(q)]
    N = np.zeros((q*q, q*(q+1)),dtype=int)
    for i,(x,y) in enumerate(points):
        for j,(m,b) in enumerate(lines):
            if (x==b if m=='v' else (y-m*x-b)%q==0):
                N[i,j]=1
    C=np.zeros((len(lines),len(lines)),dtype=int)
    for j in range(q+1):
        C[j*q:(j+1)*q,j*q:(j+1)*q]=1
    assert np.array_equal(N@N.T,q*np.eye(q*q,dtype=int)+np.ones((q*q,q*q),dtype=int))
    assert np.array_equal(N.T@N,q*np.eye(q*(q+1),dtype=int)+np.ones((q*(q+1),q*(q+1)),dtype=int)-C)
    V=len(points)+len(lines)
    adj=[[] for _ in range(V)]
    for i,j in zip(*np.where(N)):
        u,v=int(i),int(len(points)+j)
        adj[u].append(v);adj[v].append(u)
    distance=np.zeros((V,V),dtype=int)
    for source in range(V):
        a=[-1]*V; a[source]=0; queue=deque([source])
        while queue:
            u=queue.popleft()
            for v in adj[u]:
                if a[v]<0: a[v]=a[u]+1;queue.append(v)
        assert min(a)>=0
        distance[source,:]=a
    P=q*q; L=q*(q+1)
    expected=np.zeros((V,V),dtype=int)
    expected[:P,:P]=2*(np.ones((P,P),dtype=int)-np.eye(P,dtype=int))
    expected[:P,P:]=3-2*N
    expected[P:,:P]=expected[:P,P:].T
    expected[P:,P:]=2*(np.ones((L,L),dtype=int)-C)+4*(C-np.eye(L,dtype=int))
    assert np.array_equal(distance,expected)
    return distance,N,C


def check(q):
    D,N,C=instance(q)
    pstar=math.log(q/(q-1))/math.log(2)
    assert pstar<=1+1.e-14
    V=len(D)
    H=np.eye(V)-np.ones((V,V))/V
    for factor in (0.6,1.0,1.025):
        p=pstar*factor
        K=np.where(D>0,D.astype(float)**p,0.)
        B=-0.5*H@K@H
        eig=np.linalg.eigvalsh(B)
        if factor<1:
            assert eig[1]>1.e-7,(q,p,eig[:5])
        elif factor==1:
            zero_dim=q if q>=3 else q+q*q-1
            assert np.max(np.abs(eig[:zero_dim+1]))<1.e-8,(q,eig[:zero_dim+2])
            assert eig[zero_dim+1]>1.e-7,(q,eig[:zero_dim+4])
        else:
            assert eig[0]<-1.e-5,(q,eig[:4])
        # Parallel-class differences witness failure beyond pstar.
        if factor>1:
            yy=np.zeros(V);P=q*q; yy[P:P+q]=1;yy[P+q:P+2*q]=-1
            assert yy.sum()==0
            assert yy@K@yy>0
    a=q/(q-1);b=3**pstar
    det=a**3-q*(b-1)**2
    Q=a*(q*q-1)-2*q-2*q*b*(q-1)+q/(q+1)*(a*q*q+a*a*(q-1))
    assert det>-1.e-12 and Q<-1.e-8
    return q,len(D),pstar,det,Q


if __name__=='__main__':
    for q in (2,3,5,7):
        print('OK',check(q))
    print('AFFINE_NEGATIVE_TYPE_CHECK_OK')
