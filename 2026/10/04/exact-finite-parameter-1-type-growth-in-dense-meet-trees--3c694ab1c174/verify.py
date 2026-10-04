#!/usr/bin/env python3
from itertools import product


def prufer_trees(n):
    """Yield undirected labelled trees on range(n) as adjacency tuples."""
    if n == 1:
        yield ((),)
        return
    if n == 2:
        yield ((1,), (0,))
        return
    for code in product(range(n), repeat=n-2):
        deg=[1]*n
        for x in code:
            deg[x]+=1
        adj=[set() for _ in range(n)]
        for x in code:
            leaf=min(i for i,d in enumerate(deg) if d==1)
            adj[leaf].add(x); adj[x].add(leaf)
            deg[leaf]-=1; deg[x]-=1
        u,v=[i for i,d in enumerate(deg) if d==1]
        adj[u].add(v); adj[v].add(u)
        yield tuple(tuple(sorted(a)) for a in adj)


def rooted_meet_tables(n):
    """Every rooted labelled tree, represented by its meet table."""
    seen=set()
    for adj in prufer_trees(n):
        for root in range(n):
            parent=[None]*n
            parent[root]=root
            stack=[root]
            order=[root]
            while stack:
                u=stack.pop()
                for v in adj[u]:
                    if parent[v] is None:
                        parent[v]=u
                        stack.append(v)
                        order.append(v)
            depth=[0]*n
            for u in order[1:]:
                depth[u]=depth[parent[u]]+1
            def meet(a,b):
                x,y=a,b
                while depth[x]>depth[y]: x=parent[x]
                while depth[y]>depth[x]: y=parent[y]
                while x!=y:
                    x=parent[x]; y=parent[y]
                return x
            tab=tuple(tuple(meet(i,j) for j in range(n)) for i in range(n))
            if tab not in seen:
                seen.add(tab)
                yield tab


def restricts(C,B,s):
    return all(C[i][j]==B[i][j] for i in range(s) for j in range(s))


def closure(tab, seed):
    S=set(seed)
    changed=True
    while changed:
        changed=False
        old=tuple(S)
        for a in old:
            for b in old:
                c=tab[a][b]
                if c not in S:
                    S.add(c); changed=True
    return S

# Cache all small rooted meet-trees once.
tables={n:list(rooted_meet_tables(n)) for n in range(1,7)}
# Cayley/rooted-tree sanity check: n^(n-1) rooted labelled trees.
for n,ts in tables.items():
    assert len(ts)==n**(n-1), (n,len(ts),n**(n-1))

for s in range(1,5):
    base_tables=tables[s]
    one=tables[s+1]
    two=tables[s+2]
    patterns=set()
    for B in base_tables:
        c1=sum(1 for C in one if restricts(C,B,s))
        # In the s+2 case, x is the last label; the other new label must be
        # generated from B union {x}, so closure has all s+2 points.
        x=s+1
        c2=sum(1 for C in two if restricts(C,B,s) and closure(C, list(range(s))+[x])==set(range(s+2)))
        patterns.add((c1,c2))
        assert c1==2*s, (s,c1)
        assert c2==s, (s,c2)
        assert s+c1+c2==4*s
    print('s',s,'bases',len(base_tables),'extension_patterns',sorted(patterns))

# Construct a full binary comb with m leaves. Leaves are labels 0..m-1;
# internal labels m..2m-2. The meet table is obtained from a rooted tree.
def binary_comb_table(m):
    if m==1:
        return ((0,),), [0]
    n=2*m-1
    # Build rooted binary comb: first internal node joins leaves 0,1; each
    # subsequent internal node becomes the parent of the previous root and next leaf.
    parent=[None]*n
    r=m
    parent[0]=r; parent[1]=r
    current=r
    for leaf in range(2,m):
        nr=m+leaf-1
        parent[current]=nr
        parent[leaf]=nr
        current=nr
    parent[current]=current
    root=current
    depth=[0]*n
    children=[[] for _ in range(n)]
    for v,p in enumerate(parent):
        if v!=p: children[p].append(v)
    stack=[root]
    order=[root]
    while stack:
        u=stack.pop()
        for v in children[u]:
            depth[v]=depth[u]+1; stack.append(v); order.append(v)
    def meet(a,b):
        x,y=a,b
        while depth[x]>depth[y]: x=parent[x]
        while depth[y]>depth[x]: y=parent[y]
        while x!=y: x=parent[x]; y=parent[y]
        return x
    tab=tuple(tuple(meet(i,j) for j in range(n)) for i in range(n))
    return tab,list(range(m))

for m in range(1,9):
    tab,leaves=binary_comb_table(m)
    cl=closure(tab,leaves)
    assert len(cl)==2*m-1, (m,len(cl))
    # A chain of m distinct points is already meet-closed.
    chain=tuple(tuple(min(i,j) for j in range(m)) for i in range(m))
    assert closure(chain,range(m))==set(range(m))

print('binary_and_chain_witnesses_through_m',8)
print('VERIFY_OK')
