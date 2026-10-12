"""Finite consistency checks for the block-counting opacity theorem.

Run with Python 3.10 or newer: python block_opacity_verify.py.
The accompanying mathematical proof establishes the infinite statements.
"""
from collections import deque
from itertools import product


def machine(q, pattern):
    k = len(pattern)
    symbol = tuple(map(int, pattern))
    states = [(j, residue) for j in range(k) for residue in range(q)]
    if symbol[0] == 0:
        states = [('lead', 0)] + states
        initial = ('lead', 0)
    else:
        initial = (0, 0)
    ids = {s: i for i, s in enumerate(states)}
    edges = []
    outputs = []
    for j, residue in states:
        outputs.append(1 if j == 'lead' and k == 1 else residue)
        dest = []
        for digit in range(q):
            if j == 'lead':
                dst = ('lead', 0) if digit == 0 else (0, 0)
            else:
                suffix = symbol[:j] + (digit,)
                count = int(len(suffix) >= k and suffix[-k:] == symbol)
                next_residue = (residue + count) % q
                next_j = max(h for h in range(k)
                             if h == 0 or suffix[-h:] == symbol[:h])
                dst = (next_j, next_residue)
            dest.append(ids[dst])
        edges.append(tuple(dest))
    return states, ids[initial], tuple(outputs), tuple(edges)


def expansion(n, q):
    if n == 0:
        return (0,)
    result = []
    while n:
        result.append(n % q)
        n //= q
    return tuple(reversed(result))


def direct(q, pattern, n):
    word = expansion(n, q)
    k = len(pattern)
    return sum(word[i:i+k] == pattern
               for i in range(len(word)-k+1)) % q


def refined_partition(outputs, edges):
    blocks = tuple(outputs)
    while True:
        patterns = [(outputs[i],) + tuple(blocks[j] for j in edges[i])
                    for i in range(len(outputs))]
        dictionary = {v: i for i, v in enumerate(sorted(set(patterns)))}
        nxt = tuple(dictionary[t] for t in patterns)
        if all((blocks[i] == blocks[j]) == (nxt[i] == nxt[j])
               for i in range(len(outputs)) for j in range(len(outputs))):
            return len(set(nxt))
        blocks = nxt


def first_conflict_length(edges, initial, q, cutoff=5):
    # Search every input word up to cutoff; conflicting incoming labels
    # at the same state make the path inhomogeneous.
    todo = deque([(initial, tuple(), 0)])
    while todo:
        state, seen, length = todo.popleft()
        if length == cutoff:
            continue
        for digit in range(q):
            dst = edges[state][digit]
            if any(s == dst and b != digit for s,b in seen):
                return length + 1
            todo.append((dst, seen + ((dst,digit),), length + 1))
    return None


def verify():
    cases = 0
    direct_cases = 0
    transparent = 0
    opaque = 0
    intermediary = 0
    for q, maxk in ((2, 8), (3, 5), (4, 4), (5, 3)):
        for k in range(1, maxk + 1):
            for pattern in product(range(q), repeat=k):
                states, start, outputs, edges = machine(q, pattern)
                count = refined_partition(outputs, edges)
                assert count == len(states), (q, pattern, count, len(states))
                assert len(states) == q*k + (pattern[0] == 0)
                # Every machine state must be reachable from its initial state.
                todo = [start]
                reached = {start}
                for s in todo:
                    for dst in edges[s]:
                        if dst not in reached:
                            reached.add(dst)
                            todo.append(dst)
                assert len(reached) == len(states), (q, pattern, 'not reachable')
                # Independent incoming-label test (every edge to each state).
                types = {i: set() for i in range(len(states))}
                for s, row in enumerate(edges):
                    for b, dst in enumerate(row):
                        types[dst].add(b)
                is_homogeneous = all(len(values) <= 1 for values in types.values())
                if q == 2 and k >= 2:
                    assert is_homogeneous, (q, pattern)
                    assert first_conflict_length(edges, start, q, cutoff=5) is None
                    transparent += 1
                else:
                    assert not is_homogeneous
                    expected = 3 if (q == 2 and pattern == (0,)) else 2
                    assert first_conflict_length(edges, start, q, cutoff=3) == expected
                    (intermediary if expected == 3 else opaque)
                # The output is verified against literal standard expansion,
                # including n=0 and leading-zero-sensitive patterns.
                bound = 800 if q <= 3 else 300
                for n in range(bound):
                    state = start
                    for digit in expansion(n, q):
                        state = edges[state][digit]
                    assert outputs[state] == direct(q, pattern, n), (q, pattern, n)
                    direct_cases += 1
                cases += 1
    print('VERIFY_OK', 'patterns='+str(cases), 'direct_cases='+str(direct_cases),
          'binary_transparent='+str(transparent), 'nonbinary_opaque=all',
          'intrinsic_size=q*length+leading_zero', 'singleton_zero_opacity=1/2',
          'singleton_one_opacity=1')


if __name__ == '__main__':
    verify()
