#!/usr/bin/env python3
LIMIT = 1_000_000

spf = list(range(LIMIT + 1))
for i in range(2, int(LIMIT ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, LIMIT + 1, i):
            if spf[j] == j:
                spf[j] = i

def factor_blocks(n):
    out = []
    while n > 1:
        p = spf[n]
        block = 1
        while n % p == 0:
            n //= p
            block *= p
        out.append(block)
    return out

def uphi_from_blocks(blocks):
    v = 1
    for block in blocks:
        v *= block - 1
    return v

solutions = []
low_support_inputs = 0
mismatches = 0
expected = {2: 3, 3: 2, 15: 2}

for n in range(2, LIMIT + 1):
    blocks = factor_blocks(n)
    if len(blocks) > 2:
        continue
    low_support_inputs += 1
    u = uphi_from_blocks(blocks)
    actual_m = (n + 1) // u if (n + 1) % u == 0 else None
    if actual_m is not None:
        solutions.append((n, actual_m))
    predicted_m = expected.get(n)
    if actual_m != predicted_m:
        mismatches += 1

assert solutions == [(2, 3), (3, 2), (15, 2)]
assert mismatches == 0
print(
    'VERIFY_OK '
    f'limit={LIMIT} '
    f'low_support_inputs={low_support_inputs} '
    'solutions=2:3,3:2,15:2 '
    f'theorem_mismatches={mismatches}'
)
