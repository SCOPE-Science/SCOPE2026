"""Exact finite checks for weight-three, scale-two Boolean Rips complexes.

Requires Python 3 standard library only. Enumerates all faces and all coordinate
permutations for dimensions three through six; checks the predicted rational
character through the signed Lefschetz identity. Separately checks the local
vertex-link graph fold and line-graph model in dimensions three through seven.
"""
from itertools import combinations, permutations
from math import comb


def vertices(n, k=3):
    return [v for v in range(1 << n) if v.bit_count() <= k]


def cliques(n):
    vs = vertices(n)
    neighbors = {v: {w for w in vs if v != w and (v ^ w).bit_count() <= 2}
                 for v in vs}
    out = [()]

    def grow(face, options):
        for pos, v in enumerate(options):
            newface = face + (v,)
            out.append(newface)
            grow(newface, [w for w in options[pos+1:] if w in neighbors[v]])

    grow((), vs)
    return out


def permute_mask(v, perm):
    return sum(1 << perm[i] for i in range(len(perm)) if v >> i & 1)


def permutation_sign(indices):
    return (-1) ** sum(indices[i] > indices[j] for i in range(len(indices))
                       for j in range(i+1, len(indices)))


def exterior_character(perm):
    n = len(perm)
    seen = set()
    poly = [1] + [0] * n
    for i in range(n):
        if i in seen:
            continue
        length, j = 0, i
        while j not in seen:
            seen.add(j)
            j = perm[j]
            length += 1
        new = poly[:]
        factor = -(-1) ** length
        for d in range(n-length+1):
            new[d+length] += factor * poly[d]
        poly = new
    return poly[3] + (poly[4] if n >= 4 else 0)


def homology_character(faces, perm):
    # Reduced Lefschetz: empty simplex contributes -1.
    lef = -1
    action = {v: permute_mask(v, perm) for face in faces for v in face}
    for face in faces[1:]:
        mapped = [action[v] for v in face]
        if set(mapped) != set(face):
            continue
        positions = {v: i for i, v in enumerate(face)}
        lef += (-1) ** (len(face) - 1) * permutation_sign([positions[v] for v in mapped])
    return -lef  # only reduced H_3, by the uniform wedge proof


def neighbors_of_triple(n, T):
    return [u for u in range(1 << n)
            if (u.bit_count() <= 2 or (u.bit_count() == 3 and u < T))
            and u != T and (u ^ T).bit_count() <= 2]


def verify_local_link(n, T):
    a, b, c = [i for i in range(n) if T >> i & 1]
    vs = neighbors_of_triple(n, T)
    # Simpler exact selection: triples U obtained by swapping a higher than a.
    deleted = [u for u in vs if u.bit_count() == 3 and (u & ~T).bit_length()-1 > a]
    retained = [u for u in vs if u not in deleted]
    assert len(retained) == 3 * (a + 1) + 3
    adj = lambda u, v: (u ^ v).bit_count() <= 2
    for u in deleted:
        # Closed neighborhoods of removed vertices lie in that of singleton a.
        assert adj(u, 1 << a)
        assert all(adj(w, 1 << a) for w in vs if adj(u, w))
    # Model K_3 joined to an independent set of a+1 vertices: its line graph.
    # The three K_3 vertices index pairs ab,ac,bc; outside vertices are 0..a.
    pairs = [(a, b), (a, c), (b, c)]
    mapping = {}
    for row, (i, j) in enumerate(pairs):
        pairmask = (1 << i) | (1 << j)
        assert pairmask in retained
        mapping[pairmask] = (row, 0)
        for t in range(a):
            tripmask = pairmask | (1 << t)
            assert tripmask in retained
            mapping[tripmask] = (row, t + 1)
    # Assign three singletons to K_3's three internal edges between rows.
    mapping[1 << a] = ('inner', 0, 1)
    mapping[1 << b] = ('inner', 0, 2)
    mapping[1 << c] = ('inner', 1, 2)
    assert len(mapping) == len(retained)

    def endpoints(token):
        if token[0] == 'inner':
            return {('row', token[1]), ('row', token[2])}
        return {('row', token[0]), ('col', token[1])}

    for v, w in combinations(retained, 2):
        assert adj(v, w) == bool(endpoints(mapping[v]) & endpoints(mapping[w]))
    return a + 1


def main():
    for n in range(3, 7):
        faces = cliques(n)
        all_perms = list(permutations(range(n)))
        for perm in all_perms:
            actual = homology_character(faces, perm)
            expected = exterior_character(perm)
            assert actual == expected, (n, perm, actual, expected)
        print('character', n, 'vertices', len(vertices(n)),
              'faces', len(faces), 'permutations', len(all_perms), 'OK')
    for n in range(3, 8):
        total = 0
        for T in range(1 << n):
            if T.bit_count() != 3:
                continue
            total += verify_local_link(n, T)
        assert total == comb(n+1, 4)
        print('links', n, 'triples', comb(n, 3), 'sphere_count', total, 'OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
