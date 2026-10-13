from collections import Counter

D = 4
NV = 1 << D
VERTICES = list(range(NV))
EDGES = [(v, v ^ (1 << j)) for v in VERTICES for j in range(D) if v < (v ^ (1 << j))]
assert len(EDGES) == 32
ADJ = [0] * NV
for a, b in EDGES:
    ADJ[a] |= 1 << b
    ADJ[b] |= 1 << a


def connected(mask: int) -> bool:
    if mask == 0:
        return False
    seen = mask & -mask
    frontier = seen
    while frontier:
        bit = frontier & -frontier
        frontier -= bit
        v = bit.bit_length() - 1
        new = ADJ[v] & mask & ~seen
        seen |= new
        frontier |= new
    return seen == mask


def codeword(mask: int) -> int:
    # Coordinates 0..15 are the identity block; 16..47 are edge incidences.
    c = mask
    for j, (a, b) in enumerate(EDGES):
        if ((mask >> a) ^ (mask >> b)) & 1:
            c |= 1 << (NV + j)
    return c

CODE = [codeword(m) for m in range(1 << NV)]

# Method 1: classify by connected induced vertex sets and tally codeword weights.
connected_masks = []
weight_spectrum = Counter()
size_spectrum = Counter()
size_edges = Counter()
for m in range(1, 1 << NV):
    if connected(m):
        connected_masks.append(m)
        k = m.bit_count()
        internal = sum(1 for a, b in EDGES if ((m >> a) & 1) and ((m >> b) & 1))
        w_formula = 5 * k - 2 * internal
        w_direct = CODE[m].bit_count()
        assert w_formula == w_direct
        weight_spectrum[w_direct] += 1
        size_spectrum[k] += 1
        size_edges[(k, internal)] += 1

# Method 2: test minimality directly from support containment, independently of connectivity.
# Because the first 16 code coordinates equal the message indicator, any support-contained
# nonzero codeword must correspond to a nonempty submask of the message mask.
direct_minimal = []
for m in range(1, 1 << NV):
    cm = CODE[m]
    s = (m - 1) & m
    is_min = True
    while s:
        if CODE[s] & ~cm == 0:
            is_min = False
            break
        s = (s - 1) & m
    if is_min:
        direct_minimal.append(m)

assert direct_minimal == connected_masks

EXPECTED_WEIGHT = {
    5:16, 8:32, 11:96, 12:24, 14:256, 15:192, 16:105, 17:656,
    18:704, 19:704, 20:2072, 21:2640, 22:2584, 23:4752, 24:5992,
    25:5040, 26:4800, 27:3520, 28:1556, 29:1024, 30:480, 31:48,
}
EXPECTED_SIZE = {
    1:16, 2:32, 3:96, 4:280, 5:784, 6:1952, 7:4304, 8:7280,
    9:8720, 10:7136, 11:4192, 12:1804, 13:560, 14:120, 15:16, 16:1,
}
assert dict(sorted(weight_spectrum.items())) == EXPECTED_WEIGHT
assert dict(sorted(size_spectrum.items())) == EXPECTED_SIZE
assert sum(weight_spectrum.values()) == 37293
assert len(direct_minimal) == 37293

print('CODE [48,16,5]_2')
print('EDGES', len(EDGES))
print('MINIMAL_WORDS', len(direct_minimal))
print('CONNECTED_BY_SIZE', dict(sorted(size_spectrum.items())))
print('MINIMAL_WEIGHT_SPECTRUM', dict(sorted(weight_spectrum.items())))
print('MINIMAL_WEIGHT_RANGE', min(weight_spectrum), max(weight_spectrum))
print('VERIFY_OK')
