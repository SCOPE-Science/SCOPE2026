from collections import Counter
from itertools import product


def rank_mod(matrix, q):
    a = [[x % q for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col] % q), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, q)
        a[rank] = [(inv * x) % q for x in a[rank]]
        for i in range(rows):
            if i != rank and a[i][col] % q:
                factor = a[i][col] % q
                a[i] = [
                    (a[i][j] - factor * a[rank][j]) % q
                    for j in range(cols)
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def linear_codewords(generator, q):
    k = len(generator)
    n = len(generator[0])
    words = []
    for coeffs in product(range(q), repeat=k):
        words.append(
            tuple(
                sum(coeffs[i] * generator[i][j] for i in range(k)) % q
                for j in range(n)
            )
        )
    return words


def weight(word):
    return sum(x != 0 for x in word)


def minimum_distance(words):
    nonzero = [weight(w) for w in words if any(w)]
    return min(nonzero)


def projected_code(words, view):
    return {tuple(w[i] for i in view) for w in words}


def verify_locality(words, n, r, delta, views_by_coordinate):
    assert set(views_by_coordinate) == set(range(n))
    for i, view in views_by_coordinate.items():
        assert i in view
        assert len(view) <= r + delta - 1
        projected = projected_code(words, view)
        assert len(projected) >= 2
        assert minimum_distance(projected) >= delta


G14 = [
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
]

groups14 = [
    (0, 12, 13),
    (1, 4, 7),
    (2, 5, 9),
    (2, 6, 10),
    (3, 8, 11),
]
views14 = {}
for group in groups14:
    for coordinate in group:
        views14.setdefault(coordinate, group)

words14 = linear_codewords(G14, 2)
assert rank_mod(G14, 2) == 7
assert len(words14) == 128
assert minimum_distance(words14) == 4
assert Counter(map(weight, words14)) == Counter({
    0: 1, 4: 16, 5: 12, 6: 18, 7: 24, 8: 23, 9: 28, 10: 6
})
verify_locality(words14, 14, 2, 2, views14)


G15 = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
]
groups15 = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (9, 10, 11),
    (12, 13, 14),
]
views15 = {}
for group in groups15:
    for coordinate in group:
        views15[coordinate] = group

words15 = linear_codewords(G15, 2)
assert rank_mod(G15, 2) == 4
assert len(words15) == 16
assert minimum_distance(words15) == 6
assert Counter(map(weight, words15)) == Counter({0: 1, 6: 10, 12: 5})
verify_locality(words15, 15, 1, 3, views15)


G7 = [
    [1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1],
]
views7 = {
    0: (0, 1, 2),
    1: (0, 1, 2),
    2: (0, 1, 2),
    3: (3, 4, 5),
    4: (3, 4, 5),
    5: (3, 4, 5),
    6: (4, 5, 6),
}

words7 = linear_codewords(G7, 3)
assert rank_mod(G7, 3) == 2
assert len(words7) == 9
assert minimum_distance(words7) == 3
assert Counter(map(weight, words7)) == Counter({0: 1, 3: 2, 4: 2, 7: 4})
verify_locality(words7, 7, 1, 3, views7)


assert 1359968 / 8555 < 2 ** 8
assert 15 // 3 == 5 and 2 ** 5 // 2 == 16
assert 7 // 3 == 2 and 3 ** 2 == 9

print("binary [14,7,4]: all-symbol (2,2) locality verified")
print("binary [15,4,6]: all-symbol (1,3) locality verified")
print("ternary [7,2,3]: all-symbol (1,3) locality verified")
print("all checks passed")
