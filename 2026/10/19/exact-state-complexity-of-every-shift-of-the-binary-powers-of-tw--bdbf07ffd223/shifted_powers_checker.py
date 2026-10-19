#!/usr/bin/env python3
"""Independent deterministic-automaton test of the exact shift state-count formula."""
from collections import deque


def formula(c):
    assert c >= 1
    s = c.bit_length()
    if c & (c-1) == 0:
        return s+2
    b = 2**s-c
    a = format(b, 'b')
    beta = a.zfill(s)
    r = len(a)-len(a.lstrip('1'))
    h = 0
    while h < len(a)-r and a[r+h] == beta[h]:
        h += 1
    return s+r+h+3


def minimal_dfa(c):
    """Build an NFA for ALL binary expansions (including leading zeroes),
    determinize, then minimize by fixed-point partition refinement."""
    s = c.bit_length()
    is_power = c & (c-1) == 0
    if is_power:
        # Binary language: 0* union 0* 1+ 0^(s-1).
        def edge(q, d):
            if q == 'R':
                return {'R'} if d == '0' else {'L'}
            if q == 'L':
                if d == '1': return {'L'}
                return {('Z',1)} if s > 1 else set()
            typ,i = q
            if typ == 'Z' and i < s-1 and d == '0': return {('Z',i+1)}
            return set()
        def accepting(q):
            return q == 'R' or (q == 'L' if s == 1 else q == ('Z',s-1))
    else:
        a = format(2**s-c,'b')
        beta = a.zfill(s)
        def edge(q, d):
            if q == 'R':
                return {'R'} if d == '0' else {('A',1),'L'}
            if q == 'L':
                return {'L'} if d == '1' else {('B',1)}
            typ,i = q
            if typ == 'A' and i < len(a) and a[i] == d: return {('A',i+1)}
            if typ == 'B' and i < s and beta[i] == d: return {('B',i+1)}
            return set()
        def accepting(q):
            return q == ('A',len(a)) or q == ('B',s)
    q0 = frozenset({'R'})
    queue = [q0]
    idx = {q0:0}
    edges = []
    k = 0
    while k < len(queue):
        q = queue[k]
        next_ids = []
        for d in '01':
            nxt = frozenset(q2 for v in q for q2 in edge(v,d))
            if nxt not in idx:
                idx[nxt] = len(queue)
                queue.append(nxt)
            next_ids.append(idx[nxt])
        edges.append(tuple(next_ids))
        k += 1
    output = [int(any(accepting(v) for v in q)) for q in queue]
    labels = output[:]
    while True:
        signatures = [(labels[i], labels[edges[i][0]], labels[edges[i][1]]) for i in range(len(queue))]
        codes = {v:j for j,v in enumerate(sorted(set(signatures)))}
        new = [codes[x] for x in signatures]
        old_pairs = {(i,j) for i in range(len(queue)) for j in range(i+1,len(queue)) if labels[i] == labels[j]}
        new_pairs = {(i,j) for i in range(len(queue)) for j in range(i+1,len(queue)) if new[i] == new[j]}
        labels = new
        if new_pairs == old_pairs: break
    return len(set(labels)),len(queue),queue,edges,output


def test(limit=4095):
    maximal = 0
    for c in range(1,limit+1):
        count,n,states,edges,outputs = minimal_dfa(c)
        assert count == formula(c), (c,count,formula(c))
        maximal = max(maximal,n)
        if c <= 100:
            for x in range(0,180):
                q = 0
                for d in format(x, 'b'):
                    q = edges[q][int(d)]
                nval = x+c
                pred = int(nval > 0 and (nval & (nval-1)) == 0)
                assert outputs[q] == pred, (c,x,outputs[q],pred)
                # Test padded representations independently.
                q = 0
                for d in '000'+format(x,'b'):
                    q = edges[q][int(d)]
                assert outputs[q] == pred, (c,x,'padding')
    print('Exact DFA minimization and formula: c=1..%d PASS' % limit)
    print('Independent arithmetic membership: 100 shifts x 180 indices (including padding) PASS')
    print('Largest reachable determinized NFA size:',maximal)
    for c in [1,2,3,5,6,7,9,11,12,15,17,22,31,32,63,100,127,255,511,1023,2047,4095]:
        print('c=%d states=%d' % (c,formula(c)))

if __name__ == '__main__':
    test()
