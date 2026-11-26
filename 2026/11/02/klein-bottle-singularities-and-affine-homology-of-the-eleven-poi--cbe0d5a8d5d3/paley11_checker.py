"""Exhaust the Paley-11 flag complex and verify its link certificate."""

from collections import Counter
from itertools import combinations


VERTICES = tuple(range(11))
RESIDUES = {1, 3, 4, 5, 9}


def transitive(face):
    remaining = list(face)
    while remaining:
        source = next((u for u in remaining
                       if all(u == v or (v - u) % 11 in RESIDUES
                              for v in remaining)), None)
        if source is None:
            return False
        remaining.remove(source)
    return True


def incidences(faces):
    return Counter(subface for face in faces
                   for subface in combinations(face, len(face) - 1))


def connected(nodes, adjacent):
    unseen = set(nodes)
    if not unseen:
        return False
    stack = [unseen.pop()]
    while stack:
        node = stack.pop()
        neighbors = {other for other in unseen if adjacent(node, other)}
        unseen.difference_update(neighbors)
        stack.extend(neighbors)
    return not unseen


def connected_dual(faces):
    return connected(faces, lambda a, b: len(set(a) & set(b)) == len(a) - 1)


def decode(word):
    return tuple(int(c, 11) for c in word)


def main():
    faces = {d: {face for face in combinations(VERTICES, d) if transitive(face)}
             for d in range(1, 6)}
    assert tuple(len(faces[d]) for d in range(1, 6)) == (11, 55, 110, 55, 0)
    assert set(incidences(faces[2])) == faces[1]
    assert set(incidences(faces[3])) == faces[2]
    triangle_degrees = incidences(faces[4])
    assert set(triangle_degrees) == faces[3]
    assert set(triangle_degrees.values()) == {2}
    assert connected_dual(faces[4])

    link = {d: {face[1:] for face in faces[d+1] if face[0] == 0}
            for d in range(1, 4)}
    expected = set(map(decode, ('134 139 145 157 178 189 235 23a 257 267 '
                                '268 28a 34a 359 459 469 46a 67a 689 78a').split()))
    assert link[3] == expected
    assert tuple(len(link[d]) for d in range(1, 4)) == (10, 30, 20)
    edge_degrees = incidences(link[3])
    assert set(edge_degrees) == link[2]
    assert set(edge_degrees.values()) == {2}
    assert connected_dual(link[3])

    for (v,) in link[1]:
        neighbors = {next(u for u in edge if u != v) for edge in link[2] if v in edge}
        edges = {tuple(u for u in face if u != v) for face in link[3] if v in face}
        assert len(neighbors) == 6
        assert Counter(u for edge in edges for u in edge) == Counter({u: 2 for u in neighbors})
        assert connected(neighbors, lambda a, b: tuple(sorted((a, b))) in edges)

    walk = list(map(decode, '268 267 257 157 178 189 689 268'.split()))
    signs = []
    for a, b in zip(walk, walk[1:]):
        assert a in link[3] and b in link[3]
        common = set(a) & set(b)
        assert len(common) == 2
        i = next(i for i, u in enumerate(a) if u not in common)
        j = next(j for j, u in enumerate(b) if u not in common)
        signs.append((-1)**(i + j + 1))
    assert signs == [-1, -1, -1, 1, 1, -1, -1]
    assert signs.count(-1) % 2 == 1
    print('PALEY11_KLEIN_BOTTLE_LINKS_OK')


if __name__ == '__main__':
    main()
