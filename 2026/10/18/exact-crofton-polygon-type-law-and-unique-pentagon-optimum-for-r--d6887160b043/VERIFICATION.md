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

# Reproducible verification

Run `python3 check_prism.py` with Python 3; only the standard library is needed. The executable reconstructs the triangular-prism vertices and nine edges independently of the closed probability formula, samples uniformly distributed normal directions and width-weighted offsets, checks the resulting generic three-/four-/five-vertex counts, and checks the face-offset probability by an independent two-dimensional deterministic quadrature. It also checks probability normalization, positivity, the derivative identity, and the numerically bracketed unique optimizer. All assertions passed.

The theorem's continuum statements and global maximizing uniqueness are proved analytically in `RESULT.md`. Numerical comparison and finite sampling cannot independently validate those infinite claims or certify publication priority. No independent audit has been performed.
