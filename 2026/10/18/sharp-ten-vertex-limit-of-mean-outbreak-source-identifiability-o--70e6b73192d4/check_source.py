#!/usr/bin/env python3
"""Exact finite-tree source-identifiability certificate (standard library only)."""
from collections import defaultdict, deque
from itertools import combinations
from fractions import Fraction
import json


def rooted_types(limit):
    all_types = {1: ('()',)}
    for n in range(2, limit+1):
        items = sorted((code, k) for k in range(1,n) for code in all_types[k])
        out = set()
        def construct(left, first, kids):
            if not left:
                out.add('(' + ''.join(sorted(kids)) + ')')
                return
            for j in range(first, len(items)):
                code, size = items[j]
                if size <= left:
                    construct(left-size, j, kids+[code])
        construct(n-1, 0, [])
        all_types[n] = tuple(sorted(out))
    return all_types


def parse_tree(code):
    edges, stack, next_index = [], [], 0
    for c in code:
        if c == '(':
            v = next_index
            next_index += 1
            if stack:
                edges.append((stack[-1],v))
            stack.append(v)
        elif c == ')':
            assert stack
            stack.pop()
        else:
            raise ValueError('Invalid rooted-tree code')
    assert not stack
    assert len(edges) == next_index - 1
    adj = [set() for _ in range(next_index)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    return adj, edges


def rooted_canon(adj, root, parent=-1):
    return '(' + ''.join(sorted(rooted_canon(adj,c,root) for c in adj[root] if c != parent)) + ')'


def distances(adj, start):
    dis = [-1]*len(adj)
    dis[start] = 0
    q = deque([start])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if dis[v] == -1:
                dis[v]=dis[u]+1;q.append(v)
    assert -1 not in dis
    return dis


def signature(adj, root):
    d=distances(adj,root)
    return tuple(d.count(k) for k in range(len(adj)))


def outbreak_counts_at_half(adj, root):
    n=len(adj)
    edges = [(i,j) for i in range(n) for j in adj[i] if i < j]
    count=[0]*(n+1)
    for mask in range(1 << len(edges)):
        ed=[[] for _ in range(n)]
        for i, (u,v) in enumerate(edges):
            if mask & (1<<i):
                ed[u].append(v);ed[v].append(u)
        visited={root}; queue=[root]
        for node in queue:
            for v in ed[node]:
                if v not in visited:
                    visited.add(v);queue.append(v)
        count[len(visited)]+=1
    assert sum(count)==2**len(edges)
    return count


def main():
    types = rooted_types(10)
    rooted_counts = []
    free_counts = []
    collisions = []
    for n, codes in sorted(types.items()):
        rooted_counts.append(len(codes))
        classes = defaultdict(list)
        for code in codes:
            adj,edges=parse_tree(code)
            assert len(adj)==n
            free_key=min(rooted_canon(adj,v) for v in range(n))
            classes[free_key].append((code,signature(adj,0),adj))
        free_counts.append(len(classes))
        for free_key, reps in classes.items():
            signatures=defaultdict(list)
            for code,sig,adj in reps:
                signatures[sig].append((code,adj))
            for sig,pairs in signatures.items():
                if len(pairs)>1:
                    assert len(pairs)==2
                    (ca, a),(cb,b) = pairs
                    # Different canonical rooted codes cannot be related by an automorphism.
                    ca_counts=outbreak_counts_at_half(a,0)
                    cb_counts=outbreak_counts_at_half(b,0)
                    ea=sum(i*v for i,v in enumerate(ca_counts))
                    eb=sum(i*v for i,v in enumerate(cb_counts))
                    assert ea==eb
                    va=sum(i*i*v for i,v in enumerate(ca_counts))
                    vb=sum(i*i*v for i,v in enumerate(cb_counts))
                    collisions.append({'n':n,'canonical_tree':free_key,'source_roots':(ca,cb),
                        'distance_counts':sig,'outbreak_half_numerators':(ca_counts,cb_counts),
                        'mean_half_numerator':ea, 'second_moment_half_numerators':(va,vb),
                        'variance_difference':str(Fraction(va-vb,2**(n-1)))})
    assert rooted_counts==[1,1,2,4,9,20,48,115,286,719]
    assert free_counts==[1,1,1,2,3,6,11,23,47,106]
    assert len(collisions)==2 and all(c['n']==10 for c in collisions)
    assert all(c['variance_difference'] != '0' for c in collisions)
    evidence={'rooted_tree_type_counts_n1_to_10':rooted_counts,
        'unrooted_tree_type_counts_n1_to_10':free_counts,
        'number_of_same_tree_nonautomorphic_equal_mean_pairs_n_le_9':0,
        'number_of_same_tree_nonautomorphic_equal_mean_pairs_n_10':len(collisions),
        'collisions':collisions}
    print(json.dumps(evidence,sort_keys=True,separators=(',',':')))

if __name__=='__main__':
    main()
