#!/usr/bin/env python3
"""Exact, deterministic checks for the 5-by-5 nonattacking-queen complex.

Requires only the Python standard library. Enumerates all legal placements,
builds the row-major face-poset matching, checks its acyclicity and computes
the signed integral Morse boundary in degrees 2 to 1.
"""
from collections import Counter, deque
from functools import lru_cache
from fractions import Fraction

N = 5


def legal(squares):
    positions = [divmod(x, N) for x in squares]
    for i, (r, c) in enumerate(positions):
        for rr, cc in positions[i + 1:]:
            if r == rr or c == cc or abs(r-rr) == abs(c-cc):
                return False
    return True


def generate():
    # One choice per row at most: this enumerates each face exactly once.
    states = [()]
    for r in range(N):
        nxt = []
        for s in states:
            nxt.append(s)
            for c in range(N):
                q = r*N+c
                if legal(s+(q,)):
                    nxt.append(s+(q,))
        states = nxt
    faces = [tuple(sorted(s)) for s in states]
    assert len(faces) == len(set(faces))
    assert all(legal(s) for s in faces)
    return set(faces)


def boundary(face):
    return [(face[:j]+face[j+1:], -1 if j%2 else 1)
            for j in range(len(face))]


def certificate():
    faces = generate()
    vector = tuple(sum(len(f)==k for f in faces) for k in range(N+1))
    assert vector == (1,25,140,204,82,10)
    # Greedy pivot matching on the currently unmatched face poset.
    unmatched = set(faces)
    upper = {}
    lower = {}
    for v in range(N*N):
        for s in sorted((x for x in unmatched if v not in x),
                        key=lambda x:(len(x),x)):
            t = tuple(sorted(s+(v,)))
            if s in unmatched and t in unmatched:
                unmatched.remove(s)
                unmatched.remove(t)
                upper[s] = t
                lower[t] = s
    assert len(upper) == 222
    critical = Counter(len(s)-1 for s in unmatched)
    assert critical == {1:1,2:17}
    assert () in upper
    # Check every incidence, using upper orientation for paired covers,
    # downward orientation for every other cover.
    adj = {s:[] for s in faces}
    indegree = {s:0 for s in faces}
    edge_count = 0
    for t in faces:
        for s,_ in boundary(t):
            edge_count += 1
            if upper.get(s) == t:
                a,b = s,t
            else:
                a,b = t,s
            adj[a].append(b)
            indegree[b] += 1
    assert edge_count == 1295
    dq = deque(x for x in faces if indegree[x]==0)
    passed = 0
    while dq:
        x = dq.popleft()
        passed += 1
        for y in adj[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                dq.append(y)
    assert passed == len(faces), 'matching must be acyclic'
    one_cells = sorted(x for x in unmatched if len(x)==2)
    two_cells = sorted(x for x in unmatched if len(x)==3)
    assert len(one_cells)==1 and len(two_cells)==17
    critical_one = one_cells[0]
    # Exact integral elimination of matched face/coface pairs in degree 2/1.
    # For e matched upward to t, eliminate e from its coefficient-one
    # occurrence in d(t); for e matched downward to a vertex, project e
    # to zero. Acyclicity makes this recursion terminating.
    @lru_cache(None)
    def projection(e):
        assert len(e)==2
        if e in unmatched:
            return 1 if e==critical_one else 0
        if e in lower:
            return 0
        assert e in upper and len(upper[e])==3
        t=upper[e]
        sign = next(a for s,a in boundary(t) if s==e)
        return sum(-sign*a*projection(s) for s,a in boundary(t) if s!=e)
    # This projection in fact gives an explicit integral cocycle on K.
    all_triangle_evaluations = [sum(a*projection(s) for s,a in boundary(t))
                                for t in faces if len(t)==3]
    assert all(v==0 for v in all_triangle_evaluations), all_triangle_evaluations
    degrees = [sum(a*projection(s) for s,a in boundary(t))
               for t in two_cells]
    assert degrees == [0]*17, degrees
    # Connectivity gives rank(d_1)=24 over every field.
    graph = {v:set() for v in range(N*N)}
    for e in faces:
        if len(e)==2:
            a,b=e;graph[a].add(b);graph[b].add(a)
    reached={0};frontier=[0]
    while frontier:
        a=frontier.pop()
        for b in graph[a]-reached:
            reached.add(b);frontier.append(b)
    assert len(reached)==25
    # Independent exact-rational rank of the unreduced simplicial d_2.
    edges = sorted(e for e in faces if len(e)==2)
    triangles = sorted(t for t in faces if len(t)==3)
    ei = {e:i for i,e in enumerate(edges)}
    pivots = {}
    for t in triangles:
        vec = {ei[e]:Fraction(sign) for e,sign in boundary(t)}
        while vec:
            pivot = max(vec)
            if pivot not in pivots:
                a = vec[pivot]
                pivots[pivot] = {i:v/a for i,v in vec.items()}
                break
            z=vec[pivot]
            for i,w in pivots[pivot].items():
                vec[i] = vec.get(i,0)-z*w
                if vec[i]==0:del vec[i]
    assert len(pivots)==115
    # Euler characteristic independently corroborates the Morse result.
    chi = sum((-1)**(k-1)*vector[k] for k in range(1,N+1))
    assert chi == 17
    print('F_VECTOR 25 140 204 82 10')
    print('PAIRS 222 CRITICAL_1 1 CRITICAL_2 17')
    print('ACYC_HASSE 462_VERTICES 1295_EDGES')
    print('SIMPLICIAL_BOUNDARY_1_RANK_OVER_Q',24)
    print('SIMPLICIAL_BOUNDARY_2_RANK_OVER_Q', len(pivots))
    print('INTEGRAL_MORSE_D2',degrees)
    print('INTEGRAL_H1 Z H2 Z^17 ALL_OTHER_REDUCED_HOMOLOGY_ZERO')
    print('HOMOTOPY S1 wedge 17*S2')
    print('VERIFY_OK_QUEENS5_INTEGRAL_HOMOTOPY')

if __name__=='__main__':
    certificate()
