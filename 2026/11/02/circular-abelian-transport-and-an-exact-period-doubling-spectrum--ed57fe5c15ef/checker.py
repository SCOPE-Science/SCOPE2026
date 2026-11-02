"""Direct finite checks for the circular Abelian transport theorem.

This independent enumeration checks only bounded inputs; the proof is mathematical.
"""
from itertools import product


def profile(word):
    n = len(word)
    assert n > 0
    doubled = word + word
    prefix = [0]
    for symbol in doubled:
        prefix.append(prefix[-1] + symbol)
    lower, upper, number = [0], [0], [1]
    for length in range(1, n + 1):
        counts = [prefix[start + length] - prefix[start] for start in range(n)]
        a, b = min(counts), max(counts)
        assert sorted(set(counts)) == list(range(a, b + 1))
        lower.append(a)
        upper.append(b)
        number.append(b - a + 1)
    return lower, upper, number


def substitute(word):
    return tuple(v for symbol in word for v in (0, 1 - symbol))


def check_transport(word):
    n = len(word)
    lo, hi, count = profile(word)
    new = substitute(word)
    ln, un, cn = profile(new)
    for m in range(1, n + 1):
        assert ln[2 * m] == m - hi[m]
        assert un[2 * m] == m - lo[m]
        assert cn[2 * m] == count[m]
    for r in range(n):
        assert ln[2 * r + 1] == r - hi[r]
        assert un[2 * r + 1] == r + 1 - lo[r + 1]
        assert cn[2 * r + 1] == count[r] + 1 - lo[r + 1] + lo[r]
    assert sum(cn[1:]) == 2 * sum(count[1:]) + n - sum(word)


def main():
    cases = 0
    for n in range(1, 9):
        for w in product((0, 1), repeat=n):
            check_transport(w)
            cases += 1
    word = (0,)
    totals = []
    for k in range(12):
        lo, hi, count = profile(word)
        total = sum(count[1:])
        totals.append(total)
        assert len(word) == 2 ** k
        assert sum(word) == (2 ** k - (-1) ** k) // 3
        assert total == ((3 * k + 10) * 2 ** k - (-1) ** k) // 9
        if k < 11:
            check_transport(word)
            word = substitute(word)
    assert totals[:11] == [1, 3, 7, 17, 39, 89, 199, 441, 967, 2105, 4551]
    print(f"PASS: {cases} exhaustive binary input words; 12 complete period-doubling spectra")


if __name__ == "__main__":
    main()
