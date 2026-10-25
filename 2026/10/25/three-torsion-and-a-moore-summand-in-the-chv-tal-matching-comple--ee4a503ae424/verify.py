"""Exact finite certificate for the matching complex of the Chvatal graph.

Requires only Python 3.10+ standard library. No graph data downloads.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from hashlib import sha256
import json

EDGES = [
    (0,1), (0,4), (0,6), (0,9), (1,2), (1,5), (1,7),
    (2,3), (2,6), (2,8), (3,4), (3,7), (3,9), (4,5),
    (4,8), (5,10), (5,11), (6,10), (6,11), (7,8),
    (7,11), (8,10), (9,10), (9,11),
]
ORDER = [9,11,10,15,2,13,23,8,14,21,1,0,6,4,3,16,19,17,12,18,5,20,22,7]


def faces_by_size():
    families = {0: [0]}
    for i, (u,v) in enumerate(EDGES):
        # Every new face is an old face plus this edge if endpoints are free.
        for k in sorted(families, reverse=True):
            fresh=[]
            for f in families[k]:
                used=0
                for j, (a,b) in enumerate(EDGES[:i]):
                    if f>>j&1:
                        used |= 1<<a | 1<<b
                if not used & (1<<u | 1<<v):
                    fresh.append(f | 1<<i)
            families.setdefault(k+1, []).extend(fresh)
    for k in families: families[k].sort()
    return families


def oriented_boundary(face):
    for j in range(len(EDGES)):
        if face>>j&1:
            pos = (face & ((1<<j)-1)).bit_count()
            yield face ^ (1<<j), (-1 if pos%2 else 1)


def rank_mod(matrix, prime):
    if not matrix:return 0
    nrows, ncols = len(matrix), len(matrix[0]); a = [[v%prime for v in r] for r in matrix]; p=0
    for col in range(ncols):
        hit=next((i for i in range(p,nrows) if a[i][col]%prime),None)
        if hit is None:continue
        a[p],a[hit]=a[hit],a[p]
        scale=pow(a[p][col],-1,prime)
        a[p]=[(v*scale)%prime for v in a[p]]
        for i in range(p+1,nrows):
            t=a[i][col]
            if t:a[i]=[(x-t*y)%prime for x,y in zip(a[i],a[p])]
        p+=1
        if p==nrows:break
    return p


def exact_det(A):
    # Bareiss integer determinant, with row swaps.
    a=[list(r) for r in A];n=len(a)
    if n==0:return 1
    sign=1;prev=1
    for k in range(n-1):
        pivot=next((r for r in range(k,n) if a[r][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign=-sign
        z=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*z-a[i][k]*a[k][j]
                assert numerator%prev==0
                a[i][j]=numerator//prev
            a[i][k]=0
        prev=z
    return sign*a[-1][-1]


def sparse_rank_boundary_mod(families, degree, p):
    # The degree-d boundary maps (d+1)-edge matchings to d-edge matchings.
    basis = {f:i for i,f in enumerate(families[degree])}
    piv = {}
    for sigma in families[degree+1]:
        vec={basis[tau]:sgn%p for tau,sgn in oriented_boundary(sigma)}
        while vec:
            row=min(vec)
            if row not in piv:
                t=pow(vec[row],-1,p)
                piv[row]={r:(v*t)%p for r,v in vec.items()}
                break
            factor=vec[row]
            for r,v in piv[row].items():
                new=(vec.get(r,0)-factor*v)%p
                if new:vec[r]=new
                else:vec.pop(r,None)
    return len(piv)


def main():
    assert len(EDGES)==24 and len(ORDER)==24 and sorted(ORDER)==list(range(24))
    degree=Counter(v for e in EDGES for v in e)
    assert sorted(degree)==list(range(12)) and set(degree.values())=={4}
    edgeset=set(EDGES)
    assert all(not ({(a,b),(a,c),(b,c)}<=edgeset) for a in range(12)
               for b in range(a+1,12) for c in range(b+1,12))
    F=faces_by_size()
    counts=[len(F.get(k,[])) for k in range(1,7)]
    assert counts==[24,204,752,1175,628,52],counts
    faces=set().union(*(set(F[k]) for k in range(1,7)))
    live=faces.copy(); mate={};pairs=[]
    for j in ORDER:
        lower=sorted((a for a in live if not a>>j&1 and (a|1<<j) in live),
                     key=lambda x:(x.bit_count(),x))
        for a in lower:
            b=a|1<<j
            if a in live and b in live:
                mate[a]=b;mate[b]=a
                live.remove(a);live.remove(b);pairs.append((a,b))
    crit=sorted(live)
    crit_counts=Counter(f.bit_count()-1 for f in crit)
    assert crit_counts=={0:1,3:34,4:6},crit_counts
    assert len(pairs)==1397 and len(faces)==2835
    # Independent acyclicity proof: orient matching Hasse arrows upward,
    # all other Hasse arrows downward; run a complete Kahn topological sort.
    indeg={f:0 for f in faces};targets=defaultdict(list);incidences=0
    for b in faces:
        for a,_ in oriented_boundary(b):
            if a==0:continue
            s,t=(a,b) if mate.get(a)==b else (b,a)
            targets[s].append(t);indeg[t]+=1;incidences+=1
    q=deque(f for f in faces if indeg[f]==0);seen=0
    while q:
        a=q.popleft();seen+=1
        for b in targets[a]:
            indeg[b]-=1
            if indeg[b]==0:q.append(b)
    assert seen==len(faces) and incidences==10816,(seen,incidences)
    @lru_cache(None)
    def project(tau):
        if tau in live:return {tau:1}
        sigma=mate[tau]
        if sigma.bit_count()<tau.bit_count():return {} # upper matched face
        s=dict(oriented_boundary(sigma))[tau]
        ans=defaultdict(int)
        for rho,sign in oriented_boundary(sigma):
            if rho==tau:continue
            for critical,v in project(rho).items():ans[critical]-=s*sign*v
        return {r:v for r,v in ans.items() if v}
    c3=sorted(t for t in crit if t.bit_count()==4)
    c4=sorted(t for t in crit if t.bit_count()==5)
    matrix=[[0]*6 for _ in range(34)];ix={f:i for i,f in enumerate(c3)}
    for j,sigma in enumerate(c4):
        for tau,sign in oriented_boundary(sigma):
            for target,v in project(tau).items():matrix[ix[target]][j]+=sign*v
    assert rank_mod(matrix,3)==5
    assert rank_mod(matrix,2)==6 and rank_mod(matrix,5)==6
    rows5=[6,10,12,20,24];cols5=[0,1,3,4,5]
    rows6=[2,8,9,12,16,20];cols6=list(range(6))
    det5=exact_det([[matrix[r][c] for c in cols5] for r in rows5])
    det6=exact_det([[matrix[r][c] for c in cols6] for r in rows6])
    assert det5==-1 and det6==3,(det5,det6)
    # gcd of maximal 6x6 minors is exactly 3: mod 3 rank=5 means
    # every maximal minor divisible by 3; the displayed one equals 3.
    # The unimodular 5x5 minor forces first five Smith factors to be 1.
    # Therefore the complete Smith list is 1,1,1,1,1,3.
    # Additional direct raw-simplicial-chain check for p=2,3,5.
    raw={}
    for prime in [2,3,5]:
        ranks=[sparse_rank_boundary_mod(F,d,prime) for d in range(1,6)]
        assert ranks==([23,181,571,575,52] if prime==3 else [23,181,571,576,52]),(prime,ranks)
        raw[str(prime)]=ranks
    digest=sha256(json.dumps(matrix,separators=(',',':')).encode()).hexdigest()
    print('VERIFY_OK',json.dumps({
        'face_vector':counts,'matching_pairs':len(pairs),
        'critical_cells':dict(sorted(crit_counts.items())),
        'directed_hasse_arcs':incidences,'acyclic_vertices_checked':seen,
        'morse_boundary_shape':[34,6],'morse_rank_mod_3':5,'morse_rank_mod_2':6,
        'five_minor_det':det5,'six_minor_det':det6,'smith':[1,1,1,1,1,3],
        'field_boundary_ranks':raw,'morse_matrix_sha256':digest
    },sort_keys=True))

if __name__=='__main__':main()
