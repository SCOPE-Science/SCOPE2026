"""Exact rational-character calculation for the dodecahedral independence complex.

Requires NetworkX. All face and automorphism searches are exhaustive.
"""
from collections import Counter, defaultdict
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher

N = 20
G = nx.Graph()
G.add_nodes_from(range(N))
for i in range(10):
    G.add_edge(i, (i+1)%10)
    G.add_edge(10+i, 10+(i+2)%10)
    G.add_edge(i, 10+i)
assert G.number_of_edges() == 30 and all(G.degree(i)==3 for i in G)
assert nx.is_isomorphic(G,nx.dodecahedral_graph())

adj = [sum(1<<j for j in G.neighbors(i)) for i in range(N)]
faces = [0]
for j in range(N):
    faces.extend([v|(1<<j) for v in tuple(faces) if (v&adj[j])==0])
by_size = defaultdict(list)
for mask in faces:
    by_size[mask.bit_count()].append(mask)
counts = tuple(len(by_size[i]) for i in range(9))
assert counts==(1,20,160,660,1510,1912,1240,320,5)
assert len(faces)==5828

# Boundary C_d -> C_{d-1}, d>=2, over the field of two elements.
# Its column is a bitset of rows, reduced by exact XOR elimination.
def rank_gf2(d):
    rows = {s:i for i,s in enumerate(by_size[d])}
    pivots = {}
    for face in by_size[d+1]:
        col = 0
        for i in range(N):
            if face&(1<<i):
                col ^= (1<<rows[face^(1<<i)])
        while col:
            pivot = col.bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=col
                break
            col ^= pivots[pivot]
    return len(pivots)

boundary_ranks=tuple(rank_gf2(d) for d in range(1,8))
assert boundary_ranks==(19,141,519,991,921,315,5)
# Reduced homology: the augmentation C_0 -> F2 has rank one.
betti2=[]
for degree in range(8):
    nfaces = counts[degree+1]
    below = 1 if degree==0 else boundary_ranks[degree-1]
    above = boundary_ranks[degree] if degree<7 else 0
    betti2.append(nfaces-below-above)
assert tuple(betti2)==(0,0,0,0,0,4,0,0)
euler_sum=sum((-1)**i*v for i,v in enumerate(counts))
assert euler_sum==4
# Universal coefficients imply rational Betti numbers <= mod-two Betti
# numbers in each degree. The Euler characteristic forces rational H5 rank 4.

planar,embedding=nx.check_planarity(G)
assert planar
max_sets=tuple(by_size[8])
assert len(max_sets)==5

# Exhaustive graph automorphisms by constraint-respecting graph isomorphism.
perms=[]
for mapping in GraphMatcher(G,G).isomorphisms_iter():
    g=tuple(mapping[i] for i in range(N))
    assert set(g)==set(range(N))
    assert all(G.has_edge(g[u],g[v]) for u,v in G.edges())
    perms.append(g)
assert len(perms)==120 and len(set(perms))==120

# The orientation character of the canonical planar embedding is read
# from the cyclic ordering at vertex 0. For a 3-connected planar graph
# the same sign is obtained at every vertex.
def orientation(g,vertex=0):
    before=list(embedding.neighbors_cw_order(vertex))
    after=list(embedding.neighbors_cw_order(g[vertex]))
    sent=[g[i] for i in before]
    if any(sent==after[j:]+after[:j] for j in range(3)):
        return 1
    if any(sent==list(reversed(after))[j:]+list(reversed(after))[:j] for j in range(3)):
        return -1
    raise AssertionError('local rotation system not preserved')

def act_set(g,mask):
    return sum(1<<g[i] for i in range(N) if mask&(1<<i))

def perm_sign_on_set(g,mask):
    images=[g[i] for i in range(N) if mask&(1<<i)]
    crossings=sum(images[i]>images[j] for i in range(len(images))
                                      for j in range(i+1,len(images)))
    return -1 if crossings%2 else 1

def signed_euler_character(g):
    # Augmented alternating trace: equals trace on rational fifth homology.
    total=1  # The empty simplex contributes 1 to this sign convention.
    for k in range(1,9):
        for face in by_size[k]:
            if act_set(g,face)==face:
                total+=(-1)**k*perm_sign_on_set(g,face)
    return total

by_orient_fixed=Counter()
permutation_images=set()
for g in perms:
    eps=orientation(g)
    assert all(orientation(g,j)==eps for j in range(N))
    action=[max_sets.index(act_set(g,s)) for s in max_sets]
    assert set(action)==set(range(5))
    permutation_images.add(tuple(action))
    fixed=sum(action[j]==j for j in range(5))
    trace=signed_euler_character(g)
    # The claimed full character equation.
    assert trace==eps*(fixed-1),(g,eps,fixed,trace)
    by_orient_fixed[(eps,fixed,trace)]+=1

assert len(permutation_images)==60
assert set(by_orient_fixed.items())=={
    ((1,5,4),1),((1,2,1),20),((1,1,0),15),((1,0,-1),24),
    ((-1,5,-4),1),((-1,2,-1),20),((-1,1,0),15),((-1,0,1),24)
}
# The quotient action on the five independent sets is exactly A5:
def parity(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2
assert all(parity(p)==0 for p in permutation_images)
assert sum(orientation(g)==1 for g in perms)==60
assert sum(orientation(g)==-1 for g in perms)==60
print('graph: 20 vertices, 30 edges; automorphism group size 120')
print('independent-set counts by cardinality:',counts)
print('boundary ranks mod 2, dimensions 1 through 7:',boundary_ranks)
print('reduced Betti numbers mod 2, dimensions 0 through 7:',tuple(betti2))
print('rational homology: rank 4 in dimension 5 only (Euler + universal coefficients)')
print('five maximum independent sets; permutation image A5 of order 60')
print('sign/orientation, fixed sets, trace; multiplicities:')
for key,multiplicity in sorted(by_orient_fixed.items(),reverse=True):
    print(key,multiplicity)
print('all 120 rational Lefschetz traces agree with orientation*(fixed-1)')
print('VERIFY_OK')
