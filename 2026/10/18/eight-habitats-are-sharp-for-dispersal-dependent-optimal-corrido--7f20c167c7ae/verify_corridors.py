#!/usr/bin/env python3
"""Exact small-tree edge-improvement classification. Python 3 standard library only."""
from itertools import product
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush

EXPECTED_COUNTS = {2:1, 3:1, 4:2, 5:3, 6:6, 7:11, 8:23}

def graph_from_prufer(n, seq):
    degrees = [1] * n
    for v in seq:
        degrees[v] += 1
    leaves = [i for i in range(n) if degrees[i] == 1]
    heapify(leaves)
    adj = [[] for _ in range(n)]
    for v in seq:
        u = heappop(leaves)
        adj[u].append(v); adj[v].append(u)
        degrees[u] -= 1; degrees[v] -= 1
        if degrees[v] == 1:
            heappush(leaves,v)
    u,v = sorted(leaves)
    adj[u].append(v); adj[v].append(u)
    return adj

def canonical_tree(adj):
    n = len(adj)
    deg = [len(a) for a in adj]
    leaves = deque(i for i in range(n) if deg[i] <= 1)
    remaining = n
    while remaining > 2:
        number = len(leaves); remaining -= number
        for _ in range(number):
            u = leaves.popleft(); deg[u] = 0
            for v in adj[u]:
                if deg[v] > 0:
                    deg[v] -= 1
                    if deg[v] == 1: leaves.append(v)
    center = list(leaves)
    def rooted(u,parent):
        return '('+''.join(sorted(rooted(v,u) for v in adj[u] if v!=parent))+')'
    if len(center)==1: return rooted(center[0], -1)
    assert len(center)==2
    a,b=center
    return '['+''.join(sorted((rooted(a,b),rooted(b,a))))+']'

def coeff_by_edge(adj):
    n = len(adj)
    answer = {}
    for u in range(n):
        for v in adj[u]:
            if u>v: continue
            def distances(root):
                d={root:0}; queue=deque([root])
                while queue:
                    a=queue.popleft()
                    for b in adj[a]:
                        if (a,b)==(u,v) or (a,b)==(v,u):continue
                        if b not in d:
                            d[b]=d[a]+1;queue.append(b)
                return d
            A,B=distances(u),distances(v)
            assert len(A)+len(B)==n
            coeff=[0]*(n-1)
            for a in A.values():
                for b in B.values():
                    coeff[a+b]+=1
            answer[(u,v)]=tuple(coeff)
    return answer

def coeff_frontier(data):
    vectors=set(data.values())
    return sorted(v for v in vectors if not any(
        w!=v and all(x>=y for x,y in zip(w,v)) for w in vectors))

def difference(u,v):
    return tuple(x-y for x,y in zip(u,v))

def coefficients_equal_upto_sign(u,v,pattern):
    d=difference(u,v)
    pad=tuple(pattern)+(0,)*(len(d)-len(pattern))
    return d==pad or d==tuple(-v for v in pad)

# + signs below are arbitrary; each pattern's vanishing set is what matters.
EXPECTED_PATTERNS={
    7: {(0,1,-1):1},                 # p(1-p): strictly positive in (0,1)
    8: {(0,2,-1):1,                # p(2-p): strictly positive
        (0,1,0,-1):1,              # p(1-p^2): strictly positive
        (0,-1,2):1,                # p(2p-1): positive crossover at 1/2
        (0,-1,1,1):1},             # p(p^2+p-1): golden-ratio crossover
}

counts={}
pattern_totals={n:Counter() for n in EXPECTED_COUNTS}
example_by_pattern={}

for n in range(2,9):
    representatives={}
    for seq in product(range(n),repeat=n-2):
        adj=graph_from_prufer(n,seq)
        form=canonical_tree(adj)
        if form not in representatives:
            representatives[form]=adj
    counts[n]=len(representatives)
    assert counts[n]==EXPECTED_COUNTS[n],(n,counts[n])
    for tree in representatives.values():
        polys=coeff_by_edge(tree)
        front=coeff_frontier(polys)
        if len(front)==1: continue
        assert len(front)==2,('unexpected frontier',n,front)
        patterns=[pat for pat in EXPECTED_PATTERNS.get(n,{})
                  if coefficients_equal_upto_sign(front[0],front[1],pat)]
        assert len(patterns)==1,(n,front)
        pat=patterns[0]
        pattern_totals[n][pat]+=1
        example_by_pattern[(n,pat)]=(tree,polys,front)
    assert dict(pattern_totals[n])==EXPECTED_PATTERNS.get(n,{}), (n,pattern_totals[n])
assert counts == EXPECTED_COUNTS

# Exactly two switching eight-node shapes; verify their representative edge-polynomials.
TARGETS=[
    ([(0,1),(0,5),(1,2),(2,3),(2,4),(5,6),(6,7)],
     { (0,1):(1,2,4,4,3,2,0),(1,2):(1,3,3,3,3,2,0)}),
    ([(0,1),(0,5),(1,2),(2,3),(2,4),(5,6),(5,7)],
     { (0,1):(1,2,5,4,4,0,0),(1,2):(1,3,3,4,4,0,0),(0,5):(1,3,3,4,4,0,0)})
]
for edges,exp in TARGETS:
    adj=[[] for _ in range(8)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    polys=coeff_by_edge(adj)
    for e,val in exp.items():assert polys[e]==val,(e,polys[e],val)
    canon=canonical_tree(adj)
    assert any(canon==canonical_tree(e[0]) for (n,pat),e in example_by_pattern.items() if n==8 and pat in [(0,-1,2),(0,-1,1,1)])

# Direct, independent reliability enumeration at two nontrivial rational values.
from fractions import Fraction
from itertools import combinations

def expected_component_size(edges, upgraded_edge=None, q=Fraction(1,4)):
    total=Fraction(0)
    uncertain=[e for e in edges if e != upgraded_edge]
    for bits in product([0,1],repeat=len(uncertain)):
        opened=[e for e,b in zip(uncertain,bits) if b]
        if upgraded_edge is not None: opened.append(upgraded_edge)
        prob=q**sum(bits)*(1-q)**(len(bits)-sum(bits))
        parent=list(range(8))
        def find(v):
            while parent[v]!=v:v=parent[v]
            return v
        for a,b in opened:parent[find(a)]=find(b)
        counts=Counter(find(v) for v in range(8))
        total+=prob*Fraction(sum(k*k for k in counts.values()),8)
    return total

def evaluate_poly(c, q):
    return sum(Fraction(v)*q**i for i,v in enumerate(c))

independent_checks=0
for edges, exp in TARGETS:
    for q in [Fraction(1,4),Fraction(3,4)]:
        original=expected_component_size(edges,q=q)
        for e,c in exp.items():
            improved=expected_component_size(edges,upgraded_edge=e,q=q)
            assert improved-original == Fraction(2,8)*(1-q)*evaluate_poly(c,q)
            independent_checks+=1

print('VERIFY_OK Prüfer_isomorphism_classes',counts)
print('VERIFY_OK nontrivial_coefficient_frontier',dict((n,dict(c)) for n,c in pattern_totals.items() if c))
print('VERIFY_OK switching_shapes=2 thresholds=1/2,(sqrt(5)-1)/2 exact_witness_coefficients=5')
print('VERIFY_OK independent_reliability_enumerations=',independent_checks)
