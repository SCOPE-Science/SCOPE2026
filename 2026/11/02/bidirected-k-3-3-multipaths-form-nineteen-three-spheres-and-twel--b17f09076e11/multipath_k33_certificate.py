#!/usr/bin/env python3
"""Exact integral cellular reduction for the bidirected K_{3,3} multipath complex.

No external dependencies. Reconstructs all faces, a complete acyclic matching,
and the signed integral reduced boundary after elementary cancellations.
"""
from collections import Counter, deque

ORDER = (15, 0, 5, 1, 8, 4, 3, 13, 11, 12, 14, 16, 6, 7, 2, 17, 10, 9)
N_LEFT = N_RIGHT = 3
EDGES = tuple((a,b) for a in range(6) for b in range(6)
              if (a < N_LEFT) != (b < N_LEFT))


def enumerate_faces():
    by_size = [[] for _ in range(6)]
    def visit(next_edge, face, ins, outs, components, count):
        by_size[count].append(face)
        for j in range(next_edge, len(EDGES)):
            a,b = EDGES[j]
            if (outs >> a)&1 or (ins >> b)&1 or components[a]==components[b]:
                continue
            old,new = components[b],components[a]
            new_components = tuple(new if c==old else c for c in components)
            visit(j+1, face|(1<<j), ins|(1<<b), outs|(1<<a),
                  new_components, count+1)
    visit(0, 0, 0, 0, tuple(range(6)), 0)
    assert tuple(map(len,by_size)) == (1,18,108,264,252,72)
    assert len(set().union(*map(set,by_size))) == 715
    return by_size


def independently_verify_faces(by_size):
    # Exhaust the finite 18-edge power set independently of incremental union-find.
    expected=set().union(*map(set,by_size))
    brute=set()
    for mask in range(1 << 18):
        if mask.bit_count()>5:continue
        incoming=[0]*6; outgoing=[0]*6; adjacency=[[] for _ in range(6)]
        valid=True
        for j,(a,b) in enumerate(EDGES):
            if mask>>j&1:
                outgoing[a]+=1;incoming[b]+=1
                if outgoing[a]>1 or incoming[b]>1:valid=False;break
                adjacency[a].append(b)
        if not valid:continue
        # Kahn topological sorting, independent of undirected component labels.
        indegrees=incoming[:]; queue=deque(v for v in range(6) if indegrees[v]==0)
        visited=0
        while queue:
            v=queue.popleft();visited+=1
            for w in adjacency[v]:
                indegrees[w]-=1
                if indegrees[w]==0:queue.append(w)
        if visited==6:brute.add(mask)
    assert brute==expected, (len(brute),len(expected),len(brute^expected))
    return len(brute)


def build_matching(by_size):
    all_faces = set().union(*map(set,by_size))
    unmatched = set(all_faces)
    pairs = []
    for j in ORDER:
        for f in all_faces:
            g=f|(1<<j)
            if not (f>>j)&1 and f in unmatched and g in unmatched:
                pairs.append((f,g)); unmatched.remove(f); unmatched.remove(g)
    assert len(pairs)==342 and len(unmatched)==31
    assert Counter(x.bit_count()-1 for x in unmatched)==Counter({3:19,4:12})
    # Leave the empty face and its matched singleton unpaired to obtain
    # an ordinary (non-augmented) Morse matching with one critical vertex.
    augmentation_pairs=[p for p in pairs if p[0]==0]
    assert len(augmentation_pairs)==1
    pairs=[p for p in pairs if p[0]!=0]
    unmatched.update(augmentation_pairs[0]); assert len(pairs)==341
    assert Counter(x.bit_count()-1 for x in unmatched)==Counter({-1:1,0:1,3:19,4:12})
    return pairs,unmatched,all_faces


def verify_acyclic(pairs, all_faces):
    matched={(b,a) for a,b in pairs}
    incoming={f:0 for f in all_faces}
    adj={f:[] for f in all_faces}
    incidence_count=0
    for big in all_faces:
        for j in range(18):
            if big >> j & 1:
                small=big^(1<<j)
                u,v=(small,big) if (big,small) in matched else (big,small)
                adj[u].append(v);incoming[v]+=1;incidence_count+=1
    q=deque(f for f,d in incoming.items() if d==0)
    seen=0
    while q:
        u=q.popleft();seen+=1
        for v in adj[u]:
            incoming[v]-=1
            if incoming[v]==0:q.append(v)
    assert seen==len(all_faces)==715
    assert incidence_count==2394, incidence_count
    return incidence_count


def integer_cancel(pairs, all_faces):
    active=set(all_faces)
    columns={}
    reverse={f:set() for f in all_faces}
    for f in all_faces:
        col={}
        for j in range(18):
            if f >> j & 1:
                lower=f^(1<<j)
                col[lower]=(-1)**((f&((1<<j)-1)).bit_count())
                reverse[lower].add(f)
        columns[f]=col
    pending=list(pairs)
    while pending:
        options=[(len(reverse[a])*len(columns[b]),i,a,b)
                 for i,(a,b) in enumerate(pending)
                 if abs(columns[b].get(a,0))==1]
        assert options, 'No integral unit cancellation available'
        _,i,small,big=min(options)
        pending.pop(i)
        pivot=columns[big][small]
        for other in list(reverse[small]):
            if other==big:continue
            multiplier=columns[other][small]//pivot
            for row,value in columns[big].items():
                updated=columns[other].get(row,0)-multiplier*value
                if updated:
                    columns[other][row]=updated
                    reverse[row].add(other)
                else:
                    columns[other].pop(row,None)
                    reverse[row].discard(other)
        for row in columns[big]:reverse[row].discard(big)
        for row in columns[small]:reverse[row].discard(small)
        for other in list(reverse[small]):columns[other].pop(small,None)
        for other in list(reverse[big]):columns[other].pop(big,None)
        columns.pop(big);columns.pop(small)
        reverse.pop(big);reverse.pop(small)
        active.remove(big);active.remove(small)
    assert len(active)==33
    remaining=Counter(f.bit_count()-1 for f in active)
    assert remaining==Counter({-1:1,0:1,3:19,4:12}), remaining
    for f,boundary in columns.items():
        if f.bit_count()>=4:
            assert not boundary, 'Nonzero degree-four or degree-three Morse differential'
        if f.bit_count()==1:
            assert boundary=={0:1}, boundary
    assert sum(len(c) for c in columns.values())==1
    return remaining


def verify_mod2(by_size):
    # Independent elimination on the original simplicial boundary, not on the matching.
    ranks=[]
    for k in range(1,6):
        lower={f:j for j,f in enumerate(by_size[k-1])}
        pivot={}
        for f in by_size[k]:
            v=0
            for j in range(18):
                if f>>j&1:v ^= (1<<lower[f^(1<<j)])
            while v:
                t=v.bit_length()-1
                if t in pivot:v ^=pivot[t]
                else:pivot[t]=v;break
        ranks.append(len(pivot))
    assert ranks==[1,17,91,173,60],ranks
    b=[len(by_size[i])-ranks[i-1]-(ranks[i] if i<len(ranks) else 0)
       for i in range(1,len(by_size))]
    assert b==[0,0,0,19,12],b
    return ranks,b

if __name__=='__main__':
    by_size=enumerate_faces()
    independently_verify_faces(by_size)
    pairs,critical,all_faces=build_matching(by_size)
    m=verify_acyclic(pairs,all_faces)
    reduced=integer_cancel(pairs,all_faces)
    ranks,betti=verify_mod2(by_size)
    print('BIDIRECTED_K33_MULTIPATH_INTEGRAL_19S3_12S4_VERIFIED')
    print('f_vector:',tuple(len(v) for v in by_size[1:]))
    print('nonempty_faces:',len(all_faces)-1)
    print('matching_pairs:',len(pairs),'critical:',dict(reduced),'hasse_incidences:',m)
    print('signed_Morse_boundary_above_degree_0: ZERO')
    print('mod2_boundary_ranks:',ranks,'reduced_betti:',betti)
