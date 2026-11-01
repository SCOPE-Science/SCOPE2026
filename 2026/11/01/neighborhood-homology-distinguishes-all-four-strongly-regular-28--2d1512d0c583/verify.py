"""Exact mod-two homology classification of the four (28,12,6,4) graphs.

Requires only Python 3.10+ standard library. Run: python3 verify.py
The calculations are exhaustive, integer/bitwise and deterministic.
"""
import itertools
import collections
import heapq
import hashlib
import json

POINTS = range(8)
EDGES = list(itertools.combinations(POINTS, 2))
EDGE_ID = {e:i for i,e in enumerate(EDGES)}
GRAPH_NAMES = ('triangular_T8', 'Chang_matching', 'Chang_cycle8', 'Chang_cycle3_cycle5')
SWITCH_EDGES = (
    (),
    ((0,1),(2,3),(4,5),(6,7)),
    tuple(tuple(sorted((i, (i+1)%8))) for i in range(8)),
    ((0,1),(1,2),(0,2),(3,4),(4,5),(5,6),(6,7),(3,7)),
)
EXPECTED_BETTI = (
    {3:553,5:8},
    {3:253,4:12},
    {2:1,3:166,4:4},
    {2:2,3:175,4:24},
)
EXPECTED_TOTAL_FACES = (105897, 105897, 105833, 105869)
EXPECTED_CLIQUES_4_6 = ((280,56),(248,8),(240,0),(240,3))
EXPECTED_COLLAPSE_PAIRS = (49150,50538,51041,50161)


def make_graph(index):
    switch = {EDGE_ID[tuple(sorted(e))] for e in SWITCH_EDGES[index]}
    assert len(switch)==len(SWITCH_EDGES[index])
    nbrs = []
    for i,a in enumerate(EDGES):
        mask=0
        for j,b in enumerate(EDGES):
            if i==j:
                continue
            adjacent=bool(set(a).intersection(b))
            if (i in switch)!=(j in switch):
                adjacent=not adjacent
            if adjacent:
                mask|=1<<j
        nbrs.append(mask)
    # Check the complete strongly regular parameter table, not just degrees.
    for i in range(28):
        assert nbrs[i].bit_count()==12 and not ((nbrs[i]>>i)&1)
        for j in range(i):
            assert bool((nbrs[i]>>j)&1)==bool((nbrs[j]>>i)&1)
            assert (nbrs[i]&nbrs[j]).bit_count()==(6 if ((nbrs[i]>>j)&1) else 4)
    return nbrs


def enumerate_faces_a(neighborhoods):
    """Direct complete submask enumeration; includes empty face."""
    faces={0}
    for mask in neighborhoods:
        sub=mask
        while sub:
            faces.add(sub)
            sub=(sub-1)&mask
    return faces


def enumerate_faces_b(neighborhoods):
    """Independent combination-product enumeration of the same abstract complex."""
    faces={0}
    for mask in neighborhoods:
        vv=[v for v in range(28) if mask&(1<<v)]
        for size in range(1,13):
            for ss in itertools.combinations(vv,size):
                faces.add(sum(1<<v for v in ss))
    return faces


def face_groups(faces):
    groups=collections.defaultdict(list)
    for face in faces:
        if face:
            groups[face.bit_count()-1].append(face)
    for arr in groups.values():
        arr.sort()
    return groups


def boundary_ranks(faces, high_pivot=True):
    """Exact Gaussian elimination over F_2; boundary columns represented as integers."""
    groups=face_groups(faces)
    ranks={}
    for dim in sorted(groups):
        if dim==0:
            continue
        previous={v:i for i,v in enumerate(groups[dim-1])}
        pivots={}
        for simplex in groups[dim]:
            column=0
            bits=simplex
            while bits:
                bit=bits&-bits
                bits-=bit
                column ^= 1<<previous[simplex^bit]
            while column:
                pivot=(column.bit_length()-1) if high_pivot else ((column&-column).bit_length()-1)
                old=pivots.get(pivot)
                if old is None:
                    pivots[pivot]=column
                    break
                column^=old
        ranks[dim]=len(pivots)
    betti={dim:len(group)-ranks.get(dim,0)-ranks.get(dim+1,0)
           for dim,group in groups.items()}
    betti[0]-=1  # connected component, reduced homology
    assert all(v>=0 for v in betti.values())
    return ({k:v for k,v in sorted(betti.items()) if v},ranks)


def elementary_collapse(faces):
    """Actual sequential free-face deletions; no Morse acyclicity assumption."""
    alive=set(faces)-{0}
    codim_cofaces=collections.defaultdict(set)
    for face in alive:
        if face.bit_count()<2:
            continue
        mask=face
        while mask:
            bit=mask&-mask
            mask-=bit
            codim_cofaces[face^bit].add(face)
    priority=[]
    for f in alive:
        if len(codim_cofaces[f])==1:
            heapq.heappush(priority,(-f.bit_count(),f))
    count=0
    while priority:
        _,f=heapq.heappop(priority)
        if f not in alive or len(codim_cofaces[f])!=1:
            continue
        g=next(iter(codim_cofaces[f]))
        assert f in alive and g in alive and g.bit_count()==f.bit_count()+1
        # Unique codimension-one coface proves free face: an additional
        # higher coface would supply at least two codimension-one cofaces.
        assert not (f&~g)
        alive.remove(f)
        alive.remove(g)
        count+=1
        for z in (f,g):
            mask=z
            while mask:
                bit=mask&-mask
                mask-=bit
                sub=z^bit
                if sub in alive:
                    codim_cofaces[sub].discard(z)
                    if len(codim_cofaces[sub])==1:
                        heapq.heappush(priority,(-sub.bit_count(),sub))
    # Confirm closure at the end, and no invalid removed pair left a hole.
    for face in alive:
        bits=face
        while bits:
            bit=bits&-bits;bits-=bit
            assert (face^bit) in alive or face^bit==0
    assert len(faces)==len(alive)+2*count+1
    return alive,count


def clique_count(neighborhoods,n):
    # Independent graph invariant for identifying the four isomorphism classes.
    total=0
    def search(clique, candidates):
        nonlocal total
        if len(clique)==n:
            total+=1
            return
        while candidates and len(clique)+candidates.bit_count()>=n:
            bit=candidates&-candidates
            candidates-=bit
            v=bit.bit_length()-1
            search(clique+(v,), candidates&neighborhoods[v])
    search((),(1<<28)-1)
    return total


def main():
    outputs=[]
    for idx,name in enumerate(GRAPH_NAMES):
        graph=make_graph(idx)
        faces=enumerate_faces_a(graph)
        assert len(faces)==EXPECTED_TOTAL_FACES[idx]
        # Independent face-generation routine: every member is compared.
        assert faces==enumerate_faces_b(graph)
        betti,full_ranks=boundary_ranks(faces,True)
        collapsed,pairs=elementary_collapse(faces)
        betti_collapsed,collapsed_ranks=boundary_ranks(collapsed,False)
        assert betti==betti_collapsed==EXPECTED_BETTI[idx]
        assert pairs==EXPECTED_COLLAPSE_PAIRS[idx]
        cliques=(clique_count(graph,4),clique_count(graph,6))
        assert cliques==EXPECTED_CLIQUES_4_6[idx]
        full_f=face_groups(faces)
        collapsed_f=face_groups(collapsed)
        facevec=[len(full_f.get(k,[])) for k in range(12)]
        residualvec=[len(collapsed_f.get(k,[])) for k in range(12)]
        # The complete and reduced Euler-Poincare numbers agree exactly.
        chi=sum((-1)**i*qty for i,qty in enumerate(facevec))
        chi_from_betti=1+sum((-1)**i*rank for i,rank in betti.items())
        assert chi==chi_from_betti
        assert sum((-1)**i*qty for i,qty in enumerate(residualvec))==chi
        outputs.append({'graph':name,'nonempty_faces':len(faces)-1,
            'f_vector':facevec,'boundary_ranks':full_ranks,
            'reduced_mod2_betti':betti,'collapsed_nonempty_faces':len(collapsed),
            'collapse_pairs':pairs,'collapsed_f_vector':residualvec,
            'collapsed_boundary_ranks':collapsed_ranks,
            'four_cliques':cliques[0], 'six_cliques':cliques[1],
            'Euler_characteristic':chi})
    assert len({tuple(sorted(v['reduced_mod2_betti'].items())) for v in outputs})==4
    assert len({(v['four_cliques'],v['six_cliques']) for v in outputs})==4
    print(json.dumps(outputs,ensure_ascii=False,sort_keys=True,indent=2))
    print('VERIFY_FOUR_28_VERTEX_NEIGHBORHOOD_COMPLEXES_EXACT_MOD2_PASS')
if __name__=='__main__':
    main()
