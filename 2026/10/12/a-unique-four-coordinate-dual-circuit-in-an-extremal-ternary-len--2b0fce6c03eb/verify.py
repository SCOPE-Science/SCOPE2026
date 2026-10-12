#!/usr/bin/env python3
from itertools import combinations, product
from math import comb

Q=3
N=25
G=[
[1,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,1,1,0,0,1,2,2,2,1],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,2,2,1,2,0,2,2,0,1],
[0,0,1,0,0,0,0,0,0,0,0,0,2,1,0,0,1,1,0,0,0,2,1,2,2],
[0,0,0,1,0,0,0,0,0,0,0,0,2,0,1,2,2,0,2,2,2,2,1,1,1],
[0,0,0,0,1,0,0,0,0,0,0,0,2,0,0,1,2,0,0,1,2,2,0,2,2],
[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,2,2,2,0,1,2,2],
[0,0,0,0,0,0,1,0,0,0,0,0,2,1,1,0,0,0,0,1,2,0,1,2,1],
[0,0,0,0,0,0,0,1,0,0,0,0,2,2,1,1,0,0,2,2,2,1,2,2,2],
[0,0,0,0,0,0,0,0,1,0,0,0,2,2,2,2,1,2,0,2,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,0,0,1,0,2,0,2,0,0,1,2,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,2,2,1,1,0,2,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,0,2,1,0,0,2,2,1,0,1,0,2,1],
]
EXPECTED_C={0:1,9:2158,12:39522,15:202272,18:236692,21:49992,24:804}
EXPECTED_D={0:1,4:2,7:168,9:2158,10:12828,12:39522,13:159908,15:202272,16:504408,18:236692,19:348936,21:49992,22:36560,24:804,25:72}
EXPECTED_NORMALIZED_W4=((0,18,19,20),(1,2,2,2))

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))%3

def rank_mod3(A):
    A=[row[:] for row in A]
    if not A: return 0
    m,n=len(A),len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]%3),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        if A[r][c]%3==2: A[r]=[(2*x)%3 for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%3:
                f=A[i][c]%3
                A[i]=[(x-f*y)%3 for x,y in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r

def enumerate_primal():
    counts=[0]*(N+1)
    v=[0]*N
    wt=0
    def add_row(row):
        nonlocal wt
        for j,a in enumerate(row):
            if not a: continue
            old=v[j]
            new=(old+a)%3
            if old==0 and new!=0: wt+=1
            elif old!=0 and new==0: wt-=1
            v[j]=new
    def dfs(i):
        if i==len(G):
            counts[wt]+=1
            return
        dfs(i+1)
        add_row(G[i]); dfs(i+1)
        add_row(G[i]); dfs(i+1)
        add_row(G[i])
    dfs(0)
    return {i:c for i,c in enumerate(counts) if c}

def kraw(j,i):
    s=0
    for t in range(j+1):
        if t<=i and j-t<=N-i:
            s += (-1)**t*(Q-1)**(j-t)*comb(i,t)*comb(N-i,j-t)
    return s

def macwilliams(A):
    size=sum(A.values())
    B={}
    for j in range(N+1):
        num=sum(A.get(i,0)*kraw(j,i) for i in range(N+1))
        assert num%size==0
        b=num//size
        assert b>=0
        if b: B[j]=b
    return B

def normalized_low_dual(max_weight=4):
    cols=[[G[r][c] for r in range(12)] for c in range(N)]
    found=[]
    for s in range(1,max_weight+1):
        for supp in combinations(range(N),s):
            # Projective normalization: first coefficient is 1.
            for tail in product((1,2), repeat=s-1):
                coeff=(1,)+tail
                z=[0]*12
                for a,c in zip(coeff,supp):
                    col=cols[c]
                    for r in range(12): z[r]=(z[r]+a*col[r])%3
                if not any(z): found.append((supp,coeff))
    return found

def main():
    assert len(G)==12 and all(len(r)==25 for r in G)
    assert rank_mod3(G)==12
    assert all(dot(a,b)==0 for a in G for b in G)
    A=enumerate_primal()
    assert A==EXPECTED_C, (A,EXPECTED_C)
    assert sum(A.values())==3**12
    assert min(w for w in A if w)>0 and min(w for w in A if w)==9
    B=macwilliams(A)
    assert B==EXPECTED_D, (B,EXPECTED_D)
    assert sum(B.values())==3**13
    lows=normalized_low_dual(4)
    assert lows==[EXPECTED_NORMALIZED_W4], lows
    assert B.get(1,0)==B.get(2,0)==B.get(3,0)==0 and B[4]==2
    print('rank=12 self_orthogonal=yes')
    print('W_C='+str(A))
    print('W_Cperp='+str(B))
    print('normalized_weight4_dual='+str(lows[0]))
    print('unique_weight4_support_1based='+str(tuple(i+1 for i in lows[0][0])))
    print('VERIFY_OK')
if __name__=='__main__': main()
