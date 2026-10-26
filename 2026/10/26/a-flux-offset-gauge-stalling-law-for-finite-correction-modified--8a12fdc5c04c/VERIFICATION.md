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

# Reproducibility

Run `python checker.py` with Python 3.10+; no external packages are needed. The program constructs the signed-weight two-state correction in rational arithmetic for two-node and three-node Gauss–Lobatto tableaux, three positive input choices, correction counts 1, 2, 3, 4, 6, and offsets 0, 1, 10, 100, 1000, 10000. Every one of the 180 configurations checks exact mass preservation, positivity, and the original stage-balance equations, and the one-correction terminal identity. The larger-offset configurations additionally compare the rescaled drift with the coefficient in the theorem, using an explicit rational tolerance.

The universal \(C\to\infty\) conclusion is established by the large-offset induction in RESULT.md, not by sampled finite offsets. No independent audit or validation is represented by these computations. Boundary conditions: strictly positive masses, positive step, fixed finite corrections, \(C\ge0\); the proof does not cover discontinuous flux changes, vanishing denominator regularizations, or simultaneous limit \(M\to\infty\).
