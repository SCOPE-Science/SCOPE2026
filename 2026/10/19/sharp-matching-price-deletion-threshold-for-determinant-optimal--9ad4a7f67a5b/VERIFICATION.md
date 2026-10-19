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

The `verify.py` file is standalone Python 3 code using `fractions.Fraction`, rational elimination, and independent weighted spanning-tree enumeration. Reproduction command: `python3 verify.py`.

Successful output: `VERIFY_OK exact_cofactor_spectra=24 independent_tree_sums=6 exact_log_derivatives=450 threshold_sign_cases=90`.

The script checks the claimed weighted Laplacian determinant and spectral product exactly for multiple rational conductances on every graph from 3 through 8 vertices per part. It separately enumerates all spanning trees for two small sizes; checks the scalar logarithmic-derivative identity in 450 rational parameter choices; and checks the threshold and root-sign prerequisites in 90 cases. A deterministic test of the deletion-regime maximum confirms its fully simplified formula for sizes 3 through 12.

Limits: These finite exact computations are not an exhaustive search over real prices, graphs of arbitrary size, or asymmetric conductances; the universal claim follows from the analytic strict-concavity, eigenspace and derivative-sign proof in `RESULT.md`. No independent mathematical audit has been performed.
