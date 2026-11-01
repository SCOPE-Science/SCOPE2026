"""Reproducible finite-support certificate for five-color firefly dynamics on K_{a,b,c}."""
from itertools import product, permutations
from collections import Counter
from math import comb

K = 5
COLORS = range(K)
BLINK = 2


def support_step(state):
    result, maps = [], []
    for i, own in enumerate(state):
        external = 0
        for j, other in enumerate(state):
            if i != j:
                external |= other
        f = {}
        for color in COLORS:
            if (own >> color) & 1:
                f[color] = color if (color > BLINK and (external & (1 << BLINK))) else (color + 1) % K
        image = 0
        for val in f.values():
            image |= 1 << val
        result.append(image)
        maps.append(f)
    return tuple(result), maps


def all_cycles():
    seen, cycles, max_pre = set(), [], 0
    basin_periods = Counter()
    for initial in product(range(1, 1 << K), repeat=3):
        trajectory, state = {}, initial
        while state not in trajectory and state not in seen:
            trajectory[state] = len(trajectory)
            state = support_step(state)[0]
        if state in trajectory:
            circle = list(trajectory)[trajectory[state]:]
            cycles.append(circle)
        # For the basin and maximum-depth census, independently follow each state.
        visited, s = {}, initial
        while s not in visited:
            visited[s] = len(visited)
            s = support_step(s)[0]
        preperiod = visited[s]
        period = len(visited) - preperiod
        max_pre = max(max_pre, preperiod)
        basin_periods[period] += 1
        seen.update(trajectory)
    return cycles, max_pre, basin_periods


def permutation_order(f):
    g = dict(f)
    order = 1
    while any(g[c] != c for c in f):
        g = {c: f[g[c]] for c in f}
        order += 1
        assert order <= 120
    return order


def monodromy(cycle):
    orders = []
    for shore in range(3):
        colors = [c for c in COLORS if cycle[0][shore] & (1 << c)]
        mapping = {c: c for c in colors}
        for state in cycle:
            _, local = support_step(state)
            mapping = {c: local[shore][d] for c, d in mapping.items()}
        assert set(mapping) == set(colors)
        orders.append(permutation_order(mapping))
    return tuple(orders)


def q(n, r):
    return sum((-1) ** j * comb(r, j) * (r-j)**n for j in range(r+1))


def predicted_orbits_18(sizes):
    return sum(2**sizes[i] * q(sizes[j],3) * q(sizes[k],4)
               for i,j,k in permutations(range(3))) // 6


def main():
    cycles, maximum_preperiod, basins = all_cycles()
    class_sizes = Counter((len(c), monodromy(c)) for c in cycles)
    assert len(cycles) == 89, len(cycles)
    assert Counter(map(len, cycles)) == {1:27, 2:1, 3:20, 5:1, 6:40}
    assert basins == {1:27, 2:24, 3:60, 5:28684, 6:996}, basins
    assert maximum_preperiod == 40, maximum_preperiod
    assert class_sizes[(5,(1,1,1))] == 1
    assert class_sizes[(6,(1,1,1))] == 40
    assert sum(v for (length,orders),v in class_sizes.items() if length==3 and orders==(3,3,3)) == 2
    assert sum(v for (length,orders),v in class_sizes.items() if length==3 and sorted(orders)==[1,2,3]) == 18
    assert sum(v for (length,orders),v in class_sizes.items() if length==2 and orders==(3,3,3)) == 1
    assert sum(v for (length,orders),v in class_sizes.items() if length==1 and sorted(orders)==[1,1,5]) == 27
    all_micro_periods = set()
    for circle in cycles:
        length = len(circle)
        orders = monodromy(circle)
        from math import lcm
        all_micro_periods.add(length*lcm(*orders))
    assert all_micro_periods == {5,6,9,18}, all_micro_periods
    for sizes in [(1,3,4),(2,3,4),(1,4,4),(3,4,5),(4,4,4),(2,2,2)]:
        periodic_18_states = 0
        for circle in cycles:
            if len(circle) != 3 or sorted(monodromy(circle)) != [1,2,3]:
                continue
            m = 1
            for n, mask in zip(sizes, circle[0]):
                m *= q(n,mask.bit_count())
            periodic_18_states += len(circle)*m
        expected_orbits = predicted_orbits_18(sizes)
        assert periodic_18_states == 18*expected_orbits, (sizes,periodic_18_states,expected_orbits)
        print('sizes',sizes,'period18_orbits',expected_orbits,'period18_states',periodic_18_states)
    print('SUPPORT_CERTIFICATE_OK',len(cycles),maximum_preperiod,dict(sorted(basins.items())),dict(sorted(class_sizes.items())))

if __name__ == '__main__':
    main()
