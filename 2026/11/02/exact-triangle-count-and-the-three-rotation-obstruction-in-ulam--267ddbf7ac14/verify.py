"""Independent exhaustive finite checks for the Ulam one-deletion triangle theorem.

All adjacency tests compare literal single-symbol deletion reads. The proof
of the infinite formula is in RESULT.md; finite checks are corroboration.
"""
from itertools import combinations, permutations
from math import comb, factorial


def remove_symbol(word, symbol):
    return tuple(a for a in word if a != symbol)


def deletion_neighbor(u, v):
    return u != v and any(remove_symbol(u, x) == remove_symbol(v, x) for x in u)


def neighbors_by_move(word):
    result = set()
    for i in range(len(word)):
        for j in range(len(word)):
            if i != j:
                a = list(word)
                z = a.pop(i)
                a.insert(j, z)
                result.add(tuple(a))
    return result


def rotations_at(word, start):
    a, b, c = word[start:start + 3]
    left = word[:start] + (b, c, a) + word[start + 3:]
    right = word[:start] + (c, a, b) + word[start + 3:]
    return {word, left, right}


def classify_triangle(u, v, w):
    common = [x for x in u if remove_symbol(u, x) == remove_symbol(v, x) == remove_symbol(w, x)]
    rotated = [i for i in range(len(u) - 2) if {u, v, w} == rotations_at(u, i)]
    if len(common) == 1 and not rotated:
        return 'shared_read'
    if len(common) == 0 and len(rotated) == 1:
        return 'rotation'
    raise AssertionError((u, v, w, common, rotated))


def check_at_vertex(word):
    n = len(word)
    adj = sorted(neighbors_by_move(word))
    assert len(adj) == (n - 1)**2, (n, word, len(adj))
    shared = exceptional = 0
    for v, w in combinations(adj, 2):
        if deletion_neighbor(v, w):
            kind = classify_triangle(word, v, w)
            if kind == 'shared_read':
                shared += 1
            else:
                exceptional += 1
    assert shared == n * comb(n - 1, 2), (word, shared)
    assert exceptional == n - 2, (word, exceptional)
    total = shared + exceptional
    assert total == (n - 2)*(n*n - n + 2)//2
    return total


def main():
    total_vertices = 0
    for n in range(2, 7):
        counts = [check_at_vertex(p) for p in permutations(range(n))]
        assert len(counts) == factorial(n)
        triangle_instances = sum(counts)
        assert triangle_instances % 3 == 0
        observed = triangle_instances // 3
        expected = factorial(n) * (n - 2) * (n*n - n + 2) // 6
        assert observed == expected, (n, observed, expected)
        total_vertices += len(counts)
        print(f'full n={n}, vertices={factorial(n)}, triangles={observed}')
    for n in range(7, 15):
        word = tuple(range(n))
        c = check_at_vertex(word)
        print(f'local n={n}, degree={(n-1)**2}, triangles_at_vertex={c}')
    print(f'VERIFY_OK full_vertices={total_vertices} local_orders=7..14')

if __name__ == '__main__':
    main()
