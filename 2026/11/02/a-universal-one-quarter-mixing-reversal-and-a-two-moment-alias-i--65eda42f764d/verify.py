"""Exact finite checks for the four-site two-layer epidemic theorem.

Run with Python 3 standard library: python3 verify.py
The analytic proof of the general parameter identity is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations, product

V = tuple(range(4))
EDGES = tuple(combinations(V, 2))
STAR = frozenset(((0,1),(0,2),(0,3)))
PATH = frozenset(((0,1),(1,2),(2,3)))
ASSERTIONS = 0

def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)

def dsu_profile(open_edges):
    parent = list(V)
    def root(x):
        while x != parent[x]:
            x = parent[x]
        return x
    for u,v in open_edges:
        parent[root(u)] = root(v)
    sizes = {}
    for vertex in V:
        r = root(vertex)
        sizes[r] = sizes.get(r, 0) + 1
    result = [0]*5
    for size in sizes.values():
        result[size] += size
    return tuple(result)

def bfs_profile(open_edges):
    adjacency = {v:set() for v in V}
    for u,v in open_edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    result = [0]*5
    seen = set()
    for start in V:
        if start in seen:
            continue
        frontier = [start]
        seen.add(start)
        for current in frontier:
            for neighbor in adjacency[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    frontier.append(neighbor)
        result[len(frontier)] += len(frontier)
    return tuple(result)

def counts_by_strong_weak(local_tree):
    table = {(k,l): [0]*5 for k in range(4) for l in range(4)}
    for indicators in product((0,1),repeat=len(EDGES)):
        chosen = [e for e,b in zip(EDGES,indicators) if b]
        k = sum(e in local_tree for e in chosen)
        l = len(chosen)-k
        counts = dsu_profile(chosen)
        for j in range(1,5):
            table[k,l][j] += counts[j]
    return table

def bond_distribution(local_tree, p, q):
    result = [F(0)]*5
    for indicators in product((0,1),repeat=len(EDGES)):
        wt = F(1)
        open_edges = []
        for edge,bit in zip(EDGES,indicators):
            t = p if edge in local_tree else q
            wt *= t if bit else 1-t
            if bit:
                open_edges.append(edge)
        sizes = dsu_profile(open_edges)
        for j in range(1,5):
            result[j] += wt*F(sizes[j],4)
    return tuple(result)

def independent_trials_distribution(local_tree,g,r):
    result = [F(0)]*5
    base_edges = tuple(EDGES)
    local_edges = tuple(sorted(local_tree))
    for bits in product((0,1),repeat=9):
        wt = F(1)
        chosen = set()
        for edge,bit in zip(base_edges,bits[:6]):
            wt *= g if bit else 1-g
            if bit:
                chosen.add(edge)
        for edge,bit in zip(local_edges,bits[6:]):
            wt *= r if bit else 1-r
            if bit:
                chosen.add(edge)
        if not wt:
            continue
        sizes = bfs_profile(chosen)
        for j in range(1,5):
            result[j] += wt*F(sizes[j],4)
    return tuple(result)

EXPECTED_NONZERO = {
    (0,2): (1,-4,3,0),
    (0,3): (1,0,3,-4),
    (1,1): (-2,8,-6,0),
    (1,2): (-2,0,-6,8),
    (2,0): (1,-4,3,0),
    (2,1): (1,0,3,-4),
}
A=counts_by_strong_weak(STAR)
B=counts_by_strong_weak(PATH)
for k in range(4):
    for l in range(4):
        actual=tuple(A[k,l][j]-B[k,l][j] for j in range(1,5))
        check(actual==EXPECTED_NONZERO.get((k,l),(0,0,0,0)),
              'coefficient table mismatch at (%d,%d)'%(k,l))

for g in [F(0),F(1,10),F(1,5),F(1,4),F(2,5),F(1,2),F(3,4),F(1)]:
    for r in [F(0),F(1,5),F(1,2),F(4,5),F(1)]:
        p = g+(1-g)*r
        s=bond_distribution(STAR,p,g)
        t=bond_distribution(PATH,p,g)
        s_alt=independent_trials_distribution(STAR,g,r)
        t_alt=independent_trials_distribution(PATH,g,r)
        check(s==s_alt,'independent global/local trials disagree (star)')
        check(t==t_alt,'independent global/local trials disagree (path)')
        check(sum(s[1:])==1 and sum(t[1:])==1,'probabilities not normalized')
        K=(1-p)*(p-g)**2
        expected=(F(0),K/4,-(1-g)*K,3*K/4,-g*K)
        difference=tuple(s[j]-t[j] for j in range(5))
        check(difference==expected,'full-law identity mismatch')
        moment1=sum(j*difference[j] for j in range(1,5))
        moment2=sum(j*j*difference[j] for j in range(1,5))
        moment3=sum(j*j*j*difference[j] for j in range(1,5))
        check(moment1==K*(1-4*g)/2,'first moment identity mismatch')
        check(moment2==3*K*(1-4*g),'second moment identity mismatch')
        check(moment3==K*(F(25,2)-56*g),'third moment identity mismatch')
        if g==F(1,4) and 0<r<1:
            check(moment1==moment2==0 and moment3!=0,'nontrivial two-moment alias mismatch')
            check(difference[1:] == (K/4,-3*K/4,3*K/4,-K/4), 'alias-law signature mismatch')
        if 0<g<1 and 0<r<1:
            check((moment1>0)==(g<F(1,4)) if g!=F(1,4) else moment1==0,'strict crossover mismatch')
            check(t[4]>s[4], 'full-outbreak ordering mismatch')

print('PASS:',ASSERTIONS,'exact checks; local/global model, coefficient table, full distribution and moments.')
