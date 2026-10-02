"""Exact train-track data and a universal six-state legalizing certificate."""
from itertools import combinations

alphabet = 'abcdABCD'
inv = str.swapcase
f = dict(zip('abcd', ('bc', 'c', 'd', 'a')))
f.update({inv(x): inv(w[::-1]) for x, w in tuple(f.items())})

def sub(w, morph=f):
    return ''.join(morph[x] for x in w)

def reduce(w):
    out = []
    for x in w:
        if out and out[-1] == inv(x):
            out.pop()
        else:
            out.append(x)
    return ''.join(out)

inverse = dict(zip('abcd', ('d', 'aB', 'b', 'c')))
inverse.update({inv(x): inv(w[::-1]) for x, w in tuple(inverse.items())})
for x in alphabet:
    assert reduce(sub(inverse[x])) == x
    assert reduce(sub(f[x], inverse)) == x

direction = {x: f[x][0] for x in alphabet}

def legal(x, y):
    seen = set()
    while (x, y) not in seen:
        if x == y:
            return False
        seen.add((x, y))
        x, y = direction[x], direction[y]
    return True

assert {frozenset(t) for t in combinations(alphabet, 2) if not legal(*t)} == {frozenset('AB')}
turns = {frozenset((inv(x), y)) for w in f.values() for x, y in zip(w, w[1:])}
while True:
    new = turns | {frozenset(direction[x] for x in t) for t in turns}
    if new == turns:
        break
    turns = new
assert len(turns) == 13 and all(legal(*t) for t in turns)
assert {t for t in turns if 'B' not in t} == {frozenset((x,y)) for x in 'abcd' for y in 'ACD'}

M = [[f[x].count(y) for y in 'abcd'] for x in 'abcd']
def mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
power = [[int(i == j) for j in range(4)] for i in range(4)]
for _ in range(10):
    power = mul(power, M)
assert power == [[3,1,2,3],[2,1,1,1],[1,2,3,1],[1,1,3,3]]

g = {x: x for x in alphabet}
for _ in range(6):
    g = {x: sub(w) for x, w in g.items()}
assert [g[x] for x in 'ABCD'] == ['ADDC','AD','CBA','DCCB']

def trim(u, v):
    k = 0
    while k < min(len(u), len(v)) and u[k] == v[k]:
        k += 1
    return u[k:], v[k:]

initial = trim(g['A'], g['B'])
pending, states, edges, terminals = [initial], set(), {}, []
while pending:
    state = pending.pop()
    if state in states:
        continue
    states.add(state)
    u, v = state
    assert bool(u) != bool(v)
    edges[state] = []
    # All negative continuations are an over-approximation of legal arms.
    # Every positive continuation has opposite sign to the residual and is legal.
    for x in 'abcd':
        a, b = (u, g[x]) if u else (g[x], v)
        assert legal(a[0], b[0])
    for x in 'ABCD':
        a, b = trim(u, g[x]) if u else trim(g[x], v)
        assert a or b, 'simultaneous exhaustion would require extra analysis'
        if a and b:
            assert legal(a[0], b[0]), (state, x, a, b)
            terminals.append((state, x, a[0], b[0]))
        else:
            edges[state].append((a, b))
            pending.append((a, b))
assert states == {('DC',''), ('','CB'), ('A',''), ('','D'), ('CCB',''), ('','DDC')}

visited, active = set(), set()
def acyclic(s):
    assert s not in active, 'cycle: no universal conclusion permitted'
    if s in visited:
        return
    active.add(s)
    for t in edges[s]:
        acyclic(t)
    active.remove(s)
    visited.add(s)
acyclic(initial)
assert visited == states and len(terminals) == 19
print('PASS: inverse, primitive matrix, 13 taken turns, K4,3 stable graph;')
print('PASS: all 6 cancellation states reachable, graph acyclic, all exits legal.')
