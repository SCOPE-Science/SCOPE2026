"""Exact finite verification of the six-vertex bipartite jump-game classification.

Run with Python 3.10+; only the standard library is used.
The theorem is conditional on the game model and preference axioms in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product

ZERO, RED, BLUE = 0, 1, 2
CUTOFF = Q(2, 5)


def all_peaks(n):
    """Check all points where a comparison can change and one point between.

    Each realized fraction is k/t for 1 <= k <= t <= n. For f<g<1,
    normalized triangular preferences can tie only at f/(1+f-g).
    At crossings themselves strict improvements are tested exactly.
    """
    ratios = sorted({Q(k, t) for t in range(1, n + 1) for k in range(1, t + 1)})
    boundaries = {Q(0), Q(1)}
    for f in ratios:
        for g in ratios:
            if f < g < 1:
                lam = f / (1 + f - g)
                if 0 < lam < 1:
                    boundaries.add(lam)
    bs = sorted(boundaries)
    grid = set(bs[1:-1])
    grid.update((x + y) / 2 for x, y in zip(bs, bs[1:]))
    return sorted(grid)


def order_value(f, lam):
    # All admissible source utilities have exactly this ordinal ordering.
    return f / lam if f <= lam else (1 - f) / (1 - lam)


def local_fraction(state, pos, neighbors):
    c = state[pos]
    assert c in (RED, BLUE)
    occupied = [i for i in neighbors[pos] if state[i] != ZERO]
    return Q(1 + sum(state[i] == c for i in occupied), 1 + len(occupied))


def state_edges(a, b, red_count, blue_count, lam):
    n = a + b
    neighbors = tuple(tuple(range(a, n)) if v < a else tuple(range(a)) for v in range(n))
    profiles = (state for state in product((ZERO, RED, BLUE), repeat=n)
                if state.count(RED) == red_count and state.count(BLUE) == blue_count)
    edges = {}
    for state in profiles:
        moves = []
        for origin, c in enumerate(state):
            if c == ZERO:
                continue
            prior = order_value(local_fraction(state, origin, neighbors), lam)
            for dest, other in enumerate(state):
                if other != ZERO:
                    continue
                updated = list(state)
                updated[dest], updated[origin] = c, ZERO
                updated = tuple(updated)
                after = order_value(local_fraction(updated, dest, neighbors), lam)
                if after > prior:
                    moves.append(updated)
        edges[state] = moves
    return edges


def has_cycle(edges):
    # Three-color directed graph; cycle <=> no finite improvement property.
    status = {}
    def visit(state):
        status[state] = 1
        for dest in edges[state]:
            if status.get(dest) == 1:
                return True
            if status.get(dest, 0) == 0 and visit(dest):
                return True
        status[state] = 2
        return False
    return any(visit(state) for state in edges if status.get(state, 0) == 0)


def verify_explicit_witness():
    # A-side positions 0,1,2; B-side positions 3,4,5.
    # 1=red, 2=blue; three red, one blue, two vacant.
    states = [(1,2,1,0,0,1), (0,2,1,1,0,1),
              (0,0,1,1,2,1), (1,0,1,0,2,1)]
    moves = [(0,3), (1,4), (3,0), (4,1)]
    assert states[0] == (1,2,1,0,0,1)
    adj = tuple(tuple(range(3, 6)) if v < 3 else tuple(range(3)) for v in range(6))
    ratios = []
    for k, state in enumerate(states):
        old, new = moves[k]
        next_state = states[(k + 1) % 4]
        assert state[old] != 0 and state[new] == 0
        changed = list(state)
        changed[new], changed[old] = changed[old], 0
        assert tuple(changed) == next_state
        ratios.append((local_fraction(state, old, adj),
                       local_fraction(next_state, new, adj)))
    assert ratios == [(Q(1), Q(2, 3)), (Q(1, 3), Q(1, 2)),
                      (Q(1), Q(2, 3)), (Q(1, 3), Q(1, 2))]
    for lam in (Q(401, 1000), Q(9, 20), Q(1, 2), Q(99, 100)):
        assert all(order_value(y, lam) > order_value(x, lam) for x,y in ratios)
    for lam in (Q(2, 5), Q(399, 1000), Q(1, 4)):
        assert not all(order_value(y, lam) > order_value(x, lam) for x,y in ratios)
    return ratios


def main():
    ratios = verify_explicit_witness()
    instances = profiles_checked = comparisons = 0
    counts = {}
    for n in range(3, 7):
        grid = all_peaks(n)
        run_count = 0
        for a in range(1, n//2 + 1):
            b = n - a
            for red in range(1, n-1):
                for blue in range(1, n-red):
                    empty = n - red - blue
                    assert empty >= 1
                    for lam in grid:
                        edges = state_edges(a, b, red, blue, lam)
                        cyclic = has_cycle(edges)
                        predicted = (a == b == 3 and
                                     sorted((red, blue)) == [1, 3] and
                                     empty == 2 and lam > CUTOFF)
                        assert cyclic == predicted, (
                            'Unexpected transition', n, a, b, red, blue, empty, lam, cyclic)
                        instances += 1
                        run_count += 1
                        profiles_checked += len(edges)
                        comparisons += sum(len(v) for v in edges.values())
        counts[n] = {'parameter_cases':run_count, 'peak_representatives':len(grid)}
    print('PASS: exact universal six-vertex classification')
    print('Per graph-size tests:',counts)
    print('Total graph/composition/peak instances:', instances)
    print('Total examined labeled-vertex color configurations:', profiles_checked)
    print('Total strictly improving state transitions:', comparisons)
    print('Witness fraction changes:',ratios)
    return counts

if __name__ == '__main__':
    main()
