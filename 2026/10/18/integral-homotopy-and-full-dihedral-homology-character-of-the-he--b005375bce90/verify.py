"""Exact finite certificates for the Herschel matching-complex homotopy and character."""
from collections import Counter, deque
from itertools import permutations

# Vertices 0,1,2 are the degree-four vertices. Each of the three pairs
# has two common neighbours. Vertices 9,10 attach to alternate neighbours.
EDGES = tuple(sorted({
    (0,3),(0,4),(0,7),(0,8),
    (1,3),(1,4),(1,5),(1,6),
    (2,5),(2,6),(2,7),(2,8),
    (3,9),(4,10),(5,9),(6,10),(7,9),(8,10)
}))
ORDER = (6,11,1,0,16,12,7,2,13,15,17,14,4,10,3,8,5,9)
assert len(EDGES) == 18 and sorted(ORDER)==list(range(18))
vertex_sets = [(1 << u)|(1 << v) for u,v in EDGES]
deg=Counter(u for e in EDGES for u in e)
assert [deg[v] for v in range(11)] == [4,4,4,3,3,3,3,3,3,3,3]

# Enumeration is over ALL subsets of the 18 edges, with no external data.
faces={0}
for subset in range(1,1<<18):
    support=0
    good=True
    for i,mask in enumerate(vertex_sets):
        if subset & (1<<i):
            if support & mask:
                good=False
                break
            support |=mask
    if good:
        faces.add(subset)
assert len(faces)==752
nonempty=faces-{0}
fvec=Counter(s.bit_count()-1 for s in nonempty)
assert tuple(fvec.get(d,0) for d in range(5)) == (18,111,280,270,72)

# Sequential edge toggles give a complete algebraic matching on face poset.
remaining=set(nonempty)
matched=set()
for i in ORDER:
    bit=1<<i
    for sigma in list(remaining):
        tau=sigma|bit
        if not sigma & bit and tau in remaining:
            assert sigma in remaining
            remaining.remove(sigma)
            remaining.remove(tau)
            matched.add((sigma,tau))
crit=Counter(s.bit_count()-1 for s in remaining)
assert crit==Counter({0:1,3:12})
assert len(matched)==369
assert len(remaining)+2*len(matched)==len(nonempty)

# Verify the FULL oriented Hasse diagram, including all unmatched incidences.
# Each matched incidence is reversed (lower->upper); every other one goes
# upper->lower. A complete topological traversal is an acyclicity certificate.
out={f:[] for f in nonempty}
indeg={f:0 for f in nonempty}
incidences=0
for tau in nonempty:
    if tau.bit_count()==1:
        continue
    for i in range(18):
        if tau&(1<<i):
            sigma=tau^(1<<i)
            incidences += 1
            if (sigma,tau) in matched:
                u,v=sigma,tau
            else:
                u,v=tau,sigma
            out[u].append(v)
            indeg[v]+=1
queue=deque([v for v in nonempty if indeg[v]==0])
seen=0
while queue:
    u=queue.popleft()
    seen+=1
    for v in out[u]:
        indeg[v]-=1
        if indeg[v]==0:
            queue.append(v)
assert incidences==2502 and seen==751

# The graph automorphism group is S_3 x C_2. The 3 pairs of centers
# each have 2 'spokes', and the last involution simultaneously exchanges
# both parity classes of spokes and their external neighbours 9,10.
PAIR={((0,1),0):3,((0,1),1):4,
      ((1,2),0):5,((1,2),1):6,
      ((0,2),0):7,((0,2),1):8}
REVERSE={v:k for k,v in PAIR.items()}
EID={e:i for i,e in enumerate(EDGES)}

def edge_action(p,flip):
    vertex={u:p[u] for u in range(3)}
    for u,(pair,parity) in REVERSE.items():
        image_pair=tuple(sorted((p[pair[0]],p[pair[1]])))
        vertex[u]=PAIR[(image_pair,parity^flip)]
    vertex[9]=9+flip
    vertex[10]=10-flip
    assert sorted(vertex.values())==list(range(11))
    images=[tuple(sorted((vertex[u],vertex[v]))) for u,v in EDGES]
    assert set(images)==set(EDGES)
    return tuple(EID[image] for image in images)

def orient_sign(values):
    inversions=sum(x>y for i,x in enumerate(values) for y in values[i+1:])
    return -1 if inversions%2 else 1

def third_character(edgeperm):
    # Reduced Lefschetz: -1+sum_{fixed nonempty faces}(-1)^dim * sign.
    # Because only H_3 is nonzero, trace(H_3)= - reduced Lefschetz.
    reduced=-1
    for face in nonempty:
        ids=[i for i in range(18) if face & (1<<i)]
        image=[edgeperm[i] for i in ids]
        if set(image)==set(ids):
            reduced += (-1)**(len(ids)-1)*orient_sign(image)
    return -reduced

class_sizes={'e':1,'t':3,'c':2}
class_char={}
actions=set()
for p in permutations(range(3)):
    typ={3:'e',1:'t',0:'c'}[sum(i==p[i] for i in range(3))]
    for flip in (0,1):
        act=edge_action(p,flip)
        actions.add(act)
        value=third_character(act)
        if (typ,flip) in class_char:
            assert class_char[(typ,flip)]==value
        class_char[(typ,flip)]=value
assert len(actions)==12
assert class_char=={
    ('e',0):12,('t',0):0,('c',0):-3,
    ('e',1):-2,('t',1):2,('c',1):1,
}
S3_CHARS={
    'trivial':{'e':1,'t':1,'c':1},
    'sign':{'e':1,'t':-1,'c':1},
    'standard':{'e':2,'t':0,'c':-1}
}
multiplicity={}
for label,ch in S3_CHARS.items():
    for sign_power in (0,1):
        total=sum(class_sizes[typ]*class_char[(typ,flip)]*ch[typ]*
                  ((-1)**(sign_power*flip)) for typ in class_sizes for flip in (0,1))
        assert total%12==0
        multiplicity[(label,sign_power)]=total//12
assert multiplicity == {('trivial',0):1,('trivial',1):0,
                        ('sign',0):0,('sign',1):1,
                        ('standard',0):2,('standard',1):3}
assert sum(multiplicity[(label,k)]*S3_CHARS[label]['e']
           for label,k in multiplicity)==12
print('VERIFY_OK_HERSCHEL_MATCHING_COMPLEX_DIHEDRAL_HOMOLOGY')
print('GRAPH_VERTICES_EDGES',11,len(EDGES),'AUTOMORPHISMS',len(actions))
print('FACE_VECTOR',(18,111,280,270,72),'TOTAL_NONEMPTY',len(nonempty))
print('MORSE_PAIRS',len(matched),'CRITICAL',dict(sorted(crit.items())),
      'HASSE_INCIDENCES',incidences,'ACYCLIC_VISITED',seen)
print('HOMOTOPY_WEDGE_12_S3')
print('CLASS_TRACES',(class_char[('e',0)],class_char[('t',0)],class_char[('c',0)],
                      class_char[('e',1)],class_char[('t',1)],class_char[('c',1)]))
print('S3xC2_MULTIPLICITIES',multiplicity)
