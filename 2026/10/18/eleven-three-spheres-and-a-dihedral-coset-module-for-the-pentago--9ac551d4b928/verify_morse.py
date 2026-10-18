"""Exhaustive simplicial/discrete-Morse verification for a pentagonal prism.
Run: python verify_morse.py [path/to/morse_certificate.json]
All ten-vertex subsets and all cover relations are checked.
"""
import sys, json
from collections import Counter, deque
from itertools import combinations
from pathlib import Path

N=5
VERTICES=tuple(range(2*N))
EDGES=set()
for layer in range(2):
    for i in range(N):
        EDGES.add(frozenset((layer*N+i,layer*N+(i+1)%N)))
for i in range(N):
    EDGES.add(frozenset((i,N+i)))
assert len(EDGES)==15

# For three vertices, connectedness means at least two graph edges.
FORBIDDEN=[]
for triple in combinations(VERTICES,3):
    if sum(frozenset(edge).issubset(triple) for edge in EDGES)>=2:
        FORBIDDEN.append(sum(1<<v for v in triple))

faces=set()
for mask in range(1,1<<(2*N)):
    if not any((mask & triple)==triple for triple in FORBIDDEN):
        faces.add(mask)
assert len(faces)==230
fvector=dict(Counter(x.bit_count()-1 for x in faces))
assert fvector=={0:10,1:45,2:90,3:75,4:10}
assert sum((-1)**d*num for d,num in fvector.items())==-10

certificate_path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('morse_certificate.json')
cert=json.loads(certificate_path.read_text(encoding='utf-8'))
assert cert['vertex_count']==10 and cert['model']=='C5_cartesian_K2_independence_components_le_2'
order=cert['toggle_order']
assert sorted(order)==list(VERTICES)
pairs=[tuple(p) for p in cert['pairs']]
critical=cert['critical_faces']
assert len(pairs)==109 and len(critical)==12

# Check the supplied pairing against the independent vertex-toggle algorithm.
remaining=set(faces)
recreated=[]
for vertex in order:
    b=1<<vertex
    low=sorted(x for x in remaining if not x&b and (x|b) in remaining)
    for x in low:
        assert x in remaining and x|b in remaining
        remaining.remove(x);remaining.remove(x|b)
        recreated.append((x,x|b))
assert set(pairs)==set(recreated)
assert critical==sorted(remaining)

used=set()
match=set()
for low,high in pairs:
    assert low in faces and high in faces
    assert low.bit_count()+1==high.bit_count()
    assert (high^low).bit_count()==1 and (high&low)==low
    assert low not in used and high not in used
    used.update((low,high));match.add((low,high))
assert used.isdisjoint(critical) and used|set(critical)==faces
assert Counter(x.bit_count()-1 for x in critical)=={0:1,3:11}

# Reverse matched arrows of the downward Hasse diagram and certify acyclicity.
indegree={f:0 for f in faces}
outedges={f:[] for f in faces}
cover_count=0
for high in faces:
    bits=high
    if high.bit_count()<2: continue
    while bits:
        b=bits&-bits;bits^=b
        low=high^b
        assert low in faces
        src,dst=(low,high) if (low,high) in match else (high,low)
        outedges[src].append(dst);indegree[dst]+=1
        cover_count+=1
queue=deque(f for f in faces if indegree[f]==0)
removed=0
while queue:
    f=queue.popleft();removed+=1
    for nxt in outedges[f]:
        indegree[nxt]-=1
        if indegree[nxt]==0:queue.append(nxt)
assert removed==len(faces)
print('vertices=10 graph_edges=15 forbidden_connected_triples=%d' % len(FORBIDDEN))
print('nonempty_faces=%d f_vector=%s reduced_euler=%d' % (len(faces),[fvector[d] for d in range(5)],-11))
print('matched_pairs=%d hasse_cover_relations=%d reversed_dag_vertices=%d' % (len(pairs),cover_count,removed))
print('critical_cell_counts=%s' % sorted(Counter(f.bit_count()-1 for f in critical).items()))
print('homotopy_type=wedge_of_11_three_spheres')
print('MORSE_VERIFICATION_OK')
