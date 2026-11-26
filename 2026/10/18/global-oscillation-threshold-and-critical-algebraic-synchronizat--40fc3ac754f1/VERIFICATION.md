---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The standard-library `verify.py` evaluates the quartic identity exactly on a finite rational grid, samples the dissipation inequality, and numerically integrates representative trajectories below, at, and above the threshold. Its eigenvalue snippet uses the expected eigenvalues as inputs, not an independent spectral computation.

The analytic proof in `RESULT.md` gives the polynomial identity in every direction, the spectrum from the cyclic permutation, the strict rearrangement inequality, the exclusion of nonzero planar equilibria, and the critical inversion and periodic-lift arguments. The numerical diagnostics do not certify the all-initial-state or infinite-time statements.
