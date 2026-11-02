"""Exact finite certificate for a binary equal-length greedy-superstring counterexample.

Python 3 standard library only. Assertions compare every live ordered pair at each
of 251 greedy merges and every pairwise suffix-prefix overlap of 252 inputs.
"""
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256

s = 4
k = 2 * s
t = 14
fresh = 'ABCDEFGHIJKLMN'

def alt(n):
    assert n >= 0
    return 'yx' * (n // 2) if n % 2 == 0 else 'x' + 'yx' * ((n - 1) // 2)

def cyclic(w, width, start):
    return ''.join(w[(start + i) % len(w)] for i in range(width))

def overlap(left, right):
    for r in range(min(len(left), len(right)), 0, -1):
        if left[-r:] == right[:r]:
            return r
    return 0

def join(left, right):
    return left + right[overlap(left, right):]

# Construct the 252 eight-symbol words and prescribed initial cyclic paths.
inputs = []
groups = []
for ch in fresh:
    bases = (
        ('U', 'xa' + alt(s-3) + ch + 'xa' + alt(s-3) + 'y',
         alt(s-4) + ch + 'xa' + alt(s-1) + 'a'),
        ('V', 'xa' + alt(s-3) + ch,
         'a' + alt(s-3) + ch + 'xa' + alt(s-3) + ch),
        ('W', 'xa' + alt(s-1) + ch,
         alt(s-4) + ch + 'xa' + alt(s-1) + ch),
    )
    assert tuple(len(w) for _, w, _ in bases) == (8, 4, 6)
    for typ, base, border in bases:
        starts = [j for j in range(len(base))
                  if cyclic(base, 7, j) == border]
        assert len(starts) == 1
        starts = starts[0]
        path = [cyclic(base, 8, starts + i)
                for i in range(len(base))]
        assert len(path) == len(set(path))
        groups.append((ch, typ, path))
        inputs.extend(path)
assert len(inputs) == 252 == len(set(inputs))
assert all(len(w) == 8 for w in inputs)

# Check every greedy merge against the ACTUAL global maximum over live strings.
live = set(inputs)
steps = []
def step(a, b, required=None):
    assert a != b and a in live and b in live
    v = overlap(a, b)
    if required is not None:
        assert v == required, (v, required)
    best = max(overlap(x, y) for x in live for y in live if x != y)
    assert v == best, (len(live), v, best)
    out = join(a, b)
    live.remove(a)
    live.remove(b)
    assert out not in live
    live.add(out)
    # The containment-preprocessing variant makes exactly the same choices.
    assert not any(x in y for x in live for y in live if x != y)
    steps.append((a, b, v, out))
    return out

closed = {}
for ch, typ, path in groups:
    w = path[0]
    for q in path[1:]:
        w = step(w, q, 7)
    closed[ch, typ] = w
assert len(live) == 42
middle = []
for ch in fresh:
    middle.append(step(closed[ch, 'V'], closed[ch, 'U'], 1))
result = middle[0]
for nxt in middle[1:]:
    result = step(result, nxt, 1)
for ch in fresh:
    result = step(result, closed[ch, 'W'], 0)
assert len(live) == 1 and result in live
assert len(steps) == 251 and len(result) == 519
assert all(x in result for x in inputs)

# Direct de Bruijn Euler tour gives the explicit 259-character common superstring.
edges = defaultdict(list)
for w in inputs:
    edges[w[:-1]].append(w[1:])
stack = [inputs[0][:-1]]
tour = []
while stack:
    at = stack[-1]
    if edges[at]:
        stack.append(edges[at].pop())
    else:
        tour.append(stack.pop())
tour = tour[::-1]
assert len(tour) == 253 and tour[0] == tour[-1]
short = tour[0] + ''.join(v[-1] for v in tour[1:])
assert len(short) == 259 and all(w in short for w in inputs)

# A 17-element binary length-10 code; every word begins 000, ends 1,
# and has no other occurrence of 000. This proves cross-bifix-freeness.
from itertools import product
pool = [''.join(w) for w in product('01', repeat=10)
        if ''.join(w).startswith('000') and ''.join(w).endswith('1')
        and all(''.join(w)[j:j+3] != '000' for j in range(1, 8))]
assert len(pool) == 24
code = pool[:17]
assert len(set(code)) == 17
for u in code:
    for v in code:
        for r in range(1, 10):
            assert u[-r:] != v[:r], (u, v, r)
encoder = dict(zip('xya' + fresh, code))
assert len(encoder) == 17

def encode(w):
    return ''.join(encoder[c] for c in w)

binary_inputs = [encode(w) for w in inputs]
assert len(set(binary_inputs)) == 252
assert all(len(w) == 80 for w in binary_inputs)
# Not merely a sampled check: exhaust all 252*251 distinct ordered input pairs.
for i, u in enumerate(inputs):
    for j, v in enumerate(inputs):
        if i != j:
            assert overlap(binary_inputs[i], binary_inputs[j]) == 10 * overlap(u, v)
# Also verify all chosen intermediate pair overlaps and merge compatibility.
for a, b, o, out in steps:
    assert overlap(encode(a), encode(b)) == 10 * o
    assert encode(out) == encode(a) + encode(b)[10*o:]
assert len(encode(result)) == 5190
assert len(encode(short)) == 2590
assert all(w in encode(short) for w in binary_inputs)
# Each pair of distinct binary inputs has overlap at most 70; in any common
# superstring their starts are >=10 apart. Thus OPT is at least 80+251*10.
assert max(overlap(u, v) for i,u in enumerate(binary_inputs)
           for j,v in enumerate(binary_inputs) if i != j) == 70
assert 80 + 251 * 10 == 2590
assert Fraction(5190, 2590) == Fraction(519, 259) > 2
print('PASS: 17 non-overlapping length-10 codewords (24 available)')
print('PASS: 252 distinct length-80 binary inputs')
print('PASS: all 63252 ordered distinct binary input overlaps')
print('PASS: 251 exact maximum-overlap greedy merges, output length 5190')
print('PASS: common superstring length 2590 and matching lower bound')
print('PASS: greedy/optimum ratio 519/259 > 2')
print('codewords:', ' '.join(code))
print('greedy-sha256:', sha256(encode(result).encode()).hexdigest())
print('optimum-sha256:', sha256(encode(short).encode()).hexdigest())
