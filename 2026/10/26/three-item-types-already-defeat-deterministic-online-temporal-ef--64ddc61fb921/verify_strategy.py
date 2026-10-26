"""Reproduce the finite adversarial TEF1 obstruction, using Python's standard library."""
import json
from functools import lru_cache
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / 'STRATEGY.json').read_text(encoding='utf-8'))
VALUES = ((0, 1, 2), (0, 2, 1), (1, 2, 2))
TYPES = 'ABC'
ZERO = (0,) * 9
assert DATA['schema_version'] == 1 and DATA['agents'] == 3
assert DATA['maximum_arrivals'] == 7
assert tuple(tuple(DATA['item_types'][x]) for x in TYPES) == VALUES

def ef1(counts):
    assert len(counts) == 9 and all(isinstance(x, int) and x >= 0 for x in counts)
    for observer in range(3):
        own = sum(counts[3*t + observer] * VALUES[t][observer] for t in range(3))
        for recipient in range(3):
            if observer == recipient:
                continue
            rival = sum(counts[3*t + recipient] * VALUES[t][observer] for t in range(3))
            deletion = max([0] + [VALUES[t][observer] for t in range(3)
                                  if counts[3*t + recipient] > 0])
            if own + deletion < rival:
                return False
    return True

def advance(counts, typ, agent):
    z = list(counts)
    z[3 * typ + agent] += 1
    return tuple(z)

policy = {}
for entry in DATA['policy']:
    state = tuple(entry['counts'])
    assert state not in policy and sum(state) < 7
    assert ef1(state) and entry['next_type'] in TYPES
    policy[state] = TYPES.index(entry['next_type'])
assert ZERO in policy

# Verify every possible allocator response to the indicated next arrival.
visited = set()
terminal = 0
edges = 0

def check_node(state):
    global terminal, edges
    if state in visited:
        return
    visited.add(state)
    assert state in policy and ef1(state)
    typ = policy[state]
    for agent in range(3):
        nxt = advance(state, typ, agent)
        edges += 1
        if not ef1(nxt):
            terminal += 1
        else:
            assert sum(nxt) < 7, 'Fair terminal branch at the horizon'
            check_node(nxt)

check_node(ZERO)
assert visited == set(policy)
assert (len(policy), edges, terminal) == (42, 126, 74)

# Independently solve the entire finite turn-based game, without the policy.
@lru_cache(maxsize=None)
def adversary_wins(state, turns):
    if turns == 0:
        return False
    return any(all(not ef1(advance(state, typ, agent)) or
                   adversary_wins(advance(state, typ, agent), turns - 1)
                   for agent in range(3)) for typ in range(3))

assert not adversary_wins(ZERO, 6)
assert adversary_wins(ZERO, 7)

# Separately distinguish an online obstruction from an unavoidable offline one.
# Each fixed arrival sequence below has *some* allocation preserving EF1 at
# all prefixes. Its allocation choices may depend on the future sequence.
def hindsight_feasible(sequence):
    states = {ZERO}
    for typ in sequence:
        states = {nxt for state in states for agent in range(3)
                  if ef1(nxt := advance(state, typ, agent))}
        if not states:
            return False
    return True

for length in range(1, 8):
    assert all(hindsight_feasible(sequence)
               for sequence in product(range(3), repeat=length))
print('PASS: 42 certified policy nodes, 126 allocator responses, 74 immediate failures.')
print('PASS: adversary cannot force failure by turn 6 but can by turn 7.')
print('PASS: all 3279 fixed sequences of lengths 1 through 7 admit temporal EF1.')
