#!/usr/bin/env python3
"""Independent bounded checks for opposite two-run scattered-pattern intersection."""
from collections import deque
from itertools import product

def greedy(pattern, state, char):
    return state + (state < len(pattern) and pattern[state] == char)

def reachable_product(r, s):
    p = '0'*r + '1'*s
    q = '1'*s + '0'*r
    start = (0, 0)
    queue = deque([start])
    seen = {start: 0}
    arcs = []
    while queue:
        i,j = queue.popleft()
        row = []
        for c in '01':
            target = (greedy(p,i,c), greedy(q,j,c))
            if target not in seen:
                seen[target] = len(seen)
                queue.append(target)
            row.append(seen[target])
        arcs.append(tuple(row))
    return seen, arcs

def minimal_classes(seen, arcs, r, s):
    n = r+s
    finals = [int(i == n and j == n) for i,j in seen]
    blocks = finals[:]
    while True:
        sig = [(finals[i], blocks[a], blocks[b]) for i,(a,b) in enumerate(arcs)]
        mapping = {v:j for j,v in enumerate(sorted(set(sig)))}
        newblocks = [mapping[v] for v in sig]
        if len(set(newblocks)) == len(set(blocks)):
            assert all((newblocks[i] == newblocks[j]) == (blocks[i] == blocks[j]) for i in range(len(arcs)) for j in range(i+1,len(arcs)))
            return len(set(newblocks))
        blocks = newblocks

def check_subsequence(w, patt):
    cursor = 0
    for c in w:
        if cursor < len(patt) and c == patt[cursor]:
            cursor += 1
    return cursor == len(patt)

def check_all():
    tested = 0
    for r in range(1, 11):
        for s in range(1, 11):
            seen, arcs = reachable_product(r,s)
            n = r+s
            expected = n*(n+3)//2+r*s
            assert len(seen) == expected, (r,s,'reachable',len(seen),expected)
            B = {(i,j) for i in range(r) for j in range(s)}
            B |= {(i,s+t) for i in range(r) for t in range(i+1)}
            B |= {(r+u,j) for j in range(s) for u in range(j+1)}
            B |= {(i,j) for i in range(r,n+1) for j in range(s,n+1) if (i,j) != (r,s)}
            assert set(seen) == B, (r,s,'region')
            minimum = minimal_classes(seen,arcs,r,s)
            assert minimum == expected, (r,s,'minimum',minimum,expected)
            tested += 1
    word_tests = 0
    for r,s in ((1,1),(1,2),(2,1),(2,2),(2,3),(3,2),(3,3),(4,1),(1,4)):
        seen,arcs = reachable_product(r,s)
        p='0'*r+'1'*s; q='1'*s+'0'*r
        for length in range(13):
            for tup in product('01',repeat=length):
                w=''.join(tup); k=0
                for c in w:
                    k=arcs[k][int(c)]
                state = tuple(seen)[k]
                independent = check_subsequence(w,p) and check_subsequence(w,q)
                assert (state == (r+s,r+s)) == independent,(r,s,w)
                word_tests += 1
    print('VERIFY_OK', 'parameter_pairs',tested,'word_checks',word_tests)
if __name__ == '__main__':
    check_all()
