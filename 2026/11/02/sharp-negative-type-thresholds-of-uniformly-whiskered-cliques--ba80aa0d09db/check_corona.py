"""Independent finite-matrix checks for sharp negative type of complete-graph coronas.

Requires Python 3 with NumPy. Run: python check_corona.py
These checks are supplementary to the analytic proof.
"""
import math
from collections import deque
import numpy as np

LN2=math.log(2.0); LN3=math.log(3.0)

def threshold(n,r):
    assert n>=2 and r>=1
    if n==2 and r==1: return 2.0
    def test(p):
        a=2.0**p;b=3.0**p
        return r*(n-3+(n-1)*(b-2*a))+(r-1)*a
    lo,hi=1.0,2.0
    for _ in range(78):
        mid=(lo+hi)/2
        if test(mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

def graph_distance(n,r):
    N=n*(r+1)
    adjacency=[[] for _ in range(N)]
    def connect(i,j):
        adjacency[i].append(j);adjacency[j].append(i)
    for i in range(n):
        for j in range(i+1,n): connect(i,j)
        for q in range(r): connect(i,n+i*r+q)
    D=np.zeros((N,N),dtype=float)
    for i in range(N):
        seen={i:0};queue=deque([i])
        while queue:
            k=queue.popleft()
            for j in adjacency[k]:
                if j not in seen:
                    seen[j]=seen[k]+1;queue.append(j)
        assert len(seen)==N
        for j,d in seen.items(): D[i,j]=d
    return D

def finite_eigenvalues(D,p):
    N=len(D)
    A=np.where(D>0,D**p,0.)
    J=np.eye(N)-np.ones((N,N))/N
    ev=np.linalg.eigvalsh(J@A@J)
    return ev[-2] if ev[-1] < 1e-10 else ev[-1],ev

def gram_eigenvalues(D,p):
    N=len(D)
    A=np.where(D>0,D**p,0.)
    U=np.linalg.qr(np.column_stack((np.ones(N),np.eye(N)[:,:-1])))[0][:,1:]
    return np.linalg.eigvalsh(-U.T@A@U/2)

def main():
    count=0
    for n in range(2,9):
        for r in range(1,8):
            p=threshold(n,r)
            D=graph_distance(n,r)
            assert np.isclose(p,2.0) if (n,r)==(2,1) else 1.<p<2.
            # Direct full-distance Gram matrix, not the analytic two-block formula.
            for x in [0.0,0.5,1.0,(1+p)/2,p]:
                ev=gram_eigenvalues(D,x)
                zeros=int(np.sum(np.abs(ev)<1e-7))
                required=(2 if (n,r)==(2,1) else 1) if abs(x-p)<1e-8 else 0
                if x==0: required=0
                assert zeros==required,(n,r,x,zeros,required)
                assert ev[0]>-3e-7,(n,r,x,ev[0])
                count+=2
            after=p+min(0.04,(3-p)/3)
            ev=gram_eigenvalues(D,after)
            assert ev[0]<-1e-5,(n,r,p,ev[0]);count+=1
            # At critical p, global balanced load vanishes, and is orthogonal
            # to all other negative eigen-directions.
            v=np.concatenate((-r*np.ones(n),np.ones(n*r)))
            A=D**p
            vv=v@A@v
            assert abs(vv)<2e-7*(1+np.linalg.norm(v)**2),(n,r,vv)
            count+=1
    for n in range(2,20):
        for r in range(1,17):
            p=threshold(n,r)
            if n<19: assert threshold(n+1,r)<p+1e-12
            if r<16: assert threshold(n,r+1)<p+1e-12
            count+=2
    c=3*LN3-4*LN2
    for r in [1,2,4,10]:
        errs=[]
        for n in [200,400,800]:
            p=threshold(n,r)
            approx=1+2/(r*(n-1)*c+2*(r-1)*LN2)
            errs.append(abs(p-approx))
        assert errs[1]<errs[0]*.30 and errs[2]<errs[1]*.30,(r,errs)
        count+=2
    for n in [2,3,6,20]:
        errs=[]
        for r in [200,400,800]:
            p=threshold(n,r)
            approx=1+2/(r*((n-1)*c+2*LN2))
            errs.append(abs(p-approx))
        assert errs[1]<errs[0]*.30 and errs[2]<errs[1]*.30,(n,errs)
        count+=2
    print('PASS',count,'independent checks')

if __name__=='__main__':main()
