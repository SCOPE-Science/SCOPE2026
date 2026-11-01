#!/usr/bin/env python3
"""Exact, self-contained homotopy check for the closed-neighborhood complex of KG(8,3).

Requires Python 3.10 or newer; uses only the standard library.
The finite computation is exhaustive, and the accepted mathematical statement
uses elementary collapses, acyclic discrete Morse theory, and cellular 2-complex
cancellations; it does not infer a universal claim from sampling.
"""
from itertools import combinations
from collections import Counter, deque
import heapq
import random


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit
        mask -= bit


def reduce_word(seq):
    stack = []
    for x in seq:
        if stack and stack[-1] == -x:
            stack.pop()
        else:
            stack.append(x)
    return tuple(stack)


def invert(seq):
    return tuple(-x for x in reversed(seq))


def compute():
    triples = list(combinations(range(8), 3))
    assert len(triples) == 56
    nbh = []
    for i, a in enumerate(triples):
        subset = set(a)
        nbrs = [j for j, b in enumerate(triples) if i == j or subset.isdisjoint(b)]
        assert len(nbrs) == 11
        nbh.append(sum(1 << j for j in nbrs))
    assert len(set(nbh)) == 56

    faces = set()
    for facet in nbh:
        sub = facet
        while sub:
            faces.add(sub)
            sub = (sub - 1) & facet
    f_vector = tuple(sum(m.bit_count() == j for m in faces) for j in range(1, 12))
    assert f_vector == (56, 1540, 8400, 18270, 25872, 25872, 18480, 9240, 3080, 616, 56)
    assert len(faces) == 111482
    print('COMPLETE_FACE_SET_OK',len(faces),f_vector,flush=True)

    count = dict.fromkeys(faces, 0)
    coface_xor = dict.fromkeys(faces, 0)
    for higher in faces:
        for bit in bits(higher):
            lower = higher ^ bit
            if lower:
                assert lower in faces
                count[lower] += 1
                coface_xor[lower] ^= higher
    queue = [(f.bit_count(), f) for f in faces if count[f] == 1]
    heapq.heapify(queue)
    ncollapse = 0
    while queue:
        _, lower = heapq.heappop(queue)
        if lower not in faces or count[lower] != 1:
            continue
        higher = coface_xor[lower]
        assert higher in faces and higher.bit_count() == lower.bit_count()+1
        for removed in (lower, higher):
            for bit in bits(removed):
                sub = removed ^ bit
                if sub in faces and sub not in (lower, higher):
                    count[sub] -= 1
                    coface_xor[sub] ^= removed
                    assert count[sub] >= 0
                    if count[sub] == 1:
                        heapq.heappush(queue, (sub.bit_count(), sub))
            faces.remove(removed)
        ncollapse += 1
    fsmall = Counter(f.bit_count() - 1 for f in faces)
    assert ncollapse == 54910 and len(faces) == 1662
    assert fsmall == {0:56,1:628,2:978}
    print('ELEMENTARY_COLLAPSE_OK',ncollapse,'residual',dict(sorted(fsmall.items())),flush=True)

    V = sorted(f for f in faces if f.bit_count()==1)
    E = sorted(f for f in faces if f.bit_count()==2)
    T = sorted(f for f in faces if f.bit_count()==3)
    Eindex = {e:i for i,e in enumerate(E)}
    # Independent raw chain-complex ranks, before Morse reductions.
    # The boundary over F_p is formed with the usual increasing vertex
    # orientation. These checks are not used to derive the CW result.
    for prime, target_rank in ((2,572),(3,573),(5,573)):
        basis={}
        for triangle in T:
            a,b,c=[i for i in range(56) if triangle>>i&1]
            column={Eindex[(1<<a)|(1<<b)]:1,
                    Eindex[(1<<b)|(1<<c)]:1,
                    Eindex[(1<<a)|(1<<c)]:(prime-1)}
            while column:
                k=min(column)
                if k not in basis:
                    inv=pow(column[k],-1,prime)
                    basis[k]={j:(x*inv)%prime for j,x in column.items() if x%prime}
                    break
                multiplier=column[k]
                for j,val in basis[k].items():
                    new=(column.get(j,0)-multiplier*val)%prime
                    if new:column[j]=new
                    else:column.pop(j,None)
        assert len(basis)==target_rank
        print('RAW_CHAIN_RANK_OK',prime,'rank_boundary_2',len(basis),
              'reduced_betti_1',628-55-len(basis),
              'reduced_betti_2',978-len(basis),flush=True)
    Tedges = []
    for tri in T:
        v = [i for i in range(56) if tri>>i&1]
        a,b,c = v
        Tedges.append((Eindex[(1<<a)|(1<<b)],
                       Eindex[(1<<b)|(1<<c)],
                       Eindex[(1<<a)|(1<<c)]))
    TE = [tuple(Eindex[t^bit] for bit in bits(t)) for t in T]
    ET = [[] for _ in E]
    for j, edges in enumerate(TE):
        for e in edges:
            ET[e].append(j)
    alive = [True]*len(T)
    degrees = [len(ts) for ts in ET]
    rng = random.Random(0)
    critical_triangles = []
    pairs = []
    remaining = len(T)
    while remaining:
        free_edges = [i for i,d in enumerate(degrees) if d==1]
        if free_edges:
            e = rng.choice(free_edges)
            j = next(j for j in ET[e] if alive[j])
            pairs.append((e,j))
        else:
            scores = [sum(degrees[e] == 2 for e in edges) for edges in TE]
            maximum = max(scores[j] for j in range(len(T)) if alive[j])
            eligible = [j for j in range(len(T)) if alive[j] and scores[j]==maximum]
            j = rng.choice(eligible)
            critical_triangles.append(j)
        assert alive[j]
        alive[j] = False
        remaining -= 1
        for e in TE[j]:
            degrees[e] -= 1
            assert degrees[e] >= 0
    match_e_t = dict(pairs)
    assert len(match_e_t) == 569 and len(set(match_e_t.values())) == 569
    assert len(critical_triangles) == 409

    parent = list(range(56))
    def find(i):
        while parent[i]!=i:
            i=parent[i]
        return i
    tree = set()
    for e in sorted(set(range(len(E)))-set(match_e_t)):
        a,b = [i for i in range(56) if E[e]>>i&1]
        ra,rb = find(a),find(b)
        if ra != rb:
            parent[ra]=rb
            tree.add(e)
    assert len(tree)==55 and len({find(i) for i in range(56)})==1
    free_e = sorted(set(range(len(E)))-set(match_e_t)-tree)
    assert len(free_e)==4
    # Match nonroot vertices with their tree-parent edge.  Each tree edge
    # is used once.  Tree incidences cannot give a directed cycle.
    tree_adj=[[] for _ in range(56)]
    for e in tree:
        a,b=[i for i in range(56) if E[e]>>i&1]
        tree_adj[a].append((b,e));tree_adj[b].append((a,e))
    visited={0};todo=deque([0]);match_v_e={}
    while todo:
        a=todo.popleft()
        for b,e in tree_adj[a]:
            if b not in visited:
                visited.add(b);todo.append(b)
                match_v_e[1<<b]=E[e]
    assert len(match_v_e)==55
    # Full directed Hasse graph, every incidence: matched upwards,
    # all other incidences downwards. Acyclicity is checked globally.
    adj={f:[] for f in faces};indeg={f:0 for f in faces}
    nt=0
    for higher in sorted(faces):
        for bit in bits(higher):
            lower=higher^bit
            if not lower:
                continue
            assert lower in faces
            matching = (higher.bit_count()==3 and match_e_t.get(Eindex[lower],-1)==T.index(higher)) if higher.bit_count()==3 else (match_v_e.get(lower)==higher)
            a,b=(lower,higher) if matching else (higher,lower)
            adj[a].append(b);indeg[b]+=1;nt+=1
    assert nt==4190
    q=deque(f for f in faces if indeg[f]==0)
    topocount=0
    while q:
        f=q.popleft();topocount+=1
        for g in adj[f]:
            indeg[g]-=1
            if indeg[g]==0:q.append(g)
    assert topocount==len(faces)
    print('ACYCLIC_MORSE_OK','pair12',len(match_e_t),'pair01',len(match_v_e),
          'critical',(1,4,409),'incidences',nt,flush=True)

    # Remove each paired 1/2-cell by the triangle relation, retaining
    # attaching words of all critical triangles. The dependency DAG
    # below is an independent check of the substitution order.
    expansions={};active=set()
    def expand(e):
        if e not in match_e_t:
            return (e+1,)
        if e in expansions:
            return expansions[e]
        assert e not in active
        active.add(e)
        ab,bc,ac=Tedges[match_e_t[e]]
        if e==ab:
            desc=((ac,1),(bc,-1))
        elif e==bc:
            desc=((ab,-1),(ac,1))
        else:
            assert e==ac
            desc=((ab,1),(bc,1))
        w=[]
        for f,sign in desc:
            frag=expand(f)
            w.extend(frag if sign==1 else invert(frag))
        expansions[e]=reduce_word(w)
        active.remove(e)
        return expansions[e]
    for e in match_e_t:
        expand(e)
    assert len(expansions)==569
    rel=[]
    for j in sorted(critical_triangles):
        ab,bc,ac=Tedges[j]
        rel.append(reduce_word(expand(ab)+expand(bc)+invert(expand(ac))))
    assert len(rel)==409
    # Collapse the spanning tree, leaving four oriented circle generators.
    generators={e+1:i+1 for i,e in enumerate(free_e)}
    words=[]
    for w in rel:
        words.append(reduce_word(generators[abs(x)] * (1 if x>0 else -1)
            for x in w if abs(x) in generators))
    assert len(words)==409
    # In order: erase generator 2 using a relator (2), erase generator 4
    # using (4), and erase generator 1 using (-1).  Those three elementary
    # Tietze/CW cancellations do not change the homotopy type.
    for generator, relator in ((2,(2,)), (4,(4,)), (1,(-1,))):
        assert relator in words, (generator,relator)
        words.remove(relator)
        words=[reduce_word(x for x in w if abs(x)!=generator) for w in words]
    assert len(words)==406
    assert all(set(map(abs,w)) <= {3} for w in words)
    signed_degree = [sum(1 if x==3 else -1 for x in w) for w in words]
    assert all(deg%2==0 for deg in signed_degree)
    assert any(abs(deg)==2 for deg in signed_degree)
    degree_counts=dict(sorted(Counter(signed_degree).items()))
    print('CELLULAR_CANCELLATIONS_OK','remaining_1cells',1,'remaining_2cells',len(words),
          'degree_histogram',degree_counts,flush=True)
    # Since one attachment has degree 2 and all other degrees are even,
    # homotope those other maps to constants in the RP^2 2-skeleton.
    # The result is RP^2 vee 405 S^2, without higher cells.
    print('HOMOTOPY_OK RP2_wedge_405_S2',flush=True)
    print('ALL_VERIFY_OK',flush=True)

if __name__=='__main__':
    compute()
