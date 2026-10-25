"""Exact character certificate for the independence complex of GP(8,3).

Requires Python >=3.9, NetworkX >=2.8, SymPy >=1.10.
The finite group and complex are reconstructed, not read from tables.
"""
import collections
import networkx as nx
import sympy as sp

P = 101
N = 8
G = nx.Graph()
G.add_nodes_from(range(16))
for i in range(N):
    G.add_edge(i, (i + 1) % N)
    G.add_edge(i, i + 8)
    G.add_edge(i + 8, 8 + (i + 3) % N)
assert G.number_of_edges() == 24
adj = [set(G.neighbors(v)) for v in range(16)]

faces = [[()]] + [[] for _ in range(8)]
for mask in range(1, 1 << 16):
    t = tuple(i for i in range(16) if mask & (1 << i))
    if all(not (adj[v] & set(t[:j])) for j, v in enumerate(t)):
        faces[len(t)].append(t)
assert [len(f) for f in faces] == [1,16,96,272,376,240,72,16,2]
positions = [{s:i for i,s in enumerate(fs)} for fs in faces]

# Exact signed simplicial boundaries, represented in sparse columns.
def columns(k, modulo=P):
    result = []
    for simplex in faces[k]:
        result.append({positions[k-1][simplex[:i]+simplex[i+1:]]:
                       ((-1)**i % modulo if modulo else (-1)**i)
                       for i in range(k)})
    return result

def submultiple(vec, pivot, coef, mod=P):
    for j, v in pivot.items():
        y = (vec.get(j, 0)-coef*v) % mod
        if y:
            vec[j] = y
        else:
            vec.pop(j, None)

def reduce_basis(vec, basis):
    d = {j:(v % P) for j,v in vec.items() if v % P}
    while d:
        j = min(d)
        if j not in basis:
            break
        submultiple(d, basis[j], d[j])
    return d

def add_to_basis(basis, vec):
    v = reduce_basis(vec, basis)
    if not v:
        return False
    j = min(v)
    inv = pow(v[j], -1, P)
    basis[j] = {t:(q * inv)%P for t,q in v.items()}
    return True

ranks = []
for k in range(1,9):
    bas = {}
    for col in columns(k):
        add_to_basis(bas, col)
    ranks.append(len(bas))
assert ranks == [1,15,81,191,181,58,14,2], ranks
betti = [len(faces[k+1])-ranks[k]-(ranks[k+1] if k<7 else 0)
         for k in range(8)]
assert betti == [0,0,0,4,1,0,0,0], betti

# Find a non-boundary five-vertex chain cycle by elimination over F_101.
D4 = columns(5)
D5 = columns(6)
B5 = {}
for c in D5:
    add_to_basis(B5,c)
assert len(B5)==58
B4 = {}   # pivot -> (normalized column, normalized provenance)
cycle = None
for ind, col in enumerate(D4):
    d = dict(col)
    provenance = {ind:1}
    while d:
        j = min(d)
        if j not in B4:
            inv = pow(d[j],-1,P)
            B4[j] = ({x:y*inv%P for x,y in d.items()},
                     {x:y*inv%P for x,y in provenance.items()})
            break
        pivot, coeffs = B4[j]
        v = d[j]
        submultiple(d, pivot, v)
        submultiple(provenance, coeffs, v)
    else:
        residual = reduce_basis(provenance, B5)
        if residual:
            cycle = provenance
            break
assert cycle is not None
assert len(cycle)==100
assert collections.Counter((x if x<=50 else x-101) for x in cycle.values()) == {1:50,-1:50}
cycle_int = {j:(q if q<=50 else q-101) for j,q in cycle.items()}
# Verify the chosen chain is a genuine integral cycle, not just modulo P.
image = collections.Counter()
for j,coeff in cycle_int.items():
    for i,entry in columns(5, modulo=None)[j].items():
        image[i] += coeff*entry
assert not any(image.values())
# A fully exact rational nonboundary test independently checks the cycle.
M5 = sp.SparseMatrix(len(faces[5]),len(D5),
       {(i,j):v for j,col in enumerate(columns(6,modulo=None))
                    for i,v in col.items()})
assert M5.rank() == 58
z = sp.SparseMatrix(len(faces[5]),1,{(j,0):v for j,v in cycle_int.items()})
assert M5.row_join(z).rank() == 59
# Reduction modulo 101 bounds the rational Betti numbers from above;
# this explicit rational nonboundary and the Euler characteristic fix them.
assert sum((-1)**(k-1)*len(faces[k]) for k in range(9)) == -3

# All 96 graph automorphisms (exact enumeration).
autos = [tuple(mapping[v] for v in range(16))
         for mapping in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter()]
assert len(autos) == len(set(autos)) == 96

def parity(seq):
    return -1 if sum(seq[i]>seq[j]
               for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

def act_cycle(g,source):
    result = {}
    for j,c in source.items():
        transformed = tuple(g[v] for v in faces[5][j])
        index = positions[5][tuple(sorted(transformed))]
        result[index] = (result.get(index,0) + c*parity(transformed)) % P
    return {j:v for j,v in result.items() if v}

# The 16-vertex graph is a double cover of a cube: the deck involution
# rotates both eight-cycles by four places. Body diagonals are a natural
# four-element permutation set, independent of vertex labeling.
classes = sorted({frozenset((i,(i+4)%8)) for i in range(8)} |
                 {frozenset((i+8,8+(i+4)%8)) for i in range(8)},
                 key=min)
assert len(classes)==8
class_id = {i:j for j,cl in enumerate(classes) for i in cl}
Q = nx.Graph()
Q.add_nodes_from(range(8))
Q.add_edges_from((class_id[a],class_id[b]) for a,b in G.edges())
assert Q.number_of_edges()==12 and all(Q.degree(i)==3 for i in range(8))
assert nx.is_isomorphic(Q,nx.hypercube_graph(3))
opp = {i:next(j for j,d in nx.single_source_shortest_path_length(Q,i).items() if d==3)
       for i in range(8)}
diags = sorted({frozenset((i,opp[i])) for i in range(8)},key=min)
assert len(diags)==4
diag_id = {i:j for j,d in enumerate(diags) for i in d}
# A and B are the uniquely determined graph bipartition classes.
bipartition = [i%2 for i in range(8)] + [1-i%2 for i in range(8)]
assert all(bipartition[a]!=bipartition[b] for a,b in G.edges())


def reduced_lefschetz(g):
    total = -1
    for k in range(1,9):
        for f in faces[k]:
            moved=tuple(g[v] for v in f)
            if set(moved)==set(f):
                total += ((-1)**(k-1))*parity(moved)
    return total

characters=[]
deck = tuple((v+4)%8 if v<8 else 8+(v-8+4)%8 for v in range(16))
assert deck != tuple(range(16))
for g in autos:
    assert all(g[deck[v]] == deck[g[v]] for v in range(16))

    b = 1 if bipartition[g[0]]==bipartition[0] else -1
    pi = tuple(diag_id[class_id[g[min(classes[min(d)])]]] for d in diags)
    assert sorted(pi)==list(range(4))
    fixed = sum(pi[i]==i for i in range(4))
    chi3 = b * parity(pi) * fixed
    chi4 = b
    # The rank-one top action is checked on a *nonzero* rational cycle:
    # mod-P reduction is faithful since rank(D5)_Q=rank(D5)_F_P=58
    # and z is nonzero in both homologies.
    acted = act_cycle(g,cycle)
    target = {j:(b*v)%P for j,v in cycle.items() if (b*v)%P}
    difference = dict(acted)
    for j,v in target.items():
        x=(difference.get(j,0)-v)%P
        if x:difference[j]=x
        else:difference.pop(j,None)
    assert not reduce_basis(difference,B5)
    assert chi4-chi3 == reduced_lefschetz(g)
    characters.append((g,chi3,chi4,pi,b))

# The induced action on body diagonals and bipartition is exactly S4 x C2,
# with a two-element kernel (the deck group).
counts=collections.Counter((pi,b) for _,_,_,pi,b in characters)
assert len(counts)==48 and all(v==2 for v in counts.values())
identity=tuple(range(16))
assert next((a,b) for g,a,b,_,_ in characters if g==identity)==(4,1)
rot=lambda shift:tuple((i+shift)%8 for i in range(8))+tuple(8+(i+shift)%8 for i in range(8))
assert [(next(a for g,a,_,_,_ in characters if g==rot(j)),
         next(b for g,_,b,_,_ in characters if g==rot(j))) for j in range(8)] == [
    (4,1),(0,-1),(0,1),(0,-1),(4,1),(0,-1),(0,1),(0,-1)]
# Fixed-subspace dimensions by averaging rational characters.
for predicate,expected in [
    (lambda pi,b:True,(0,0)),
    (lambda pi,b:b==1,(0,1)),
    (lambda pi,b:b*parity(pi)==1,(1,0))]:
    members=[(x,y) for _,x,y,pi,b in characters if predicate(pi,b)]
    assert sum(a for a,b in members)%len(members)==0
    assert sum(b for a,b in members)%len(members)==0
    assert (sum(a for a,b in members)//len(members),
            sum(b for a,b in members)//len(members))==expected
print('MK_FULL_AUTOMORPHISM_CHARACTER_VERIFIED')
print('faces=',[len(f) for f in faces], 'mod101 boundary ranks=',ranks)
print('rational Betti(3,4)=(4,1); exact cycle: 100 terms; rank_Q(D5)=58; rank_Q([D5,z])=59')
print('automorphisms=96; S4-by-bipartition image=48 with kernel=2')
print('chi3=b*sign(pi)*fixed(pi); chi4=b; all 96 signed Lefschetz and top actions verified')
print('full / ker(b) / ker(b*sign(pi)) invariant ranks:',(0,0),(0,1),(1,0))
