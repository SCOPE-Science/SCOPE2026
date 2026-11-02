"""Exact finite census for Littlestone dimension of rooted-tree order ideals.
Only Python standard library is required. Two distinct tree generators and
separate dimension algorithms reproduce the same rooted isomorphism profiles.
"""
from itertools import product
from functools import lru_cache
from collections import defaultdict


def canonical(children, root=0, parent=-1):
    return '(' + ''.join(sorted(canonical(children, x, root) for x in children[root] if x != parent)) + ')'


def edge_list_from_prufer(n, code):
    if n == 1:
        return []
    deg = [1] * n
    for x in code:
        deg[x] += 1
    edges = []
    for x in code:
        leaf = next(i for i in range(n) if deg[i] == 1)
        edges.append((leaf, x))
        deg[leaf] -= 1
        deg[x] -= 1
    a, b = [i for i in range(n) if deg[i] == 1]
    edges.append((a, b))
    return edges


def adjacency(n, edges):
    adj = [[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def rooted_ideals(n, adj, r):
    # Construct ancestral masks with graph DFS, then test all 2^n node sets.
    anc = [0] * n
    def walk(x,p,mask):
        anc[x] = mask | (1<<x)
        for v in adj[x]:
            if v != p:
                walk(v,x,anc[x])
    walk(r,-1,0)
    return tuple(mask for mask in range(1<<n)
                 if all((mask & (1<<v)) == 0 or (mask & anc[v]) == anc[v]
                        for v in range(n)))


def dimension_masks(concepts, n):
    column = [sum(1<<j for j,c in enumerate(concepts) if c & (1<<i)) for i in range(n)]
    @lru_cache(None)
    def value(state):
        if not state or state & (state-1) == 0:
            return 0
        d=0
        for column_mask in column:
            yes = state & column_mask
            no = state ^ yes
            if yes and no:
                d=max(d, 1 + min(value(yes),value(no)))
        return d
    return value((1<<len(concepts))-1)


def dimension_feasibility(concepts, n):
    # Independent feasibility test: a full binary shattered tree of depth d
    # exists iff some coordinate splits into two feasible depth-(d-1) classes.
    def words_to_bools(S):
        return tuple(tuple((c>>i)&1 for i in range(n)) for c in S)
    initial=words_to_bools(concepts)
    @lru_cache(None)
    def feasible(S, depth):
        if depth==0:return bool(S)
        if len(S)<(1<<depth):return False
        for i in range(n):
            Z=tuple(v for v in S if v[i]==0)
            O=tuple(v for v in S if v[i]==1)
            if Z and O and feasible(Z,depth-1) and feasible(O,depth-1):
                return True
        return False
    d=0
    while feasible(initial,d+1):d+=1
    return d


def by_prufer(n):
    result={}
    for seq in product(range(n), repeat=max(0,n-2)):
        adj=adjacency(n,edge_list_from_prufer(n,seq))
        for root in range(n):
            shape=canonical(adj,root)
            if shape in result:continue
            ideals=rooted_ideals(n,adj,root)
            result[shape]=(len(ideals),dimension_masks(ideals,n))
    return result


def by_recursive_labels(n):
    result={}
    for parents in product(*(range(i) for i in range(1,n))):
        edges=[(i,p) for i,p in enumerate(parents,start=1)]
        adj=adjacency(n,edges)
        shape=canonical(adj,0)
        if shape in result:continue
        ideals=rooted_ideals(n,adj,0)
        result[shape]=(len(ideals),dimension_feasibility(ideals,n))
    return result


def main():
    out=[]
    counts=[1,1,2,4,9,20]
    exceptions={'((()())(()))':(16,3), '((())(())())':(19,3)}
    for n in range(1,7):
        first=by_prufer(n)
        second=by_recursive_labels(n)
        assert first==second,(n,first,second)
        assert len(first)==counts[n-1],(n,len(first))
        bad={s:v for s,v in first.items() if v[1]<(v[0].bit_length()-1)}
        assert bad==(exceptions if n==6 else {}),(n,bad)
        for s,(N,d) in sorted(first.items()):
            out.append((n,s,N,d,N.bit_length()-1))
        print('ROOTED_CENSUS_PASS',n,len(first),'exceptions',len(bad))
    with open('rooted_census.tsv','w',encoding='utf-8',newline='\n') as f:
        f.write('vertices\tcanonical_shape\tideals\tLdim\tentropy_floor\n')
        for vals in out:
            f.write('\t'.join(map(str,vals))+'\n')
    print('INDEPENDENT_ROOTED_ENTROPY_CHECKS_PASS',len(out),'exceptional_shapes',2)


if __name__=='__main__':main()
