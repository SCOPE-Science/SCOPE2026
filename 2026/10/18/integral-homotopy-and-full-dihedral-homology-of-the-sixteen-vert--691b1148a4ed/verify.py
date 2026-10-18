"""Reproduce the ordinary matching-complex and dihedral-homology calculation
for the 16-vertex Mobius ladder. Requires only Python 3 standard library.
All assertions are exact finite calculations; no external input files.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

N = 16
EDGES = sorted({tuple(sorted((i, (i+1)%N))) for i in range(N)} |
               {tuple(sorted((i, (i+8)%N))) for i in range(8)})
assert len(EDGES) == 24
EDGE_ID = {e:i for i,e in enumerate(EDGES)}
ORDER = [23,20,5,4,2,14,3,22,13,1,12,17,0,9,7,19,8,11,15,16,6,10,18,21]
P = 97


def faces_by_dimension():
    by_size = {0:[0]}
    for k in range(1,9):
        output=[]
        for face in by_size[k-1]:
            vertices=0
            for i in range(24):
                if face>>i & 1:
                    a,b=EDGES[i]
                    vertices |= (1<<a)|(1<<b)
            begin = face.bit_length()
            for j in range(begin,24):
                u,v=EDGES[j]
                if not vertices & ((1<<u)|(1<<v)):
                    output.append(face|(1<<j))
        if not output: break
        by_size[k]=output
    return {k-1:sorted(v) for k,v in by_size.items() if k>0}

F = faces_by_dimension()
ALL = [f for d in sorted(F) for f in F[d]]
assert len(ALL)==11393
assert [len(F[d]) for d in range(8)]==[24,228,1096,2834,3880,2588,696,47]


def facets(face):
    a=face; i=0
    while a:
        low=a&-a
        yield face ^ low, (-1 if i%2 else 1)
        a-=low;i+=1


def modrank(columns,p):
    pivots={}
    for col in columns:
        col={k:(v%p) for k,v in col.items() if v%p}
        while col:
            j=max(col)
            if j not in pivots:
                c=pow(col[j],-1,p)
                pivots[j]={i:(v*c)%p for i,v in col.items()}
                break
            a=col.pop(j)
            for i,v in pivots[j].items():
                if i==j:continue
                b=(col.get(i,0)-a*v)%p
                if b:col[i]=b
                else:col.pop(i,None)
    return len(pivots)


def boundary_ranks(p):
    ranks={}
    for d in range(1,8):
        irow={x:i for i,x in enumerate(F[d-1])}
        columns=[{irow[g]:s for g,s in facets(x)} for x in F[d]]
        ranks[d]=modrank(columns,p)
    return ranks

R2=boundary_ranks(2)
assert [R2[i] for i in range(1,8)]==[23,205,891,1943,1935,649,47]
assert [len(F[d])-R2.get(d,0)-R2.get(d+1,0) for d in range(8)]==[1,0,0,0,2,4,0,0]
print('F_VECTOR',*[len(F[d]) for d in range(8)])
print('BOUNDARY_RANKS_MOD2',*[R2[d] for d in range(1,8)])


def gradient_matching():
    remain=set(ALL); pairs=[]
    for e in ORDER:
        v=1<<e
        for face in ALL:
            if face not in remain or face & v:continue
            upper=face|v
            if upper in remain:
                remain.remove(face);remain.remove(upper)
                pairs.append((face,upper))
    return remain,pairs

CRIT,PAIRS=gradient_matching()
assert len(PAIRS)==5690
assert Counter(x.bit_count()-1 for x in CRIT)=={0:1,4:5,5:7}
MATCHED=set(PAIRS)

# Exhaustively certify absence of directed cycles after reversing each matching edge.
out=defaultdict(list)
indeg={x:0 for x in ALL}
for upper in ALL:
    if upper.bit_count()==1:continue
    for lower,_ in facets(upper):
        u,v=(lower,upper) if (lower,upper) in MATCHED else (upper,lower)
        out[u].append(v);indeg[v]+=1
queue=deque(u for u in ALL if indeg[u]==0)
count=0
while queue:
    u=queue.popleft();count+=1
    for v in out[u]:
        indeg[v]-=1
        if indeg[v]==0:queue.append(v)
assert count==len(ALL)
print('ACYCLIC_MORSE_MATCHING',len(PAIRS),'CRITICAL',sorted(Counter(f.bit_count()-1 for f in CRIT).items()))

# Signed algebraic cancellation along gradient paths (critical 5-boundaries into
# critical 4-cells). This is independent of mod-2 ranks.
LOW_HIGH=dict(PAIRS)
UPPERS=set(LOW_HIGH.values())
C4=sorted(f for f in CRIT if f.bit_count()==5)
C5=sorted(f for f in CRIT if f.bit_count()==6)
cache={};active=set()

def project4(face):
    if face in cache:return cache[face]
    assert face not in active
    active.add(face)
    if face in C4:ans={face:1}
    elif face in UPPERS:ans={}
    else:
        upper=LOW_HIGH[face]
        coeff=next(s for g,s in facets(upper) if g==face)
        ans=defaultdict(int)
        for g,s in facets(upper):
            if g==face:continue
            for k,a in project4(g).items():ans[k]-=coeff*s*a
        ans={k:v for k,v in ans.items() if v}
    active.remove(face)
    cache[face]=ans
    return ans

A=[]
for x in C5:
    col=defaultdict(int)
    for g,s in facets(x):
        for k,a in project4(g).items():col[k]+=s*a
    A.append([col[y] for y in C4])
assert A==[[0,0,0,0,0],[0,1,0,-1,-1],[0,0,-1,0,1],
           [0,0,-1,0,1],[0,0,0,0,0],[0,0,-1,0,1],[0,1,0,1,0]]


def determinant(mat):
    n=len(mat)
    if n==0:return 1
    if n==1:return mat[0][0]
    return sum((-1)**j * a * determinant([row[:j]+row[j+1:] for row in mat[1:]])
               for j,a in enumerate(mat[0]))

M=[[A[j][i] for j in range(7)] for i in range(5)]
assert determinant([[M[r][c] for c in (1,2,6)] for r in (1,2,4)])==-1
for rows in combinations(range(5),4):
    for cols in combinations(range(7),4):
        assert determinant([[M[r][c] for c in cols] for r in rows])==0
print('MORSE_BOUNDARY_5_BY_7',A)
print('UNIT_THREE_MINOR',(-1),'RANK',3,'INTEGER_HOMOLOGY_H4_2_H5_4')


def edge_permutation(a,reflect):
    v=lambda i:(a-i)%16 if reflect else (a+i)%16
    return [EDGE_ID[tuple(sorted((v(u),v(w))))] for u,w in EDGES]

def signed_action(face,perm):
    jj=[perm[i] for i in range(24) if face>>i & 1]
    sign=(-1)**sum(jj[i]>jj[j] for i in range(len(jj)) for j in range(i+1,len(jj)))
    return sum(1<<j for j in jj),sign

# Independent signed simplicial Lefschetz test for every dihedral automorphism.
for a in range(16):
    for reflect in (False,True):
        perm=edge_permutation(a,reflect)
        L=0
        for d,arr in F.items():
            for f in arr:
                g,s=signed_action(f,perm)
                if f==g:L+=(-1)**d*s
        expect=(1 if a%2==0 else 5) if reflect else ([-1,1,3,1][a%4])
        assert L==expect,(a,reflect,L)
print('D16_SIGNED_LEFSCHETZ_ALL_32_OK')


def orbit_eigen_bases(perm,degree,lam,p):
    seen=set();vecs=[];coordinates={}
    for f in F[degree]:
        if f in seen:continue
        orbit=[];signs=[];g=f
        while g not in seen:
            seen.add(g);orbit.append(g)
            g,s=signed_action(g,perm)
            signs.append(s)
        assert g==f
        product=1
        for s in signs:product*=s
        if (pow(lam,len(orbit),p)-product)%p:continue
        a=1;vec=[]
        for i,h in enumerate(orbit):
            vec.append((h,a))
            a=a*signs[i]*pow(lam,-1,p)%p
        assert a==1
        coordinates[f]=len(vecs);vecs.append(vec)
    return vecs,coordinates


def eigen_homology(perm,lam,p):
    base={d:orbit_eigen_bases(perm,d,lam,p) for d in F}
    ranks={}
    for d in range(1,8):
        rows=base[d-1][1]; cols=[]
        for vec in base[d][0]:
            b=defaultdict(int)
            for f,a in vec:
                for g,s in facets(f):b[g]+=a*s
            cols.append({idx:b[g] for g,idx in rows.items() if b[g]%p})
        ranks[d]=modrank(cols,p)
    return [len(base[d][0])-ranks.get(d,0)-ranks.get(d+1,0) for d in F]

# 8 is a primitive 16th root modulo 97, and 97 is coprime to |D_16|=32.
assert pow(8,16,97)==1 and pow(8,8,97)==-1%97
rot=edge_permutation(1,False)
rot_eigen=[]
for k in range(16):
    hom=eigen_homology(rot,pow(8,k,97),97)
    assert all(h>=0 for h in hom)
    rot_eigen.append((hom[4],hom[5]))
assert [(k,v) for k,v in enumerate(rot_eigen) if v!=(0,0)]==[
    (0,(1,1)),(4,(0,1)),(8,(1,1)),(12,(0,1))]
print('ROTATION_EIGEN_MULTIPLICITIES',[(k,v) for k,v in enumerate(rot_eigen) if v!=(0,0)])

for parity in (0,1):
    refl=edge_permutation(parity,True)
    plus=eigen_homology(refl,1,101)
    minus=eigen_homology(refl,100,101)
    assert (plus[4],minus[4],plus[5],minus[5])==(
        (1,1,2,2) if parity==0 else (2,0,1,3))
    print('REFLECTION_PARITY',parity,'H4_PLUS_MINUS',plus[4],minus[4],
          'H5_PLUS_MINUS',plus[5],minus[5])
print('VERIFY_OK_MOBIUS16_ORDINARY_MATCHING_COMPLEX')
