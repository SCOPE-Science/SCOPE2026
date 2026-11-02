from fractions import Fraction
from math import gcd
import numpy as np

def predicted(n,s,r):
    g=gcd(2*s-1,n)
    ans=2*n-g+1
    if r==1:
        ans-=int(n%2==0)
        ans-=int(n%3==0 and (2*s-1)%3!=0)
    if r==Fraction(3,2):
        ans-=int(n%3==0)
    return ans

def make_scaled_laplacian(n,r):
    a,b=r.numerator,r.denominator
    N=2*n
    E=[]
    for row in range(2):
        for j in range(n-1): E.append((row*n+j,row*n+j+1,b))
    for j in range(n): E.append((j,n+j,a))
    L=np.zeros((N,N), dtype=np.int64)
    for i,j,w in E:
        L[i,i]+=w; L[j,j]+=w; L[i,j]-=w; L[j,i]-=w
    return L

def modular_rank(A,n,s,p):
    N=2*n
    v=np.zeros(N,dtype=np.int64);v[s-1]=1
    K=np.zeros((N,N),dtype=np.int64)
    for k in range(N):
        K[:,k]=v
        v=(A@v)%p
    rank=0
    for c in range(N):
        loc=np.flatnonzero(K[rank:,c]%p)
        if len(loc)==0: continue
        pivot=rank+int(loc[0]);K[[rank,pivot]]=K[[pivot,rank]]
        K[rank,c:]=(K[rank,c:]*pow(int(K[rank,c]),-1,p))%p
        for i in range(rank+1,N):
            f=K[i,c]
            if f: K[i,c:]=(K[i,c:]-f*K[rank,c:])%p
        rank+=1
        if rank==N:break
    return rank

if __name__=='__main__':
    weights=[Fraction(1),Fraction(3,2),Fraction(4,3),Fraction(5,2),Fraction(7,4),Fraction(2),Fraction(9,7)]
    cnt=0
    for n in range(2,21):
        for r in weights:
            A=make_scaled_laplacian(n,r)
            for s in sorted({1,2,(n+1)//2,n}):
                want=predicted(n,s,r)
                got=modular_rank(A,n,s,1000003)
                assert got==want, (n,s,r,want,got)
                cnt+=1
    print('PASS',cnt,'independent modular Krylov ranks; n=2..20; 7 rational rung weights; representative vertices')
