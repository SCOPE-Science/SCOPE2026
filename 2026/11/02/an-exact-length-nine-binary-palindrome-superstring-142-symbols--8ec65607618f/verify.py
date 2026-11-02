"""Check a length-nine palindrome-cover witness and a finite integer lower bound."""
import json
from pathlib import Path

C = json.loads((Path(__file__).resolve().parent / 'certificate.json').read_text(encoding='utf-8'))
n = C['order']
assert n == 9 and C['alphabet'] == '01'
words = []
for i in range(1 << 5):
    half = format(i, '05b')
    words.append(half + half[-2::-1])
assert len(words) == len(set(words)) == 32

def cost(a, b):
    return next(s for s in range(1, n + 1) if a[s:] == b[:n - s])

u = C['potentials']
assert len(u) == 32 and all(type(v) is int for v in u)
assert sum(u) == C['expected_potential_sum'] == 81
bad = []
for i in range(32):
    for j in range(i + 1, 32):
        cij = cost(words[i], words[j])
        assert cij == cost(words[j], words[i])
        deficit = max(0, u[i] + u[j] - cij)
        if deficit:
            bad.append([i, j, deficit])
assert bad == C['expected_pair_deficits']
assert sum(e[2] for e in bad) == C['expected_deficit_sum'] == 20
assert 2 * sum(u) - sum(e[2] for e in bad) == C['expected_lower_bound'] == 142

w = C['linear_witness']
assert set(w) <= {'0','1'} and len(w) == 142
windows = {w[i:i+n] for i in range(len(w)-n+1)}
assert set(words) <= windows
assert len(set(words) & windows) == 32
# The same word can also be read cyclically, so both upper bounds are 142.
print('VERIFY_OK: 496 pair inequalities, 7 deficits totaling 20, 32 palindromes, length 142')
