from collections import Counter

# Complete census of unordered perfect matchings of F_2^4.  Vertices are
# the integers 0,...,15, and vector addition is bitwise XOR.
counts = Counter()

def matchings(mask, diffs):
    if mask == 0:
        counts[tuple(sorted(diffs))] += 1
        return
    low = mask & -mask
    i = low.bit_length() - 1
    rest = mask ^ low
    x = rest
    while x:
        bit = x & -x
        j = bit.bit_length() - 1
        matchings(rest ^ bit, diffs + (i ^ j,))
        x ^= bit

matchings((1 << 16) - 1, ())
assert sum(counts.values()) == 2027025  # 15!!

# Independent census of all multisets of eight nonzero differences whose
# XOR sum is zero.  A nondecreasing tuple is a canonical multiset encoding.
admissible = []
def profiles(lo, left, xor_sum, values):
    if left == 0:
        if xor_sum == 0:
            admissible.append(tuple(values))
        return
    for v in range(lo, 16):
        profiles(v, left - 1, xor_sum ^ v, values + [v])

profiles(1, 8, 0, [])
assert len(admissible) == 20295
assert set(admissible) == set(counts)

expected = {
    1: 15, 4: 210, 6: 105, 12: 1365, 16: 735, 24: 420,
    32: 1890, 40: 840, 48: 840, 64: 3360, 88: 105, 96: 3360,
    128: 2520, 160: 1575, 224: 2520, 384: 435,
}
histogram = Counter(counts.values())
assert histogram == expected
unique = [profile for profile, multiplicity in counts.items() if multiplicity == 1]
assert len(unique) == 15
assert all(len(set(profile)) == 1 for profile in unique)
assert min(m for p, m in counts.items() if len(set(p)) > 1) == 4

print('MATCHINGS', sum(counts.values()))
print('ADMISSIBLE_PROFILES', len(admissible))
print('MULTIPLICITY_HISTOGRAM', sorted(histogram.items()))
print('UNIQUE_CONSTANT_PROFILES', len(unique))
print('VERIFY_OK')
