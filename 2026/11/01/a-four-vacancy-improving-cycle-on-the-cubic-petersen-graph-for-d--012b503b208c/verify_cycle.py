"""Exact, dependency-free certificate for a diversity-seeking jump cycle.

Vertices are numbered 0 through 9. Each state identifies six distinct agents,
with the remaining four vertices unoccupied. Utilities are rational numbers.
"""
from fractions import Fraction

EDGES = (
    (0, 1), (0, 4), (0, 5), (1, 2), (1, 6),
    (2, 3), (2, 7), (3, 4), (3, 8), (4, 9),
    (5, 7), (5, 8), (6, 8), (6, 9), (7, 9),
)
BLOCK = (
    (5, 0), (1, 7), (6, 1), (2, 8), (7, 2),
    (3, 9), (8, 3), (4, 5), (9, 4), (0, 6),
)

neighbors = {v: set() for v in range(10)}
for a, b in EDGES:
    assert 0 <= a < b < 10
    neighbors[a].add(b)
    neighbors[b].add(a)
assert len(set(EDGES)) == 15
assert all(len(neighbors[v]) == 3 for v in range(10))
assert all(len(neighbors[v] & neighbors[u]) == 0 for v, u in EDGES)

agent_type = {'r1': 'R', 'r2': 'R', 'r3': 'R',
              'b1': 'B', 'b2': 'B', 'b3': 'B'}
initial = {1: 'r1', 2: 'b1', 3: 'r2',
           4: 'b2', 5: 'r3', 6: 'b3'}
state = dict(initial)

def utility(placement, vertex):
    agent = placement[vertex]
    occupied = [u for u in neighbors[vertex] if u in placement]
    if not occupied:
        return Fraction(0)
    different = sum(agent_type[placement[u]] != agent_type[agent]
                    for u in occupied)
    return Fraction(different, len(occupied))

for repetition in range(6):
    for index, (source, target) in enumerate(BLOCK):
        assert source in state and target not in state
        before = utility(state, source)
        mover = state.pop(source)
        state[target] = mover
        after = utility(state, target)
        expected = ((Fraction(0), Fraction(1, 2)) if index % 2 == 0
                    else (Fraction(2, 3), Fraction(1)))
        assert (before, after) == expected, (repetition, index, before, after)
        assert after > before
        assert len(state) == 6
    if repetition % 2 == 0:
        assert tuple(agent_type[state[v]] for v in range(1, 7)) == (
            'B', 'R', 'B', 'R', 'B', 'R')
    else:
        assert tuple(agent_type[state[v]] for v in range(1, 7)) == (
            'R', 'B', 'R', 'B', 'R', 'B')
    assert set(state) == set(range(1, 7))

assert state == initial, (state, initial)
print('PASS: Petersen degree 3, 4 vacancies, 6 labeled agents,')
print('      60 exact strictly improving jumps, labeled state restored.')
