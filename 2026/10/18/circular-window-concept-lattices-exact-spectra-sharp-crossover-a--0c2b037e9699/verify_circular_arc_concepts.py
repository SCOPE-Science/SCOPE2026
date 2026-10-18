"""Independent finite verification of circular-window formal-concept counts.

No external dependencies. Runs closure intersections, run-length word tests,
transfer-matrix traces and the cyclic-composition formula independently.
"""
from math import comb


def intersections(n, r):
    ell = n - r
    arcs = [sum(1 << ((s + j) % n) for j in range(ell))
            for s in range(n)]
    full = (1 << n) - 1
    family = {full}
    for arc in arcs:
        family |= {x & arc for x in tuple(family)}
    return family


def cyclic_run_family(n, r):
    full = (1 << n) - 1
    out = set()
    for c in range(1 << n):
        # c marks the complement of an intersection, i.e. the union of r-arcs.
        if c == 0 or c == full:
            out.add(full ^ c)
            continue
        valid = True
        for j in range(n):
            if c & (1 << j) and not c & (1 << ((j-1) % n)):
                length = 0
                while c & (1 << ((j + length) % n)):
                    length += 1
                if length < r:
                    valid = False
                    break
        if valid:
            out.add(full ^ c)
    return out


def trace_count(n, r):
    a = [[0] * (r + 1) for _ in range(r + 1)]
    a[0][0], a[0][1] = 1, 1
    for j in range(1, r):
        a[j][j+1] = 1
    a[r][r], a[r][0] = 1, 1
    total = 0
    for initial in range(r + 1):
        vec = [0] * (r + 1)
        vec[initial] = 1
        for _ in range(n):
            nxt = [0] * (r + 1)
            for i in range(r + 1):
                for j in range(r + 1):
                    nxt[j] += vec[i] * a[i][j]
            vec = nxt
        total += vec[initial]
    return total


def cyclic_comp_count(n, r):
    return 2 + sum(n * comb(n - k * (r - 1) - 1, 2 * k - 1) // k
                   for k in range(1, n // (r + 1) + 1))


def recurrence_count(n, r):
    a = [r + 1] + [2] * r
    for j in range(r + 1, n + 1):
        a.append(2*a[-1] - a[-2] + a[j-r-1])
    return a[n]


def main():
    checks = 0
    subsets_evaluated = 0
    for n in range(2, 12):
        values = []
        for r in range(1, n):
            by_intersection = intersections(n, r)
            by_runs = cyclic_run_family(n, r)
            assert by_intersection == by_runs, (n, r, by_intersection ^ by_runs)
            counts = (len(by_intersection), trace_count(n, r),
                      cyclic_comp_count(n, r), recurrence_count(n, r))
            assert len(set(counts)) == 1, (n, r, counts)
            values.append(counts[0])
            checks += 1
            subsets_evaluated += 1 << n
        assert all(x > y for x, y in zip(values, values[1:])), (n, values)
    print(f'VERIFY_OK parameter_pairs={checks} independent_bit_patterns={subsets_evaluated} '
          'n=2..11 exact_intersections=PASS cyclic_runs=PASS transfer_trace=PASS '
          'composition=PASS recurrence=PASS fixed_n_strict_inverse=PASS')
    for n in (6, 8, 10):
        print(f'n={n}:', [len(intersections(n, r)) for r in range(1, n)])


if __name__ == '__main__':
    main()

# Optional exhaustive small-lattice modularity verification. It is intentionally
# independent of the formula for the count, relying only on intersections.
def modularity_census():
    cases = 0
    for n in range(3, 8):
        full = (1 << n) - 1
        for r in range(1, n):
            closed = sorted(intersections(n, r))
            join = {}
            for x in closed:
                for y in closed:
                    joined = x | y
                    minimal = full
                    for v in closed:
                        if (v & joined) == joined:
                            minimal &= v
                    join[x, y] = minimal
            modular = True
            for x in closed:
                for z in closed:
                    if x & z != x:
                        continue
                    for y in closed:
                        if join[x, y & z] != (join[x, y] & z):
                            modular = False
                            break
                    if not modular:
                        break
                if not modular:
                    break
            assert modular == (r == 1 or n-r == 1), (n, r, modular)
            cases += 1
    print(f'MODULARITY_OK cases={cases} n=3..7 criterion=(arc_length=1 or complement_length=1)')

if __name__ == '__main__':
    modularity_census()
