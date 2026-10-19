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

Run `python verify_gap.py` with the dependencies specified in `requirements.txt`. The saved `verification_output.txt` is the output from a local replay of this exact program. Checks include exact symbolic expansion of the compressed quadratic form and determinant, its three dual-norm identities, twelve independently integrated ellipsoid probabilities, four Monte Carlo interior checks, three coordinate-aligned checks, a two-zero-coordinate check, and three finite-perturbation Schur-bound checks. All checks complete with `VERIFICATION_PASS 23`.

# Analytical proof boundary

The program uses finite floating-point grids and random draws as cross-checks only. The continuous distribution identity, all-parameter quantifiers, inverse-moment cutoffs, and perturbative limit are justified by exact algebra, geometric integration, one-dimensional convolution, layer cake, and Schur-complement inertia in `RESULT.md`. In particular a finite sample does not prove a tail exponent, a missing event does not demonstrate impossibility, and the program supplies no claim of external certification.
