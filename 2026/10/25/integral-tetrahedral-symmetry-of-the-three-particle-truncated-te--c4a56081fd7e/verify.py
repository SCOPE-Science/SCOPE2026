"""Exact top-degree configuration-homology checks for the truncated tetrahedral graph.

The weight-three, degree-three reduced Swiatkowski differential is reconstructed
from the cubic graph. All arithmetic is exact; this script requires Python 3.9+.
"""
from collections import defaultdict
from itertools import combinations, permutations, product

LABELS=tuple(range(4))
VERTICES=tuple((u,v) for u in LABELS for v in LABELS if u!=v)
VINDEX={v:i for i,v in enumerate(VERTICES)}
EDGES=[]
for u in LABELS:
    corner=sorted(VINDEX[(u,v)] for v in LABELS if v!=u)
    EDGES.extend(combinations(corner,2))
for u,v in combinations(LABELS,2):
    EDGES.append(tuple(sorted((VINDEX[(u,v)],VINDEX[(v,u)]))))
EDGES=tuple(sorted(EDGES))
EINDEX={e:i for i,e in enumerate(EDGES)}
INC=tuple(tuple(i for i,e in enumerate(EDGES) if v in e) for v in range(len(VERTICES)))
assert len(VERTICES)==12 and len(EDGES)==18 and all(len(x)==3 for x in INC)

# Homological degree d uses d distinct vertex half-edge differences and (3-d)
# edge variables. For d=3 and d=2, the bases are as follows.
TOP_BASIS=tuple((vs,opts) for vs in combinations(range(12),3)
                for opts in product((1,2), repeat=3))
TOP_INDEX={b:i for i,b in enumerate(TOP_BASIS)}
LOWER_BASIS=tuple((vs,opts,e) for vs in combinations(range(12),2)
                  for opts in product((1,2),repeat=2) for e in range(18))
LOWER_INDEX={b:i for i,b in enumerate(LOWER_BASIS)}
assert len(TOP_BASIS)==1760 and len(LOWER_BASIS)==4752

def differential_column(vs, opts):
    output=defaultdict(int)
    for j,vertex in enumerate(vs):
        smaller=vs[:j]+vs[j+1:]
        chosen=opts[:j]+opts[j+1:]
        for edge,coef in ((INC[vertex][opts[j]],1),(INC[vertex][0],-1)):
            output[LOWER_INDEX[(smaller,chosen,edge)]]+=(-1 if j%2 else 1)*coef
    return {r:c for r,c in output.items() if c}

COLS=tuple(differential_column(*b) for b in TOP_BASIS)
assert all(len(c)==6 for c in COLS)

def rank_mod_two(cols):
    pivots={}
    for col in cols:
        z=0
        for r,c in col.items():
            if c&1:z^=1<<r
        while z:
            r=z.bit_length()-1
            if r not in pivots:
                pivots[r]=z;break
            z^=pivots[r]
    return len(pivots)

def rank_mod_prime(cols,p):
    pivots={}
    for col in cols:
        z={r:c%p for r,c in col.items() if c%p}
        while z:
            r=min(z)
            if r not in pivots:
                inv=pow(z[r],-1,p)
                pivots[r]={i:(coef*inv)%p for i,coef in z.items()}
                break
            coef=z[r]
            for i,y in pivots[r].items():
                val=(z.get(i,0)-coef*y)%p
                if val:z[i]=val
                else:z.pop(i,None)
    return len(pivots)

def local_triangle_cycle(u):
    neighbors=tuple(v for v in LABELS if v!=u)
    vs=tuple(VINDEX[(u,v)] for v in neighbors)
    coeff=defaultdict(int)
    for i,vertex in enumerate(vs):
        outgoing=EINDEX[tuple(sorted((vs[i],vs[(i+1)%3])))]
        incoming=EINDEX[tuple(sorted((vs[(i-1)%3],vs[i])))]
        for option in (1,2):
            coeff[(vertex,option)]+=int(INC[vertex][option]==outgoing)-int(INC[vertex][option]==incoming)
    coeff={b:c for b,c in coeff.items() if c}
    # Integral degree-one boundary vanishes edge by edge.
    boundary=defaultdict(int)
    for (vertex,option),coef in coeff.items():
        boundary[INC[vertex][option]]+=coef
        boundary[INC[vertex][0]]-=coef
    assert not any(boundary.values())
    return coeff

TRIANGLES=tuple(local_triangle_cycle(u) for u in LABELS)

def triple_product(missing):
    remaining=tuple(u for u in LABELS if u!=missing)
    out=defaultdict(int)
    for terms in product(*(TRIANGLES[u].items() for u in remaining)):
        vopts=tuple(b for b,_ in terms)
        vv=tuple(x[0] for x in vopts)
        assert vv==tuple(sorted(vv)) and len(set(vv))==3
        oo=tuple(x[1] for x in vopts)
        coefficient=1
        for _,c in terms: coefficient*=c
        out[TOP_INDEX[(vv,oo)]]+=coefficient
    return {r:c for r,c in out.items() if c}

CYCLES=tuple(triple_product(j) for j in LABELS)
assert all(CYCLES)
assert all(all(abs(c)==1 for c in z.values()) for z in CYCLES)
assert not set.intersection(*(set(z) for z in CYCLES))
assert all(set(CYCLES[i]).isdisjoint(CYCLES[j]) for i in LABELS for j in LABELS if i<j)
assert all(len(z)>0 for z in CYCLES)

for z in CYCLES:
    out=defaultdict(int)
    for col_index,coef in z.items():
        for row,boundary_coef in COLS[col_index].items():out[row]+=coef*boundary_coef
    assert not any(out.values()), 'integral top cycle has nonzero boundary'

assert rank_mod_two(COLS)==1756
assert rank_mod_prime(COLS,32003)==1756

# Every permutation on the four original tetrahedron vertices induces
# an automorphism on the truncated tetrahedron, with a defined chain action.
def sign_reordering(sequence):
    return -1 if sum(sequence[i]>sequence[j] for i in range(len(sequence))
                     for j in range(i+1,len(sequence)))%2 else 1

def transformed_basis_terms(b, sigma):
    vs, opts=b
    original_to_new=[VINDEX[(sigma[VERTICES[v][0]],sigma[VERTICES[v][1]])] for v in vs]
    sign=sign_reordering(original_to_new)
    expanded=[]
    for v,option,w in zip(vs,opts,original_to_new):
        target_edges={EINDEX[tuple(sorted((VINDEX[(sigma[VERTICES[a][0]],sigma[VERTICES[a][1]])],
                                             VINDEX[(sigma[VERTICES[b][0]],sigma[VERTICES[b][1]])])))]
                      for a,b in (EDGES[INC[v][option]],EDGES[INC[v][0]])}
        assert len(target_edges)==2
        edge_selected=EDGES[INC[v][option]]
        edge_baseline=EDGES[INC[v][0]]
        def map_edge(edge):
            return EINDEX[tuple(sorted(VINDEX[(sigma[VERTICES[a][0]],sigma[VERTICES[a][1]])]
                                           for a in edge))]
        mapped_selected=map_edge(edge_selected)
        mapped_baseline=map_edge(edge_baseline)
        choices={opt:(int(INC[w][opt]==mapped_selected)-int(INC[w][opt]==mapped_baseline)) for opt in (1,2)}
        expanded.append([(w,opt,coef) for opt,coef in choices.items() if coef])
    output=defaultdict(int)
    for combination in product(*expanded):
        indexed=sorted(combination,key=lambda x:x[0])
        vv=tuple(x[0] for x in indexed); oo=tuple(x[1] for x in indexed)
        c=sign
        for _,_,coef in indexed:c*=coef
        output[TOP_INDEX[(vv,oo)]]+=c
    return {r:c for r,c in output.items() if c}

def transform_chain(z,sigma):
    out=defaultdict(int)
    for idx,c in z.items():
        for target,c2 in transformed_basis_terms(TOP_BASIS[idx],sigma).items():
            out[target]+=c*c2
    return {k:v for k,v in out.items() if v}

for sigma in permutations(LABELS):
    for j in LABELS:
        assert transform_chain(CYCLES[j],sigma)==CYCLES[sigma[j]],(sigma,j)

# Direct calculation of the integral homology representation: the four top cycles
# are visibly primitive in the ambient free chain group, have disjoint support,
# and span the rational kernel by the two exact rank computations above.
print('TRUNCATED_TETRAHEDRON_B3_Z4_S4_PERMUTATION_VERIFIED')
print('vertices=12 edges=18 C3=1760 C2=4752 rank_d3_mod2=1756 rank_d3_mod32003=1756')
print('integral_top_cycles=4 symmetry_checks=96 supports='+str([len(z) for z in CYCLES]))
