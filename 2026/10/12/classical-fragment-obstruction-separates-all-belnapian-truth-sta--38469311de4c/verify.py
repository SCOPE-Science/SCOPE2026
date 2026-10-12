#!/usr/bin/env python3
"""Finite semantic checks for four-valued S5 status modalities (no dependencies)."""
from itertools import product

T, F = "t", "f"
BITS = {"t": (True, False), "b": (True, True), "n": (False, False), "f": (False, True)}
REVERSE = {v: k for k, v in BITS.items()}
STAR = {"t": "t", "f": "f", "b": "n", "n": "b"}
KINDS = ("circle", "bullet", "neg_circle", "neg_bullet")

def implies(a, b):
    return (not a) or b

def in_status(v, status):
    return (BITS[v][0] if status == "T" else BITS[v][1])

def modal(kind, status, values, root):
    """Return exact (truth-bit,falsity-bit) of Petrukhin's 24 operators.

    'status' in {t,b,n,f,T,F}; 'values' indexed by all S5 worlds.
    Definition 2.6 (arXiv v1), Definition 11 (journal version).
    """
    x = values[root]
    if status in ("T", "F"):
        opposite = "F" if status == "T" else "T"
        P = lambda v: in_status(v, status)
        Q = lambda v: in_status(v, opposite)
        if kind == "circle":
            truth = implies(P(x), all(P(v) for v in values))
            falsity = P(x) and any(Q(v) for v in values)
        elif kind == "neg_circle":
            truth = implies(not P(x), all(not P(v) for v in values))
            falsity = (not P(x)) and any(not Q(v) for v in values)
        elif kind == "bullet":
            truth = P(x) and any(not P(v) for v in values)
            falsity = implies(not Q(x), all(not Q(v) for v in values))
        else:
            truth = (not P(x)) and any(P(v) for v in values)
            falsity = implies(Q(x), all(Q(v) for v in values))
    else:
        twin = STAR[status]
        if kind == "circle":
            truth = implies(x == status, all(v == status for v in values))
            falsity = x == status and any(v != twin for v in values)
        elif kind == "neg_circle":
            truth = implies(x != status, all(v != status for v in values))
            falsity = x != status and any(v == twin for v in values)
        elif kind == "bullet":
            truth = x == status and any(v != status for v in values)
            falsity = implies(x == twin, all(v == twin for v in values))
        else:
            truth = x != status and any(v == status for v in values)
            falsity = implies(x != twin, all(v != twin for v in values))
    return REVERSE[(truth, falsity)]

def boolean_ops(a, b):
    ta, fa = BITS[a]; tb, fb = BITS[b]
    return [REVERSE[z] for z in ((fa, ta), (not ta, not fa),
            (ta and tb, fa or fb), (ta or tb, fa and fb),
            (implies(ta, tb), ta and fb))]

# Base subalgebra: the five nonmodal propositional connectives preserve {t,f}.
for a, b in product((T, F), repeat=2):
    assert all(z in (T, F) for z in boolean_ops(a, b)), (a,b)

# All eight exceptional-status modalities are constants on any classical-only
# interpretation, even with different values at different worlds.
for local, remote in product((T, F), repeat=2):
    for kind in KINDS:
        for status in ("b", "n"):
            val = modal(kind, status, (local, remote), 0)
            desired = F if "bullet" in kind else T
            assert val == desired, (kind, status, local, remote, val)

# All 16 ordinary-status operators detect a change outside the designated
# root, while the entire b/n fragment cannot detect that change.
checks = []
for kind in KINDS:
    for status in ("t", "f", "T", "F"):
        target = "t" if status in ("t", "T") else "f"
        local = target if kind in ("circle", "bullet") else ("f" if target == "t" else "t")
        remote = "f" if local == "t" else "t"
        v0, v1 = (local, local), (local, remote)
        a = modal(kind, status, v0, 0)
        b = modal(kind, status, v1, 0)
        assert BITS[a][0] != BITS[b][0], (kind, status, a, b)
        assert all(modal(k, i, v0, 0) == modal(k, i, v1, 0)
                   for k in KINDS for i in ("b", "n"))
        checks.append((kind, status, local, a, b))

print("VERIFY_OK: 4 classical operand pairs; 32 exceptional-status constancy cases; 16 ordinary-status separations")
for kind, status, local, a, b in checks:
    print(kind, status, "root", local, "constant", a, "flipped", b)
