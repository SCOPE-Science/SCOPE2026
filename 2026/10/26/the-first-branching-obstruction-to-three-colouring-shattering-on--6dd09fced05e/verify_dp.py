"""Independent finite verification: unlabeled trees from NetworkX;
shattering tested via bottom-up three-color list-constraint propagation.
Requires Python 3 and networkx >=2.8.
"""
import networkx as nx
from itertools import product

def rooted_structure(T):
    parent = {0: -1}; order = [0]
    for u in order:
        for v in T.neighbors(u):
            if v not in parent:
                parent[v]=u
                order.append(v)
    return parent, order

def is_p4_free(T,S):
    for connected in nx.connected_components(T.subgraph(S)):
        if len(connected) >= 4 and nx.diameter(T.subgraph(connected)) >= 3:
            return False
    return True

def list_colorable(parent,order,lists):
    feasible={}
    for u in reversed(order):
        good=0
        for color in range(3):
            if not (lists[u] >> color)&1:continue
            if all(feasible[v] & (7^(1<<color))
                   for v in order if parent[v]==u):
                good|=1<<color
        feasible[u]=good
    return bool(feasible[0])

def shatters(T,S):
    S=tuple(sorted(S)); k=len(S)
    parent,order=rooted_structure(T)
    for target in product(range(3),repeat=k):
        d=dict(zip(S,target))
        if any(d[a]==d[b] for a,b in T.edges() if a in d and b in d):continue
        for pattern in range(1<<k):
            lists=[7]*T.number_of_nodes()
            for j,u in enumerate(S):
                lists[u]=1<<target[j] if pattern>>j&1 else 7^(1<<target[j])
            if not list_colorable(parent,order,lists):break
        else:return True
    return False

def main():
    for n in range(1,8):
        graphset=[nx.Graph()] if n==1 else list(nx.generators.nonisomorphic_trees(n))
        if n==1:graphset[0].add_node(0)
        pairs=0;fails=[]
        for T in graphset:
            T=nx.convert_node_labels_to_integers(T)
            for mask in range(1<<n):
                S={v for v in range(n) if mask>>v&1}
                if not is_p4_free(T,S):continue
                pairs+=1
                if not shatters(T,S):fails.append((T,S))
        print(f'n={n} trees={len(graphset)} p4_free_pairs={pairs} failures={len(fails)}',flush=True)
        assert len(fails)==(1 if n==7 else 0)
        if n==7:
            T,S=fails[0]
            r=next(v for v in T if v not in S)
            assert len(S)==6 and len(T)==7 and sorted(len(c) for c in nx.connected_components(T.subgraph(set(T)-S)))==[1]
            arm_sizes=[]
            for v in T[r]:
                arm_sizes.append(len(nx.node_connected_component(T.subgraph(set(T)-{r}),v)))
            assert sorted(arm_sizes)==[1,2,3]
    print('INDEPENDENT_LIST_DP_PASS')
if __name__=='__main__': main()
