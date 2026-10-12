"""Independent exact verification of the 78-word single-grain code.

Uses explicit tuples of bits rather than the integer adjacency formulation
used for the upper bound. Python standard library only.
"""
from pathlib import Path

N = 9
first_half = [int(t) for t in Path(__file__).with_name('witness.txt').read_text().split()]
assert len(first_half) == len(set(first_half)) == 39
assert min(first_half) >= 0 and max(first_half) < 256

def bits(x):
    return tuple((x >> (8-i)) & 1 for i in range(N))

def outputs(x):
    b = bits(x)
    candidates = {b}
    for i in range(1, N):
        modified = list(b)
        modified[i] = b[i-1]
        candidates.add(tuple(modified))
    return candidates

code = [bits(x) for x in first_half]
code += [tuple(1-c for c in b) for b in code]
assert len(code) == len(set(code)) == 78
owner = {}
ball_sizes = []
for x in code:
    ball = outputs(sum(t << (8-i) for i, t in enumerate(x)))
    ball_sizes.append(len(ball))
    for y in ball:
        if y in owner:
            raise AssertionError(f'conflicting words {owner[y]} and {x}, output {y}')
        owner[y] = x
assert all(len(y) == 9 for y in owner)
print('WITNESS_OK', 'codewords', len(code), 'distinct_received', len(owner),
      'min_ball', min(ball_sizes), 'max_ball', max(ball_sizes))
