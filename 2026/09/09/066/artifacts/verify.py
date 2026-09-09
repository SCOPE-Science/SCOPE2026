"""Independent verifier: brute-force im, QQ-homology (Fraction) Hochster, deletion upper bound."""
from fractions import Fraction
import itertools

def adj_of(n, edges):
    adj=[0]*n
    for u,v in edges:
        adj[u]|=(1<<v); adj[v]|=(1<<u)
    return adj

def im_bruteforce(adj,n):
    E=[]
    for i in range(n):
        for j in range(i+1,n):
            if (adj[i]>>j)&1: E.append((i,j))
    best=0; bestsets=[]
    for r in range(len(E)+1):
        for S in itertools.combinations(E,r):
            verts=set()
            ok=True
            for e in S:
                if e[0] in verts or e[1] in verts: ok=False;break
                verts.add(e[0]); verts.add(e[1])
            if not ok: continue
            for a in range(len(S)):
                for b in range(a+1,len(S)):
                    e1,e2=S[a],S[b]
                    cross=False
                    for x in e1:
                        for y in e2:
                            if (adj[x]>>y)&1: cross=True
                    if cross: ok=False;break
                if not ok: break
            if ok and r>=best:
                if r>best: bestsets=[]
                best=r; bestsets.append(S)
    return best,bestsets[:3]

def rank_Q(mat):
    if not mat or not mat[0]: return 0
    M=[[Fraction(x) for x in row] for row in mat]
    r,c=len(M),len(M[0]); rk=0
    for j in range(c):
        p=None
        for i in range(rk,r):
            if M[i][j]!=0: p=i;break
        if p is None: continue
        M[rk],M[p]=M[p],M[rk]
        iv=M[rk][j]; M[rk]=[x/iv for x in M[rk]]
        for i in range(r):
            if i!=rk and M[i][j]!=0:
                f=M[i][j]; M[i]=[a-f*b for a,b in zip(M[i],M[rk])]
        rk+=1
    return rk

def indep_faces(adj,n,W):
    L=[v for v in range(n) if (W>>v)&1]
    faces={0:[()]}
    for k in range(1,len(L)+1):
        fk=[]
        for c in itertools.combinations(sorted(L),k):
            cs=set(c); ok=True
            for a in c:
                for b in c:
                    if b!=a and ((adj[a]>>b)&1): ok=False;break
                if not ok: break
            if ok: fk.append(tuple(sorted(c)))
        if fk: faces[k]=fk
    return faces

def homology_Q(adj,n,W):
    faces=indep_faces(adj,n,W)
    maxsz=max(faces.keys())
    ranks={}
    for j in range(1,maxsz+1):
        Fk=faces.get(j,[]); Fkm=faces.get(j-1,[])
        if not Fk or not Fkm:
            if j==1: ranks[1]=1 if Fk else 0
            else: ranks[j]=0
            continue
        if j==1:
            ranks[1]=1  # d1: each vertex -> pt; rank 1
            continue
        idx={f:i for i,f in enumerate(Fkm)}
        M=[[0]*len(Fk) for _ in range(len(Fkm))]
        for jj,f in enumerate(Fk):
            for t in range(len(f)):
                g=f[:t]+f[t+1:]
                i=idx.get(g)
                if i is not None: M[i][jj]= 1 if t%2==0 else -1
        ranks[j]=rank_Q(M)
    dims={}
    for k in range(1,maxsz+1):
        Fk=faces.get(k,[])
        if not Fk: continue
        ker=len(Fk)-ranks.get(k,0)
        img=ranks.get(k+1,0)
        if ker-img>0: dims[k-1]=ker-img
    return dims,ranks,{k:len(v) for k,v in faces.items()}

def reg_ub(adj,n,memo=None):
    if memo is None: memo={}
    def R(V):
        if V==0: return 0
        if V in memo: return memo[V]
        has=False
        for v in range(n):
            if (V>>v)&1 and (adj[v]&V): has=True;break
        if not has: memo[V]=0;return 0
        best=min(n,10**9)
        # try every vertex, take min over max (valid upper bound for each v)
        for v in range(n):
            if (V>>v)&1:
                Gv=V^(1<<v); Gn=V&~((1<<v)|(adj[v]&V))
                val=max(R(Gv),R(Gn)+1)
                if val<best: best=val
        memo[V]=best; return best
    return R((1<<n)-1)

def report(n,edges,name):
    adj=adj_of(n,edges)
    im,ims=im_bruteforce(adj,n)
    ub=reg_ub(adj,n)
    W=(1<<n)-1
    dims,ranks,sizes=homology_Q(adj,n,W)
    lb=max([k+1 for k in dims],default=0)
    print(f'== {name} ==')
    print(f'  im={im} e.g.{ims[0] if ims else None}  del-UB={ub}  fullset-Htilde={dims}  LB={lb}')
    print(f'  face sizes={sizes} ranks={ranks}')
    return im,ub,dims

# wedge helpers
def wedge_cycles(ls):
    # cycles of lengths ls sharing vertex 0
    edges=[]; nxt=1
    for L in ls:
        vs=[0]+list(range(nxt,nxt+L-1)); nxt+=L-1
        for i in range(L):
            edges.append((vs[i],vs[(i+1)%L]))
    return nxt,edges

for ls in [(5,5,5),(5,5),(3,3,3),(3,3,5),(5,5,3),(4,4,4),(6,6,6),(5,5,5,5)]:
    n,edges=wedge_cycles(list(ls))
    report(n,edges,f'wedge{ls}')
