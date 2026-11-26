"""Bounded checks of square-reduction counts by direct enumeration of words."""

from itertools import product


def reduction_outputs(word):
    n = len(word)
    return {
        word[:start + p] + word[start + 2 * p:]
        for start in range(n)
        for p in range(1, (n - start) // 2 + 1)
        if word[start:start + p] == word[start + p:start + 2 * p]
    }


def run_slots(word):
    n = len(word)
    slots = charge = 0
    for start in range(n):
        for end in range(start + 2, n + 1):
            factor = word[start:end]
            length = end - start
            for d in range(1, length // 2 + 1):
                if factor[:-d] == factor[d:]:
                    break
            else:
                continue
            if start > 0 and word[start - 1] == word[start + d - 1]:
                continue
            if end < n and word[end] == word[end - d]:
                continue
            slots += length // (2 * d)
            charge += length // d - 1
    return slots, charge


def main():
    counts = []
    for alphabet, max_n in [('01', 11), ('012', 7)]:
        checked = 0
        for n in range(1, max_n + 1):
            for chars in product(alphabet, repeat=n):
                word = ''.join(chars)
                slots, charge = run_slots(word)
                assert len(reduction_outputs(word)) == slots, word
                assert slots <= charge <= n - 1, word
                checked += 1
        counts.append(checked)
    assert reduction_outputs('00100') == {'0100', '0010'}
    print(f'CHECK_OK binary_words {counts[0]} ternary_words {counts[1]}')


if __name__ == '__main__':
    main()
