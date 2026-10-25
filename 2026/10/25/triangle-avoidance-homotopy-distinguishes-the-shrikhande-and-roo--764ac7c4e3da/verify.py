#!/usr/bin/env python3
"""Self-contained exact verification of two induced-triangle-avoidance complexes.

Only the Python standard library is required. Vertex labels are 4*i+j.
"""
import collections
import itertools

ORDER = 16
VERTICES = tuple((i,j) for i in range(4) for j in range(4))
STEPS = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
MATCH_ORDERS = {
    'rook': (12,14,10,11,8,6,1,3,5,15,0,13,4,2,7,9),
    'shrikhande': (4,2,7,11,9,12,1,6,13,10,5,0,15,14,3,8),
}


def graph(kind):
    adj=[0]*ORDER
    for a,(x,y) in enumerate(VERTICES):
        for b,(u,v) in enumerate(VERTICES):
            if a==b:continue
            if kind=='rook': edge=(x==u or y==v)
            else: edge=((u-x)%4,(v-y)%4) in STEPS
            if edge:adj[a]|=1<<b
    assert all(not (adj[a]>>a&1) and adj[a].bit_count()==6
               for a in range(ORDER))
    for a in range(ORDER):
        for b in range(a+1,ORDER):
            assert ((adj[a]>>b)&1)==((adj[b]>>a)&1)
            assert (adj[a]&adj[b]).bit_count()==2
    return adj


def independently_triangle_free(mask,adj):
    # Test on the induced graph directly, without the stored forbidden triples.
    for a in range(ORDER):
        if not (mask>>a&1):continue
        nb=mask&adj[a]
        while nb:
            bit=nb&-nb;b=bit.bit_length()-1
            if adj[b]&(nb^bit):return False
            nb^=bit
    return True


def complex_faces(kind):
    adj=graph(kind)
    triangles=[]
    for a,b,c in itertools.combinations(range(ORDER),3):
        if adj[a]>>b&1 and adj[a]>>c&1 and adj[b]>>c&1:
            triangles.append((1<<a)|(1<<b)|(1<<c))
    assert len(triangles)==32
    faces=[]
    for mask in range(1<<ORDER):
        yes=all(mask&t!=t for t in triangles)
        assert yes==independently_triangle_free(mask,adj)
        if yes:faces.append(mask)
    return faces


def morse_matching(faces,order):
    assert set(order)==set(range(ORDER))
    unmatched=set(faces)
    matching={}
    # At each stage pair every as-yet-unmatched lower face lacking the
    # specified vertex with its upper face, if both are present.
    for vertex in order:
        bit=1<<vertex
        for lo in faces:
            if not lo&bit and lo in unmatched and lo|bit in unmatched:
                hi=lo|bit
                unmatched.remove(lo);unmatched.remove(hi)
                matching[lo]=hi
    assert 0 in matching
    return unmatched,matching


def directed_hasse_check(faces,matching):
    # All codimension-one incidences, including incidences with the empty face.
    # Reverse each matched incidence, otherwise direct from upper to lower.
    ids={face:i for i,face in enumerate(faces)}
    indegree=[0]*len(faces)
    outgoing=[[] for _ in faces]
    count=0
    for hi in faces:
        h=ids[hi]; bits=hi
        while bits:
            bit=bits&-bits;lo=hi^bit;l=ids[lo]
            if matching.get(lo)==hi:
                outgoing[l].append(h);indegree[h]+=1
            else:
                outgoing[h].append(l);indegree[l]+=1
            count+=1;bits^=bit
    queue=collections.deque(i for i,d in enumerate(indegree) if d==0)
    seen=0
    while queue:
        u=queue.popleft();seen+=1
        for v in outgoing[u]:
            indegree[v]-=1
            if indegree[v]==0:queue.append(v)
    assert seen==len(faces), 'nonacyclic Morse matching'
    return count


def independently_mod2_betti(faces):
    # Incremental bit-vector elimination in the entire *augmented* simplicial
    # chain complex, independent of the discrete-Morse construction.
    bydegree=collections.defaultdict(list)
    for f in faces:bydegree[f.bit_count()-1].append(f)
    ranks={}
    for d in sorted(bydegree):
        if d<0:continue
        lower={f:i for i,f in enumerate(bydegree[d-1])}
        pivots={}
        for f in bydegree[d]:
            col=0;bits=f
            while bits:
                bit=bits&-bits
                col^=1<<lower[f^bit]
                bits^=bit
            while col:
                p=col.bit_length()-1
                if p in pivots:col^=pivots[p]
                else:pivots[p]=col;break
        ranks[d]=len(pivots)
    betti={}
    for d in range(max(bydegree)+1):
        b=len(bydegree[d])-ranks.get(d,0)-ranks.get(d+1,0)
        if b:betti[d]=b
    return betti


def verify(kind,expected_faces,expected_crit,expected_betti):
    faces=complex_faces(kind)
    assert len(faces)==expected_faces
    fvector=dict(sorted(collections.Counter(m.bit_count()-1 for m in faces if m).items()))
    unmatched,matching=morse_matching(faces,MATCH_ORDERS[kind])
    crit=dict(sorted(collections.Counter(m.bit_count()-1 for m in unmatched).items()))
    assert crit==expected_crit,crit
    assert len(matching)*2+len(unmatched)==len(faces)
    incidences=directed_hasse_check(faces,matching)
    betti=independently_mod2_betti(faces)
    assert betti==expected_betti,(betti,expected_betti)
    print(kind,'faces_including_empty=',len(faces),'f_vector=',fvector)
    print(kind,'matching_order=',MATCH_ORDERS[kind])
    print(kind,'matched_pairs=',len(matching),'critical_dim_counts=',crit,
          'has_empty_vertex_pair=',0 in matching,
          'hasse_incidences=',incidences,'acyclic=True',
          'mod2_reduced_betti=',betti)

if __name__=='__main__':
    verify('rook',7343,{5:15},{5:15})
    verify('shrikhande',8951,{6:9},{6:9})
    print('VERIFY_OK')
