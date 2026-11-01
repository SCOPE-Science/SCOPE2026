#!/usr/bin/env python3
"""Finite transfer-graph certificate for the majority CA entry theorem.

Python 3, standard library only.  Every possible input window and local
transition is constructed; Kosaraju SCCs identify all cyclic predecessor
walks.  Independent direct updates verify the displayed witnesses.
"""
from collections import defaultdict
from itertools import product


def majority_string(word, radius):
    n = len(word)
    assert n >= 2 * radius + 1
    return ''.join(str(int(sum(int(word[(i + delta) % n])
                               for delta in range(-radius, radius + 1))
                           >= radius + 1)) for i in range(n))


def predecessor_graph(pattern, radius):
    d = len(pattern)
    vcount = d * (1 << (2 * radius))
    graph = [[] for _ in range(vcount)]
    for phase in range(d):
        for state in range(1 << (2 * radius)):
            start = phase * (1 << (2 * radius)) + state
            for new_bit in (0, 1):
                if int(state.bit_count() + new_bit >= radius + 1) != int(pattern[(phase + radius) % d]):
                    continue
                next_state = (state >> 1) | (new_bit << (2 * radius - 1))
                target = ((phase + 1) % d) * (1 << (2 * radius)) + next_state
                graph[start].append(target)
    return graph


def scc(graph):
    n = len(graph)
    reverse = [[] for _ in range(n)]
    for a, row in enumerate(graph):
        for b in row: reverse[b].append(a)
    seen = [False] * n
    order = []
    for v in range(n):
        if seen[v]: continue
        seen[v] = True
        stack = [(v, 0)]
        while stack:
            a, k = stack[-1]
            if k == len(graph[a]):
                order.append(a)
                stack.pop()
                continue
            b = graph[a][k]
            stack[-1] = (a, k+1)
            if not seen[b]:
                seen[b] = True
                stack.append((b, 0))
    owner = [-1] * n
    groups = []
    for v in reversed(order):
        if owner[v] != -1: continue
        idx = len(groups)
        owner[v] = idx
        stack = [v]
        comp = []
        while stack:
            a = stack.pop()
            comp.append(a)
            for b in reverse[a]:
                if owner[b] == -1:
                    owner[b] = idx
                    stack.append(b)
        groups.append(comp)
    cyclic = []
    for comp in groups:
        vertices = set(comp)
        ecount = sum(b in vertices for a in comp for b in graph[a])
        if len(comp) > 1 or ecount > 0:
            cyclic.append((vertices, ecount))
    return cyclic


def monodromy_core(graph, length, radius, core):
    q = 1 << (2 * radius)
    answer = []
    for a in core:
        row = {a: 1}
        for _ in range(length):
            next_row = defaultdict(int)
            for vertex, count in row.items():
                for target in graph[vertex]: next_row[target] += count
            row = next_row
        answer.append([row.get(b, 0) for b in core])
    return answer


def certify_one(pattern, r):
    graph = predecessor_graph(pattern, r)
    recurrent = scc(graph)
    assert len(recurrent) == 1, (pattern, r, [(len(v), e) for v,e in recurrent])
    vertices, edges = recurrent[0]
    assert len(vertices) == len(pattern), (pattern, r, len(vertices))
    assert edges == len(vertices), (pattern, r, edges)
    assert all(sum(v in vertices for v in graph[u]) == 1 for u in vertices)
    phase0 = [v for v in vertices if v // (1 << (2*r)) == 0]
    assert len(phase0) == 1
    assert monodromy_core(graph,len(pattern),r,phase0)==[[1]]
    print('UNIQUE',r,pattern,'recurrent_vertices',len(vertices),'recurrent_edges',edges)


for pattern in ('01',): certify_one(pattern,1)
for pattern in ('0011','001101','001011'): certify_one(pattern,2)

Y='0011001110'
Z='1000111001'
P='1001011001'
assert majority_string(Y,3)==Z
assert majority_string(Z,3)==Y
assert majority_string(P,3)==Y
assert P != Z

graph=predecessor_graph(Y,3)
recurrent=scc(graph)
assert len(recurrent)==1
vertices, edges=recurrent[0]
assert (len(vertices),edges)==(17,18)
phase0=sorted(v for v in vertices if v//64==0)
assert phase0==[41,49],phase0
matrix=monodromy_core(graph,10,3,phase0)
assert matrix==[[1,1],[1,1]],matrix
print('BRANCHING',3,Y,'recurrent_vertices',len(vertices),'recurrent_edges',edges,'phase0',phase0,'return_matrix',matrix)

# Each independent length-10 choice gives an incoming configuration.
for m in range(1,6):
    target=Y*m
    for blocks in product((Z,P),repeat=m):
        assert majority_string(''.join(blocks),3)==target
    assert len(list(product((Z,P),repeat=m)))==2**m
print('MOSAIC_CONSTRUCTION_OK m=1..5')

# A separate, microscopic first-entry enumeration at the initial small sizes.
for r,lo,hi in [(1,3,12),(2,5,12),(3,7,10)]:
    for n in range(lo,hi+1):
        mask=(1<<n)-1
        image={}
        period2=[]
        for x in range(1<<n):
            word=format(x,f'0{n}b')
            out=majority_string(word,r)
            image[word]=out
        for x in image:
            y=image[x]
            if image[y]==x and x!=y:period2.append(x)
        incoming=defaultdict(list)
        for x,y in image.items():incoming[y].append(x)
        extra=sum(len(incoming[t])-1 for t in period2)
        if r<=2 or n<10:assert extra==0,(r,n,extra)
        if r==3 and n==10:assert extra>0
        print('MICRO',r,n,'two_cycle_states',len(period2),'extra_direct_preimages',extra)
print('RADIUS_THRESHOLD_CERTIFICATE_OK')
