#!/usr/bin/env python3
"""Finite integral topological certificate for the first three higher-independence complexes of GP(6,2).

Pure Python 3, standard library only.  Run: python3 verify.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N = 12
EDGES = set()
for i in range(6):
    EDGES.add(tuple(sorted((i, (i+1)%6))))
    EDGES.add((i, i+6))
    EDGES.add(tuple(sorted((6+i, 6+(i+2)%6))))
assert len(EDGES) == 18
ADJ = [0]*N
for a,b in EDGES:
    ADJ[a] |= 1<<b
    ADJ[b] |= 1<<a
assert all(a.bit_count() == 3 for a in ADJ)


def components_at_most(mask, r):
    left=mask
    while left:
        first=left & -left
        active=first
        left ^= first
        comp_count=1
        while active:
            reachable=0
            moving=active
            while moving:
                bit=moving & -moving
                moving ^= bit
                reachable |= ADJ[bit.bit_length()-1]
            reachable &= left
            active = reachable
            left ^= reachable
            comp_count += reachable.bit_count()
            if comp_count > r:
                return False
    return True


def connected(mask):
    if not mask: return False
    first=mask & -mask
    reached=first
    new=first
    while new:
        neighbor=0
        while new:
            b = new & -new
            new ^= b
            neighbor |= ADJ[b.bit_length()-1]
        neighbor &= mask & ~reached
        reached |= neighbor
        new=neighbor
    return reached==mask


def forbidden_sets(r):
    return [sum(1<<v for v in comb) for comb in combinations(range(N), r+1)
            if connected(sum(1<<v for v in comb))]


def get_faces(r):
    forbidden=forbidden_sets(r)
    f=[]
    for mask in range(1<<N):
        test1=components_at_most(mask,r)
        test2=all(mask & bad != bad for bad in forbidden)
        assert test1 == test2, (r,mask)
        if test1:f.append(mask)
    return f, forbidden


def greedy_augmented(F):
    face_set=set(F)
    paired={}
    for v in range(N):
        b=1<<v
        for f in F:
            if f in paired or f&b:continue
            g=f|b
            if g in face_set and g not in paired:
                paired[f]=g
                paired[g]=f
    assert paired[0]==1
    assert paired[1]==0
    del paired[0]
    del paired[1]
    critical=[f for f in F if f and f not in paired]
    return paired,critical


def oriented_boundary(face):
    bits=face
    out=[]
    sign=1
    while bits:
        bit=bits&-bits
        bits ^= bit
        out.append((face^bit,sign))
        sign=-sign
    return out


def acyclic_and_incidence_count(F,paired):
    faces=[f for f in F if f]
    face_set=set(faces)
    successors={f:[] for f in faces}
    indegrees={f:0 for f in faces}
    incidences=0
    for high in faces:
        for low,_ in oriented_boundary(high):
            if not low:continue
            assert low in face_set
            if paired.get(low)==high:
                u,v=low,high
            else:
                u,v=high,low
            successors[u].append(v)
            indegrees[v] +=1
            incidences+=1
    queue=deque(v for v in faces if indegrees[v]==0)
    visited=0
    while queue:
        v=queue.popleft()
        visited +=1
        for w in successors[v]:
            indegrees[w] -=1
            if not indegrees[w]:queue.append(w)
    assert visited==len(faces), ('cyclic',visited,len(faces))
    return incidences


def morse_boundary(paired,crit,low_dimension):
    row_cells=[f for f in crit if f.bit_count()==low_dimension+1]
    col_cells=[f for f in crit if f.bit_count()==low_dimension+2]
    row_index={f:i for i,f in enumerate(row_cells)}
    rows=set(row_cells)

    @lru_cache(None)
    def reduce_face(f):
        if f in rows:return {f:1}
        if f not in paired:return {}
        mate=paired[f]
        if mate.bit_count() < f.bit_count():return {}
        incidence=dict(oriented_boundary(mate))[f]
        assert abs(incidence)==1
        result=defaultdict(int)
        for h,a in oriented_boundary(mate):
            if h==f:continue
            for k,v in reduce_face(h).items():
                result[k] -= incidence*a*v
        return {k:v for k,v in result.items() if v}

    B=[[0]*len(col_cells) for _ in row_cells]
    for j,g in enumerate(col_cells):
        for h,a in oriented_boundary(g):
            for k,v in reduce_face(h).items():
                B[row_index[k]][j] += a*v
    return B


def determinant(A):
    n=len(A)
    assert all(len(row)==n for row in A)
    if n==0:return 1
    M=[row[:] for row in A]
    sgn=1
    prev=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if M[i][k]),None)
        if p is None:return 0
        if p!=k:
            M[p],M[k]=M[k],M[p]
            sgn=-sgn
        pivot=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=M[i][j]*pivot - M[i][k]*M[k][j]
                assert numerator % prev == 0
                M[i][j]=numerator//prev
            M[i][k]=0
        prev=pivot
    return sgn*M[-1][-1]


def mod2_rank(columns):
    basis={}
    for v in columns:
        while v:
            pos=v.bit_length()-1
            if pos not in basis:
                basis[pos]=v
                break
            v ^= basis[pos]
    return len(basis)


def full_mod2_betti(F):
    faces_by_dim=defaultdict(list)
    for face in F:
        if face:faces_by_dim[face.bit_count()-1].append(face)
    dims=sorted(faces_by_dim)
    ranks={}
    for d in dims:
        if d==0:
            ranks[d]=0
            continue
        lower=faces_by_dim[d-1]
        row_ids={f:i for i,f in enumerate(lower)}
        columns=[]
        for upper in faces_by_dim[d]:
            vec=0
            for f,_ in oriented_boundary(upper):
                vec ^= 1<<row_ids[f]
            columns.append(vec)
        ranks[d]=mod2_rank(columns)
    bettis={d:len(faces_by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in dims}
    assert bettis[0]==1
    return {d:b for d,b in bettis.items() if b and d!=0},ranks


def main():
    expected={
        1:dict(faces=171,crit={0:1,2:1},homology={2:1}),
        2:dict(faces=810,crit={0:1,3:4,4:2},homology={3:3,4:1}),
        3:dict(faces=1469,crit={0:1,3:1,4:8,5:16},homology={5:9}),
    }
    for r in (1,2,3):
        F,forbidden=get_faces(r)
        match,critical=greedy_augmented(F)
        assert len(F)==expected[r]['faces']
        crit_count=dict(Counter(f.bit_count()-1 for f in critical))
        assert crit_count==expected[r]['crit'],(r,crit_count)
        edges=acyclic_and_incidence_count(F,match)
        bettis,full_ranks=full_mod2_betti(F)
        assert bettis==expected[r]['homology'],(r,bettis)
        mats={}
        for d in sorted(crit_count):
            if d>0 and d+1 in crit_count:
                mats[d]=morse_boundary(match,critical,d)
        if r==2:
            assert mats[3]==[[-1,-1],[0,0],[0,0],[0,0]]
            assert determinant([[-1]])==-1
        if r==3:
            assert mats[3]==[[-1,1,0,0,0,1,0,-1]]
            B=mats[4]
            assert len(B)==8 and all(len(row)==16 for row in B)
            assert [sum(mats[3][0][k]*B[k][j] for k in range(8)) for j in range(16)]==[0]*16
            cols=[0,1,2,3,4,5,8]
            sub=[[B[i][j] for j in cols] for i in range(1,8)]
            assert determinant(sub)==1,determinant(sub)
        print('r=%d faces=%d forbidden_connected_%d=%d ordinary_matching_pairs=%d directed_hasse_incidences=%d critical=%s full_mod2_betti=%s'%(r,len(F),r+1,len(forbidden),len(match)//2,edges,crit_count,bettis))
        print('r=%d mod2_boundary_ranks=%s'%(r,dict(sorted(full_ranks.items()))))
        for d,B in mats.items():print('r=%d integral_morse_boundary_%d_to_%d=%s'%(r,d+1,d,B))
    print('DURER_INITIAL_HIGHER_INDEPENDENCE_INTEGRAL_OK')

if __name__=='__main__':main()
