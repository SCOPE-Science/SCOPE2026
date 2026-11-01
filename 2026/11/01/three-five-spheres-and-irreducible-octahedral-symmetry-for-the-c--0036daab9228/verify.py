#!/usr/bin/env python3
"""Complete finite verification for M_2(Q_3), including its 48-element symmetry character."""
from collections import Counter, deque
from itertools import permutations, product

N=8
EDGES=tuple((u,v) for u in range(N) for v in range(u+1,N) if (u^v).bit_count()==1)
assert len(EDGES)==12
INDEX={e:i for i,e in enumerate(EDGES)}
FACES=set()
for mask in range(1,1<<12):
    degree=[0]*8
    for i,(u,v) in enumerate(EDGES):
        if (mask>>i)&1:
            degree[u]+=1
            degree[v]+=1
    if max(degree)<=2:
        FACES.add(mask)
assert len(FACES)==1698
assert tuple(Counter(x.bit_count()-1 for x in FACES)[i] for i in range(8))==(12,66,212,423,516,352,108,9)

# Independent triangle-avoidance characterization in the cuboctahedral line graph.
FORBIDDEN=[sum(1<<j for j,(a,b) in enumerate(EDGES) if v in (a,b)) for v in range(8)]
assert all(q.bit_count()==3 for q in FORBIDDEN)
assert all(((m in FACES)==all(m&q!=q for q in FORBIDDEN)) for m in range(1,1<<12))

# Repeated toggles on decreasing graph-edge indices.
free=set(FACES)
paired={}
for pivot in reversed(range(12)):
    for face in sorted(free):
        larger=face|(1<<pivot)
        if not (face>>pivot)&1 and larger in free:
            free.remove(face)
            free.remove(larger)
            paired[face]=larger
            paired[larger]=face
critical=Counter(x.bit_count()-1 for x in free)
assert len(paired)==1694 and len(free)==4
assert critical=={0:1,5:3}, (len(paired),free,critical)

# Direct Forman acyclicity check: reverse precisely the matched Hasse incidences.
adj={s:[] for s in FACES}
indeg={s:0 for s in FACES}
incidences=0
for high in FACES:
    for i in range(12):
        if not ((high>>i)&1):
            continue
        low=high^(1<<i)
        if not low:
            continue  # empty face is not part of the ordinary face poset
        assert low in FACES
        incidences+=1
        if paired.get(low)==high:
            a,b=low,high
        else:
            a,b=high,low
        adj[a].append(b)
        indeg[b]+=1
queue=deque(s for s in FACES if indeg[s]==0)
visited=0
while queue:
    s=queue.popleft()
    visited+=1
    for t in adj[s]:
        indeg[t]-=1
        if indeg[t]==0:
            queue.append(t)
assert visited==len(FACES),('cyclic matching',visited,len(FACES))

# Every cube automorphism is an affine signed coordinate permutation on F_2^3.
def vertex_permutation(axis,shift):
    return tuple(sum(((((v>>i)&1)^((shift>>axis[i])&1))<<axis[i]) for i in range(3)) for v in range(8))

def edges_permutation(axis,shift):
    on_vertices=vertex_permutation(axis,shift)
    return tuple(INDEX[tuple(sorted((on_vertices[u],on_vertices[v])))] for u,v in EDGES)

def restriction_sign(img):
    return -1 if sum(img[i]>img[j] for i in range(len(img)) for j in range(i+1,len(img)))%2 else 1

def top_character(edge_perm):
    # Reduced Lefschetz number: sum (-1)^dimension * signed chain traces, minus 1.
    reduced_lefschetz=-1
    for face in FACES:
        indices=[i for i in range(12) if (face>>i)&1]
        images=[edge_perm[i] for i in indices]
        if set(images)==set(indices):
            reduced_lefschetz+=(-1)**(len(indices)-1)*restriction_sign(images)
    return -reduced_lefschetz  # only nonzero reduced homology is in degree 5

trace_counts=Counter()
unique_actions=set()
for axis in permutations(range(3)):
    parity=(-1)**sum(axis[i]>axis[j] for i in range(3) for j in range(i+1,3))
    for shift in range(8):
        ep=edges_permutation(axis,shift)
        unique_actions.add(ep)
        actual=top_character(ep)
        expected=parity*sum((-1)**((shift>>axis[i])&1) for i in range(3) if axis[i]==i)
        assert actual==expected,('bad character',axis,shift,actual,expected)
        trace_counts[actual]+=1
assert len(unique_actions)==48
assert trace_counts==Counter({1:15,-1:15,0:16,3:1,-3:1}),trace_counts
assert sum(t*t*m for t,m in trace_counts.items())==48,trace_counts
assert sum(t*m for t,m in trace_counts.items())==0

# The cube is the crown graph K_{4,4} minus its diagonal perfect matching.
# Label the even vertices by rows and their antipodes by matching columns.
ROWS=tuple(v for v in range(8) if v.bit_count()%2==0)
COLS=tuple(v^7 for v in ROWS)
assert all(((ROWS[i]^COLS[j]).bit_count()==1)==(i!=j)
           for i in range(4) for j in range(4))
def crown_edge_action(rowperm,transpose):
    vperm={}
    for i in range(4):
        vperm[ROWS[i]]=COLS[rowperm[i]] if transpose else ROWS[rowperm[i]]
        vperm[COLS[i]]=ROWS[rowperm[i]] if transpose else COLS[rowperm[i]]
    return tuple(INDEX[tuple(sorted((vperm[u],vperm[v])))] for u,v in EDGES)
all_crown_actions=set()
for p in permutations(range(4)):
    parity=(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
    std=sum(i==p[i] for i in range(4))-1
    for t in (0,1):
        eperm=crown_edge_action(p,t)
        all_crown_actions.add(eperm)
        expected=(-1)**t*parity*std
        assert top_character(eperm)==expected,(p,t,expected)
assert all_crown_actions==unique_actions

facets=[f for f in FACES if not any((f|(1<<i)) in FACES for i in range(12) if not (f>>i)&1)]
print('VERIFY_OK cube_edges=12 forbidden_triangles=8 faces=1698 face_vector=(12,66,212,423,516,352,108,9)')
print('VERIFY_OK maximal_faces=%d matched_pairs=%d critical=(1_dimension0,3_dimension5) hasse_incidences=%d dag=%d' %(len(facets),len(paired)//2,incidences,visited))
print('VERIFY_OK affine_cube_automorphisms=48 traces=%s character=sign(axis_permutation)*natural_signed_axis_character' %dict(sorted(trace_counts.items())))
print('VERIFY_OK crown_model=K4,4_minus_diagonal all_48_traces=sign(S4)*standard(S4)*sign(transpose)')
print('VERIFY_OK rational_module_3dim irreducible=True invariants=0; homotopy=wedge_3_S5')
