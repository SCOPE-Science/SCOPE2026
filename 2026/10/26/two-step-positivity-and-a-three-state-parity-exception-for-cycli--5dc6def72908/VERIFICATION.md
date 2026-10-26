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

The analytical argument establishes the result for every integer cycle length and every positive real step size, with a fixed number of steps. The matrix identity \(C_h=2R_s-I\), the closed circulant geometric resolvent, and \(C_h^2=I+4sR_s'\) lead to exact off-diagonal signs; differentiating the first cyclic coefficient yields the sharp two-step polynomial. A high-step asymptotic expansion excludes every fixed even power for cycles of length at least four. The stochastic-matrix argument verifies that positivity of the end-step operator applies to every nonnegative initial vector.

Reproducibility: place `verify.py` next to this file and run `python verify.py` with Python 3. It uses only standard-library rational arithmetic. The executed checker returned `PASS: 4496 exact-rational assertions`, including direct inverse constructions and matrix powers. The independent scientific audit has not been performed. Finite verification is not an exhaustive check of all real steps, all cycle lengths, or all powers; the proof handles those quantifiers.
