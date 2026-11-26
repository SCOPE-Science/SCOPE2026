"""Exact certificate for the palindrome saturation length of a binary fixed point."""
from bisect import bisect_left
from itertools import product

F = {'0': '010011', '1': '1001'}
PAIRS = tuple(''.join(p) for p in product('01', repeat=2))
COUNTS = (2,2,3,2,2,2,2,2,2,2,2,1,3,0,2,0,2,0,2,0,2,0,2,0,0)
MISSING = '01100101001110010100110'


def iterate(word, depth):
    for _ in range(depth):
        word = ''.join(F[c] for c in word)
    return word


def factors(word, n):
    return {word[j:j+n] for j in range(len(word)-n+1)}


assert F['0'].startswith('0') and factors(F['0'], 2) == set(PAIRS)
assert tuple(len(iterate(c, 3)) for c in '01') == (150, 100)
small = [iterate(p, 3) for p in PAIRS]
by_length = [{v for s in small for v in factors(s, n) if v == v[::-1]}
             for n in range(1, 26)]
assert tuple(map(len, by_length)) == COUNTS
palindromes = set().union(*by_length)
assert len(palindromes) == 37 and MISSING in palindromes
assert all(all(p in iterate(c, 3) for p in palindromes) for c in '01')

assert tuple(len(iterate(c, 4)) for c in '01') == (750, 500)
large = {p: iterate(p, 4) for p in PAIRS}
window_counts = []
for word in large.values():
    starts = len(word) - 172 + 1
    window_counts.append(starts)
    for p in sorted(palindromes):
        positions = [j for j in range(len(word)-len(p)+1) if word.startswith(p,j)]
        for j in range(starts):
            k = bisect_left(positions, j)
            assert k < len(positions) and positions[k]+len(p) <= j+172
assert window_counts == [1329, 1079, 1079, 829]

witness = large['00'][325:325+171]
assert len(witness) == 171 and MISSING not in witness
print('palindromes=37; window counts=1329,1079,1079,829; witness=00:325:171; threshold=172')
