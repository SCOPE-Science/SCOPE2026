#!/usr/bin/env python3
"""Low-degree C2 group-cohomology consistency check; not a proof of Lefschetz."""

def trivial_z_cyclic2(p):
    if p == 0:
        return 'Z'
    if p % 2 == 0:
        return 'Z/2'
    return '0'

# These are the geometric hypotheses proved separately by Lefschetz.
cover = {0: 'Z', 1: '0', 2: 'Z', 3: '0'}

def e2(p, q):
    if cover[q] == '0':
        return '0'
    return trivial_z_cyclic2(p)

rows = {degree: [(p, degree-p, e2(p, degree-p))
                 for p in range(degree+1)]
        for degree in range(4)}
assert all(entry[2] == '0' for entry in rows[3])
assert [z for _, _, z in rows[2] if z != '0'] == ['Z', 'Z/2']
assert rows[1] == [(0, 1, '0'), (1, 0, '0')]
# Possible d_2 and d_3 from (0,2) have zero targets (2,1),(3,0).
assert e2(2, 1) == '0' and e2(3, 0) == '0'
assert e2(0, 2) == 'Z' and e2(2, 0) == 'Z/2'
print('VERIFY_OK degree3_empty=true degree2=Z,Z/2 d2_d3_targets_zero=true')
