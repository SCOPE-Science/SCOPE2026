"""Independent cyclic-word state count and bichromatic-component calculation."""
from collections import Counter
from itertools import product
import json


def run(n):
    # Diagonal-coloring case: top and bottom cycles receive the same word.
    hist = Counter()
    all_words = 0
    for word in product(range(3), repeat=n):
        if any(word[i] == word[(i + 1) % n] for i in range(n)):
            continue
        all_words += 1
        number_used = len(set(word))
        components = n + (2 if number_used == 2 else 0)
        hist[components - 3] += 1
    # Off-diagonal-coloring case: one spoke color, with the other two
    # alternating in opposite orders around the two rims.
    if n % 2 == 0:
        hist[1] += 6
    assert all_words == 2 ** n + 2 * (-1) ** n
    assert all(v % 6 == 0 for v in hist.values())
    unlabeled = {str(degree): count // 6 for degree, count in sorted(hist.items())}
    assert sum(hist.values()) // 6 == ((2 ** n - 2) // 6 if n % 2 else (2 ** n + 8) // 6)
    return {'n': n, 'normalized_coloring_count': sum(hist.values()) // 6, 'degree_multiplicities': unlabeled}


def main():
    print(json.dumps({'method': 'independent cyclic-word enumeration and component formula', 'cases': [run(n) for n in range(3, 13)]}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
