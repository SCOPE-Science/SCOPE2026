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

# Reproduction checks

Run `python artifacts/verify_polar_order.py` with Python 3 and NumPy. The script checks exact-rational post/pre recurrence and finite proximal threshold cases; tests dense random rectangular matrices in 54 configurations; and checks the full rank-flat asymptotic regimes, the sign/period behavior, and the critical order case. On execution, 13,554 exact-rational recurrence checks and 18,636 dense-matrix checks passed, including the critical update-order case. These are finite numerical and finite rational tests, not a proof of the universal global claims, whose elementary contraction and signed recurrence proofs are in RESULT.md. The exhaustive set of possible real initial matrices cannot be computationally enumerated.
