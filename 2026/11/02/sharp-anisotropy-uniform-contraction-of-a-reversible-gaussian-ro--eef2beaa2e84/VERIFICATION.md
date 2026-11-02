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

The analytic derivation in `RESULT.md` is the proof. The standalone standard-library program `verify_split.py` was run directly and reported 466 successful checks, testing the exact squared-error map by independent Gaussian-angle quadrature, polynomial spectral identities, finite-iteration coupling inequalities, anisotropy monotonicity, and endpoint consistency. None of these finite numerical tests is represented as an infinite verification.

The method uses exact OU transitions and trigonometric random rotations; floating-point evaluation, sampling cost, higher-dimensional and non-Gaussian problems are unverified. Independent mathematical audit has not been performed.
