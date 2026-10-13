#!/usr/bin/env python3
from itertools import product

# Elementary binary cellular-automaton local rules are encoded by an 8-bit
# truth table indexed by (left,center,right) -> 4*left+2*center+right.

def bit(rule, triple):
    a,b,c = triple
    return (rule >> (4*a+2*b+c)) & 1

def compose_center(f, g, w5):
    # Apply f at positions -1,0,+1 and then g at the center.
    y = [bit(f, w5[i:i+3]) for i in range(3)]
    return bit(g, y)

words5 = list(product((0,1), repeat=5))
inverse_pairs = []
checks = 0
for f in range(256):
    for g in range(256):
        fg = True
        gf = True
        for w in words5:
            checks += 1
            if compose_center(f, g, w) != w[2]:
                fg = False
            checks += 1
            if compose_center(g, f, w) != w[2]:
                gf = False
        if fg and gf:
            inverse_pairs.append((f,g))

expected_pairs = {(15,85),(51,51),(85,15),(170,240),(204,204),(240,170)}
assert set(inverse_pairs) == expected_pairs
assert len(inverse_pairs) == 6

# Identify the six rules semantically: left/center/right coordinate, with or
# without bit complement.
semantics = {
    240: lambda a,b,c: a,
    204: lambda a,b,c: b,
    170: lambda a,b,c: c,
    15:  lambda a,b,c: 1-a,
    51:  lambda a,b,c: 1-b,
    85:  lambda a,b,c: 1-c,
}
for rule, fn in semantics.items():
    for t in product((0,1), repeat=3):
        checks += 1
        assert bit(rule,t) == fn(*t)

# Test the radius-1 recodings on a long universal finite word obtained by
# concatenating all binary words through length 8. Every word of length <=8
# occurs in it; this is a finite diagnostic for the dense-pattern mechanism.
u = []
for n in range(1,9):
    for w in product((0,1), repeat=n):
        u.extend(w)

def apply_radius1(rule, seq):
    return [bit(rule, seq[i-1:i+2]) for i in range(1, len(seq)-1)]

for f,g in inverse_pairs:
    y = apply_radius1(f,u)
    z = apply_radius1(g,y)
    # Two boundary layers are lost; the remaining center must be recovered.
    for i, val in enumerate(z, start=2):
        checks += 1
        assert val == u[i]

print('radius1_inverse_pairs', sorted(inverse_pairs))
print('radius1_reversible_rules', sorted({f for f,_ in inverse_pairs}))
print('composition_truth_table_checks', 256*256*32*2)
print('VERIFY_OK', checks, 'exact assertions')
