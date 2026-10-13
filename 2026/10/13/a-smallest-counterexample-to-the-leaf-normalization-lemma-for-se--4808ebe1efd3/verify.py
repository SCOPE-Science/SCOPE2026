from itertools import product


def adjacency(n, edges):
    a=[set() for _ in range(n)]
    for u,v in edges:
        a[u].add(v); a[v].add(u)
    return a


def italian(adj, f):
    for v,x in enumerate(f):
        if x==0 and sum(f[u] for u in adj[v]) < 2:
            return False
    return True


def transfer(f,u,v):
    g=list(f)
    if g[u] <= 0 or g[v] != 0:
        return None
    g[u]-=1
    g[v]=1
    return tuple(g)


def secure_italian(adj, f):
    if not italian(adj,f):
        return False
    for v,x in enumerate(f):
        if x!=0:
            continue
        ok=False
        for u in adj[v]:
            if f[u]>0:
                g=transfer(f,u,v)
                if g is not None and italian(adj,g):
                    ok=True
                    break
        if not ok:
            return False
    return True


def minima(adj):
    n=len(adj)
    best=None; ms=[]
    for f in product(range(3), repeat=n):
        w=sum(f)
        if best is not None and w>best:
            continue
        if secure_italian(adj,f):
            if best is None or w<best:
                best=w; ms=[f]
            elif w==best:
                ms.append(f)
    return best,ms


def edges_from_mask(n,mask):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    return [e for k,e in enumerate(pairs) if (mask>>k)&1]

# Target graph order: ell=0,x=1,y=2,p=3,q=4.
target_edges=[(0,1),(1,2),(1,3),(1,4),(2,3),(2,4)]
adj=adjacency(5,target_edges)
best,ms=minima(adj)
assert best==3
assert ms==[(0,2,1,0,0)], (best,ms)
leaf=0
assert len(adj[leaf])==1
assert ms[0][leaf]==0
# Candidate security witnesses: x defends ell; y defends p and q.
f=ms[0]
assert italian(adj, transfer(f,1,0))
assert italian(adj, transfer(f,2,3))
assert italian(adj, transfer(f,2,4))
# The transfer used in the published leaf-normalization proof need not preserve security.
g=transfer(f,1,0)
assert g==(1,1,1,0,0)
assert italian(adj,g)
assert not secure_italian(adj,g)

# Exhaust all simple labeled graphs of order <5 with at least one leaf.
# A graph is a counterexample to the normalization lemma if none of its
# minimum SIDFs assigns label 1 to every leaf.
relevant=0
counter=0
labelings_checked=0
by_n=[]
for n in range(1,5):
    pairs=n*(n-1)//2
    rn=0
    for mask in range(1<<pairs):
        es=edges_from_mask(n,mask)
        a=adjacency(n,es)
        leaves=[v for v in range(n) if len(a[v])==1]
        if not leaves:
            continue
        rn+=1; relevant+=1
        b,mins=minima(a)
        labelings_checked += 3**n
        assert b is not None
        good=any(all(ff[v]==1 for v in leaves) for ff in mins)
        if not good:
            counter+=1
    by_n.append((n,rn))
assert counter==0

print('VERIFY_OK')
print('target_order = 5')
print('target_edges =', target_edges)
print('target_gamma_secure_italian =', best)
print('target_minimum_functions =', len(ms))
print('target_unique_minimum =', ms[0])
print('transferred_leaf_function_is_italian =', italian(adj,g))
print('transferred_leaf_function_is_secure =', secure_italian(adj,g))
print('smaller_leaf_graphs_by_order =', by_n)
print('smaller_leaf_graphs_checked =', relevant)
print('smaller_graph_labelings_checked =', labelings_checked)
print('smaller_counterexamples =', counter)
