"""Exact finite cross-check for the weighted four-cycle retraction theorem.

Runs over four vertices of {0,1}^2 with weighted Hamming distance,
enumerating every vertex ordering rooted at 0 and all commuting prefix maps.
This corroborates, but does not replace, the symbolic lower-bound table.
"""
from fractions import Fraction
from itertools import permutations, product

V = tuple(range(4))

def distance(u, v, a, b):
    return (a if (u ^ v) & 1 else 0) + (b if (u ^ v) & 2 else 0)

def lip(image, a, b):
    return max(Fraction(distance(image[u], image[v], a, b), distance(u, v, a, b))
               for u in V for v in V if u != v)

def exact_constant(a, b):
    a, b = Fraction(a), Fraction(b)
    assert 0 < a <= b
    best = None
    best_certificate = None
    checked = 0
    for second, third, fourth in permutations((1, 2, 3)):
        for img_third, img_fourth in product((0, second), repeat=2):
            p2 = [0] * 4
            p2[second] = second
            p2[third] = img_third
            p2[fourth] = img_fourth
            for img_fourth3 in (0, second, third):
                p3 = list(V)
                p3[fourth] = img_fourth3
                if any(p2[p3[v]] != p2[v] for v in V):
                    continue
                candidate = max(lip(p2, a, b), lip(p3, a, b))
                checked += 1
                if best is None or candidate < best:
                    best = candidate
                    best_certificate = (second, third, fourth, tuple(p2), tuple(p3))
    return best, best_certificate, checked

def check():
    tests = 0
    evaluations = 0
    examples = []
    for a in range(1, 21):
        for b in range(a, 21):
            exact, cert, checked = exact_constant(a, b)
            predicted = min(Fraction(b, a), Fraction(a + b, b))
            assert exact == predicted, (a, b, exact, predicted)
            evaluations += checked
            tests += 1
            if (a, b) in ((1, 1), (3, 4), (2, 3), (1, 2), (1, 5)):
                examples.append((a, b, str(exact), cert))
    for a, b in ((Fraction(2, 7), Fraction(3, 5)),
                 (Fraction(13, 17), Fraction(20, 17))):
        exact, _, checked = exact_constant(a, b)
        assert exact == min(b/a, 1+a/b)
        tests += 1
        evaluations += checked
    print(f'PASS {tests} weight pairs, {evaluations} commuting filtration candidates')
    for row in examples:
        print('sample', row)

if __name__ == '__main__':
    check()
