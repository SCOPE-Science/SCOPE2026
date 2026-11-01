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

# Verification of the rank-one metric threshold

The mathematical proof in RESULT.md uses exact operator equalities and a positive metric constructed by formula. It verifies both reflexive inverse equations and both metric Penrose self-adjointness equations, including the spectral obstruction at and beyond the boundary. These arguments are valid for rank-one operators on any complex Hilbert space and require no finite truncation.

The standalone `verify.py` performs sampled rational-parameter identity checks and numerical matrix calculations in dimension two, including several complex phases. It independently tests the displayed algebraic formulas. Its finite tests cannot establish an infinite-dimensional theorem, rule out a metric at an untested parameter, or verify literature priority.

Scientific limitations: only rank one; no higher-rank classification; all positive boundedly invertible metrics use one common inner product; no independent audit has been performed.
