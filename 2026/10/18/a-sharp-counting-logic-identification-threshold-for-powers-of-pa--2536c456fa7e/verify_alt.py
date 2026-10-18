"""Independent adjacency-matrix refinement implementation and finite threshold checks."""
from collections import Counter

def pair(n,k):
    a=[[int(0<abs(i-j)<=k) for j in range(n)] for i in range(n)]
    b=[r[:] for r in a]
    if k>=2 and n>=k+5:
        for i,j in ((0,2),(n-1,n-3)):b[i][j]=b[j][i]=0
        for i,j in ((0,n-3),(n-1,2)):b[i][j]=b[j][i]=1
    return a,b

def rounds(A,B):
    n=len(A)
    # recursively intern fingerprints with synchronized names on both structures.
    z=[[0]*n,[0]*n]
    for rr in range(n+2):
        raw=[]
        for mat,labels in ((A,z[0]),(B,z[1])):
            for v in range(n):
                nums=tuple(sorted(Counter(labels[w] for w in range(n) if mat[v][w]).items()))
                raw.append((labels[v],nums))
        names={t:i for i,t in enumerate(sorted(set(raw)))}
        out=[[names[t] for t in raw[:n]],[names[t] for t in raw[n:]]]
        if Counter(out[0])!=Counter(out[1]):return False
        if out==z:return True
        z=out
    raise AssertionError('round bound')

def small_signature(n,k):
    A,_=pair(n,k)
    if n<=k+1:
        assert sum(A[0])==n-1;return
    t=n-k-1
    groups=[(i,n-1-i) for i in range(t)]
    center=list(range(t,n-t))
    assert all(all(A[u][v]==1 for v in center if v!=u) for u in range(n))
    match_edges=[]
    for a in range(t):
      for b in range(a+1,t):
        block=[[A[u][v] for v in groups[b]] for u in groups[a]]
        if a+b>=t:assert block==[[1,1],[1,1]]
        else:
            assert block==[[1,0],[0,1]]
            match_edges.append((a,b))
    assert not (t==3 and len(match_edges)!=2)

for k in range(1,18):
  for n in range(1,75):
    A,B=pair(n,k)
    if n<=k+4 and k>=2:small_signature(n,k)
    assert rounds(A,B)
    if n>=k+5 and k>=2:
        X=[(i,n-1-i) for i in range(3)]
        def rainbow(mat):
            return sum(mat[a][b]*mat[b][c]*mat[c][a] for a in X[0] for b in X[1] for c in X[2])
        assert rainbow(A)==2 and rainbow(B)==0
print('ALT_VERIFY_OK',{'k_max':17,'n_max':74})
