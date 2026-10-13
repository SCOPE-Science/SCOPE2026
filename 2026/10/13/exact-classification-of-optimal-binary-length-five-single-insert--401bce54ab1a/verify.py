"""Independent, standard-library enumeration using subsequence predicates."""
from itertools import product

centers = tuple(''.join(t) for t in product('01', repeat=5))
targets = tuple(''.join(t) for t in product('01', repeat=6))
parents = {y: frozenset(y[:j] + y[j + 1:] for j in range(6)) for y in targets}
balls = {x: frozenset(y for y in targets if x in parents[y]) for x in centers}
assert len(centers) == 32 and len(targets) == 64
assert all(len(balls[x]) == 7 for x in centers)

solutions = set()
visited = 0

def explore(chosen, uncovered, limit):
    global visited
    visited += 1
    if not uncovered:
        solutions.add(frozenset(chosen))
        return
    if len(chosen) == limit or len(uncovered) > 7 * (limit - len(chosen)):
        return
    y = min(uncovered, key=lambda v: (len(parents[v] - chosen), v))
    for x in sorted(parents[y] - chosen):
        explore(chosen | {x}, uncovered - balls[x], limit)

explore(frozenset(), frozenset(targets), 11)
assert not solutions, 'code of size at most eleven exists'
explore(frozenset(), frozenset(targets), 12)
assert len(solutions) == 6
assert all(len(c) == 12 for c in solutions)
assert all(any(x in parents[y] for x in c) for c in solutions for y in targets)

unseen = set(solutions)
orbits = []
while unseen:
    base = min(unseen, key=lambda a: tuple(sorted(a)))
    orbit = {
        frozenset(''.join(str(int(bit) ^ flip) for bit in (word[::-1] if rev else word))
                  for word in base)
        for flip in (0, 1) for rev in (0, 1)
    }
    assert orbit <= unseen and len(orbit) == 2
    orbits.append(orbit)
    unseen -= orbit
assert len(orbits) == 3
print('optimal_size=12 labeled_optima=6 complement_reversal_orbits=3 nodes=',
      visited, 'VERIFY_OK')
