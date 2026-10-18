"""Complete first-uncovered-vertex branching for optimal open-neighborhood covers.
Run with Python 3.8 or newer; requires only the standard library.
"""
from itertools import combinations
triples = [sum(1 << k for k in c) for c in combinations(range(1, 8), 3) if c[0] ^ c[1] ^ c[2]]
assert len(triples) == 28
neighbors = [sum(1 << j for j in range(28) if i != j and not(triples[i] & triples[j])) for i in range(28)]
assert all(mask.bit_count() == 3 for mask in neighbors)
all_vertices = (1 << 28) - 1
solutions = set()
calls = 0

def explore(selected, covered):
    global calls
    calls += 1
    if covered == all_vertices:
        if selected.bit_count() == 10:
            solutions.add(selected)
        return
    remaining = 10 - selected.bit_count()
    if remaining == 0 or (all_vertices ^ covered).bit_count() > 3 * remaining:
        return
    first_uncovered = ((all_vertices ^ covered) & -(all_vertices ^ covered)).bit_length() - 1
    options = neighbors[first_uncovered]
    while options:
        vbit = options & -options
        options -= vbit
        v = vbit.bit_length() - 1
        explore(selected | vbit, covered | neighbors[v])

explore(0, 0)
assert len(solutions) == 28
print('branch_states=', calls, sep='')
print('minimum_masks=', ','.join(map(str, sorted(solutions))), sep='')
print('BRANCH_CERTIFICATE_OK')
