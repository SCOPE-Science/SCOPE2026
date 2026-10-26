#!/usr/bin/env python3
"""Standalone finite checks of an involutive erasure/projection witness."""
from collections import deque
from itertools import product


def generators(k):
    """Five permutations on 2*k states, indexed by (pair, lane)."""
    assert k >= 2
    n = 2*k
    h = tuple(2*i + (1-j) for i in range(k) for j in (0, 1))
    def lift(fn):
        return tuple(2*fn(i)+j for i in range(k) for j in (0, 1))
    b = lift(lambda i: 1 if i == 0 else 0 if i == 1 else i)
    c = lift(lambda i: -i % k)
    d = lift(lambda i: (1-i) % k)
    e = list(range(n))
    e[0], e[2] = e[2], e[0]
    e = tuple(e)
    return h, (b, c, d, e)


def closure(mask, k):
    # Independent on-state epsilon closure for the erased matching.
    ans = mask
    for i in range(k):
        if mask & (3 << (2*i)):
            ans |= 3 << (2*i)
    return ans


def image(mask, p):
    return sum((1 << p[i]) for i in range(len(p)) if mask & (1 << i))


def projected(k):
    hidden, visible = generators(k)
    assert len(set(hidden)) == 2*k
    for p in (hidden,) + visible:
        assert all(p[p[i]] == i for i in range(2*k))
    start = closure(1, k)
    q = deque([start]); visited = {start}; transitions = {}
    while q:
        state = q.popleft()
        successors = tuple(closure(image(state, p), k) for p in visible)
        transitions[state] = successors
        for nxt in successors:
            if nxt not in visited:
                visited.add(nxt);q.append(nxt)
    # Partition refinement; independent of the combinatorial reachability proof.
    cls = {s: int(bool(s & 1)) for s in visited}
    while True:
        keys = {s: (cls[s],tuple(cls[t] for t in transitions[s])) for s in visited}
        values = {x:i for i,x in enumerate(sorted(set(keys.values())))}
        refined = {s: values[keys[s]] for s in visited}
        if len(set(refined.values())) == len(set(cls.values())):
            break
        cls = refined
    return visited, transitions, len(set(cls.values()))


def accepts_projection_bruteforce(observed, k):
    """Enumerate a/no-a at every gap, directly run the original DFA."""
    h, visible = generators(k)
    for gap in product((0, 1), repeat=len(observed)+1):
        q = 0
        for j, symbol in enumerate(observed):
            if gap[j]: q = h[q]
            q = visible[symbol][q]
        if gap[-1]: q = h[q]
        if q == 0: return True
    return False


def original_is_minimal(k):
    h, visible = generators(k)
    # Every original state can be sent to the unique final state; every letter
    # is bijective. Therefore all pairs of states have different right languages.
    reach = {0}; todo = deque([0]); perms=(h,)+visible
    while todo:
        v=todo.popleft()
        for g in perms:
            w=g[v]
            if w not in reach:reach.add(w);todo.append(w)
    return len(reach)==2*k


def verify():
    configurations=0
    for k in range(2, 11):
        states, transitions, classes = projected(k)
        expected = (1 << k) - 1
        assert len(states) == expected, (k, len(states), expected)
        assert classes == expected, (k, classes, expected)
        assert original_is_minimal(k), k
        for state in states:
            assert closure(state,k) == state
            assert state > 0
        configurations += 1
    comparisons=0
    # Independently enumerate all (bounded) a insertions; k <= 4, word length <= 5.
    for k in range(2, 5):
        _, transitions, _ = projected(k)
        initial = closure(1,k)
        for length in range(6):
            for observed in product(range(4),repeat=length):
                q=initial
                for a in observed:q=transitions[q][a]
                got=bool(q & 1)
                want=accepts_projection_bruteforce(observed,k)
                assert got == want, (k,observed,got,want)
                comparisons+=1
    print('VERIFY_OK configurations=', configurations,
          ' independent_projected_words=',comparisons,
          ' largest_projected_states=', (1<<10)-1, sep='')


if __name__ == '__main__':
    verify()
