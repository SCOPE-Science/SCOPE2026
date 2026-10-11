from itertools import combinations
from fractions import Fraction
FACET_TOKENS='124 125 136 138 1310 148 149 157 1510 167 169 235 237 238 246 2410 267 268 2810 356 359 379 3710 456 457 458 479 4710 589 5810 689'.split()
def parse(t):
    return tuple(sorted(tuple(map(int,t[:-2]))+(10,))) if t.endswith('10') else tuple(sorted(map(int,t)))
FACETS=[parse(t) for t in FACET_TOKENS]
VERTS=tuple(range(1,11))

def faces_on(S):
    S=set(S); F=[set() for _ in range(3)]
    for t in FACETS:
        for r in (1,2,3):
            for s in combinations(t,r):
                if set(s)<=S:F[r-1].add(tuple(s))
    return [sorted(x) for x in F]

def rank_q(A):
    if not A:return 0
    M=[[Fraction(x) for x in row] for row in A]
    m=len(M); n=len(M[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if M[i][c]),None)
        if p is None:continue
        M[r],M[p]=M[p],M[r]
        q=M[r][c]; M[r]=[x/q for x in M[r]]
        for i in range(m):
            if i!=r and M[i][c]:
                q=M[i][c]; M[i]=[M[i][j]-q*M[r][j] for j in range(n)]
        r+=1
        if r==m:break
    return r

def betti(S):
    Vf,E,T=faces_on(S); V=[x[0] for x in Vf]; vi={v:i for i,v in enumerate(V)}; ei={e:i for i,e in enumerate(E)}
    d1=[[0]*len(E) for _ in V]
    for j,(a,b) in enumerate(E):d1[vi[a]][j]=-1; d1[vi[b]][j]=1
    d2=[[0]*len(T) for _ in E]
    for j,t in enumerate(T):
        a,b,c=t
        for e,sgn in [((b,c),1),((a,c),-1),((a,b),1)]:d2[ei[e]][j]=sgn
    r1=rank_q(d1);r2=rank_q(d2)
    return (len(V)-r1, len(E)-r1-r2, len(T)-r2), (len(V),len(E),len(T)), (r1,r2)

bfull,fvfull,rfull=betti(VERTS)
assert fvfull==(10,40,31) and bfull==(1,0,0)
prof=[]
for v in VERTS:
    S=[x for x in VERTS if x!=v]
    b,fv,r=betti(S)
    edeg=sum(v in e for e in faces_on(VERTS)[1])
    tdeg=sum(v in t for t in FACETS)
    assert b[0]==1 and b[2]==0 and b[1]>0
    assert b[1]==tdeg-edeg+1
    prof.append((v,edeg,tdeg,b[1],fv[1],fv[2]))
mult={}
for *_,b1,__,___ in prof:mult[b1]=mult.get(b1,0)+1
assert mult=={3:5,2:3,1:2}
print('VERIFY_OK f=10,40,31 full_betti_Q=1,0,0 deletion_b1_multiset=3x5,2x3,1x2')
for row in prof:print('v=%d edge_degree=%d triangle_degree=%d b1=%d deleted_edges=%d deleted_triangles=%d'%row)
