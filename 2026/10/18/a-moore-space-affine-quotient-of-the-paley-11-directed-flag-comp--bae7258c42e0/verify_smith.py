"""Exact integer chains and Smith normal form for the directed-flag complex of P11."""
import itertools,collections,json
from sympy import zeros,ZZ
from sympy.matrices.normalforms import smith_normal_form
p=11
Q={1,3,4,5,9}
def t(S):
    # Equivalent but independently coded obstruction: a transitive tournament
    # has no directed cycle, and cycles in tournaments have cyclic triangles.
    for a,b,c in itertools.combinations(S,3):
        edges=lambda x,y:(y-x)%p in Q
        if (edges(a,b) and edges(b,c) and edges(c,a)) or (edges(a,c) and edges(c,b) and edges(b,a)):
            return False
    return True
chains={k:[tuple(c) for c in itertools.combinations(range(p),k+1) if t(c)] for k in range(4)}
assert [len(chains[k]) for k in range(4)]==[11,55,110,55]
matrices={}
for k in (1,2,3):
    lower={c:i for i,c in enumerate(chains[k-1])}
    D=zeros(len(lower),len(chains[k]))
    for col,simplex in enumerate(chains[k]):
        for j in range(k+1):D[lower[simplex[:j]+simplex[j+1:]],col]+=(-1)**j
    matrices[k]=D
assert matrices[1]*matrices[2]==zeros(11,110)
assert matrices[2]*matrices[3]==zeros(55,55)
smith={};rank={}
for k,D in matrices.items():
    diag=smith_normal_form(D,domain=ZZ)
    invariant=[abs(int(diag[i,i])) for i in range(min(diag.shape)) if diag[i,i]!=0]
    smith[k]=dict(sorted(collections.Counter(invariant).items()))
    rank[k]=len(invariant)
assert rank=={1:10,2:45,3:55}
assert smith=={1:{1:10},2:{1:45},3:{1:54,2:1}},smith
# H2 free rank = 110 - rank(d2) - rank(d3) = 10. H3=0.
# coker(d3) has Z/2 torsion; coker(d2) is torsion-free, hence H2 has Z/2.
print(json.dumps({'face_vector':[11,55,110,55],'boundary_ranks':rank,'smith_invariants':smith,'integral_reduced_homology':{'degree_2':'Z^10 + Z/2','other_degrees':'zero'},'chain_property':True},sort_keys=True))
