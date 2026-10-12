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

The proof is algebraic. It verifies the update and admissible parameters from the definition, enumerates the four possible size-three subsets symbolically, and closes the covariance recursion on permutation-invariant matrices. It relates the entire space of deterministic starting vectors to that recursion using self-adjointness and conjugacy, then uses exact degree-two Schur conditions and Perron--Frobenius theory to establish the infinite-time alternatives. The largest eigenvalue of the exact expected squared one-step map gives the separate transient boundary.

The supplied `verify.py` uses only the Python standard library. It independently constructs the four row-coordinate updates and expected squared-error map over rational numbers, checking twelve rational coherence parameters, the entire two-coordinate recurrence, both one-step eigenvalue formulas and the factored characteristic identities. Command: `python verify.py` (expected final line begins `EXACT_CHECK_OK`). These are reproducibility checks only; no finite experiment proves the infinite-time statements. An independent scientific audit has not been performed.
