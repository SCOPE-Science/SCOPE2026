"""Exhaustive certificate for minimum overlap-free binary square products.

Run with Python 3 using only the standard library. All strings are ordinary
binary words; square factors are nonempty, and their order matters.
"""
from collections import defaultdict

LIMIT = 48
MAX_FACTORS = 9
EXPECTED_MIN = (2, 4, 6, 8, 14, 16, 18, 24, 48)
EXPECTED_COUNT = (2, 2, 2, 2, 6, 4, 2, 8, 2)
WITNESS = "001001101001011010011001011001101001011010011011"


def no_new_overlap(s):
    """For overlap-free s[:-1], detect every newly created terminal axaxa."""
    n = len(s)
    for p in range(1, (n - 1) // 2 + 1):
        if s[n - 2*p - 1:n - p] == s[n - p - 1:n]:
            return False
    return True


def global_overlap_free(s):
    """Separate all-start-position test, including nonterminal overlaps."""
    n = len(s)
    for start in range(n):
        for p in range(1, (n - start - 1) // 2 + 1):
            if s[start:start+p+1] == s[start+p:start+2*p+1]:
                return False
    return True


def factor_counts(s):
    """Number of ordered square-factorizations for every k <= MAX_FACTORS."""
    n = len(s)
    f = [[0] * (MAX_FACTORS + 1) for _ in range(n + 1)]
    f[0][0] = 1
    for end in range(2, n + 1, 2):
        for half in range(1, end // 2 + 1):
            before = end - 2 * half
            if s[before:before+half] == s[before+half:end]:
                for k in range(1, MAX_FACTORS + 1):
                    f[end][k] += f[before][k-1]
    return f[n]


def complement(w):
    return w.translate(str.maketrans("01", "10"))


def method_all_words():
    layer = [""]
    found = {}
    all_squares = set()
    nine = {}
    counts_per_length = [1]
    for n in range(1, LIMIT + 1):
        next_layer = []
        for w in layer:
            for b in "01":
                t = w + b
                fast = no_new_overlap(t)
                slow = global_overlap_free(t)
                assert fast == slow, (t, fast, slow)
                if slow:
                    next_layer.append(t)
        layer = next_layer
        counts_per_length.append(len(layer))
        if n % 2:
            continue
        for w in layer:
            c = factor_counts(w)
            if c[1] and c[1] > 0:
                all_squares.add(w)
            for k in range(1, MAX_FACTORS + 1):
                if c[k] > 0:
                    if k not in found:
                        found[k] = [n, 0, 0, 0]
                    if found[k][0] == n:
                        found[k][1] += 1
                        found[k][2] += c[k]
                        found[k][3] = max(found[k][3], c[k])
                    if k == 9:
                        nine[w] = c[k]
    assert tuple(found[k][0] for k in range(1,10)) == EXPECTED_MIN
    assert tuple(found[k][1] for k in range(1,10)) == EXPECTED_COUNT
    assert all(found[k][2] == found[k][1] and found[k][3] == 1 for k in range(1,10))
    assert nine == {WITNESS:1, complement(WITNESS):1}
    assert len(counts_per_length) == LIMIT + 1 and counts_per_length[-1] == 416
    return found, all_squares, nine, counts_per_length


def method_square_breadth_first(squares):
    """Independent state generation by appending complete square blocks."""
    layer = {"": 1}
    found = {}
    for k in range(1, MAX_FACTORS + 1):
        new_layer = defaultdict(int)
        for w, mult in layer.items():
            for block in squares:
                if len(w) + len(block) > LIMIT:
                    continue
                t = w + block
                if global_overlap_free(t):
                    new_layer[t] += mult
        layer = dict(new_layer)
        assert layer, k
        m = min(map(len, layer))
        min_layer = {w:count for w,count in layer.items() if len(w) == m}
        found[k] = (m, len(min_layer), sum(min_layer.values()), max(min_layer.values()))
        if k == 9:
            assert min_layer == {WITNESS:1, complement(WITNESS):1}
    return found


def main():
    found, squares, nine, count = method_all_words()
    independent = method_square_breadth_first(sorted(squares))
    for k in range(1, MAX_FACTORS + 1):
        assert independent[k] == tuple(found[k]), (k,independent[k],found[k])
    print("All overlap-free binary words of lengths 0..48 enumerated by two overlap predicates.")
    print("Length-48 count:", count[-1])
    print("Overlap-free squares of length <=48:", len(squares))
    print("k | minimum_length | minimum_words | minimum_factorizations | maximum_factorizations_per_word")
    for k in range(1, 10):
        print(k, *found[k], sep=" | ")
    print("Nine-square minimizers, each with exactly one nine-square factorization:")
    for w in sorted(nine):
        print(w)
    print("INDEPENDENT_BFS_AGREEMENT: PASS")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
