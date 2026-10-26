"""Finite exact tests of endpoint coupling and local profile identities.
Run: python check_signed_words.py. This is finite verification, not an asymptotic proof.
"""
from itertools import product
from collections import Counter

def form(u, signs):
    return ''.join(u if s == '+' else u[::-1] for s in signs)

def edge_profile(w, b):
    return (w[:b], w[-b:])

def hanf_profile(w, radius, cap):
    # Radius-local paths have truncated ends. Counts are capped.
    counts = Counter()
    n = len(w)
    for i in range(n):
        left = max(0, i-radius)
        right = min(n, i+radius+1)
        typ = (i-left, right-i-1, w[left:right])
        counts[typ] += 1
    return {k: min(v, cap) for k,v in counts.items()}

tests = 0
for m in (2, 3, 4):
    for signs in product('+-', repeat=m):
        for n in range(2, 9):
            for b in (1, 2):
                if n < 2*b:
                    continue
                counts = Counter(edge_profile(form(''.join(bits), signs), b)
                                 for bits in product('01', repeat=n))
                if signs[0] == signs[-1]:
                    assert len(counts) == 2**(2*b)
                    assert set(counts.values()) == {2**(n-2*b)}
                else:
                    assert len(counts) == 2**b
                    assert set(counts.values()) == {2**(n-b)}
                    assert all(y == x[::-1] for x,y in counts)
                tests += 1

# Every fixed template is injective as a map u -> w, because its first block is u or reverse(u).
for m in (2,3,4):
    for signs in product('+-', repeat=m):
        for n in range(1, 8):
            words = {form(''.join(u),signs) for u in product('01',repeat=n)}
            assert len(words) == 2**n
            tests += 1

# Construct a saturating base with every ternary radius-1 window repeated >= 2.
# Verify the exact capped neighbourhood signature is a function only of end profiles.
u = ('00010111' * 30) + ('11001010' * 30)
n = len(u)
b = 3
ref = '0' * 20 + u[:b] + ('00010111'*90) + u[-b:] + '1' * 20
# Compare only words whose ACTUAL first/last b symbols coincide.
for signs in product('+-', repeat=4):
    w = form(u,signs)
    x,y = edge_profile(w,b)
    v = x + ('00010111'*120) + y
    assert hanf_profile(w,1,2) == hanf_profile(v,1,2)
    tests += 1

print('SIGNED_COPY_REVERSE_EXACT_OK', tests, 'endpoint_and_local_tests')
