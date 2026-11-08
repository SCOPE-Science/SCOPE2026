"""Reproducible exact finite verification for the ordinary five-cut complex of the cuboctahedral graph (cube line graph).
Python 3, standard library only. All counts are derived afresh from the graph construction.
"""
import itertools, collections
from functools import lru_cache
from fractions import Fraction

N=12
CUBE_EDGES=sorted((i,j) for i in range(8) for j in range(i+1,8) if (i^j).bit_count()==1)
assert len(CUBE_EDGES)==12
ADJ=[set() for _ in range(N)]
for i,e in enumerate(CUBE_EDGES):
    for j in range(i+1,N):
        if set(e)&set(CUBE_EDGES[j]):
            ADJ[i].add(j); ADJ[j].add(i)
assert sum(len(z) for z in ADJ)==48 and all(len(z)==4 for z in ADJ)
FULL=(1<<N)-1

def connected(subset):
    V=[v for v in range(N) if subset&(1<<v)]
    if not V: return False
    seen={V[0]}; todo=[V[0]]
    while todo:
        for v in ADJ[todo.pop()]:
            if (subset>>v)&1 and v not in seen:
                seen.add(v);todo.append(v)
    return len(seen)==len(V)

def facets_and_faces():
    FAC=[]
    for S in itertools.combinations(range(N),5):
        bits=sum(1<<v for v in S)
        if not connected(bits):FAC.append(FULL^bits)
    FACES={0}
    for F in FAC:
        A=F
        while A:
            FACES.add(A);A=(A-1)&F
    return sorted(FAC),FACES
FAC,FACES=facets_and_faces()
assert len(FAC)==516
# Completely independent face membership test: each of 2**12 subsets.
MEMBERS={x for x in range(1<<N) if any((x&f)==x for f in FAC)}
assert MEMBERS==FACES
FV=[sum(int(x.bit_count()==k) for x in FACES) for k in range(1,8)]
assert FV==[12,66,220,495,792,872,516],FV
assert len(FACES)==2974
assert len([x for x in itertools.combinations(range(N),5) if connected(sum(1<<v for v in x))])==276

# Standard lexicographic element matching. 0-face {0} is deliberately kept critical.
def matching(order):
    remaining=set(FACES)-{0}; pairs=[]
    for v in order:
        bit=1<<v
        for a in sorted(remaining):
            b=a|bit
            if a&bit==0 and b in remaining:
                remaining.remove(a);remaining.remove(b);pairs.append((a,b))
    return pairs,remaining

def hasse_check(pairs):
    pset=set(pairs)
    assert len(pset)==len(pairs)
    assert all(a in FACES and b in FACES and b.bit_count()==a.bit_count()+1 and b&a==a for a,b in pairs)
    assert len(set(y for ab in pairs for y in ab))==2*len(pairs)
    # Unmatched Hasse arrows down; matched arrows up. Kahn algorithm checks every incidence.
    verts=FACES-{0}; indegree={x:0 for x in verts}; children={x:[] for x in verts}
    incidences=0
    for upper in verts:
        for v in range(N):
            if not upper>>v&1:continue
            lower=upper^(1<<v)
            if not lower:continue
            incidences+=1
            src,dst=(lower,upper) if (lower,upper) in pset else (upper,lower)
            children[src].append(dst); indegree[dst]+=1
    queue=collections.deque(x for x,d in indegree.items() if d==0)
    visited=0
    while queue:
        x=queue.popleft();visited+=1
        for y in children[x]:
            indegree[y]-=1
            if indegree[y]==0:queue.append(y)
    assert visited==len(verts),(visited,len(verts))
    return incidences

def boundary_matrix(pairs,critical):
    up=dict(pairs);down={b:a for a,b in pairs}
    crit6=sorted(x for x in critical if x.bit_count()==6)
    crit7=sorted(x for x in critical if x.bit_count()==7)
    @lru_cache(None)
    def reduce(a):
        if a in critical:return {a:1}
        if a in down:return {}
        b=up[a]
        vertices=[v for v in range(N) if b>>v&1]
        ia=vertices.index((b^a).bit_length()-1)
        sign_a=(-1)**ia
        result=collections.defaultdict(int)
        for i,v in enumerate(vertices):
            c=b^(1<<v)
            if c==a:continue
            for z,w in reduce(c).items():result[z]-=sign_a*((-1)**i)*w
        return {z:w for z,w in result.items() if w}
    mat=[[0]*len(crit7) for _ in crit6]
    loc={x:i for i,x in enumerate(crit6)}
    for j,a in enumerate(crit7):
        for i,v in enumerate(x for x in range(N) if a>>x&1):
            for z,w in reduce(a^(1<<v)).items():
                if z in loc:mat[loc[z]][j]+=(-1)**i*w
                else:assert z.bit_count()!=6
    return mat,crit6,crit7

def rational_rank(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A);n=len(A[0]) if A else 0;r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if A[i][c]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        a=A[r][c]
        for j in range(c,n):A[r][j]/=a
        for i in range(r+1,m):
            z=A[i][c]
            if z:
                for j in range(c,n):A[i][j]-=z*A[r][j]
        r+=1
        if r==m:break
    return r

def det_int(M):
    assert len(M)==len(M[0]);n=len(M)
    A=[row[:] for row in M]
    if n==0:return 1
    sign=1;prev=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if A[i][k]!=0),None)
        if p is None:return 0
        if p!=k:A[k],A[p]=A[p],A[k];sign*=-1
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=A[i][j]*A[k][k]-A[i][k]*A[k][j]
                assert val%prev==0
                A[i][j]=val//prev
        prev=A[k][k]
        for i in range(k+1,n):A[i][k]=0
    return sign*A[-1][-1]

def unit_minor(M,r):
    nzrows=range(len(M)); nzcols=range(len(M[0]))
    for rows in itertools.combinations(nzrows,r):
        for cols in itertools.combinations(nzcols,r):
            d=det_int([[M[i][j] for j in cols] for i in rows])
            if abs(d)==1:return rows,cols,d
    return None

def mod2_rank_boundary(k):
    lower=sorted(x for x in FACES if x.bit_count()==k)
    upper=sorted(x for x in FACES if x.bit_count()==k+1)
    idx={x:i for i,x in enumerate(lower)};basis={}
    for s in upper:
        col=0
        for v in range(N):
            if s>>v&1:col^=1<<idx[s^(1<<v)]
        while col:
            p=col.bit_length()-1
            if p not in basis:basis[p]=col;break
            col^=basis[p]
    return len(basis)

checks=[]
for ordering in (list(range(N)),list(reversed(range(N)))):
    pairs,crit=matching(ordering)
    inc=hasse_check(pairs)
    M,c6,c7=boundary_matrix(pairs,crit)
    assert len(crit)==len(FACES)-1-2*len(pairs)
    assert sorted(x.bit_count()-1 for x in crit if x.bit_count()!=1)==[5]*len(c6)+[6]*len(c7)
    assert len([x for x in crit if x.bit_count()==1])==1
    assert inc==sum(x.bit_count() for x in FACES if x.bit_count()>1)
    r=rational_rank(M)
    assert r==({0:3,1:1}[len(checks)]),(r,len(checks))
    minor=unit_minor(M,r)
    assert minor is not None
    assert len(c6)-r==12 and len(c7)-r==118
    checks.append((len(pairs),len(c6),len(c7),r,minor,inc,max(abs(x) for row in M for x in row)))

# Simplicial mod-2 ranks as another independent implementation.
r6=mod2_rank_boundary(5)
r7=mod2_rank_boundary(6)
assert FV[5]-r6-r7==12,(r6,r7)
assert FV[6]-r7==118
print('CUBOCTAHEDRAL_FIVECUT_MIXED_WEDGE_VERIFIED')
print('fvector',FV,'facets',len(FAC),'faces_including_empty',len(FACES))
for k,c in enumerate(checks):print('morse',k,'pairs_critical5_critical6_rank_unitminor_incidences_maxcoeff',c)
print('mod2 rank boundary C5->C4',r6,'C6->C5',r7)
print('homotopy type wedge 12 S5 and 118 S6; not shellable')
