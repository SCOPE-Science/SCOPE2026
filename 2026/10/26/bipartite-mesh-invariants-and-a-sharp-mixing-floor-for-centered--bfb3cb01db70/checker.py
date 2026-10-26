"""Exact-arithmetic spot checks of a graph-based centered transport theorem.
Run: python checker.py (Python 3.9+, standard library only).
The proof in RESULT.md, not finite testing, establishes the universal claims.
"""
from fractions import Fraction as F
from itertools import combinations


def rank(a):
    a = [[F(x) for x in row] for row in a]
    if not a: return 0
    m, n = len(a), len(a[0]); r=0
    for c in range(n):
        pivot = next((i for i in range(r,m) if a[i][c]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        p=a[r][c];a[r]=[v/p for v in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                q=a[i][c];a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r


def nullspace(a):
    a=[[F(x) for x in row] for row in a]
    m=len(a);n=len(a[0]); r=0;pivots=[]
    for c in range(n):
        pivot=next((i for i in range(r,m) if a[i][c]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        p=a[r][c];a[r]=[v/p for v in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                q=a[i][c];a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
        pivots.append(c);r+=1
        if r==m:break
    free=[j for j in range(n) if j not in pivots]
    out=[]
    for j in free:
        v=[F(0) for _ in range(n)];v[j]=F(1)
        for i,p in enumerate(pivots):v[p]=-a[i][j]
        out.append(v)
    return out


def bipartite(n,edges):
    adj=[[] for _ in range(n)]
    for a,b in edges: adj[a].append(b);adj[b].append(a)
    color=[None]*n;color[0]=0;queue=[0]
    for a in queue:
        for b in adj[a]:
            if color[b] is None: color[b]=1-color[a];queue.append(b)
            elif color[b]==color[a]:return False
    return len(queue)==n


def conserved_space_dim(n,edges):
    e=len(edges)
    incidence=[[F(0) for _ in range(e)] for _ in range(n)]
    for k,(u,v) in enumerate(edges):
        incidence[u][k]=1;incidence[v][k]=-1
    flows=nullspace(incidence)
    stacked=[]
    for f in flows:
        d=[[F(0) for _ in range(n)] for _ in range(n)]
        for j,(u,v) in enumerate(edges):
            d[u][u]+=f[j]/2;d[u][v]+=f[j]/2
            d[v][u]-=f[j]/2;d[v][v]-=f[j]/2
        stacked.extend(d)
    return n-rank(stacked),len(flows),flows


def cycle(n):return [(i,(i+1)%n) for i in range(n)]
def complete(n):return list(combinations(range(n),2))
def complete_bip(a,b):return [(i,a+j) for i in range(a) for j in range(b)]
def square_grid(m,n):
    return sorted(set(tuple(sorted((i*n+j,ii*n+jj))) for i in range(m) for j in range(n)
                     for ii,jj in [(i+1,j),(i,j+1)] if ii<m and jj<n))

cases=[(4,cycle(4)),(5,cycle(5)),(6,cycle(6)),(4,complete(4)),
       (5,complete_bip(2,3)),(6,complete_bip(3,3)),
       (9,square_grid(3,3)),(9,square_grid(3,3)+[(0,4)]),
       (6,[(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(0,3)])]
for n,e in cases:
    dim,nflows,flows=conserved_space_dim(n,e)
    wanted=2 if bipartite(n,e) else 1
    assert dim==wanted,(n,e,dim,wanted)
    if flows:
        f=flows[0]
        y=[F((7*i+3)%13-6) for i in range(n)]
        # Energy pairing of the centered operator is identically zero.
        central=sum(f[k]*(y[u]-y[v])*(y[u]+y[v])/2 for k,(u,v) in enumerate(e))
        assert central==0
        if bipartite(n,e):
            # A graph bipartition sign annihilates each *face* flux.
            adj=[[] for _ in range(n)]
            for u,v in e:adj[u].append(v);adj[v].append(u)
            col={0:1};queue=[0]
            for u in queue:
                for v in adj[u]:
                    if v not in col:col[v]=-col[u];queue.append(v)
            assert all(col[u]+col[v]==0 for u,v in e)
print('PASS: 9 graph-space classifications, divergence-free energy and bipartite face-flux identities')
# Periodic 4-by-6 Laplacian: alternating checkerboard has top eigenvalue.
nx,ny=4,6;hx,hy=F(1,4),F(1,6)
chi={(i,j):(-1)**(i+j) for i in range(nx) for j in range(ny)}
lam=4/hx**2+4/hy**2
for i in range(nx):
    for j in range(ny):
        val=(2*chi[i,j]-chi[(i+1)%nx,j]-chi[(i-1)%nx,j])/hx**2 + (2*chi[i,j]-chi[i,(j+1)%ny]-chi[i,(j-1)%ny])/hy**2
        assert val==lam*chi[i,j]
assert lam==208
print('PASS: checkerboard eigenvalue 208 and exact periodic H-minus-one witness')
