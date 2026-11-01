"""Complete orbit-face enumeration for the action of S_7 on Ind(KG(7,3)).

For each conjugacy class, enumerate every invariant simplex exactly once and
compute the reduced signed Lefschetz number directly. No homology routine or
previous tabulation is used.
"""
from itertools import combinations
from collections import Counter


def partitions(total, minimum=1):
    if total == 0:
        yield ()
    for x in range(minimum, total + 1):
        for rest in partitions(total - x, x):
            yield (x,) + rest


def permutation(cycle_lengths):
    n = sum(cycle_lengths)
    perm = list(range(n))
    offset = 0
    for cycle in cycle_lengths:
        for j in range(cycle):
            perm[offset + j] = offset + (j + 1) % cycle
        offset += cycle
    return tuple(perm)


def lefschetz_by_faces(cycle_lengths):
    pi = permutation(cycle_lengths)
    vertices = [tuple(t) for t in combinations(range(7), 3)]
    index = {v: i for i, v in enumerate(vertices)}
    vperm = [index[tuple(sorted(pi[j] for j in v))] for v in vertices]
    seen = set()
    vertex_orbits = []
    for i in range(len(vertices)):
        if i in seen:
            continue
        orbit = []
        j = i
        while j not in seen:
            seen.add(j)
            orbit.append(j)
            j = vperm[j]
        vertex_orbits.append(tuple(orbit))

    # An invariant simplex is a union of complete vertex orbits.
    compatible_orbits = []
    for orbit in vertex_orbits:
        if all(set(vertices[a]) & set(vertices[b])
               for a,b in combinations(orbit, 2)):
            compatible_orbits.append(orbit)
    full = len(compatible_orbits)
    can_add = [[True]*full for _ in range(full)]
    for i in range(full):
        for j in range(i + 1, full):
            can_add[i][j] = all(set(vertices[a]) & set(vertices[b])
                                for a in compatible_orbits[i]
                                for b in compatible_orbits[j])
    tally = Counter()
    def visit(i, chosen, number_vertices):
        if i == full:
            tally[(len(chosen), number_vertices)] += 1
            return
        visit(i + 1, chosen, number_vertices)
        if all(can_add[j][i] for j in chosen):
            visit(i + 1, chosen + [i], number_vertices + len(compatible_orbits[i]))
    visit(0, [], 0)
    # For a fixed oriented simplex, the sign of the vertex permutation is
    # (-1)^(N-c), where N=number of vertices and c=number of vertex orbits.
    # Including the empty simplex gives reduced Lefschetz=-sum (-1)^c.
    number = -sum((-1)**c * count for (c,N),count in tally.items())
    return number, sum(tally.values()), len(vertex_orbits), len(compatible_orbits)

if __name__ == '__main__':
    EXPECTED={
      (1,1,1,1,1,1,1):22,(1,1,1,1,1,2):6,
      (1,1,1,1,3):-5,(1,1,1,2,2):2,
      (1,1,1,4):4,(1,1,2,3):3,(1,1,5):-3,
      (1,2,2,2):2,(1,2,4):0,(1,3,3):4,(1,6):2,
      (2,2,3):-1,(2,5):1,(3,4):1,(7,):1}
    for p in partitions(7):
        value, count, all_orbits, valid = lefschetz_by_faces(p)
        assert value == EXPECTED[p], (p, value)
        print('%-25s Lefschetz=%3d  invariant_faces=%8d  orbits=%2d valid=%2d' % (str(p), value, count, all_orbits,valid))
    print('PASS: all 15 conjugacy classes verified by exhaustive invariant-face enumeration.')
