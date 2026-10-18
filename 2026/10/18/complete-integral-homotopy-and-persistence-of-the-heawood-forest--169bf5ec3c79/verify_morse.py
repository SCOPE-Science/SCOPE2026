#!/usr/bin/env python3
"""Exhaustive integral discrete-Morse verification of a graph forest filtration.

The graph has points p_i= i and lines ell_j=7+j (0<=i,j<7),
with adjacency iff (i-j) modulo 7 is one of 0,1,3.
This script uses only Python's standard library.
"""
from collections import Counter, deque

N = 14
EDGES = [(i, 7+j) for i in range(7) for j in range(7)
         if (i-j) % 7 in (0,1,3)]
NEIGHBORS = [0]*N
for a,b in EDGES:
    NEIGHBORS[a] |= 1<<b
    NEIGHBORS[b] |= 1<<a
EXPECTED = {0:(457,{0:1,3:6}), 1:(2256,{0:1,5:13}),
            2:(8654,{0:1,6:1}), 3:(12791,{0:1,8:8})}

def forest_and_degree(mask):
    """Union/find rejects exactly the subsets with an undirected cycle."""
    parents = list(range(N))
    def find(a):
        while parents[a] != a:
            a=parents[a]
        return a
    degree = 0
    for v in range(N):
        if mask>>v & 1:
            degree=max(degree,(mask&NEIGHBORS[v]).bit_count())
    for a,b in EDGES:
        if mask>>a & 1 and mask>>b & 1:
            x,y=find(a),find(b)
            if x==y:
                return None
            parents[x]=y
    return degree

def generate():
    faces=[set() for _ in range(4)]
    for mask in range(1,1<<N):
        d=forest_and_degree(mask)
        if d is None:
            continue
        for i in range(d,4):
            faces[i].add(mask)
    for i in range(4):
        assert all((x&(x-1)) in faces[i] for x in faces[i] if (x&(x-1))!=0)
    return faces

def certify(faces):
    """Sequential-coordinate matching; explicitly test the whole oriented Hasse DAG."""
    partner = [-1]*(1<<N)
    pair_count=0
    for i in range(N):
        bit=1<<i
        for low in range(1,1<<N):
            if low not in faces or low & bit or partner[low]!=-1:
                continue
            high=low|bit
            if high in faces and partner[high]==-1:
                partner[low]=high
                partner[high]=low
                pair_count+=1
    critical=Counter((x.bit_count()-1) for x in faces if partner[x]==-1)
    adjacency=[[] for _ in range(1<<N)]
    indegree=[0]*(1<<N)
    covering=0
    for upper in faces:
        sub=upper
        while sub:
            bit=sub&-sub
            sub-=bit
            lower=upper^bit
            if not lower:continue
            assert lower in faces
            if partner[lower]==upper:
                a,b=lower,upper
            else:
                a,b=upper,lower
            adjacency[a].append(b)
            indegree[b]+=1
            covering+=1
    ready=deque(x for x in faces if indegree[x]==0)
    visited=0
    while ready:
        a=ready.popleft()
        visited+=1
        for b in adjacency[a]:
            indegree[b]-=1
            if indegree[b]==0:
                ready.append(b)
    assert visited==len(faces),f'Hasse orientation contains cycle: {visited}/{len(faces)}'
    assert len(faces)==2*pair_count+sum(critical.values())
    return pair_count,critical,covering,visited

def main():
    assert len(EDGES)==21
    assert all(NEIGHBORS[i].bit_count()==3 for i in range(N))
    stages=generate()
    for d,faces in enumerate(stages):
        pair_count,critical,covering,visited=certify(faces)
        assert len(faces)==EXPECTED[d][0]
        assert dict(critical)==EXPECTED[d][1]
        fv=dict(sorted(Counter(x.bit_count()-1 for x in faces).items()))
        print(f'F_{d}: faces={len(faces)}, f_vector={fv}, pairs={pair_count}, '
              f'critical={dict(sorted(critical.items()))}, '
              f'Hasse_covers={covering}, topo_visited={visited}')
    print('PASS: all four exhaustive acyclic matchings; integral wedge conclusions follow.')

if __name__=='__main__':
    main()
