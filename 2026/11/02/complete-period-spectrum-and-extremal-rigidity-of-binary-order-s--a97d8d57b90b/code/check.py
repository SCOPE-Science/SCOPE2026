#!/usr/bin/env python3
"""Exact exhaustive enumeration of cyclic binary order-seven orientable words.

A seven-window is the directed edge from its six-symbol prefix to its
six-symbol suffix.  The DFS visits all directed closed walks whose edges
contain at most one element from each reversal pair and no palindrome.
Every closed walk is normalized under rotation, so different start vertices
and initial phases cannot introduce distinct classes of the same word.
There are 56 nonpalindromic reversal pairs, which makes the search finite.
"""
from collections import Counter, defaultdict
from hashlib import sha256
from pathlib import Path

N = 7
BASE = Path(__file__).resolve().parent.parent
EXPECTED = {
    6: 2, 7: 4, 8: 12, 9: 12, 10: 12, 11: 12,
    12: 20, 13: 24, 14: 22, 15: 28, 16: 44,
    17: 48, 18: 78, 19: 100, 20: 138, 21: 144,
    22: 160, 23: 168, 24: 232, 25: 200,
    26: 268, 27: 248, 28: 444, 29: 224,
    30: 656, 32: 352, 33: 352, 34: 448,
    36: 336,
}

def reverse_bits(x):
    return int(f'{x:07b}'[::-1], 2)

def necklace(w):
    return min(w[t:] + w[:t] for t in range(len(w)))

def complement(w):
    return w.translate(str.maketrans('01', '10'))

def cyclic_counts(w, length):
    loop = w + w[:length-1]
    return Counter(loop[i:i+length] for i in range(len(w)))

def is_orientable(w):
    windows = cyclic_counts(w, N)
    if any(k == k[::-1] or c != 1 for k,c in windows.items()):
        return False
    return not any(k[::-1] in windows for k in windows)

# Distinct reversal-pairs of seven-bit words.  This is constructed
# independently of the C++ enumeration's numeric reverse and root rule.
reversal_pairs = sorted({tuple(sorted((z, reverse_bits(z))))
                         for z in range(1 << N) if z != reverse_bits(z)})
assert len(reversal_pairs) == 56
which_pair = {z: i for i, pair in enumerate(reversal_pairs) for z in pair}
found = defaultdict(set)
rooted = Counter()
calls = 0

def walk(state, start, used, bits):
    global calls
    calls += 1
    # The 56-bit mask guarantees that the recursion terminates.
    for symbol in ('0','1'):
        edge = (state << 1) | int(symbol)
        if edge not in which_pair:
            continue
        one = 1 << which_pair[edge]
        if used & one:
            continue
        nxt = edge & 63
        extension = bits + symbol
        if nxt == start:
            found[len(extension)].add(necklace(extension))
            rooted[len(extension)] += 1
        walk(nxt, start, used | one, extension)

for state in range(64):
    walk(state, state, 0, '')

assert {k:len(v) for k,v in found.items()} == EXPECTED
assert sum(len(v) for v in found.values()) == 4788
assert max(found) == 36
assert all(is_orientable(w) for words in found.values() for w in words)

maximal = found[36]
assert len(maximal) == 336
certificate = (BASE / 'certificates/maximum_necklaces.txt').read_text(encoding='utf-8')
assert certificate.endswith('\n')
assert certificate.splitlines() == sorted(maximal)
assert len({w for w in certificate.splitlines()}) == 336

assert all(w.count('1') == 18 for w in maximal)
assert all(sum(w[j] != w[j-1] for j in range(len(w))) == 20 for w in maximal)
expected_trigrams = {'000':3, '111':3, '001':5, '010':5, '011':5,
                     '100':5, '101':5, '110':5}
assert all(cyclic_counts(w, 3) == expected_trigrams for w in maximal)
assert all(cyclic_counts(w, 2) == {'00':8, '11':8, '01':10, '10':10}
           for w in maximal)

# Complementation and reversal act on rotational classes and commute.
seen = set()
orbits = Counter()
for w in sorted(maximal):
    orbit = {necklace(x) for x in (w, w[::-1], complement(w),
                                 complement(w)[::-1])}
    assert orbit <= maximal
    if w in seen: continue
    seen.update(orbit)
    orbits[len(orbit)] += 1
assert seen == maximal
assert orbits == {2:12, 4:78}
fix_complement = sum(necklace(complement(w)) == w for w in maximal)
fix_reversal = sum(necklace(w[::-1]) == w for w in maximal)
fix_reverse_complement = sum(necklace(complement(w)[::-1]) == w for w in maximal)
assert (fix_complement, fix_reversal, fix_reverse_complement) == (0, 0, 24)
assert (len(maximal)+fix_complement+fix_reversal+fix_reverse_complement)//4 == 90

print('CHECK_OK: every cyclic closed trail enumerated without length pruning')
print('NONPALINDROMIC_REVERSAL_PAIRS:',len(reversal_pairs))
print('DFS_STATES:',calls)
print('PERIOD_COUNTS:',','.join(f'{k}:{v}' for k,v in sorted(EXPECTED.items())))
print('TOTAL_ROTATION_CLASSES:',sum(map(len,found.values())))
print('MAX_PERIOD:',max(found))
print('MAX_ROTATION_CLASSES:',len(maximal))
print('MAX_ROOTED_WALKS:',rooted[36])
print('MAX_WEIGHT:',18)
print('MAX_CYCLIC_RUNS:',20)
print('MAX_3GRAM_PROFILE:',','.join(f'{k}:{v}' for k,v in sorted(expected_trigrams.items())))
print('COMPLEMENT_REVERSAL_ORBITS: 90 = 78 of size 4 + 12 of size 2')
print('FIXED_C,R,RC:',fix_complement,fix_reversal,fix_reverse_complement)
print('MAX_CERTIFICATE_SHA256:',sha256(certificate.encode('utf-8')).hexdigest())
