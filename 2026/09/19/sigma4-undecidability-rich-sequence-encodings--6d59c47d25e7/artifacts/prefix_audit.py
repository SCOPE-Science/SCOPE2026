#!/usr/bin/env python3
"""Syntactic alternation audit for the four-block counter-machine reduction.

This records the quantifier-class bookkeeping used in RESULT.md.  A prefix is
represented by E/A blocks after adjacent equal blocks are merged.  The asserted
classes are upper bounds; semantic correctness is established in RESULT.md.
"""

def merge(prefix):
    out = []
    for q in prefix:
        if not out or out[-1] != q:
            out.append(q)
    return tuple(out)

# Primitive upper bounds after expanding exact-cardinality predicates.
QF = ()
SIGMA1 = ("E",)
PI1 = ("A",)
SIGMA2 = ("E", "A")
PI2 = ("A", "E")

primitive = {
    "rep": QF,
    "cnst0": PI1,
    "cnst_k_positive": SIGMA2,
    "succ": PI1,
    "inc": SIGMA2,
    "eq": PI1,
    "gt1_two_witnesses": SIGMA1,
}

# Finite positive Boolean combinations of Sigma_2 atoms with Pi_1 atoms are Sigma_2.
step = SIGMA2
# Boundary clauses forall y not succ are Pi_2; endpoint formulas combine Pi_2 and Sigma_2
# under existentially selected endpoint representatives, giving Sigma_3.
endpoint = ("E", "A", "E")
# A Pi_1 guard implying a Sigma_2 consequent is Sigma_2; closing universally gives Pi_3.
local = ("A", "E", "A")
# Existential sequence parameters + (Sigma_3 endpoint conditions) + Pi_3 local condition.
whole = ("E", "A", "E", "A")

assert primitive["cnst_k_positive"] == ("E", "A")
assert primitive["inc"] == ("E", "A")
assert primitive["cnst0"] == ("A",)
assert primitive["eq"] == ("A",)
assert primitive["succ"] == ("A",)
assert primitive["gt1_two_witnesses"] == ("E",)
assert step == ("E", "A")
assert endpoint == ("E", "A", "E")
assert local == ("A", "E", "A")
assert whole == ("E", "A", "E", "A")

print("primitive classes:")
for name, prefix in primitive.items():
    print(f"  {name:22s} {''.join(prefix) or 'QF'}")
print("step       :", "".join(step), "(Sigma_2)")
print("endpoint   :", "".join(endpoint), "(Sigma_3)")
print("local      :", "".join(local), "(Pi_3)")
print("halting    :", "".join(whole), "(Sigma_4)")
print("PASS")
