#!/usr/bin/env python3
"""Exact finite certificate for the ordinary matching complex of the 4-by-4 grid."""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N=4
EDGES=[]
for row in range(N):
    for col in range(N):
        u=row*N+col
        if row+1<N: EDGES.append((u,(row+1)*N+col))
        if col+1<N: EDGES.append((u,row*N+col+1))
MASKS=[(1<<u)|(1<<v) for u,v in EDGES]
assert len(MASKS)==24
ORDER=[23,17,21,10,5,11,14,20,9,7,6,12,22,19,3,0,1,2,13,16,4,8,18,15]
assert sorted(ORDER)==list(range(24))

def faces_build():
    faces=[0]
    used=[0]
    for j,pair in enumerate(MASKS):
        add=[(face|(1<<j),mask|pair) for face,mask in zip(faces,used) if not mask&pair]
        faces.extend(face for face,_ in add)
        used.extend(mask for _,mask in add)
    return faces

def boundary(simplex):
    indices=[i for i in range(24) if simplex&(1<<i)]
    return [(simplex^(1<<i),-1 if p%2 else 1) for p,i in enumerate(indices)]

def verify():
    faces=faces_build()
    assert len(faces)==len(set(faces))==10012
    face_set=set(faces)
    count=Counter(f.bit_count()-1 for f in faces)
    assert [count[d] for d in range(-1,8)]==[1,24,224,1044,2593,3388,2150,552,36]
    remains=set(faces)
    matched_lower={}
    matched_upper={}
    for edge in ORDER:
        b=1<<edge
        for f in faces:
            if not(f&b) and f in remains and (f|b) in remains:
                remains.remove(f);remains.remove(f|b)
                matched_lower[f]=f|b
                matched_upper[f|b]=f
    assert len(matched_lower)==5002
    # Removing the empty-face pair leaves one critical vertex and an ordinary Morse matching.
    assert 0 in matched_lower and matched_lower[0].bit_count()==1
    assert len(remains)==8
    critical=Counter(f.bit_count()-1 for f in remains)
    assert critical=={4:6,5:2}, critical
    # Hasse diagram: default high -> low; paired edges reversed low -> high.
    indegree={f:0 for f in faces}
    outgoing=defaultdict(list)
    arcs=0
    for upper in faces:
        for lower,sgn in boundary(upper):
            if upper in matched_upper and matched_upper[upper]==lower:
                u,v=lower,upper
            else:
                u,v=upper,lower
            outgoing[u].append(v)
            indegree[v]+=1
            arcs+=1
    Q=deque(f for f in faces if indegree[f]==0)
    processed=0
    while Q:
        f=Q.popleft();processed+=1
        for g in outgoing[f]:
            indegree[g]-=1
            if indegree[g]==0:Q.append(g)
    assert processed==len(faces), (processed,len(faces))
    critical_4=sorted(f for f in remains if f.bit_count()==5)
    critical_5=sorted(f for f in remains if f.bit_count()==6)

    @lru_cache(None)
    def reduction(lower):
        assert lower.bit_count()==5
        if lower in remains:return {lower:1}
        if lower in matched_upper:return {}
        upper=matched_lower[lower]
        assert upper.bit_count()==6
        coef=dict(boundary(upper))[lower]
        out=defaultdict(int)
        for other,sign in boundary(upper):
            if other!=lower:
                for target,amount in reduction(other).items():
                    out[target]-=sign*coef*amount
        return {k:v for k,v in out.items() if v}

    matrix=[]
    for top in critical_5:
        totals=defaultdict(int)
        for low,sign in boundary(top):
            for target,amount in reduction(low).items():
                totals[target]+=sign*amount
        matrix.append([totals[k] for k in critical_4])
    assert matrix==[[0]*6,[0]*6],matrix
    print('VERIFY_OK', 'faces',len(faces),'augmented_matching_pairs',len(matched_lower),'ordinary_matching_pairs',len(matched_lower)-1,'critical_vertices',1,'critical_dimensions',dict(critical),'hasse_arcs',arcs,'acyclic_processed',processed,'integer_morse_boundary',matrix)
    return True

if __name__=='__main__':verify()
