#!/usr/bin/env python3
import hashlib
import itertools

STATES = tuple(range(8))
MESSAGES = tuple(range(4))

def above(x, y):
    return (x & ~y) == 0

UP = {x: tuple(y for y in STATES if above(x, y)) for x in STATES}

def admissible(alpha):
    """Return possible first-write states for each message, or None."""
    witnesses = {}
    for m in MESSAGES:
        xs = []
        for x in STATES:
            if alpha[x] != m:
                continue
            # After first write x, every second message must be reachable.
            if all(any(alpha[y] == target for y in UP[x]) for target in MESSAGES):
                xs.append(x)
        if not xs:
            return None
        witnesses[m] = tuple(xs)
    return witnesses

valid = []
for alpha in itertools.product(MESSAGES, repeat=8):
    w = admissible(alpha)
    if w is not None:
        valid.append((alpha, w))

assert len(valid) == 24

canonical = (0,1,2,3,3,2,1,0)
# Every valid decoder is exactly a message relabeling of the canonical decoder.
expected = set()
for p in itertools.permutations(MESSAGES):
    expected.add(tuple(p[v] for v in canonical))
actual = {a for a,_ in valid}
assert actual == expected and len(expected) == 24

# The four first-write states are forced: 000 and the three unit vectors.
low = {0,1,2,4}
reduced_encoder_count = 0
for alpha, witnesses in valid:
    used_first = set()
    for m in MESSAGES:
        assert len(witnesses[m]) == 1
        x = witnesses[m][0]
        used_first.add(x)
        assert alpha[x] == m
    assert used_first == low

    # Complementary cube vertices decode to the same message.
    for x in STATES:
        assert alpha[x] == alpha[x ^ 7]

    # Count choices for the second-write table on the four reachable first states.
    choices = 1
    for m in MESSAGES:
        x = witnesses[m][0]
        for target in MESSAGES:
            c = sum(1 for y in UP[x] if alpha[y] == target)
            assert c >= 1
            choices *= c
    assert choices == 16
    reduced_encoder_count += choices
assert reduced_encoder_count == 384

# Directly verify the Rivest-Shamir XOR decoder formula.
def rs_decoder(x):
    a=(x>>2)&1; b=(x>>1)&1; c=x&1
    return ((b^c)<<1) | (a^c)
rs = tuple(rs_decoder(x) for x in STATES)
# Our canonical numbering may differ by a fixed message permutation; it must be one valid decoder.
assert rs in actual

# Canonical newline-terminated representation of all valid interpretation functions.
rows=[]
for alpha in sorted(actual):
    rows.append(''.join(str(v) for v in alpha))
blob=('\n'.join(rows)+'\n').encode('ascii')
digest=hashlib.sha256(blob).hexdigest()
assert digest == '9afddc5cdab8eeea0ca83cf1d4d5261165fd40795d7cc7648cf413d982201081'

print('VERIFY_OK states=8 interpretations_checked=65536 admissible_decoders=24 message_relabeling_orbits=1 forced_first_states=000,001,010,100 complement_pairs=true reduced_second_write_choices_per_decoder=16 reduced_schemes=384 decoder_sha256='+digest)
