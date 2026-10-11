"""Exact mod-2 Vietoris--Rips persistence for the 24 rankings of four objects.

Run with Python 3.9 or later; no third-party dependencies. Pairwise distances are
numbers of adjacent swaps, not Euclidean distances in the permutahedron.
"""
from itertools import permutations
from collections import Counter

V = list(permutations(range(4)))
assert len(V) == 24
vertex_index = {p: i for i, p in enumerate(V)}

def inversion_distance(p, q):
    order = {a: j for j, a in enumerate(q)}
    x = [order[a] for a in p]
    return sum(x[i] > x[j] for i in range(4) for j in range(i+1, 4))

def graph_distance_matrix():
    adj = [set() for _ in V]
    for i,p in enumerate(V):
        for s in range(3):
            q = list(p)
            q[s],q[s+1] = q[s+1],q[s]
            adj[i].add(vertex_index[tuple(q)])
    D = []
    for s in range(len(V)):
        d = [-1]*len(V);d[s] = 0;queue = [s]
        for u in queue:
            for w in adj[u]:
                if d[w] < 0:
                    d[w] = d[u] + 1;queue.append(w)
        D.append(d)
    return D, adj

D, adj = graph_distance_matrix()
assert all(D[i][j] == inversion_distance(V[i],V[j]) for i in range(24) for j in range(24))
assert all(D[i][j] == D[j][i] for i in range(24) for j in range(24))
assert max(map(max,D)) == 6
assert sum(len(a) for a in adj)//2 == 36
assert all(sum(D[i][j]==6 for j in range(24)) == 1 for i in range(24))


def cliques_at(scale):
    """Exhaustively enumerate every nonempty clique exactly once in increasing-label order."""
    nbr = [sum(1<<j for j in range(i+1,24) if D[i][j] <= scale)
           for i in range(24)]
    by_dimension = [[] for _ in range(12)]
    def visit(tail, candidates):
        by_dimension[len(tail)-1].append(tail)
        while candidates:
            vbit = candidates & -candidates
            candidates ^= vbit
            v = vbit.bit_length()-1
            visit(tail+(v,), candidates & nbr[v])
    visit0 = (1<<24)-1
    while visit0:
        b=visit0 & -visit0;visit0^=b
        v=b.bit_length()-1
        visit((v,), visit0 & nbr[v])
    while by_dimension and not by_dimension[-1]:
        by_dimension.pop()
    return by_dimension


def mod2_rank(columns):
    """Rank of bit-set columns by exact F_2 Gaussian elimination."""
    pivot = {}
    for a in columns:
        while a:
            p = a.bit_length()-1
            if p not in pivot:
                pivot[p] = a
                break
            a ^= pivot[p]
    return len(pivot)


def boundary_columns(faces,dim):
    target = {a:i for i,a in enumerate(faces[dim-1])}
    for s in faces[dim]:
        b=0
        for j in range(len(s)):
            b ^= 1 << target[s[:j]+s[j+1:]]
        yield b


def betti_profile(faces):
    r=[0] + [mod2_rank(boundary_columns(faces,k)) for k in range(1,len(faces))] + [0]
    b=[len(faces[k])-r[k]-r[k+1] for k in range(len(faces))]
    b[0]-=1
    return r,b

EXPECTED_F = {
    0: [24],
    1: [24,36],
    2: [24,96,112,30],
    3: [24,168,472,618,384,92],
    4: [24,228,1112,3042,4848,4592,2592,822,112],
}
EXPECTED_B = {
    0: [23],
    1: [0,13],
    2: [0,0,9,0],
    3: [0,0,1,0,0,0],
    4: [0,0,0,0,5,2,0,0,0],
}
EXPECTED_R = {
    0: [0,0],
    1: [0,23,0],
    2: [0,23,73,30,0],
    3: [0,23,145,326,292,92,0],
    4: [0,23,205,907,2135,2708,1882,710,112,0],
}

faces = {}
for scale in range(5):
    f = cliques_at(scale)
    assert [len(a) for a in f] == EXPECTED_F[scale], (scale, list(map(len,f)))
    r,b=betti_profile(f)
    assert b == EXPECTED_B[scale],(scale,b)
    assert r == EXPECTED_R[scale],(scale,r)
    faces[scale]=f

# Compute the only possibly nonzero inclusion map between positive-degree
# homology at successive scales: H_2(K_2) -> H_2(K_3).
# First, column reduction of d_2(K_2) tracks every relation (cycle) among
# columns; then reduce the images of those cycles modulo B_2(K_3).
f2,f3 = faces[2],faces[3]
id2 = {s:i for i,s in enumerate(f2[1])}
col_basis={}
z2=[]
for i,s in enumerate(f2[2]):
    x=0
    for j in range(3):
        x ^= 1<<id2[s[:j]+s[j+1:]]
    coeff=1<<i
    while x:
        p=x.bit_length()-1
        if p not in col_basis:
            col_basis[p]=(x,coeff)
            break
        a,b=col_basis[p]
        x ^= a
        coeff ^= b
    if not x:
        z2.append(coeff)
assert len(z2)==39
id3={s:i for i,s in enumerate(f3[2])}
embed=[id3[s] for s in f2[2]]
basis={}
def insert(x):
    while x:
        p=x.bit_length()-1
        if p not in basis:
            basis[p]=x
            return 1
        x^=basis[p]
    return 0
for s in f3[3]:
    col=0
    for j in range(4):
        col ^= 1<<id3[s[:j]+s[j+1:]]
    insert(col)
assert len(basis)==326
for cycle in z2:
    col=0
    while cycle:
        bit=cycle & -cycle
        cycle ^= bit
        col ^= 1<<embed[bit.bit_length()-1]
    insert(col)
assert len(basis)==327
image_rank=len(basis)-326
assert image_rank==1

# For scale five the 12 disjoint distance-six pairs are the only forbidden
# pairs, so K_5 is a 12-fold join of S^0, i.e. a single S^11.
antipodes={frozenset((i,j)) for i in range(24) for j in range(i+1,24) if D[i][j]==6}
assert len(antipodes)==12
assert len(set().union(*map(set,antipodes)))==24

# The modules have disjoint support across all other neighboring scales;
# the above rank determines the complete barcode. H_0 is listed unreduced.
BARS = {
    (0,0,1):23,
    (0,0,None):1,
    (1,1,2):13,
    (2,2,3):8,
    (2,2,4):1,
    (4,4,5):5,
    (5,4,5):2,
    (11,5,6):1,
}
assert sum(x for (dim,birth,death),x in BARS.items() if dim==2 and birth==2)==9
assert sum(x for (dim,birth,death),x in BARS.items() if dim==2 and birth<=3 and (death is None or death>3))==1
assert sum(x for (dim,birth,death),x in BARS.items() if birth==4)==7
print('VERIFY_OK', '24_rankings', '36_edges', 'diameter_6',
      'face_vectors', EXPECTED_F, 'reduced_F2_betti', EXPECTED_B,
      'H2_inclusion_rank', image_rank, 'bars', BARS)
