---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification notes

Run `python3 verify.py` using only the Python standard library. The checker recomputes the exact generator and weighted pair derivatives for positive rational inputs, confirms the far-pair identity, checks the closed low-dimensional inequalities, verifies the elementary far-pair graph mechanism in many dimensions, constructs nonconstant admissible six-cycle weights for several unequal-mass samples, and tests explicit seven-cycle infinitesimal amplification. Mathematical limits: finitely many computations do not prove a statement for arbitrary dimension, positive real weights or all continuous times; these quantifiers are covered by the proof in RESULT.md. All positive-time conclusions use semigroup submultiplicativity and a zero-time derivative, not a finite time grid. No external certification or independent audit is asserted.
