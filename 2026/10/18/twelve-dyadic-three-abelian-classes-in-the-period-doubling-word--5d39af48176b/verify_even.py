from collections import Counter
from itertools import product


def image(word, j):
    for _ in range(j):
        word = ''.join('01' if c == '0' else '00' for c in word)
    return word


patterns = [''.join(p) for k in (1, 2, 3) for p in product('01', repeat=k)]
lengths = sorted(set(range(4, 130, 2)) | {256, 512})
for n in lengths:
    j = (n-1).bit_length()
    factors = set()
    for pair in ('00', '01', '10'):
        word = image(pair, j)
        factors.update(word[i:i+n] for i in range(len(word)-n+1))
    signatures = set()
    for word in factors:
        counts = Counter(word[i:i+k] for k in (1, 2, 3) for i in range(n-k+1))
        signatures.add(((word.count('1'), word[:2], word[-2:]),
                        tuple(counts[p] for p in patterns)))
    assert len(signatures) == len({x for x, _ in signatures})
    assert len(signatures) == len({y for _, y in signatures})
print('Exact equivalence check at', len(lengths), 'even lengths')
