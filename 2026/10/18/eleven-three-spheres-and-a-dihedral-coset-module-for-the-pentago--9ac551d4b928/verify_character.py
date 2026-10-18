"""Independent face enumeration and rational symmetry-character verifier.
Run: python verify_character.py
Uses component traversal instead of forbidden-triple enumeration.
"""
from collections import Counter

N=5
ADJ=[0]*(2*N)
for a in range(2):
    for i in range(N):
        u=a*N+i
        for v in ((a*N+(i-1)%N),(a*N+(i+1)%N),((1-a)*N+i)):
            ADJ[u]|=1<<v

def valid(mask):
    unseen=mask
    while unseen:
        wave=unseen&-unseen
        unseen^=wave
        size=0
        while wave:
            b=wave&-wave;wave^=b;size+=1
            if size>2:return False
            neighbors=ADJ[b.bit_length()-1]&unseen
            wave|=neighbors
            unseen^=neighbors
    return True

faces={mask for mask in range(1,1<<(2*N)) if valid(mask)}
assert len(faces)==230
assert dict(Counter(x.bit_count()-1 for x in faces))=={0:10,1:45,2:90,3:75,4:10}

def action(k,reflect,swap):
    return tuple((a^swap)*N+(((-i if reflect else i)+k)%N)
                 for a in range(2) for i in range(N))

def compose(p,q):return tuple(p[q[i]] for i in range(2*N))

def transported(mask,g):
    result=0
    while mask:
        bit=mask&-mask;mask-=bit
        result|=1<<g[bit.bit_length()-1]
    return result

def orientation_sign(mask,g):
    image=[g[v] for v in range(2*N) if mask>>v&1]
    inversions=sum(image[i]>image[j]
                   for i in range(len(image)) for j in range(i+1,len(image)))
    return -1 if inversions%2 else 1

elts={(k,reflect,swap):action(k,reflect,swap)
       for swap in range(2) for reflect in range(2) for k in range(N)}
assert len(elts)==20 and len(set(elts.values()))==20
for p in elts.values():
    for u in range(2*N):
        assert transported(ADJ[u],p)==ADJ[p[u]]
assert all(compose(p,q) in elts.values() for p in elts.values() for q in elts.values())

# The simplicial Lefschetz number is the alternating oriented face trace.
# Reduced H_3 is the sole nonzero reduced group, so chi(g)=1-L(g).
characters={}
for key,g in elts.items():
    lefschetz=sum((-1)**(face.bit_count()-1)*orientation_sign(face,g)
                  for face in faces if transported(face,g)==face)
    characters[key]=1-lefschetz

assert characters[(0,0,0)]==11
for (k,reflect,swap),trace in characters.items():
    expected=11 if (k,reflect,swap)==(0,0,0) else (3 if (reflect,swap)==(1,1) else 1)
    assert trace==expected
assert sum(characters.values())==40

# Test the full permutation character of G/H, H=<reflection * layer_swap>.
e=elts[(0,0,0)]
h=elts[(0,1,1)]
H={e,h};assert compose(h,h)==e
cosets=set()
for p in elts.values():
    cosets.add(frozenset(compose(p,z) for z in H))
assert len(cosets)==10
cosets=list(cosets)
for key,g in elts.items():
    fixed=sum(frozenset(compose(g,c) for c in C)==C for C in cosets)
    assert characters[key]==1+fixed

# Independent mod-two Betti check, not used to infer the wedge decomposition.
bydim={d:sorted(f for f in faces if f.bit_count()==d+1) for d in range(5)}
ranks={}
for degree in range(1,5):
    indices={mask:i for i,mask in enumerate(bydim[degree-1])}
    pivots={}
    for mask in bydim[degree]:
        column=0
        bits=mask
        while bits:
            bit=bits&-bits;bits-=bit
            column^=1<<indices[mask^bit]
        while column:
            pivot=column.bit_length()
            if pivot in pivots:column^=pivots[pivot]
            else:
                pivots[pivot]=column
                break
    ranks[degree]=len(pivots)
betti={d:len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in bydim}
betti[0]-=1
assert betti=={0:0,1:0,2:0,3:11,4:0}
print('independent_components_faces=%d reduced_F2_Betti=%s' % (len(faces),[betti[d] for d in range(5)]))
print('character_by_D5xC2_classes:')
for (k,r,s) in ((0,0,0),(1,0,0),(2,0,0),(0,1,0),(0,0,1),(1,0,1),(2,0,1),(0,1,1)):
    print('rotation=%d reflection=%d layer_swap=%d trace=%d' % (k,r,s,characters[(k,r,s)]))
print('Q_representation=trivial_plus_coset_permutation_on_10_cosets')
print('group_order=20 subgroup_order=2 invariants_dimension=2')
print('CHARACTER_VERIFICATION_OK')
