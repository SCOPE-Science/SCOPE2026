"""Independent finite checks for isolated-rooted-forest homology characters.

Run: python3 verify.py
Only Python standard library is required.
"""
from itertools import product
from collections import defaultdict
from math import comb


def directed_forests(m):
    """Enumerate parent functions of rooted oriented forests on [m]."""
    choices = [[-1] + [u for u in range(m) if u != v] for v in range(m)]
    for parent in product(*choices):
        good = True
        for start in range(m):
            seen = set()
            cur = start
            while parent[cur] != -1:
                if cur in seen:
                    good = False
                    break
                seen.add(cur)
                cur = parent[cur]
            if not good:
                break
        if good:
            yield frozenset((parent[v], v) for v in range(m) if parent[v] >= 0)


def has_isolate(edges, m):
    incident = set()
    for u, v in edges:
        incident.add(u)
        incident.add(v)
    return len(incident) < m


def sign_of_permutation(indices):
    return -1 if sum(indices[i] > indices[j]
                     for i in range(len(indices))
                     for j in range(i+1, len(indices))) % 2 else 1


def direct_character(m, permutation):
    alt = 0
    for edges in directed_forests(m):
        if not has_isolate(edges, m):
            continue
        ordered = sorted(edges)
        image = [(permutation[a], permutation[b]) for a, b in ordered]
        if set(image) != edges:
            continue
        where = {edge: j for j, edge in enumerate(ordered)}
        sign = sign_of_permutation([where[e] for e in image])
        alt += (-1)**len(edges) * sign
    return (-1)**(m-2) * alt


def determinant(a):
    n = len(a)
    if not n:
        return 1
    b = [list(row) for row in a]
    previous_pivot, sign = 1, 1
    for k in range(n-1):
        if b[k][k] == 0:
            swap = next((i for i in range(k+1, n) if b[i][k] != 0), None)
            if swap is None:
                return 0
            b[k], b[swap] = b[swap], b[k]
            sign = -sign
        pivot = b[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = b[i][j]*pivot - b[i][k]*b[k][j]
                assert numerator % previous_pivot == 0
                b[i][j] = numerator // previous_pivot
        for i in range(k+1,n):
            b[i][k] = 0
        previous_pivot = pivot
    return sign*b[-1][-1]


def cycle_determinant_character(lengths):
    """Character via determinants on the cycle-orbit directed-divisor graph."""
    k, m = len(lengths), sum(lengths)
    total = 0
    for forced_isolates in range(1, 1 << k):
        remaining = [i for i in range(k) if not (forced_isolates >> i & 1)]
        matrix = [[0] * len(remaining) for _ in remaining]
        for row, i in enumerate(remaining):
            for col, j in enumerate(remaining):
                if i != j and lengths[i] % lengths[j] == 0:
                    matrix[row][row] -= lengths[j]
                    matrix[row][col] += lengths[j]
        for i in range(len(remaining)):
            matrix[i][i] += 1
        total += (-1)**(forced_isolates.bit_count()+1) * determinant(matrix)
    return (-1)**(m-2) * total


def permutation_of_cycles(lengths):
    ans = []
    offset = 0
    for length in lengths:
        ans.extend(offset + ((j+1) % length) for j in range(length))
        offset += length
    return tuple(ans)


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None:
        maximum = n
    for first in range(min(n, maximum), 0, -1):
        for rest in partitions(n-first, first):
            yield (first,) + rest


def mod2_rank(columns):
    pivot = {}
    for value in columns:
        while value:
            b = value.bit_length() - 1
            if b not in pivot:
                pivot[b] = value
                break
            value ^= pivot[b]
    return len(pivot)


def homology_mod2(m):
    faces = list(edges for edges in directed_forests(m)
                 if has_isolate(edges, m))
    bydim = defaultdict(list)
    for face in faces:
        bydim[len(face)-1].append(tuple(sorted(face)))
    rank = {}
    for dim in range(0, m-1):
        rows = {face:i for i,face in enumerate(bydim[dim-1])} if dim else {():0}
        columns = []
        for face in bydim[dim]:
            value=0
            if dim == 0:
                value=1
            else:
                for j in range(len(face)):
                    value ^= 1 << rows[face[:j]+face[j+1:]]
            columns.append(value)
        rank[dim]=mod2_rank(columns)
    return {dim:len(faces)-rank[dim]-rank.get(dim+1,0)
            for dim,faces in bydim.items() if dim>=0}


def dimension_formula(m):
    return m-1 + sum(comb(m,j)*(j-1)**(j-1) for j in range(2,m))


def run():
    cases = 0
    for m in range(3,7):
        for cycle_lengths in partitions(m):
            permutation = permutation_of_cycles(cycle_lengths)
            got = direct_character(m, permutation)
            expected = cycle_determinant_character(cycle_lengths)
            assert got == expected, (m,cycle_lengths,got,expected)
            cases += 1
        assert cycle_determinant_character((1,)*m) == dimension_formula(m)
    for cycle_lengths in [(7,), (4,3), (2,2,2,1), (3,2,1,1)]:
        got = direct_character(7, permutation_of_cycles(cycle_lengths))
        expected = cycle_determinant_character(cycle_lengths)
        assert got == expected,(7,cycle_lengths,got,expected)
        cases += 1
    for m in range(3,6):
        ranks = homology_mod2(m)
        assert ranks.get(m-3) == dimension_formula(m),(m,ranks)
        assert all(v==0 for i,v in ranks.items() if i!=m-3),(m,ranks)
    print('VERIFY_OK', 'character_cases', cases, 'homology_cases',3)
    for m in (4,5,6):
        print('example',m, 'identity',cycle_determinant_character((1,)*m),
              'transposition',cycle_determinant_character((2,)+(1,)*(m-2)),
              'full_cycle',cycle_determinant_character((m,)))

if __name__ == '__main__':
    run()
