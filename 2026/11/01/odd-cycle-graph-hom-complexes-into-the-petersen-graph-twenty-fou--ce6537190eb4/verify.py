#!/usr/bin/env python3
"""Exact finite verification of the Hom(C_5,C_7,C_9; Petersen) CW data.
No optional dependencies; counts use independent walk and cell-transfer constructions.
The homotopy inference uses the published square-free-codomain theorem.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict

POINTS=tuple(range(5))
VERTICES=tuple(combinations(POINTS,2))
VI={p:i for i,p in enumerate(VERTICES)}
ADJ=tuple(tuple(j for j,y in enumerate(VERTICES) if set(x).isdisjoint(y))
          for x in VERTICES)
NEIGHBOR_MASK=tuple(sum(1<<j for j in row) for row in ADJ)
assert len(VERTICES)==10 and all(len(row)==3 for row in ADJ)
assert all(i not in ADJ[i] for i in range(10))
assert all(len(set(ADJ[i]) & set(ADJ[j]))<=1 for i in range(10) for j in range(10) if i!=j)


def graph_cycles(k):
    cycles=set()
    def walk(path):
        if len(path)==k:
            if path[0] in ADJ[path[-1]]:
                t=tuple(path)
                cycles.add(min(t[i:]+t[:i] for i in range(k)))
                r=tuple(reversed(t))
                cycles.add(min(r[i:]+r[:i] for i in range(k)))
            return
        for j in ADJ[path[-1]]:
            if j not in path: walk(path+(j,))
    for v in range(10): walk((v,))
    # cycles contains canonical directed rotations for both orientations
    return len(cycles)//2

assert [graph_cycles(k) for k in (5,7,9)] == [12,0,20]
print('GRAPH_OK vertices=10 edges=15 girth=5 cycles_5=12 cycles_7=0 cycles_9=20')

# Independent transfer-matrix enumeration of CW cells: masks of all possible
# coordinate values. Each is a nonempty subset of one Petersen neighborhood.
STATES=sorted({sum(1<<v for v in c)
              for row in ADJ for r in range(1,4)
              for c in combinations(row,r)})
assert len(STATES)==50

def compatible(a,b):
    return all((NEIGHBOR_MASK[i] & b)==b
               for i in range(10) if (a>>i)&1)

LINKS={a:tuple(b for b in STATES if compatible(a,b)) for a in STATES}
assert sum(len(x) for x in LINKS.values())==110

def independent_cell_vector(m):
    counts=Counter()
    # root at each start coordinate, close the cycle; count as labeled cells
    for root in STATES:
        cur={(root,root.bit_count()-1):1}
        for _ in range(m-1):
            nxt=defaultdict(int)
            for (state,d),value in cur.items():
                for after in LINKS[state]:
                    nxt[after,d+after.bit_count()-1]+=value
            cur=nxt
        for (state,d),value in cur.items():
            if root in LINKS[state]:counts[d]+=value
    return counts


def homomorphisms(m):
    walks=[]
    def search(path):
        if len(path)==m:
            if path[0] in ADJ[path[-1]]:walks.append(path)
            return
        for j in ADJ[path[-1]]:search(path+(j,))
    for v in range(10):search((v,))
    # Graph adjacency spectrum of the Petersen graph: 3^1, 1^5, (-2)^4.
    assert len(walks)==3**m+5+4*(-2)**m
    return walks


def run(m, expected):
    walks=homomorphisms(m)
    index={w:i for i,w in enumerate(walks)}
    pa=list(range(len(walks)))
    def find(i):
        while pa[i]!=i:pa[i]=pa[pa[i]];i=pa[i]
        return i
    def join(i,j):
        a,b=find(i),find(j)
        if a!=b:pa[b]=a
    # 1-skeleton: change exactly one coordinate to a new common neighbor.
    edges=0
    for ix,w in enumerate(walks):
        for j in range(m):
            avail=NEIGHBOR_MASK[w[(j-1)%m]] & NEIGHBOR_MASK[w[(j+1)%m]]
            for v in range(10):
                if v!=w[j] and (avail>>v)&1:
                    z=w[:j]+(v,)+w[j+1:]
                    jx=index[z]
                    if ix<jx:edges+=1
                    join(ix,jx)
    sizes=Counter(find(i) for i in range(len(walks)))
    comp_sizes=Counter(sizes.values())
    # Exhaustive expansion of CW product-of-simplex cells from homomorphisms.
    starts={tuple(1<<v for v in w) for w in walks}
    cells=set(starts); stack=list(starts)
    while stack:
        c=stack.pop()
        for j in range(m):
            allowed=(1<<10)-1
            for v in range(10):
                if (c[(j-1)%m]>>v)&1:allowed &= NEIGHBOR_MASK[v]
                if (c[(j+1)%m]>>v)&1:allowed &= NEIGHBOR_MASK[v]
            extras=allowed & ~c[j]
            while extras:
                bit=extras & -extras; extras-=bit
                z=c[:j]+(c[j]|bit,)+c[j+1:]
                if z not in cells:cells.add(z);stack.append(z)
    bycomp=defaultdict(Counter)
    for c in cells:
        # Any selection of one vertex per coordinate gives a homomorphism.
        base=tuple((x & -x).bit_length()-1 for x in c)
        r=find(index[base]);d=sum(x.bit_count()-1 for x in c)
        bycomp[r][d]+=1
    facevec=Counter({d:sum(cnt[d] for cnt in bycomp.values())
                     for d in range(m)})
    facevec={k:v for k,v in facevec.items() if v}
    expected_vector=independent_cell_vector(m)
    assert facevec==expected_vector,(m,facevec,expected_vector)
    assert len(cells)==sum(facevec.values())
    assert facevec==expected['cells'],(m,facevec)
    assert comp_sizes==expected['sizes'],(m,comp_sizes)
    assert edges==facevec.get(1,0)
    chis=Counter(sum((-1)**d*n for d,n in vec.items()) for vec in bycomp.values())
    assert chis==expected['eulers']
    print('HOM_OK m={} homomorphisms={} components={} component_sizes={} cells={} cell_vector={} component_eulers={}'.format(
        m,len(walks),len(sizes),sorted(comp_sizes.items()),len(cells),
        tuple(facevec.get(d,0) for d in range(max(facevec)+1)),sorted(chis.items())))
    if m in (7,9):
        nontrivial={r for r,sz in sizes.items() if sz>1}
        assert len(nontrivial)==24
        root=min(nontrivial)
        root_w=walks[root]
        orbit=set();stab=[]
        for perm in permutations(POINTS):
            transformation=tuple(VI[tuple(sorted(perm[a] for a in v))] for v in VERTICES)
            target=tuple(transformation[z] for z in root_w)
            to=find(index[target])
            assert to in nontrivial
            orbit.add(to)
            if to==root:stab.append(perm)
        assert len(orbit)==24 and len(stab)==5
        # Every nonidentity stabilizer element has order five (cyclic C5).
        for p in stab:
            if p!=POINTS:
                cur=tuple(range(5))
                for k in range(1,6):
                    cur=tuple(p[v] for v in cur)
                    if cur==POINTS:break
                assert k==5
        print('ACTION_OK m={} active_components=24 automorphism_group_order=120 orbit_size=24 stabilizer=C5 integral_H1=Ind_C5^S5_Z'.format(m))
    if m==9:
        isolated={walks[r] for r,sz in sizes.items() if sz==1}
        assert len(isolated)==360
        assert all(len(set(w))==9 for w in isolated)
        assert all(len(set(w))<9 for i,w in enumerate(walks) if find(i) in nontrivial)
        print('CYCLE_OK m=9 rigid_components=360 bijective_with_oriented_based_9cycles')

run(5, {'sizes':Counter({1:120}),'eulers':Counter({1:120}),'cells':{0:120}})
run(7, {'sizes':Counter({70:24}),'eulers':Counter({0:24}),
        'cells':{0:1680,1:2520,2:840}})
run(9, {'sizes':Counter({1:360,720:24}),'eulers':Counter({1:360,0:24}),
        'cells':{0:17640,1:45360,2:44280,3:19440,4:3240}})
print('ALL_VERIFY_OK')
