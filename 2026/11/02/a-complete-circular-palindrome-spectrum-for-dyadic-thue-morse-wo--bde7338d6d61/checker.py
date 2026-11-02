"""Independent finite checks for circular palindrome and antipalindrome recurrences.

Only bounded ranks are enumerated; the all-rank result relies on the proof.
Run: python checker.py
"""
from collections import defaultdict


def morphism(w):
    return "".join("01" if c == "0" else "10" for c in w)


def cyclic_spectra(w):
    n = len(w)
    doubled = w + w
    pal, anti = defaultdict(set), defaultdict(set)
    trans = str.maketrans("01", "10")
    for length in range(1, n + 1):
        for start in range(n):
            fragment = doubled[start:start + length]
            if fragment == fragment[::-1]:
                pal[length].add(fragment)
            if fragment == fragment[::-1].translate(trans):
                anti[length].add(fragment)
    return {i: len(v) for i, v in pal.items()}, {i: len(v) for i, v in anti.items()}


def expected_total(rank):
    if rank % 2:
        return (4 * (2 ** rank) + 4) // 3
    return (7 * (2 ** rank) + 8) // 6


def check():
    word = "0"
    spectra = {}
    for rank in range(1, 10):
        word = morphism(word)
        p, a = cyclic_spectra(word)
        spectra[rank] = (p, a)
        n = len(word)
        assert not any(word[i % n] == word[(i + 1) % n] == word[(i + 2) % n]
                       for i in range(n))
        if rank >= 3:
            doubled = word * 3
            assert not any(doubled[i:i+5] == doubled[i:i+5][::-1]
                           for i in range(n))
        assert all(l % 2 == 0 for l in a)
        if rank >= 2:
            assert sum(p.values()) == expected_total(rank), (rank, p)
        if rank >= 3:
            prev_p, prev_a = spectra[rank - 1]
            assert p.get(1, 0) == 2 and p.get(3, 0) == 2
            assert all(p.get(j, 0) == 0 for j in range(5, n + 1, 2))
            for t in range(1, n // 2 + 1):
                source_length = t + (t % 2)
                assert p.get(2 * t, 0) == prev_a.get(source_length, 0), (
                    rank, 2 * t, 'P', p.get(2*t,0), prev_a.get(source_length,0))
                assert a.get(2 * t, 0) == (prev_p.get(t, 0)
                                          + prev_p.get(t + 1, 0)
                                          - (2 if t == 1 else 0)), (
                    rank, 2 * t, 'A', a.get(2*t,0),
                    prev_p.get(t,0), prev_p.get(t+1,0))
            assert sum(p.values()) == 4 + 2 * sum(prev_a.values())
            assert sum(a.values()) == 2 * sum(prev_p.values()) - 4
        print(f"rank={rank:2d} length={n:4d} pal={sum(p.values()):4d} anti={sum(a.values()):4d} verified")
    print('all finite checks passed; unbounded ranks require the symbolic proof')


if __name__ == '__main__':
    check()
