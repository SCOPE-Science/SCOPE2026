from fractions import Fraction as F
from itertools import combinations
from collections import defaultdict

EDGES=list(combinations(range(4),2));eid={p:i for i,p in enumerate(EDGES)}
A=[]
for t in combinations(range(4),3):
  for a,b in combinations(t,2):
    z=[0]*6; z[eid[(a,b)]]=-1
    c=next(v for v in t if v not in (a,b))
    z[eid[tuple(sorted((a,c)))]]=1
    z[eid[tuple(sorted((b,c)))]]=1
    A.append(tuple(z))
assert len(A)==12
# exact rational rref canonical row space, no external dependencies

def rref(rows):
    m=[[F(v) for v in row] for row in rows]; piv=[]
    h=0; N=6
    for j in range(N):
        k=next((i for i in range(h,len(m)) if m[i][j]),None)
        if k is None:continue
        m[h],m[k]=m[k],m[h]
        c=m[h][j];m[h]=[v/c for v in m[h]]
        for i in range(len(m)):
            if i==h:continue
            c=m[i][j]
            if c: m[i]=[v-c*w for v,w in zip(m[i],m[h])]
        piv.append(j);h+=1
        if h==len(m):break
    return tuple(tuple(row) for row in m[:h])

def invert(m):
    n=len(m); X=[list(map(F,row))+[F(i==j) for j in range(n)] for i,row in enumerate(m)]
    for j in range(n):
        k=next(i for i in range(j,n) if X[i][j])
        X[j],X[k]=X[k],X[j];v=X[j][j];X[j]=[x/v for x in X[j]]
        for i in range(n):
            if i!=j:
                v=X[i][j]
                if v:X[i]=[x-v*y for x,y in zip(X[i],X[j])]
    return [row[n:] for row in X]

def projector(B):
    n=len(B)
    if n==0:return [[F(int(i==j)) for j in range(6)] for i in range(6)]
    G=[[sum(B[i][k]*B[j][k] for k in range(6)) for j in range(n)] for i in range(n)]
    Ginv=invert(G)
    return [[F(int(i==j))-sum(B[a][i]*Ginv[a][b]*B[b][j] for a in range(n) for b in range(n)) for j in range(6)] for i in range(6)]

spaces=defaultdict(int)
for mask in range(1<<12):
    B=rref([A[i] for i in range(12) if mask>>i&1]);spaces[B]+=1
assert len(spaces)==466
maxes=defaultdict(F);counts=defaultdict(int);top=[]
for B,n in spaces.items():
    P=projector(B);v=max(sum(abs(x) for x in row) for row in P);r=len(B)
    counts[r]+=n;maxes[r]=max(v,maxes[r]);
    if v==F(8,5):top.append((r,n,B))
assert dict(counts)=={0:1,1:12,2:66,3:238,4:639,5:1345,6:1795}
assert sum(n for r,n,B in top)==52
assert len(spaces)>100
assert len(counts)==7
assert sum(counts.values())==4096
assert max(maxes.values())==F(8,5)
assert dict(maxes)=={0:F(1),1:F(4,3),2:F(3,2),3:F(8,5),4:F(3,2),5:F(10,7),6:F(0)}
# rational witness
idx=(3,8,11);B=[list(A[i]) for i in idx];m=[F(x,11) for x in (2,2,1,2,1,3)]
assert all(sum(A[i][j]*m[j] for j in range(6))==0 for i in idx)
assert all(sum(A[i][j]*m[j] for j in range(6))>0 for i in range(12) if i not in idx)
P=projector(B);rowid=0;v=[F(1) if t>0 else F(-1) for t in P[rowid]]
assert sum(P[rowid][i]*v[i] for i in range(6))==F(8,5)
# residual z=m - eta B^T 1, z'=z+eps v, projection of z'=m+eps P v
eta=F(1,100);eps=F(1,10000)
z=[m[j]-eta*sum(B[i][j] for i in range(3)) for j in range(6)]
pv=[sum(P[j][i]*v[i] for i in range(6)) for j in range(6)]
mprime=[m[j]+eps*pv[j] for j in range(6)]
assert all(x>0 for x in z)
assert all(x>0 for x in [z[i]+eps*v[i] for i in range(6)])
assert all(sum(A[i][j]*mprime[j] for j in range(6))>0 for i in range(12) if i not in idx)
# active multipliers shift via (B B^T) inverse Bv
BB=[[sum(B[i][j]*B[k][j] for j in range(6)) for k in range(3)] for i in range(3)]
IB=invert(BB);bv=[sum(B[i][j]*v[j] for j in range(6)) for i in range(3)]
a=[eta-eps*sum(IB[i][j]*bv[j] for j in range(3)) for i in range(3)]
assert all(q>0 for q in a)
assert all(z[j]+eps*v[j]-mprime[j] == -sum(a[i]*B[i][j] for i in range(3)) for j in range(6))
assert max(abs(t) for t in v)==1
assert max(abs(t) for t in pv)==F(8,5)
print('PASS: all 4096 four-point active subsets and four-point positive sharp witness')

# Exhaustive three-point cone face calculation (the four-point helper
# above is deliberately specialized to six edge coordinates).
E3=list(combinations(range(3),2))
I3={e:i for i,e in enumerate(E3)}
A3=[]
for e in E3:
    rr=[F(1)]*3
    rr[I3[e]]=F(-1)
    A3.append(tuple(rr))

def rref3(rows):
    out=[list(map(F,row)) for row in rows]
    h=0
    for j in range(3):
        i=next((i for i in range(h,len(out)) if out[i][j]),None)
        if i is None: continue
        out[h],out[i]=out[i],out[h]
        v=out[h][j]
        out[h]=[x/v for x in out[h]]
        for k in range(len(out)):
            if k!=h:
                v=out[k][j]
                out[k]=[x-v*y for x,y in zip(out[k],out[h])]
        h+=1
        if h==len(out):break
    return out[:h]

def p3(rows):
    B=rref3(rows)
    r=len(B)
    if not r: return [[F(i==j) for j in range(3)] for i in range(3)]
    G=[[sum(B[i][k]*B[j][k] for k in range(3)) for j in range(r)] for i in range(r)]
    Gi=invert(G)
    return [[F(i==j)-sum(B[a][i]*Gi[a][b]*B[b][j] for a in range(r) for b in range(r)) for j in range(3)] for i in range(3)]

three=[]
for mask in range(8):
    P3=p3([A3[i] for i in range(3) if mask>>i&1])
    three.append(max(sum(abs(z) for z in row) for row in P3))
assert max(three)==F(4,3)
# Witness for a three-point metric: only one inequality active.
tri=[F(2),F(1),F(1)]
normal=[F(-1),F(1),F(1)]
low=[tri[i]-F(1,100)*normal[i] for i in range(3)]
low_prime=[low[i]+F(1,10000) for i in range(3)]
pbase=tri
pper=[tri[i]+F(1,10000)*q for i,q in enumerate([F(4,3),F(2,3),F(2,3)])]
assert all(x>0 for x in low+low_prime+pbase+pper)
assert max(abs(pper[i]-pbase[i]) for i in range(3)) / max(abs(low_prime[i]-low[i]) for i in range(3))==F(4,3)
assert sum(normal[i]*pper[i] for i in range(3))==0
assert all(sum(A3[k][j]*pper[j] for j in range(3))>0 for k in (1,2))
assert all(low_prime[i]-pper[i]==(-F(1,100)+F(1,30000))*normal[i] for i in range(3))
print('PASS: three-point equality witness')
