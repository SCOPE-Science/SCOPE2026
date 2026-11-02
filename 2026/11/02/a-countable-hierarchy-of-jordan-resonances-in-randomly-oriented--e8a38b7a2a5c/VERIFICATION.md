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

# Verification scope

Run `python verify.py`. The checker uses exact rational arithmetic for the coefficients in 72 claims across three finite-branch truncations and compares the exact Jordan recurrence through four powers. The independent high-precision moment-sum diagnostics test the first eight positive odd degrees; these truncations are **not** infinite-case proofs. The analytic argument in RESULT.md separately proves positivity of the interdegree coefficient by a uniform tail estimate, distinctness and limiting behavior through strict moment log-convexity, and the annealed cross-correlation through Legendre orthogonality.

The physical map is defined only almost everywhere at branch endpoints; the theorem concerns Lebesgue-integrated quantities. The singular Jordan eigenvalue pertains to finite-dimensional polynomial subspaces, not an asserted isolated spectral resonance in a global Banach-space spectrum. No independent scientific review was performed.
