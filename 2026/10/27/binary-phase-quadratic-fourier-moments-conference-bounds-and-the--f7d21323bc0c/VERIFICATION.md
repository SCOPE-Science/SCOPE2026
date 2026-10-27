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

# Reproducibility

Run `python3 checker.py` in a directory containing this file and compare its stdout byte-for-byte with `CHECKS.txt`. Only the Python standard library is used. All sign assignments in the seven-vertex switching gauge are exhausted, and all finite-field calculations and moments are performed using exact integers. An independent coefficient-convolution implementation was separately exercised on twenty sign arrays in each of dimensions four, five, and six; those comparisons agreed with the matching-collision formula.

These computations verify the finite enumerative base and examples, not the character-sum statement over infinitely many fields, the all-dimensional Fourier identity, or literature priority. Those infinite assertions require the algebraic proof in `RESULT.md`. The status line above records that independent audit has not been performed.
