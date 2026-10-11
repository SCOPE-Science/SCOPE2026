#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

def edge(n,u,v):
    # vertices are (block, local); blocks 0->1->2->0
    bu,iu=divmod(u,n); bv,iv=divmod(v,n)
    if bu==bv:
        m=(n-1)//2
        return 1 <= ((iv-iu)%n) <= m
    return ((bv-bu)%3)==1

def is_transitive(n,face):
    for a,b,c in combinations(face,3):
        tri=(a,b,c)
        deg=[sum(edge(n,x,y) for y in tri if y!=x) for x in tri]
        if sorted(deg)!=[0,1,2]:
            return False
    return True

def faces(n):
    N=3*n
    return [f for r in range(1,N+1) for f in combinations(range(N),r) if is_transitive(n,f)]

def block_faces(n,b):
    vs=range(b*n,(b+1)*n)
    return {f for r in range(1,n+1) for f in combinations(vs,r) if is_transitive(n,f)}

def check_decomposition(n,fs):
    X=[block_faces(n,b) for b in range(3)]
    for f in fs:
        supp={v//n for v in f}
        assert len(supp)<=2
        for b in supp:
            part=tuple(v for v in f if v//n==b)
            assert part in X[b]
    # converse: any union of block faces from an outer edge is transitive
    for a,b in [(0,1),(1,2),(2,0)]:
        for fa in X[a]:
            for fb in X[b]:
                assert tuple(sorted(fa+fb)) in set(fs)

def rank_mod(A,p):
    A=[[(x%p) for x in row] for row in A]
    m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(z*inv)%p for z in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[(A[i][j]-q*A[r][j])%p for j in range(n)]
        r+=1
    return r

def betti(n,fs,p):
    by={d:[f for f in fs if len(f)==d+1] for d in range(max(map(len,fs)))}
    ranks={}
    for d in range(1,max(by)+1):
        rows={f:i for i,f in enumerate(by[d-1])}
        A=[[0]*len(by[d]) for _ in rows]
        for j,f in enumerate(by[d]):
            for i in range(len(f)):
                g=f[:i]+f[i+1:]
                A[rows[g]][j]=1 if i%2==0 else -1
        ranks[d]=rank_mod(A,p)
    return [len(by[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(max(by)+1)]

def main():
    expected={3:None,5:([15,105,315,450,300,75],[1,1,3,3,0,0])}
    for n in (3,5):
        fs=faces(n)
        check_decomposition(n,fs)
        N=3*n
        deg=[sum(edge(n,u,v) for v in range(N) if v!=u) for u in range(N)]
        assert len(set(deg))==1 and deg[0]==(N-1)//2
        common_same=sum(edge(n,0,w) and edge(n,1,w) for w in range(N) if w not in (0,1))
        common_cross=sum(edge(n,0,w) and edge(n,n,w) for w in range(N) if w not in (0,n))
        assert common_same!=common_cross
        fv=[sum(len(f)==d+1 for f in fs) for d in range(max(map(len,fs)))]
        b2=betti(n,fs,2); b3=betti(n,fs,3)
        assert b2==b3
        if n==5:
            assert fv==expected[5][0]
            assert b2==expected[5][1]
        print('n=',n,'faces=',len(fs),'f=',fv,'betti=',b2,'outdegree=',deg[0],
              'common_same=',common_same,'common_cross=',common_cross)
    print('VERIFY_OK')

if __name__=='__main__': main()
