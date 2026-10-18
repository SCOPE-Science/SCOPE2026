#!/usr/bin/env python3
"""Finite topological certificates for the two-independence complex of the Chvatal graph.

Uses only Python standard library, independently enumerates every subset and every
face-poset incidence. Runs no external solvers or network requests.
"""
from collections import Counter, deque

N = 12
EDGES = ((0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),
         (2,3),(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),
         (5,10),(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),
         (9,10),(9,11))
NEIGH = [0] * N
for x,y in EDGES:
    NEIGH[x] |= 1 << y
    NEIGH[y] |= 1 << x

def is_face(s):
    return all((s & NEIGH[i]).bit_count() <= 1 for i in range(N) if s & (1 << i))

FULL = frozenset(s for s in range(1,1 << N) if is_face(s))
ORDERS = {
    'K': (9,11,3,4,7,6,8,2,5,10,1,0),
    'D0': (2,11,4,10,9,5,8,1,7,3,6),
    'L0': (3,6,8,10,1,9,11,7,2,5,4),
    'D2': (1,6,7,0,11,5,8,3,9,10,4),
    'L2': (9,10,1,3,6,4,8,5,0,11,7),
}

def subcomplex(kind, v=None):
    if kind == 'K': return FULL
    if kind == 'D': return frozenset(s for s in FULL if not (s >> v & 1))
    if kind == 'L':
        return frozenset(s & ~(1 << v) for s in FULL if s >> v & 1 and s != 1 << v)
    raise ValueError(kind)

def check_matching(faces, order):
    # Enumerate complete matching (lower, upper) with a fixed pivot order.
    unmatched = set(faces)
    matching = []
    for p in order:
        b = 1 << p
        for a in sorted(unmatched):
            if a & b: continue
            z = a | b
            if a in unmatched and z in unmatched:
                matching.append((a,z))
                unmatched.remove(a)
                unmatched.remove(z)
    assert len(matching) * 2 + len(unmatched) == len(faces)
    assert len(set(a for a,b in matching) | set(b for a,b in matching)) == 2*len(matching)
    # Acyclicity is verified on the complete Hasse diagram, not sampled gradient paths.
    matching_pairs = set(matching)
    verts = sorted(faces)
    index = {f:i for i,f in enumerate(verts)}
    forward = [[] for _ in verts]
    indegree = [0]*len(verts)
    incidences = 0
    for upper in verts:
        for i in range(N):
            if upper & (1 << i):
                lower = upper & ~(1 << i)
                if lower in faces:
                    source, target = ((upper,lower) if (lower,upper) in matching_pairs
                                      else (lower,upper))
                    a,b = index[source],index[target]
                    forward[a].append(b)
                    indegree[b] += 1
                    incidences += 1
    queue = deque(i for i,d in enumerate(indegree) if d == 0)
    visited = 0
    while queue:
        i = queue.popleft()
        visited += 1
        for j in forward[i]:
            indegree[j] -= 1
            if indegree[j] == 0: queue.append(j)
    assert visited == len(verts), (visited,len(verts))
    return len(matching),dict(sorted(Counter(s.bit_count()-1 for s in unmatched).items())),incidences,visited

def elementary_collapses(faces):
    # This is an additional simplicial-collapse check, independent of the Morse pairing.
    remaining=set(faces)
    count=0
    while len(remaining)>1:
        cofaces = {s:0 for s in remaining}
        unique={}
        for b in remaining:
            for i in range(N):
                if b >> i & 1:
                    a=b^(1<<i)
                    if a in remaining:
                        cofaces[a] += 1
                        unique[a]=b
        candidates=[a for a in remaining if cofaces[a]==1]
        if not candidates:
            return (False,count,len(remaining))
        a=min(candidates,key=lambda s:(s.bit_count(),s))
        b=unique[a]
        assert b in remaining and a in remaining and b.bit_count()==a.bit_count()+1
        remaining.remove(a);remaining.remove(b)
        count+=1
    assert next(iter(remaining)).bit_count()==1
    return True,count,len(remaining)

def automorphisms():
    # Exact degree- and adjacency-preserving backtracking tests all possible images.
    edge=set(tuple(sorted(e)) for e in EDGES)
    found=[]
    def backtrack(images, used):
        k=len(images)
        if k==N:
            found.append(tuple(images));return
        for q in range(N):
            if q in used: continue
            if all(((min(i,k),max(i,k)) in edge) ==
                   ((min(images[i],q),max(images[i],q)) in edge)
                   for i in range(k)):
                backtrack(images+[q],used|{q})
    backtrack([],set())
    return found

def main():
    assert len(EDGES)==24 and len(FULL)==424
    assert all(NEIGH[i].bit_count()==4 for i in range(N))
    assert all(not ((NEIGH[i] & NEIGH[j]) & (1 << k))
               for i,j in EDGES for k in range(N) if k!=i and k!=j)
    F={'K':subcomplex('K'),'D0':subcomplex('D',0),'D2':subcomplex('D',2),
       'L0':subcomplex('L',0),'L2':subcomplex('L',2)}
    expectation={'K':(424,211,{0:1,3:1}),
                 'D0':(302,150,{0:1,3:1}),
                 'L0':(121,60,{0:1}),
                 'D2':(305,152,{0:1}),
                 'L2':(118,58,{0:1,2:1})}
    for name,faces in F.items():
        matched,critical,covers,visited=check_matching(faces,ORDERS[name])
        cnt,expected_pairs,expected_critical=expectation[name]
        assert (len(faces),matched,critical)==(cnt,expected_pairs,expected_critical), name
        print(name,'faces',len(faces),'f_vector',dict(sorted(Counter(x.bit_count()-1 for x in faces).items())),
              'pairs',matched,'critical',critical,'covers',covers,'toposort_visited',visited)
    for name in ('L0','D2'):
        collapsed,steps,rem=elementary_collapses(F[name]); assert collapsed and rem==1
        print(name+'_COLLAPSE',steps,'pairs_to_single_vertex')
    autos=automorphisms()
    assert len(autos)==8
    orbit0={g[0] for g in autos}
    orbit2={g[2] for g in autos}
    assert orbit0=={0,1,4,5} and orbit2==set(range(N))-orbit0
    assert all({sum(1 for s in FULL if not s>>v&1) for v in orb}==({302} if orb==orbit0 else {305})
               for orb in (orbit0,orbit2))
    print('AUTOMORPHISM_COUNT',len(autos),'ORBITS',sorted(orbit0),sorted(orbit2))
    print('MORSE_CERTIFICATE_OK')
if __name__=='__main__':main()
