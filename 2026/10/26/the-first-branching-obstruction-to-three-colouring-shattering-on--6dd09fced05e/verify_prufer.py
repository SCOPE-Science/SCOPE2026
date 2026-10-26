"""Self-contained exhaustive verification of the first tree-colouring shattering obstruction.
Requires Python 3.10+ only. All graphs are simple trees on 1..7 vertices.
"""
from itertools import product, combinations
from collections import defaultdict


def edges_from_prufer(seq, n):
    if n == 1: return ()
    degree = [1] * n
    for x in seq: degree[x] += 1
    edges = []
    for x in seq:
        y = min(i for i in range(n) if degree[i] == 1)
        edges.append(tuple(sorted((x,y))))
        degree[x] -= 1; degree[y] -= 1
    a,b = (i for i in range(n) if degree[i] == 1)
    edges.append((a,b))
    return tuple(sorted(edges))


def canon(n, edges):
    adj = [set() for _ in range(n)]
    for a,b in edges: adj[a].add(b); adj[b].add(a)
    centers=set(range(n))
    while len(centers)>2:
        leaves={u for u in centers if len(adj[u]&centers)<=1}
        centers-=leaves
    def rooted(u,prev):
        return '('+''.join(sorted(rooted(v,u) for v in adj[u] if v!=prev))+')'
    return min(rooted(c,-1) for c in centers)


def all_trees(n):
    ans={}
    if n==1: return [(1,())]
    for seq in product(range(n),repeat=max(0,n-2)):
        ed=edges_from_prufer(seq,n)
        key=canon(n,ed)
        if key not in ans:ans[key]=ed
    return [(n,ans[k]) for k in sorted(ans)]


def has_induced_p4(S, E):
    S=set(S); a={v:set() for v in S}
    for u,v in E:
        if u in S and v in S:a[u].add(v);a[v].add(u)
    for u in S:
        for v in a[u]:
            for w in a[v]-{u}:
                for z in a[w]-{v}:
                    if z!=u and z not in a[u]:return True
    return False


def proper_colorings(n, E):
    return [a for a in product(range(3),repeat=n) if all(a[u]!=a[v] for u,v in E)]


def shatterable(n,E,S,C):
    S=tuple(S);size=len(S)
    induced=[(S.index(a),S.index(b)) for a,b in E if a in S and b in S]
    for target in product(range(3),repeat=size):
        if any(target[i]==target[j] for i,j in induced):continue
        got=set()
        for coloring in C:
            pat=sum((coloring[u]==target[i])<<i for i,u in enumerate(S))
            got.add(pat)
            if len(got)==(1<<size):return True
    return False


def main():
    for n in range(1,8):
        trees=all_trees(n);num=0;bad=[]
        for _,E in trees:
            C=proper_colorings(n,E)
            for mask in range(1<<n):
                S=tuple(i for i in range(n) if mask>>i&1)
                if has_induced_p4(S,E):continue
                num+=1
                if not shatterable(n,E,S,C): bad.append((E,S))
        print(f'n={n} trees={len(trees)} p4_free_pairs={num} failures={len(bad)}',flush=True)
        if bad:
            for E,S in bad:print('  obstruction_edges='+str(E)+' selected='+str(S))
        assert (len(bad)==1 if n==7 else len(bad)==0)
        if n==7:
            E,S=bad[0]
            assert sorted(sorted(len(c) for c in tree_arms(n,E,u)) for u in range(n) if u not in S if len(tree_arms(n,E,u))==3)==[[1,2,3]]
    print('FIRST_OBSTRUCTION_UNIQUE_UP_TO_TREE_AND_MARKED_SET_ISOMORPHISM_PASS')

def tree_arms(n,E,r):
    adj=[set() for _ in range(n)]
    for u,v in E:adj[u].add(v);adj[v].add(u)
    arms=[]
    for w in adj[r]:
        stack=[(w,r)];count=0
        while stack:
            u,p=stack.pop();count+=1;stack.extend((v,u) for v in adj[u] if v!=p)
        arms.append([None]*count)
    return arms

if __name__=='__main__':main()
