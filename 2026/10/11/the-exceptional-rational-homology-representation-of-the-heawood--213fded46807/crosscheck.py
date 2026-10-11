"""Second implementation: row matrices, oriented faces, exact GF(3) chains."""
from collections import Counter
from itertools import combinations

# Enumerate the Fano point-line graph by bilinear pairing.
def pairing(a, b):
    bits = a & b
    parity = 0
    while bits:
        bits &= bits-1
        parity ^= 1
    return parity

vertex_labels = [(0, k) for k in range(1, 8)] + [(1, k) for k in range(1, 8)]
incidences = {(i, j) for i, (kind_i, vec_i) in enumerate(vertex_labels)
              for j, (kind_j, vec_j) in enumerate(vertex_labels)
              if kind_i == 0 and kind_j == 1 and pairing(vec_i, vec_j) == 0}
assert len(incidences) == 21

simplices = {0: [()]}  # dimensions offset +1, including augmented empty face
for k in range(1, 9):
    simplices[k] = [t for t in combinations(range(14), k)
                    if all((u, v) not in incidences for u, v in combinations(t, 2))]
assert tuple(len(simplices[k]) for k in range(9)) == (1, 14, 70, 154, 147, 56, 14, 2, 0)

# Sparse modular Gaussian elimination on signed incidence matrices.
def rank_mod_prime(k, prime):
    rows = {simplex: pos for pos, simplex in enumerate(simplices[k-1])}
    reduced = {}
    for simplex in simplices[k]:
        column = {rows[simplex[:i] + simplex[i+1:]]: (1 if i % 2 == 0 else prime-1)
                  for i in range(k)}
        while column:
            pivot = max(column)
            value = column[pivot]
            if pivot in reduced:
                other = reduced[pivot]
                for j, coeff in other.items():
                    nval = (column.get(j, 0)-value*coeff) % prime
                    if nval:
                        column[j] = nval
                    else:
                        column.pop(j, None)
            else:
                inverse = pow(value, -1, prime)
                reduced[pivot] = {j: (coeff*inverse)%prime for j, coeff in column.items()}
                break
    return len(reduced)

ranks3 = [rank_mod_prime(k, 3) for k in range(2, 8)]
assert tuple(ranks3) == (13, 57, 97, 44, 12, 2), ranks3

# Enumerate invertible 3x3 matrices as triples of ROWS.
actions = []
for rows in ((a,b,c) for a in range(1,8) for b in range(1,8) for c in range(1,8)):
    def linear(v):
        return sum(pairing(v, row) << i for i, row in enumerate(rows))
    images = {v: linear(v) for v in range(1,8)}
    if set(images.values()) != set(range(1,8)):
        continue
    dual_action = {}
    for old_line in range(1, 8):
        possible = [new_line for new_line in range(1, 8)
                    if all(pairing(old_line, point)==pairing(new_line,images[point])
                           for point in range(1,8))]
        assert len(possible) == 1
        dual_action[old_line] = possible[0]
    perm = tuple([images[i]-1 for i in range(1,8)] +
                 [7+dual_action[i]-1 for i in range(1,8)])
    actions.append(perm)
assert len(actions)==168 and len(set(actions))==168

# Compute traces directly from oriented simplicial chain actions (not orbit-weight formula).
def permutation_order(perm):
    result = list(range(14))
    for step in range(1, 9):
        result = [perm[v] for v in result]
        if result == list(range(14)):
            return step
    raise AssertionError('unexpected group order')

char_counts=Counter()
for perm in actions:
    alternating_trace = -1  # augmented -1-chain, the empty simplex
    for k in range(1, 9):
        sign_dim = -1 if k % 2 == 0 else 1
        for simplex in simplices[k]:
            mapped = [perm[j] for j in simplex]
            if set(mapped) != set(simplex):
                continue
            inversions = sum(mapped[i] > mapped[j] for i in range(k) for j in range(i+1,k))
            alternating_trace += sign_dim * (-1 if inversions % 2 else 1)
    char_counts[(permutation_order(perm), -alternating_trace)] += 1
assert char_counts == Counter({(1,6):1,(2,-2):21,(3,0):56,(4,2):42,(7,-1):48})
print('CROSSCHECK_OK')
print('GF3 signed-boundary ranks:', ranks3)
print('direct oriented-simplicial-chain traces:', dict(sorted(char_counts.items())))
