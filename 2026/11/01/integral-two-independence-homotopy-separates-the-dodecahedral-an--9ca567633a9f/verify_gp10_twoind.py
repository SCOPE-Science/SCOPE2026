#!/usr/bin/env python3
"""Exact finite verification for the second independence complexes of GP(10,2), GP(10,3).

Requires only Python 3.10+ (standard library). All graph, chain and matching
objects are rebuilt from definitions. Cell signs use ascending vertex order.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations

EXPECTED = {
    2: {
        'faces': 63142,
        'f': [20,190,1080,3985,9772,15870,16640,10770,4000,750,60,5],
        'pairs': 31565,
        'critical': {0:1,5:1,6:6,7:4},
        'ranks': [19,171,909,3076,6696,9174,7465,3305,695,55,5],
        'betti': {6:1},
        'morse': {(6,5):[[0,0,-1,0,1,0]],
                  (7,6):[[1,1,0,0],[0,0,0,-1],[0,1,0,0],
                         [0,-1,1,0],[0,1,0,0],[0,0,-1,0]]},
    },
    3: {
        'faces': 62048,
        'f': [20,190,1080,3985,9784,15910,16600,10390,3460,564,60,5],
        'pairs': 31000,
        'critical': {0:1,6:3,7:44},
        'ranks': [19,171,909,3076,6708,9202,7398,2951,509,55,5],
        'betti': {7:41},
    }
}

def generalized_petersen(n, k):
    a=[0]*(2*n)
    def edge(i,j):
        assert i!=j
        a[i] |= 1<<j
        a[j] |= 1<<i
    for i in range(n):
        edge(i,(i+1)%n)
        edge(i,i+n)
        edge(i+n,n+(i+k)%n)
    assert len(a)==2*n and all(z.bit_count()==3 for z in a)
    assert sum(z.bit_count() for z in a)//2==3*n
    return a

def is_face(mask, adjacent):
    """Each induced connected component has at most two vertices iff max degree <=1."""
    t=mask
    while t:
        one=t & -t; t-=one
        neighbors=mask & adjacent[one.bit_length()-1]
        if neighbors & (neighbors-1):return False
    return True

def enumerate_faces(adj):
    F=[s for s in range(1<<len(adj)) if is_face(s,adj)]
    f=Counter(s.bit_count()-1 for s in F if s)
    return F,f

def signed_boundary(s):
    t=s; j=0
    while t:
        bit=t & -t; t-=bit
        yield s^bit, -1 if j&1 else 1
        j+=1

def staged_matching(faces, n):
    """Pair an unpaired face s with s union {v}, for v=0,...,n-1."""
    R=set(faces)
    pairs={}
    for v in range(n):
        bit=1<<v
        todo=[s for s in R if not s&bit and s|bit in R]
        for s in todo:
            R.remove(s);R.remove(s|bit);pairs[s]=s|bit
    # Turn the empty-face pair into a critical base vertex.
    assert 0 in pairs
    vertex=pairs.pop(0)
    R.update((0,vertex))
    assert len(faces)==2*len(pairs)+len(R)
    assert 0 in R and vertex.bit_count()==1
    return pairs,R

def verify_acyclicity(faces,pairs):
    """Kahn check of the full *nonempty* Hasse graph, reverse paired edges."""
    V=set(faces);V.remove(0)
    upper_to_lower={v:k for k,v in pairs.items()}
    indeg={u:0 for u in V}
    edges=0
    for high in V:
        for low,_ in signed_boundary(high):
            if not low:continue
            edges+=1
            if pairs.get(low)==high:indeg[high]+=1
            else:indeg[low]+=1
    queue=deque(u for u,d in indeg.items() if d==0)
    count=0
    while queue:
        u=queue.popleft();count+=1
        if u in pairs:
            t=pairs[u];indeg[t]-=1
            if indeg[t]==0:queue.append(t)
        paired_low=upper_to_lower.get(u)
        for low,_ in signed_boundary(u):
            if low and low!=paired_low:
                indeg[low]-=1
                if indeg[low]==0:queue.append(low)
    assert count==len(V),('closed gradient cycle',count,len(V))
    assert all(d==0 for d in indeg.values())
    return edges

def critical_dimensions(crit):
    C=defaultdict(list)
    for s in crit:
        if s:C[s.bit_count()-1].append(s)
    for L in C.values():L.sort()
    return C

def morse_boundary(pairs, crit_by_dim, degree):
    """Signed cancellation recursion: critical degree -> critical degree-1."""
    ups={u:l for l,u in pairs.items()}
    lows=crit_by_dim[degree-1]
    highs=crit_by_dim[degree]
    low_set=set(lows)
    @lru_cache(None)
    def reduce_face(s):
        if s in low_set:return {s:1}
        if s in ups:return {}
        assert s in pairs, ('noncritical, unmatched',s)
        top=pairs[s]
        added=top^s
        incidence=-1 if ((top & (added-1)).bit_count()&1) else 1
        out={}
        for face,coefficient in signed_boundary(top):
            if face==s:continue
            for target,val in reduce_face(face).items():
                out[target]=out.get(target,0)-incidence*coefficient*val
        return {a:b for a,b in out.items() if b}
    mat=[[0]*len(highs) for _ in lows]
    pos={v:i for i,v in enumerate(lows)}
    for j,high in enumerate(highs):
        for face,sgn in signed_boundary(high):
            for low,val in reduce_face(face).items():
                mat[pos[low]][j]+=sgn*val
    return mat

def determinant(M):
    n=len(M)
    assert all(len(r)==n for r in M)
    if not n:return 1
    if n==1:return M[0][0]
    return sum((-1 if j&1 else 1)*v*determinant([row[:j]+row[j+1:] for row in M[1:]])
               for j,v in enumerate(M[0]) if v)

def submatrix(M,rows,cols):
    return [[M[i][j] for j in cols] for i in rows]

def matrix_multiply(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def verify_integer_matrices(k,M):
    if k==2:
        a=M[(6,5)];b=M[(7,6)]
        assert a==EXPECTED[2]['morse'][(6,5)] and b==EXPECTED[2]['morse'][(7,6)]
        assert matrix_multiply(a,b)==[[0]*4]
        assert a[0][2]==-1
        assert determinant(submatrix(b,[0,1,2,3],[0,1,2,3]))==-1
        # The two primitive maps have ranks 1 and 4; their composition is zero.
        return {'d6_shape':[1,6],'d7_shape':[6,4],
                'unit_minor_d6':-1,'unit_minor_d7':-1}
    b=M[(7,6)]
    assert len(b)==3 and len(b[0])==44
    assert determinant(submatrix(b,[0,1,2],[0,3,14]))==-1
    # A 3x44 matrix cannot have rank larger than three. The unit minor proves
    # rank exactly three, a saturated image, and no integral torsion.
    return {'d7_shape':[3,44], 'unit_minor_d7':-1}

def boundary_ranks_mod_two(faces):
    buckets=defaultdict(list)
    for s in faces:
        if s:buckets[s.bit_count()-1].append(s)
    rank={}
    for d in range(1,max(buckets)+1):
        pos={s:j for j,s in enumerate(buckets[d-1])}
        pivots={}
        for s in buckets[d]:
            col=0
            for face,_ in signed_boundary(s):col ^= 1<<pos[face]
            while col:
                bit=col.bit_length()-1
                if bit not in pivots:
                    pivots[bit]=col;break
                col ^= pivots[bit]
        rank[d]=len(pivots)
    reduced={d:len(L)-rank.get(d,0)-rank.get(d+1,0) for d,L in buckets.items()}
    reduced[0]-=1
    return rank,reduced

def check(k):
    target=EXPECTED[k]
    adj=generalized_petersen(10,k)
    faces,fvec=enumerate_faces(adj)
    assert len(faces)-1==target['faces']
    assert [fvec[i] for i in range(12)]==target['f']
    pairs,critical=staged_matching(faces,20)
    assert len(pairs)==target['pairs']
    C=critical_dimensions(critical)
    assert {d:len(a) for d,a in C.items()}==target['critical']
    incidences=verify_acyclicity(faces,pairs)
    matrix={}
    for d in sorted(C):
        if d-1 in C:
            matrix[(d,d-1)]=morse_boundary(pairs,C,d)
    matrix_checks=verify_integer_matrices(k,matrix)
    ranks, betti=boundary_ranks_mod_two(faces)
    assert [ranks[d] for d in range(1,12)]==target['ranks']
    assert {d:v for d,v in betti.items() if v}==target['betti']
    assert sum((-1)**d*fvec[d] for d in fvec)==sum((-1)**d*r for d,r in betti.items())+1
    print(f'GP(10,{k}): nonempty_faces={len(faces)-1}, incidences={incidences}, matched_pairs={len(pairs)}')
    print(f'  critical={dict(sorted((d,len(s)) for d,s in C.items()))}, exact_boundaries={matrix_checks}')
    print(f'  mod2_boundary_ranks={[ranks[d] for d in range(1,12)]}')
    print(f'  reduced_integral_homology: degree {6 if k==2 else 7}, rank {1 if k==2 else 41}, torsion-free')

if __name__=='__main__':
    check(2)
    check(3)
    print('GP10_TWO_INDEPENDENCE_INTEGRAL_HOMOTOPY_CERTIFICATE_OK')
