from collections import Counter
from math import comb


def brute(a, b, t):
    vertex_count = a + b
    neighbors = [0] * vertex_count
    for i in range(a):
        for j in range(b):
            if i == j and i < t:
                continue
            neighbors[i] |= 1 << (a + j)
            neighbors[a + j] |= 1 << i

    def is_dissociation(mask):
        for v in range(vertex_count):
            if (mask >> v) & 1 and (neighbors[v] & mask).bit_count() > 1:
                return False
        return True

    faces, facets = Counter(), Counter()
    for mask in range(1 << vertex_count):
        if not is_dissociation(mask):
            continue
        faces[mask.bit_count()] += 1
        if all(not is_dissociation(mask | (1 << v))
               for v in range(vertex_count) if not (mask >> v) & 1):
            facets[mask.bit_count()] += 1
    return faces, facets


def formulas(a, b, t):
    faces = Counter()
    facets = Counter()
    for j in range(a + 1):
        faces[j] += comb(a, j)
    for j in range(b + 1):
        faces[j] += comb(b, j)
    faces[0] -= 1
    faces[2] += a * b
    faces[3] += t * (a + b - 2)
    faces[4] += comb(t, 2)
    facets[a] += 1
    facets[b] += 1
    facets[2] += (a - t) * (b - t)
    facets[3] += t * (a + b - 2 * t)
    facets[4] += comb(t, 2)
    return faces, facets


profiles = 0
vertex_subsets = 0
for a in range(3, 7):
    for b in range(3, 7):
        for t in range(min(a, b) + 1):
            profiles += 1
            vertex_subsets += 1 << (a + b)
            calculated = brute(a, b, t)
            predicted = formulas(a, b, t)
            assert calculated == predicted, (a, b, t, calculated, predicted)

print(f'VERIFICATION_OK profiles={profiles} vertex_subsets={vertex_subsets}')
