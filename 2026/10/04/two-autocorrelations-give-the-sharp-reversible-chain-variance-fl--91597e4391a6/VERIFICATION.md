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

The proof is analytic. The accompanying checker uses exact rational arithmetic.

It verifies the bound for finitely supported rational spectral probability measures by clearing denominators. It then generates rational equality measures supported on \(\{-1,q\}\), reconstructs the prescribed first two moments, and checks the exact equality value.

The checker verifies the \(-1\) and \(q\) eigenvectors of the explicit four-state stochastic matrix. It also applies the recalibration preceding lazification, confirms that the lazy chain preserves the target first two autocorrelations exactly, and checks the strict inequality in the aperiodic case when the second moment exceeds the square of the first.

Finite replay does not prove the infinite-dimensional inequality. The universal argument is the Cauchy--Schwarz proof in `RESULT.md`.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK generic_checks=20000 equality_checks=36000 matrix_checks=48000 lazy_checks=60000 one_lag_checks=20000`.
