"""Finite checks for remanent languages of graphs with matching clique and chromatic numbers.
This enumerates actual orientations and automata, independently of the mathematical proof.
"""
from collections import deque
from itertools import product

SIGNS = ('+', '-')

def walk(images, n, word):
    """Every graph vertex is initial and final, and + follows arcs; - reverses arcs."""
    positions = set(range(n))
    for symbol in word:
        next_positions = set()
        for a, b in images:
            if symbol == '+' and a in positions:
                next_positions.add(b)
            if symbol == '-' and b in positions:
                next_positions.add(a)
        positions = next_positions
        if not positions:
            return False
    return bool(positions)

def all_orientations(edges):
    for mask in range(1 << len(edges)):
        yield tuple((a, b) if ((mask >> i) & 1) else (b, a)
                    for i, (a, b) in enumerate(edges))

def all_words_to(bound):
    for length in range(bound + 1):
        yield from (''.join(p) for p in product(SIGNS, repeat=length))

def run_avoiding(word, k):
    return '+' * k not in word and '-' * k not in word

def tournament(k):
    return tuple((i, j) for i in range(k) for j in range(i + 1, k))

def remnant(n, edges, word):
    return all(walk(oriented, n, word) for oriented in all_orientations(edges))

def dfa_transitions(k):
    # 0: start; 1..k-1: + run lengths; k..2k-2: - run lengths; 2k-1: reject sink
    dead = 2 * k - 1
    def move(state, symbol):
        if state == dead:
            return dead
        if state == 0:
            return 1 if symbol == '+' else k
        if 1 <= state <= k - 1:
            return state + 1 if symbol == '+' and state + 1 < k else (dead if symbol == '+' else k)
        length = state - k + 1
        return state + 1 if symbol == '-' and length + 1 < k else (dead if symbol == '-' else 1)
    if k == 1:
        return lambda state, symbol: 1, 1
    return move, dead

def check_dfa(k):
    move, dead = dfa_transitions(k)
    seen = {0: ''}
    q = deque([0])
    while q:
        state = q.popleft()
        for sym in SIGNS:
            nxt = move(state, sym)
            if nxt not in seen:
                seen[nxt] = seen[state] + sym
                q.append(nxt)
    assert len(seen) == 2 * k, ('unreachable', k, seen)
    # Partition-refinement independently checks exact DFA state count.
    groups = [set(range(dead)), {dead}]
    while True:
        grp_of = {state: i for i, grp in enumerate(groups) for state in grp}
        refined = []
        for grp in groups:
            buckets = {}
            for state in grp:
                key = tuple(grp_of[move(state, ch)] for ch in SIGNS)
                buckets.setdefault(key, set()).add(state)
            refined.extend(buckets.values())
        if len(refined) == len(groups):
            break
        groups = refined
    assert len(groups) == 2 * k, ('not minimal', k, len(groups))
    for word in all_words_to(10):
        s = 0
        for symbol in word:
            s = move(s, symbol)
        assert (s != dead) == run_avoiding(word, k)

for k in range(1, 12):
    arcs = tournament(k)
    for word in all_words_to(11):
        assert walk(arcs, k, word) == run_avoiding(word, k), (k, word)
    check_dfa(k)
    print('Transitive tournament and minimal DFA: k=', k, 'states=', 2 * k)

# Independent graph tests: enumerate every orientation, not a sample of orientations.
examples = [
    ('edgeless-1', 1, [], 1),
    ('path-3', 3, [(0,1), (1,2)], 2),
    ('cycle-4', 4, [(0,1), (1,2), (2,3), (3,0)], 2),
    ('triangle-plus-leaf', 4, [(0,1), (0,2), (1,2), (2,3)], 3),
    ('triangle-plus-path', 5, [(0,1), (0,2), (1,2), (2,3), (3,4)], 3),
    ('clique-4', 4, tournament(4), 4),
    ('biclique-3-3', 6, [(i,j) for i in range(3) for j in range(3,6)], 2),
]
for title, n, edges, k in examples:
    for word in all_words_to(8):
        assert remnant(n, edges, word) == run_avoiding(word, k), (title, word)
    print('Complete orientation enumeration:', title, 'orientations=', 1 << len(edges))

c5_arcs = ((0,1), (2,1), (2,3), (4,3), (0,4))
w = '++-++'
assert run_avoiding(w, 3) and walk(tournament(3), 3, w)
assert not walk(c5_arcs, 5, w)
print('Odd-cycle boundary witness: C5, word=++-++, rejected by given orientation')

for k in range(1, 9):
    counts = [sum(run_avoiding(w, k) for w in (''.join(p) for p in product(SIGNS, repeat=n)))
              for n in range(13)]
    comp = [0] * 13
    comp[0] = 1
    for n in range(1, 13):
        comp[n] = sum(comp[n-j] for j in range(1, k) if n >= j)
    target = [1] + [2 * c for c in comp[1:]]
    assert counts == target, (k, counts, target)
    print('Run-composition enumerator: k=', k, 'a_0..a_12=', counts)
print('ALL CHECKS PASS')
