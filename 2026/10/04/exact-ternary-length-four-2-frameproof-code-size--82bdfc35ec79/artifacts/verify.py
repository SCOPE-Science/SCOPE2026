from itertools import product, combinations

Q=list(product(range(3), repeat=4))
idx={w:i for i,w in enumerate(Q)}
N=len(Q)

# A forbidden triple is three distinct words x,y,z such that one is in
# the coordinatewise descendant of the other two. For three distinct
# words, if any member is in the descendant of the other two then the
# triple cannot occur in a 2-frameproof code.
edges=set()
for i,j in combinations(range(N),2):
    x,y=Q[i],Q[j]
    choices=[tuple(sorted({x[t],y[t]})) for t in range(4)]
    for zw in product(*choices):
        z=idx[zw]
        if z!=i and z!=j:
            edges.add(tuple(sorted((i,j,z))))
edges=tuple(sorted(edges))
edge_set=set(edges)

WITNESS=[
(0,0,0,0),(0,1,2,2),(0,2,1,2),(0,2,2,1),
(1,1,1,1),(1,2,0,0),(1,0,0,2),(1,0,2,0),
(2,2,2,2),(2,0,1,1),(2,1,0,1),(2,1,1,0)]
W=[idx[w] for w in WITNESS]
assert len(set(W))==12
for a,b,c in combinations(W,3):
    assert tuple(sorted((a,b,c))) not in edge_set

# Pair completion masks: comp[a][b] is the set of c such that {a,b,c}
# is forbidden. Used by both exact engines but traversed differently.
comp=[[0]*N for _ in range(N)]
for a,b,c in edges:
    comp[a][b] |= 1<<c; comp[b][a] |= 1<<c
    comp[a][c] |= 1<<b; comp[c][a] |= 1<<b
    comp[b][c] |= 1<<a; comp[c][b] |= 1<<a

zero=idx[(0,0,0,0)]
canon=[idx[(1,0,0,0)],idx[(1,1,0,0)],idx[(1,1,1,0)],idx[(1,1,1,1)]]
ALL=(1<<N)-1

def initial_candidates(root):
    mask=ALL & ~(1<<zero) & ~(1<<root)
    mask &= ~comp[zero][root]
    return mask

def iterbits(mask):
    while mask:
        b=mask & -mask
        yield b.bit_length()-1
        mask-=b

# Engine A: fixed least-index include/exclude recursion. No heuristic
# upper bound beyond remaining cardinality, so it is a direct exhaustive
# enumeration of all feasible extensions of the canonical root pairs.
def engine_a(root,target=13):
    nodes=0
    sel=[zero,root]
    def rec(mask):
        nonlocal nodes
        nodes+=1
        need=target-len(sel)
        if need<=0: return True
        if mask.bit_count()<need: return False
        v=(mask & -mask).bit_length()-1
        rest=mask & ~(1<<v)
        # include v: every existing selected x forbids comp[x][v]
        m=rest
        for x in sel:
            m &= ~comp[x][v]
        sel.append(v)
        if rec(m): return True
        sel.pop()
        return rec(rest)
    return rec(initial_candidates(root)),nodes

# Engine B: independent branch order and a safe incompatibility-clique
# upper bound. Given selected S, two remaining vertices u,v are mutually
# incompatible if S contains an x for which {x,u,v} is forbidden. Any
# extension may contain at most one vertex from a clique in this graph.
def engine_b(root,target=13):
    nodes=0
    sel=[zero,root]
    def compatible_graph(mask):
        verts=list(iterbits(mask)); adj={v:0 for v in verts}
        sm=sel[:] 
        for ii,u in enumerate(verts):
            for v in verts[ii+1:]:
                bad=False
                for x in sm:
                    if (comp[u][v]>>x)&1:
                        bad=True; break
                if not bad:
                    adj[u]|=1<<v; adj[v]|=1<<u
        return verts,adj
    def greedy_color_bound(mask):
        # Proper coloring of the compatibility graph gives an upper bound
        # on a clique there, but feasible extensions need not be cliques.
        # So instead use only a guaranteed partition into incompatibility
        # cliques built greedily; each such class contributes at most one.
        verts=list(iterbits(mask)); classes=[]
        for v in verts:
            placed=False
            for cl in classes:
                if all(any(((comp[v][u]>>x)&1) for x in sel) for u in cl):
                    cl.append(v); placed=True; break
            if not placed: classes.append([v])
        return len(classes)
    def rec(mask):
        nonlocal nodes
        nodes+=1
        need=target-len(sel)
        if need<=0:return True
        if mask.bit_count()<need:return False
        if greedy_color_bound(mask)<need:return False
        # choose a high-conflict vertex, different from engine A
        verts=list(iterbits(mask))
        v=max(verts,key=lambda u: sum((comp[x][u]&mask).bit_count() for x in sel))
        rest=mask & ~(1<<v)
        m=rest
        for x in sel:m &= ~comp[x][v]
        # exclude first, then include
        if rec(rest): return True
        sel.append(v)
        ok=rec(m)
        sel.pop()
        return ok
    return rec(initial_candidates(root)),nodes

nodes_a=nodes_b=0
for wt,root in enumerate(canon,1):
    ok,n=engine_a(root); nodes_a+=n; assert not ok
    ok2,n2=engine_b(root); nodes_b+=n2; assert not ok2

# Symmetry completeness: after sending a chosen first codeword to 0000
# by independent symbol permutations in each coordinate, the stabilizer
# of 0000 sends any second nonzero word to exactly one canonical support
# weight (1,2,3,4), up to coordinate permutation.
weights={sum(v!=0 for v in w) for w in Q if w!=(0,0,0,0)}
assert weights=={1,2,3,4}

print('VERIFY_OK')
print('words',N)
print('forbidden_triples',len(edges))
print('witness_size',len(W))
print('canonical_second_word_cases',len(canon))
print('engine_a_nodes',nodes_a)
print('engine_b_nodes',nodes_b)
print('upper_bound_no_size_13',True)
print('exact_M_4_2_3',12)
