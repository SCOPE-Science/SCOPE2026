#!/usr/bin/env python3
"""Exact reproducible checks for the Paley-17 independence-complex result.

No external dependencies. All arithmetic is over integers or finite fields.
"""
from itertools import combinations
from collections import Counter, deque

p=17
qr={x*x%p for x in range(1,p)}
assert sorted(qr)==[1,2,4,8,9,13,15,16]
verts=tuple(range(p))

def edge(x,y):
    return x!=y and ((x-y)%p in qr)

def independent(face):
    return all(not edge(x,y) for x,y in combinations(face,2))

def clique(face):
    return all(edge(x,y) for x,y in combinations(face,2))

# A nonresidue maps P_17 to its complement, intertwining their complexes.
nonresidue=3
assert nonresidue not in qr
for u,v in combinations(verts,2):
    assert edge(u,v) != edge(u*nonresidue%p,v*nonresidue%p)

faces={tuple(c) for k in (1,2,3) for c in combinations(verts,k) if independent(c)}
assert not any(independent(c) for c in combinations(verts,4))
face_counts=Counter(map(len,faces))
assert face_counts=={1:17,2:68,3:68},face_counts
assert len(faces)==153

# A complete (ordinary, nonrelative) acyclic matching of the face poset.
left=set(faces)
pairs=[]
for v in verts:
    for lo in sorted((x for x in left if v not in x), key=lambda x:(len(x),x)):
        hi=tuple(sorted(lo+(v,)))
        if lo in left and hi in left:
            left.remove(lo);left.remove(hi)
            pairs.append((lo,hi))
assert len(pairs)==68,(len(pairs),Counter(map(len,left)))
assert Counter(map(len,left))=={1:1,3:16},Counter(map(len,left))
match=set(pairs)

# In the oriented Hasse diagram, upward arrows are matched cover relations;
# all other cover relations point down. Kahn eliminates every face iff acyclic.
adj={face:[] for face in faces}
indegree={face:0 for face in faces}
hasse=0
for hi in faces:
    if len(hi)==1:continue
    for j in range(len(hi)):
        lo=hi[:j]+hi[j+1:]
        if (lo,hi) in match: src,dst=lo,hi
        else: src,dst=hi,lo
        adj[src].append(dst);indegree[dst]+=1;hasse+=1
assert hasse==340,hasse
ready=deque(x for x in faces if indegree[x]==0)
seen=0
while ready:
    x=ready.popleft();seen+=1
    for y in adj[x]:
        indegree[y]-=1
        if indegree[y]==0: ready.append(y)
assert seen==len(faces),(seen,len(faces))

# Independent mod-two boundary ranks, checking the Morse cell dimensions.
by_k={k:sorted(x for x in faces if len(x)==k) for k in (1,2,3)}
def rank_mod2(rows):
    pivots={}
    for row in rows:
        z=row
        while z:
            lead=z.bit_length()-1
            if lead not in pivots:
                pivots[lead]=z;break
            z^=pivots[lead]
    return len(pivots)
for k,expected in [(2,16),(3,52)]:
    rows=[]
    index={c:i for i,c in enumerate(by_k[k-1])}
    for upper in by_k[k]:
        b=0
        for j in range(k):b ^= 1<<index[upper[:j]+upper[j+1:]]
        rows.append(b)
    assert rank_mod2(rows)==expected,(k,rank_mod2(rows))

# For affine automorphisms x -> a*x + b (a quadratic residue), compute exact
# traces on oriented simplicial chains; Lefschetz gives the trace on H_2.
def sign_of_sort(t):
    return -1 if sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))%2 else 1
char_values=Counter()
for a in sorted(qr):
    for b in verts:
        image=lambda x: (a*x+b)%p
        traces=[]
        for k in (1,2,3):
            trace=0
            for face in by_k[k]:
                image_face=tuple(image(x) for x in face)
                if tuple(sorted(image_face))==face:
                    trace+=sign_of_sort(image_face)
            traces.append(trace)
        L=traces[0]-traces[1]+traces[2]
        character=L-1 # reduced H_0=0 and H_1=0 by acyclic Morse proof.
        expected=sum(image(x)==x for x in verts)-1
        assert character==expected,(a,b,traces,character,expected)
        char_values[character]+=1
assert char_values=={16:1,-1:16,0:119},char_values

# Explicit critical involution contribution.
a=-1%p;b=0
fixed_signed=[]
for k in (1,2,3):
    z=[(face,sign_of_sort(tuple(a*x%p for x in face))) for face in by_k[k]
       if tuple(sorted(a*x%p for x in face))==face]
    fixed_signed.append(z)
assert [sum(s for face,s in z) for z in fixed_signed]==[1,-4,-4]

# Augmentation is 16 dimensional; transitive affine vertex action means no invariants.
assert len(qr)*p==136
assert len(set(b for b in verts))==p
print('PALEY17_INDEPENDENCE_MORSE_68_PAIRS_AFFINE_136_CHARACTER_OK')
print('faces',dict(face_counts),'hasse',hasse,'critical',dict(Counter(map(len,left))))
print('character',dict(char_values))
