"""Reproducible finite sanity checks for three labeled particles on radial trees.

The all-parameter theorem in RESULT.md is proved symbolically; the finite
cubical computations here are corroboration, not extrapolation.
Standard library only. Run with Python 3.10+.
"""
from collections import defaultdict, deque
from itertools import combinations
from math import factorial

N_PARTICLES = 3
ARM_LENGTH_EDGES = 3


def star_cells(m):
    """Atoms (closed vertex or edge, dimension) of the subdivided radial tree."""
    vertices = [(0, 0)] + [(arm, j) for arm in range(1, m+1) for j in range(1, 4)]
    vertex_id = {v: i for i, v in enumerate(vertices)}
    edges = []
    for arm in range(1, m+1):
        edges.append((vertex_id[(0, 0)], vertex_id[(arm, 1)]))
        edges.extend((vertex_id[(arm, j)], vertex_id[(arm, j+1)]) for j in (1, 2))
    atoms = [(frozenset([v]), 0) for v in range(len(vertices))]
    atoms += [(frozenset(e), 1) for e in edges]
    reverse = {c: i for i, c in enumerate(atoms)}
    return vertices, atoms, reverse


def valid_cells(atoms):
    """All product cubes whose three closed cell supports are disjoint."""
    n = len(atoms)
    # Precalculate conflicts before the direct triple enumeration.
    disjoint = [[not (atoms[i][0] & atoms[j][0]) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if not disjoint[i][j]:
                continue
            for k in range(n):
                if disjoint[i][k] and disjoint[j][k]:
                    yield (i, j, k)


def arm_permutations_representatives(m):
    """Generate a cycle representative of every partition of m."""
    def partitions(n, maximum):
        if n == 0:
            yield ()
        else:
            for k in range(min(maximum, n), 0, -1):
                for rest in partitions(n - k, k):
                    yield (k,) + rest

    for parts in partitions(m, m):
        sigma = list(range(m+1))
        c = 1
        for length in parts:
            for i in range(length):
                sigma[c+i] = c+(i+1) % length
            c += length
        yield parts, tuple(sigma)


def counts(sigma):
    seen = set()
    out = defaultdict(int)
    for arm in range(1, len(sigma)):
        if arm in seen:
            continue
        j = arm
        length = 0
        while j not in seen:
            seen.add(j)
            length += 1
            j = sigma[j]
        out[length] += 1
    return out


def predicted_trace(sigma, tau):
    c = counts(sigma)
    if tau == (0, 1, 2):
        f = c[1]
        return -f*(f+1)*(2*f-5)
    if tau == (1, 0, 2):
        return 2*c[2]
    if tau == (1, 2, 0):
        return 3*c[3]
    raise AssertionError('unexpected label permutation')


def direct_trace(sigma, tau, vertices, atoms, reverse, cubes):
    vm = [vertices.index((sigma[a], d) if d else (0, 0)) for a, d in vertices]
    image = [reverse[(frozenset(vm[v] for v in support), d)] for support,d in atoms]
    result = 0
    fixed_count = [0]*4
    for cube in cubes:
        moved = [None]*3
        for i in range(3):
            moved[tau[i]] = image[cube[i]]
        if tuple(moved) != cube:
            continue
        edge_coords = [i for i in range(3) if atoms[cube[i]][1] == 1]
        dim = len(edge_coords)
        parity = sum(tau[edge_coords[i]] > tau[edge_coords[j]]
                     for i in range(dim) for j in range(i+1,dim))
        result += (-1)**(dim+parity)
        fixed_count[dim] += 1
    return result, fixed_count


def check_connected(m, atoms, cubes):
    # Build the 1-skeleton from cubes containing one open edge and two vertices.
    # The two endpoints must be legal product 0-cells because all supports are disjoint.
    cell_to_vertex = {next(iter(support)): i for i,(support,d) in enumerate(atoms) if d == 0}
    nodes = set()
    adjacency = defaultdict(set)
    for c in cubes:
        d = sum(atoms[i][1] for i in c)
        if d == 0:
            nodes.add(c)
        elif d == 1:
            epos = next(p for p in range(3) if atoms[c[p]][1])
            a,b = tuple(sorted(atoms[c[epos]][0]))
            endpoints = []
            for v in (a,b):
                u = list(c)
                u[epos] = cell_to_vertex[v]
                endpoints.append(tuple(u))
            left,right = endpoints
            adjacency[left].add(right)
            adjacency[right].add(left)
    if not nodes:
        return 0
    root = next(iter(nodes))
    seen = {root}
    queue = deque([root])
    while queue:
        for other in adjacency[queue.popleft()]:
            if other not in seen:
                seen.add(other)
                queue.append(other)
    assert seen == nodes, (m,len(seen),len(nodes))
    return len(nodes)


def main():
    tau_reps = [(0,1,2), (1,0,2), (1,2,0)]
    case_count = 0
    for m in (3,4,5):
        vertices,atoms,reverse = star_cells(m)
        cubes = tuple(valid_cells(atoms))
        cell_counts = [0]*4
        for cube in cubes:
            cell_counts[sum(atoms[i][1] for i in cube)] += 1
        euler = sum((-1)**i*x for i,x in enumerate(cell_counts))
        expected = -m*(m+1)*(2*m-5)
        assert euler == expected, (m,cell_counts,euler,expected)
        n0 = check_connected(m, atoms, cubes)
        assert n0 == cell_counts[0]
        for parts,sigma in arm_permutations_representatives(m):
            for tau in tau_reps:
                trace,fixed_count = direct_trace(sigma,tau,vertices,atoms,reverse,cubes)
                expected = predicted_trace(sigma,tau)
                assert trace == expected, (m,parts,tau,trace,expected,fixed_count)
                case_count += 1
        print('m=%d cubes=%s Euler=%d H1_rank=%d conjugacy_cases=%d'%(
            m,cell_counts,euler,1-euler,
            sum(1 for _ in arm_permutations_representatives(m))*3))
    assert case_count == 3*(3+5+7), case_count
    print('STAR_TRIPLE_JOINT_CHARACTER_OK cases=%d'%case_count)

if __name__ == '__main__':
    main()
