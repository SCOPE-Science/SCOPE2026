"""Independent integer-bit replay of the palindrome overlap and dual certificate."""
import json
import os

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'certificate.json'), encoding='utf8') as f:
    data = json.load(f)

N = 9
pal_values = []
for k in range(512):
    b = [(k >> shift) & 1 for shift in range(8, -1, -1)]
    if all(b[t] == b[8-t] for t in range(4)):
        pal_values.append(k)
assert len(pal_values) == 32

def jump(x, y):
    for shift in range(1, 10):
        length = 9-shift
        if (x & ((1 << length)-1)) == (y >> shift):
            return shift
    raise AssertionError('9-bit words must have zero-length overlap')

P = data['potentials']
check_deficits = []
for j in range(32):
    for i in range(j):
        e = jump(pal_values[i], pal_values[j])
        assert e == jump(pal_values[j], pal_values[i])
        over = P[i] + P[j] - e
        if over > 0:
            check_deficits.append((i, j, over))
assert sorted(check_deficits) == sorted(map(tuple, data['expected_pair_deficits']))
assert sum(v for _,_,v in check_deficits) == 20
assert 2*sum(P)-20 == 142

s = data['linear_witness']
assert len(s)==142
represented = set()
for start in range(len(s)-8):
    value = 0
    for ch in s[start:start+9]:
        value = 2*value + (ch == '1')
    represented.add(value)
assert all(v in represented for v in pal_values)
print('INDEPENDENT_OK: bit-mask overlap identities and linear witness agree')
