"""Finite tests of the stated Lyndon-factor classification.

Run: python checker.py
This is a finite regression check, not the proof for unbounded ranks.
"""

def zimin(rank):
    value = ""
    for j in range(1, rank + 1):
        value = value + chr(96 + j) + value
    return value


def is_lyndon_by_suffix(word):
    return all(word < word[k:] for k in range(1, len(word)))


def is_lyndon_by_rotation(word):
    return all(word < word[k:] + word[:k] for k in range(1, len(word)))


def valuation_two(i):
    return (i & -i).bit_length() - 1


def run():
    for n in range(1, 10):
        word = zimin(n)
        all_distinct = set()
        observed_by_length = {}
        expected_by_length = {}
        total_occ = 0
        for end in range(1, len(word) + 1):
            rank = valuation_two(end) + 1
            observed = []
            for start in range(end):
                fragment = word[start:end]
                if is_lyndon_by_suffix(fragment):
                    observed.append(fragment)
                    all_distinct.add(fragment)
                    observed_by_length[len(fragment)] = observed_by_length.get(len(fragment), 0) + 1
            expected = [zimin(i - 1) + chr(96 + rank) for i in range(1, rank + 1)]
            assert set(observed) == set(expected), (n, end, observed, expected)
            assert len(observed) == rank
            total_occ += rank
        expected_factors = {zimin(i - 1) + chr(96 + j)
                            for i in range(1, n + 1) for j in range(i, n + 1)}
        assert all_distinct == expected_factors
        assert len(all_distinct) == n * (n + 1) // 2
        assert total_occ == 2 ** (n + 1) - n - 2
        for i in range(1, n + 1):
            length = 2 ** (i - 1)
            assert sum(len(x) == length for x in all_distinct) == n - i + 1
            assert observed_by_length[length] == 2 ** (n - i + 1) - 1
        assert set(observed_by_length) == {2 ** (i - 1) for i in range(1, n + 1)}
        if n <= 6:
            for fragment in all_distinct:
                assert is_lyndon_by_rotation(fragment), (n, fragment)
        print(f"rank={n}: length={len(word)} distinct={len(all_distinct)} occurrences={total_occ} passed")


if __name__ == "__main__":
    run()
