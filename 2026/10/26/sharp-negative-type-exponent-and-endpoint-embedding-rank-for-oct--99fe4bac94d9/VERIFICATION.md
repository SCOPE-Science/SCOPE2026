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

# Checks and reproducibility

- Explicit integer signed-permutation construction yields 24 distinct matrices and relative-angle class counts (1,6,3,8,6).
- For eight exponents, direct symmetric distance-matrix eigenvalues match the four nontrivial character spectra with predicted multiplicities.
- Centered squared-distance Gram matrices have numerical ranks 23 below and 19 at the analytic threshold.
- The exact character-table proof separately verifies signs for all positive real exponents; sampling does not establish this.
- At larger exponents the two-dimensional block is positive, so small-scale exponentials are indefinite; large-scale exponentials converge to identity.

Run `python rotation_negative_type_check.py` with NumPy. This program uses only locally constructed integer rotation matrices. Exact infinite-parameter validity is supplied by the character proof, not finite numerical examples.
