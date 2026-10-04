#!/usr/bin/env python3
from itertools import product

# Finite analogue of complete truth theories.
# A signature gives truth values to m formulas; the language also contains
# their negations, so the full theory contains one literal from each pair.
for m in range(1, 7):
    sigs = list(product((False, True), repeat=m))

    def theory(s):
        # Literal i is represented as (i, truth_value).
        return {(i, s[i]) for i in range(m)}

    def R(s, t):
        return theory(s) <= theory(t)

    for s in sigs:
        assert R(s, s)
    for s in sigs:
        for t in sigs:
            assert R(s, t) == R(t, s)
            for u in sigs:
                if R(s, t) and R(t, u):
                    assert R(s, u)

# Explicit reflexive nontransitive frame.
W = (0, 1, 2)
R = {
    (0, 0), (1, 1), (2, 2),
    (0, 1), (1, 2),
}
p = {0: True, 1: True, 2: False}

def box_truth(phi):
    return {
        w: all(phi[v] for v in W if (w, v) in R)
        for w in W
    }

box_p = box_truth(p)
box_box_p = box_truth(box_p)

assert box_p[0] is True
assert box_box_p[0] is False
assert all((w, w) in R for w in W)
assert (0, 1) in R and (1, 2) in R and (0, 2) not in R

print("VERIFY_OK")
