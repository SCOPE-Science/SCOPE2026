"""Exact rational checks for weighted-star copying and ancestral-pair response."""
from fractions import Fraction as F
from itertools import combinations

def solve(A,b):
    A=[list(map(F,row))+[F(v)] for row,v in zip(A,b)]
    n=len(A)
    for j in range(n):
        k=next(k for k in range(j,n) if A[k][j]);A[j],A[k]=A[k],A[j]
        v=A[j][j];A[j]=[x/v for x in A[j]]
        for k in range(n):
            if k!=j:
                v=A[k][j]
                if v:A[k]=[x-v*y for x,y in zip(A[k],A[j])]
    return [row[-1] for row in A]

def check(weights):
    w=list(map(F,weights));N=len(w)+1;W=[[F(0) for _ in range(N)] for _ in range(N)]
    for a,v in enumerate(w,1):W[0][a]=W[a][0]=v
    d=[sum(row) for row in W];P=[[W[i][j]/d[i] for j in range(N)] for i in range(N)]
    pairs=list(combinations(range(N),2));key={x:i for i,x in enumerate(pairs)}
    A=[[F(0) for _ in pairs] for _ in pairs]
    for row,(i,j) in enumerate(pairs):
        for u,z in ((i,j),(j,i)):
            for v in range(N):
                if not W[u][v]:continue
                A[row][row]+=W[u][v]
                if v!=z:A[row][key[tuple(sorted((v,z)))]]-=W[u][v]
    Tvec=solve(A,[F(1)]*len(pairs));T=lambda i,j:F(0) if i==j else Tvec[key[tuple(sorted((i,j)))]]
    K=[[W[i][j]-sum(W[i][q]*P[q][j] for q in range(N)) for j in range(N)] for i in range(N)]
    ub_pair=-sum(K[i][j]*T(i,j) for i in range(N) for j in range(N))/N**2
    Astar=[T(0,a) for a in range(1,N)]
    assert all(w[a-1]*Astar[a-1]>F(1,2) for a in range(1,N))
    assert all(Astar[a-1]+Astar[b-1]>T(a,b) for a in range(1,N) for b in range(a+1,N))
    S=(2*sum(w[a-1]**2*Astar[a-1] for a in range(1,N))+
       sum(w[a-1]*w[b-1]*(Astar[a-1]+Astar[b-1]-T(a,b)) for a in range(1,N) for b in range(1,N) if a!=b))/sum(w)
    assert ub_pair==-S/N**2 and S>F(1)
    mixed=list(range(1,(1<<N)-1));ind={v:j for j,v in enumerate(mixed)}
    H=[[F(0) for _ in mixed] for _ in mixed];benefit=[];cost=[]
    for idx,v in enumerate(mixed):
        n=[(v>>i)&1 for i in range(N)];f=[sum(P[i][j]*n[j] for j in range(N)) for i in range(N)]
        zb=F(0);zc=F(0)
        for i in range(N):
            for j in range(N):
                if not W[i][j] or n[i]==n[j]:continue
                vv=v^(1<<j);H[idx][idx]+=W[i][j]
                if vv in ind:H[idx][ind[vv]]-=W[i][j]
                zb+=W[i][j]*f[i]*(n[i]-n[j])/N
                zc-=W[i][j]*n[i]*(n[i]-n[j])/N
        benefit.append(zb);cost.append(zc)
    ub=solve(H,benefit);uc=solve(H,cost)
    ub_avg=sum(ub[ind[1<<i]] for i in range(N))/N
    uc_avg=sum(uc[ind[1<<i]] for i in range(N))/N
    assert ub_avg==ub_pair and uc_avg<0
    print(f'N={N}, weights={weights}, benefit_slope={ub_avg}, cost_slope={uc_avg}, S={S}')

if __name__=='__main__':
    for w in [(1,1),(1,1,1),(1,2,4),(1,2,4,8)]:check(w)
    print('exact-rational verification: PASS')
