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
# Verification

The infinite statement is verified by the symbolic proof in `RESULT.md`. The accompanying `verify_two_heavy_wps.py` is an independent finite regression check, not a substitute for that proof.

It implements both local cyclic-quotient Reid--Tai ages and the global fractional-part criterion of Kasprzyk, then compares each with the closed-form inequalities over a parameter box extending beyond the predicted feasible region. The executed output was:

`VERIFY_OK cases=18612 r=2..12; pair-count formulas checked through r=30`

Limits: the script checks finitely many parameters only. The universal quantifiers and exact counting formulas rest on the residue proof, not on extrapolation from the computation.
