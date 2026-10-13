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

# Verification record

The enclosed `verify.py` was executed from its actual local file with the Python standard library and emitted `VERIFY_OK`. It checked the model fixed-point equations at the exact crossover \(I=\log 3\), verified the factorization \((1-t)(1-3t)\) for rational test values, recomputed the three Schur margins using high-precision decimal arithmetic, and tested 25 parameter/level combinations against the original equilibrium equations and the population-sign identity.

The precise mathematical proof for every admissible parameter uses strict monotonicity of \(r(I)\), strict decrease of \(L'(I)\) and its bounded integral, and exact analytical treatment of boundary cases. Finite checks are only consistency tests. The supplied example's Schur positivity follows analytically from \(1<\log3<2\). This document does not assert independent verification, journal review, or global epidemic stability.
