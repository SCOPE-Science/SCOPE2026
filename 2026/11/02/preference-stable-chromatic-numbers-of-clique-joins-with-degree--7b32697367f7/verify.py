#!/usr/bin/env python3
"""Standalone finite checks of preference-stable clique-join claims."""
import itertools


def edges_path(n):
    return {(i, i+1) for i in range(n-1)}


def edges_cycle(n):
    return edges_path(n) | {(0,n-1)}


def join_clique(t, h_edges, h_n):
    edges = {(i,j) for i in range(t) for j in range(i+1,t)}
    edges |= {(i,j+t) for i in range(t) for j in range(h_n)}
    edges |= {(i+t,j+t) for i,j in h_edges}
    return t+h_n, edges


def proper(c, edges):
    return all(c[u] != c[v] for u,v in edges)


def stable(c, edges, rank):
    n=len(c)
    arcs=[[] for _ in range(n)]
    for u,v in edges:
        if rank[u][c[v]]<rank[u][c[u]]:arcs[u].append(v)
        if rank[v][c[u]]<rank[v][c[v]]:arcs[v].append(u)
    state=[0]*n
    def dfs(v):
        state[v]=1
        for w in arcs[v]:
            if state[w]==1:return False
            if state[w]==0 and not dfs(w):return False
        state[v]=2
        return True
    return all(state[v] or dfs(v) for v in range(n))


def check_all_profiles(n,edges,k):
    perms=list(itertools.permutations(range(k)))
    proper_list=[c for c in itertools.product(range(k),repeat=n) if proper(c,edges)]
    for profile in itertools.product(perms, repeat=n):
        rank=[{col:i for i,col in enumerate(p)} for p in profile]
        if not any(stable(c,edges,rank) for c in proper_list):
            return False
    return True


# Self-contained Grundy certificate for all tested clique sizes.
for t in range(1,16):
    n, edges=join_clique(t,edges_path(4),4)
    colors=list(range(4,t+4))+[1,2,3,1]
    assert len(colors)==n and proper(colors,edges)
    for v in range(n):
        seen={colors[w] for u,w in edges if u==v}|{colors[u] for u,w in edges if w==v}
        assert set(range(1,colors[v])).issubset(seen)
print('GRUNDY_JOIN_CERTIFICATES_OK t=1..15')

# Independent direct profile enumeration on the small base graph classes.
instances=[('P1',1,set(),1),('P2',2,edges_path(2),2),
           ('P3',3,edges_path(3),2),('P4',4,edges_path(4),3),
           ('C3',3,edges_cycle(3),3),('C4',4,edges_cycle(4),3)]
for name,n,edges,k in instances:
    assert check_all_profiles(n,edges,k)
    print('ALL_PREFERENCE_PROFILES_ADMIT_STABLE_COLORING',name,k)

# Direct joint-profile checks for small clique joins, beyond the base components.
for core_n,core_edges,k in [(1,set(),2),(2,edges_path(2),3),(3,edges_path(3),3)]:
    nn,ee=join_clique(1,core_edges,core_n)
    assert check_all_profiles(nn,ee,k)
    print('JOIN_PROFILE_EXHAUSTIVE_OK',core_n,k)

# Direct universal obstruction: this three-color preference profile blocks all
# proper colorings of K_1 join P_4, independently of the Grundy theorem.
orders=[(0,1,2),(0,1,2),(0,2,1),(2,0,1),(1,0,2)]
rank=[{col:i for i,col in enumerate(p)} for p in orders]
n, edges=join_clique(1,edges_path(4),4)
colors=[c for c in itertools.product(range(3),repeat=n) if proper(c,edges)]
assert len(colors)==6 and all(not stable(c,edges,rank) for c in colors)
print('EXPLICIT_FAN_OBSTRUCTION_OK', len(colors))
print('VERIFY_OK')
