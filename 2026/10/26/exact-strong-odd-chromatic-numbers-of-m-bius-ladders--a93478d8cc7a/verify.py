"""Finite reproducibility checks for Möbius-ladder strong odd chromatic numbers.

The unbounded cases are established by the accompanying mathematical proof;
these checks do not purport to enumerate infinitely many graphs.
"""
from collections import Counter

BASE = ((0, 1), (2, 3), (1, 0), (3, 2))
TAIL = ((2, 4), (1, 0), (4, 3), (0, 2), (3, 4), (2, 1), (4, 3))
SIX = ((0, 2), (3, 1), (4, 0), (1, 3),
       (2, 4), (3, 0), (4, 2), (5, 1))


def neighbours(n):
    assert n >= 3
    return [tuple(sorted({(i - 1) % (2*n), (i + 1) % (2*n),
                          (i + n) % (2*n)})) for i in range(2*n)]


def color(n):
    if n & 1:
        return [i % 2 for i in range(2*n)]
    if n % 4 == 2:
        return [i % 4 for i in range(2*n)]
    if n == 4:
        return list(range(8))
    if n == 8:
        pairs = SIX
    else:
        assert n >= 12 and n % 4 == 0
        pairs = (BASE * ((n-7+3)//4))[:n-7] + TAIL
    assert len(pairs) == n
    return [a for a,b in pairs] + [b for a,b in pairs]


def check(n, colors, square=False):
    N = neighbours(n)
    assert len(colors) == 2*n
    for v in range(2*n):
        assert colors[v] not in {colors[w] for w in N[v]}
        counts = Counter(colors[w] for w in N[v])
        assert all(c % 2 for c in counts.values())
        if square:
            D = set(N[v])
            for u in N[v]: D.update(N[u])
            D.discard(v)
            assert all(colors[v] != colors[w] for w in D)


def odd_independent_sets(n):
    N = [sum(1 << u for u in r) for r in neighbours(n)]
    good = []
    def go(chosen, undecided):
        if any((nb & chosen).bit_count() == 2 and not (nb & undecided)
               for nb in N):
            return
        if not undecided:
            if chosen: good.append(chosen)
            return
        one = undecided & -undecided
        v = one.bit_length()-1
        go(chosen, undecided ^ one)
        if not (N[v] & chosen):
            go(chosen | one, undecided ^ one)
    go(0, (1 << (2*n))-1)
    return good


def main():
    for n in range(3, 301):
        c = color(n)
        expected = (2 if n%2 else 4 if n%4==2 else
                    8 if n==4 else 6 if n==8 else 5)
        assert len(set(c)) == expected, (n, expected, len(set(c)))
        check(n, c, square=(n%2==0))
    print('Constructive strong-odd checks: all 3 <= n <= 300 PASS')
    for n, mx, ct in [(4,1,8),(6,3,40),(8,3,128),(12,5,1496)]:
        good = odd_independent_sets(n)
        assert len(good) == ct
        assert max(s.bit_count() for s in good) == mx
        for s in good:
            rungs = {i % n for i in range(2*n) if (s >> i) & 1}
            assert all((i+1) % n not in rungs for i in rungs)
        print(f'Exhaustive color classes n={n}: {ct} valid, max size {mx}, no adjacent rungs')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
