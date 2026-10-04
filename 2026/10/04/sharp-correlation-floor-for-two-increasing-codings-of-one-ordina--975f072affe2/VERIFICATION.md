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

The proof is analytic. The accompanying checker uses exact rational arithmetic for the covariance and squared-correlation inequalities.

For random rational probability profiles and two random strictly increasing rational score vectors it verifies:

- the centered cumulative-cut decomposition;
- the exact cut covariance matrix;
- that the least cut-pair correlation occurs at the first and last cuts;
- the strict global lower correlation inequality for \(m\ge3\);
- exact correlation one for positive affine recodings;
- the two-category equality case;
- the equal-mass floor \(1/(m-1)\).

It also constructs opposite one-dominant-gap score families and numerically checks convergence toward the sharp endpoint.

Finite replay is supplementary. The universal result is established by the exact cut covariance formula and the Hilbert-space triangle inequality in `RESULT.md`.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK decomposition_checks=5000 cut_covariance_checks=97406 cut_minimum_checks=2500 global_lower_checks=2127 affine_checks=2500 binary_checks=373 boundary_checks=2127 equal_mass_checks=98`.
