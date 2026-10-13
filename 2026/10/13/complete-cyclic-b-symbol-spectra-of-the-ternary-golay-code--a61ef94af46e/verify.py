from collections import Counter
from itertools import product
import json
from pathlib import Path

Q = 3
N = 11
G = (2,0,1,2,1,1)  # low-to-high coefficients


def multiply_message(message):
    out = [0] * N
    for i, a in enumerate(message):
        for j, b in enumerate(G):
            out[i+j] = (out[i+j] + a*b) % Q
    return tuple(out)


def direct_b_weight(word, b):
    return sum(any(word[(i+j) % N] != 0 for j in range(b)) for i in range(N))


def zero_gaps(word):
    support = [i for i, x in enumerate(word) if x]
    if not support:
        return (N,)
    if len(support) == N:
        return ()
    gaps = []
    for i, s in enumerate(support):
        t = support[(i+1) % len(support)]
        gap = (t-s-1) % N
        if gap:
            gaps.append(gap)
    return tuple(gaps)


def gap_b_weight(word, b):
    if not any(word):
        return 0
    gaps = zero_gaps(word)
    return N - sum(max(g-b+1, 0) for g in gaps)

cert = json.loads(Path(__file__).with_name('certificate.json').read_text())
words = [multiply_message(m) for m in product(range(Q), repeat=6)]
assert len(words) == Q**6
assert len(set(words)) == Q**6

observed = {b: Counter() for b in range(1, N+1)}
for w in words:
    for b in range(1, N+1):
        a = direct_b_weight(w, b)
        c = gap_b_weight(w, b)
        assert a == c, (w, b, a, c, zero_gaps(w))
        observed[b][a] += 1

expected = {
    int(b): Counter({int(k): v for k, v in dist.items()})
    for b, dist in cert['b_symbol_weight_enumerators'].items()
}
for b in range(1, N+1):
    assert observed[b] == expected[b], (b, observed[b], expected[b])
    assert sum(observed[b].values()) == Q**6

hamming = Counter(sum(x != 0 for x in w) for w in words)
expected_hamming = Counter({int(k):v for k,v in cert['ordinary_hamming_weight_enumerator'].items()})
assert hamming == expected_hamming
assert observed[1] == hamming

mins = {}
for b in range(1, N+1):
    mins[b] = min(w for w, count in observed[b].items() if w > 0 and count)
expected_mins = {int(k):v for k,v in cert['minimum_b_symbol_distances'].items()}
assert mins == expected_mins

for b in range(1, N+1):
    print('b=%d %s' % (b, dict(sorted(observed[b].items()))))
print('VERIFY_OK')
