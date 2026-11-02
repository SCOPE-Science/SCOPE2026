#!/usr/bin/env python3
"""Exact finite checks for ordinary zero forcing on prisms (stdlib only).
These tests corroborate, but do not replace, the all-n structural proof.
"""
from itertools import combinations
from collections import Counter, deque

ORBIT_TYPES = ('A', 'B', 'C', 'D', 'E')
MATRIX = ((2,4,2,0,0), (2,1,2,1,2), (1,2,0,1,1),
          (0,4,4,0,4), (0,4,2,2,0))

def neighbours(n):
    return [frozenset({l*n+(i-1)%n, l*n+(i+1)%n, (1-l)*n+i})
            for l in range(2) for i in range(n)]

def closure(S, adj):
    blue = set(S)
    while True:
        new = set()
        for v in blue:
            white = adj[v] - blue
            if len(white) == 1:
                new.update(white)
        if not (new - blue):
            return frozenset(blue)
        blue.update(new)

def reps(n):
    return (
        frozenset((0,1,2,3)),
        frozenset((0,1,2,n)),
        frozenset((0,1,3,n+1)),
        frozenset((0,1,n,n+1)),
        frozenset((0,1,n,2*n-1)),
    )

def orbit(R,n):
    return {frozenset((((v//n)^flip)*n+(sgn*(v%n)+offset)%n)
                       for v in R)
            for flip in (0,1) for sgn in (-1,1) for offset in range(n)}

def edges_for(S, valid, adj, mode):
    available = set(range(len(adj))) - S
    result = set()
    for v in S:
        for w in (available if mode == 'exchange' else (adj[v] - S)):
            candidate = frozenset((S-{v})|{w})
            if candidate in valid:
                result.add(candidate)
    return result

def inspect(n):
    adj = neighbours(n)
    all_vertices = set(range(2*n))
    good = {frozenset(S) for S in combinations(range(2*n),4)
            if closure(S, adj) == all_vertices}
    for S in combinations(range(2*n),3):
        assert closure(S, adj) != all_vertices, (n, 'unexpected 3-seed set', S)
    types = {}
    for j, rep in enumerate(reps(n)):
        assert closure(rep, adj) == all_vertices
        for S in orbit(rep,n):
            assert S not in types, (n, 'overlapping symmetry orbits')
            types[S] = j
    assert good == set(types), (n, 'missing extra minimum sets', good-set(types))
    orbit_counts = Counter(types.values())
    assert tuple(orbit_counts[j] for j in range(5)) == (2*n,4*n,4*n,n,2*n)
    assert len(good) == 13*n
    E = {S:edges_for(S,good,adj,'exchange') for S in good}
    assert all(S in E[T] for T,near in E.items() for S in near)
    assert sum(map(len,E.values()))//2 == 48*n
    assert Counter(map(len,E.values())) == {5:4*n,8:8*n,12:n}
    assert all(not edges_for(S,good,adj,'slide') for S in good)
    for j, rep in enumerate(reps(n)):
        row=Counter(types[T] for T in E[rep])
        assert tuple(row[k] for k in range(5))==MATRIX[j], (n,j,row)
    seen={next(iter(good))}; todo=deque(seen)
    while todo:
        for T in E[todo.popleft()]:
            if T not in seen:
                seen.add(T);todo.append(T)
    assert len(seen)==len(good)
    print('n=',n,'bases=',len(good),'TE edges=',sum(map(len,E.values()))//2,
          'TS edges=0','orbits=',tuple(orbit_counts[j] for j in range(5)))

def necessity_local(n):
    adj=neighbours(n); full=set(range(2*n))
    templates=[(frozenset((0,1,2)), frozenset((3,n-1,n,n+2))),
               (frozenset((0,1,n)), frozenset((2,n-2,n+1,2*n-1)))]
    for T, allowed in templates:
        actual={v for v in full-T if closure(T|{v},adj)==full}
        assert actual==allowed, (n,T,allowed,actual)
    print('n=',n,'two local initial-force classifications verified')

if __name__ == '__main__':
    for n in range(7,13):
        inspect(n)
    for n in range(7,25):
        necessity_local(n)
    print('VERIFY_OK')
