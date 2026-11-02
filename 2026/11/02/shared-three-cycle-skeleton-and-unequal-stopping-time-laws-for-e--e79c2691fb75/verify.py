"""Finite-state proof certificate for three-state excitation on triangle bouquets.

Run with Python 3.10 or newer; only the standard library is used.
"""
from collections import Counter
from itertools import product
from math import comb

PAIRS = [(a, b) for a in range(3) for b in range(3)]


def local_update(model, x, neighbours):
    if model == 'CCA':
        return (x + 1) % 3 if (x + 1) % 3 in neighbours else x
    assert model == 'GHM'
    return 1 if x == 0 and 1 in neighbours else ((x + 1) % 3 if x != 0 else 0)


def symbolic_image(model, center, mask, t):
    """Exact t-th image of the center and EVERY initially represented pair type.

    A mask describes the set of initial ordered types that occur at least once.
    Multiplicity never affects contact updates, so all n-tuples with that
    support have precisely the same center and type trajectories.
    """
    present = tuple(i for i in range(9) if mask & (1 << i))
    current = {i: PAIRS[i] for i in present}
    for _ in range(t):
        old_center = center
        leaf_colors = set(z for i in present for z in current[i])
        center = local_update(model, old_center, leaf_colors)
        nxt = {}
        for i in present:
            a, b = current[i]
            nxt[i] = (local_update(model, a, (b, old_center)),
                      local_update(model, b, (a, old_center)))
        current = nxt
    return center, tuple(current[i] for i in present)


def catalytic(center, mask):
    return any(mask & (1 << i) and set(PAIRS[i]) == set(range(3)) - {center}
               for i in range(9))


def onto(s, n):
    return sum((-1) ** j * comb(s, j) * (s - j) ** n
               for j in range(s + 1))


def desired(model, n):
    if model == 'CCA':
        return [3 * 3 ** n, 3 * 6 ** n,
                3 * (9 ** n - 6 ** n - 3 ** n)]
    return [3 ** (n + 1) - 2,
            6 ** n + 4 ** n - 3 ** n,
            9 ** n - 3 ** n + 1,
            9 ** n - 4 ** n + 1,
            9 ** n - 6 ** n - 3 ** n]


def certificate():
    size_by_time = {}
    periodic_by_model = {}
    for model, bound in [('CCA', 2), ('GHM', 4)]:
        bytime = [Counter() for _ in range(bound + 1)]
        periodic = set()
        for c in range(3):
            for mask in range(1, 1 << 9):
                z = [symbolic_image(model, c, mask, t)
                     for t in range(bound + 4)]
                assert z[bound] == z[bound + 3], (model, c, mask)
                t = next(t for t in range(bound + 1)
                         if z[t] == z[t + 3])
                bytime[t][mask.bit_count()] += 1
                expected = catalytic(c, mask)
                assert (z[bound] != z[bound + 1]) == expected
                for s in [0, 1, 2]:
                    if z[0] == z[3] and z[0] != z[1]:
                        # Every n-tuple using these types is already periodic.
                        assert mask.bit_count() <= 3
                if z[0] == z[3] and z[0] != z[1]:
                    periodic.add((c, mask))
        size_by_time[model] = bytime
        periodic_by_model[model] = periodic
        for n in range(1, 10):
            counts = [sum(a * onto(s, n) for s, a in row.items())
                      for row in bytime]
            assert counts == desired(model, n), (model, n, counts)
            assert sum(counts) == 3 * 9 ** n
        print(model, 'support profiles', sum(sum(v.values()) for v in bytime),
              'by time', [sum(v.values()) for v in bytime])
        print(model, 'first-entry counts n=3:', desired(model, 3))
    assert periodic_by_model['CCA'] == periodic_by_model['GHM']
    # Stronger: the maps have exactly the same action on each periodic type.
    for c, mask in periodic_by_model['CCA']:
        assert symbolic_image('CCA', c, mask, 1) == symbolic_image('GHM', c, mask, 1)
    # All period-three images use the per-petal set of exactly three types,
    # with at least one unsynchronized ordered type.
    for c in range(3):
        admissible = {3 * ((c + 1) % 3) + ((c + 2) % 3),
                      3 * ((c + 2) % 3) + ((c + 1) % 3),
                      3 * ((c + 2) % 3) + ((c + 2) % 3)}
        catalyst_types = admissible - {3 * ((c + 2) % 3) + ((c + 2) % 3)}
        for mask in range(1, 512):
            actual = (c, mask) in periodic_by_model['CCA']
            expected = all(i in admissible for i in range(9) if mask & (1 << i)) \
                and any(mask & (1 << i) for i in catalyst_types)
            assert actual == expected
    print('COMMON_PERIODIC_CYCLES_EXACT')


def independent_vertex_check():
    """Separate vertex-neighborhood implementation, not using symbolic_image."""
    for n in range(1, 6):
        neighbors = []
        for v in range(2 * n + 1):
            if v == 0:
                neighbors.append(tuple(range(1, 2 * n + 1)))
            else:
                neighbors.append((0, v + 1 if v % 2 else v - 1))
        assert all(0 <= v < 2 * n + 1 for row in neighbors for v in row)
        for model in ['CCA', 'GHM']:
            counts = Counter()
            periodic = set()
            for state in product(range(3), repeat=2 * n + 1):
                trajectory = [state]
                horizon = 7 if model == 'GHM' else 5
                for _ in range(horizon):
                    old = trajectory[-1]
                    nxt = []
                    for v in range(2 * n + 1):
                        a = old[v]
                        adj = {old[w] for w in neighbors[v]}
                        if model == 'CCA':
                            b = (a + 1) % 3 if ((a + 1) % 3) in adj else a
                        elif a == 1:
                            b = 2
                        elif a == 2:
                            b = 0
                        else:
                            b = 1 if 1 in adj else 0
                        nxt.append(b)
                    trajectory.append(tuple(nxt))
                bound = 4 if model == 'GHM' else 2
                assert trajectory[bound] == trajectory[bound + 3]
                t = next(j for j in range(bound + 1)
                         if trajectory[j] == trajectory[j + 3])
                counts[t] += 1
                if trajectory[0] == trajectory[3] and trajectory[0] != trajectory[1]:
                    periodic.add(state)
                center = state[0]
                is_catalytic = any({state[2 * j + 1], state[2 * j + 2]}
                                   == set(range(3)) - {center} for j in range(n))
                assert (trajectory[bound] != trajectory[bound + 1]) == is_catalytic
            assert [counts[t] for t in range(bound + 1)] == desired(model, n)
            assert len(periodic) == 3 ** (n + 1) - 3
            if model == 'CCA':
                c_set = periodic
            else:
                assert periodic == c_set
            print('n', n, model, 'states', 3 ** (2 * n + 1),
                  'time counts', [counts[t] for t in range(bound + 1)])


if __name__ == '__main__':
    certificate()
    independent_vertex_check()
    print('TRIANGLE_BOUQUET_EXCITATION_VERIFY_OK')
