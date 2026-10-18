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

# Reproduction and limits

Execute `python3 phylogenetic_transfer_check.py` using Python 3 standard libraries. Expected terminal output includes five PASS statements and an exact count of `186` small-population cut comparisons.

The verifier implements the clade-detection formula with exact rational arithmetic and a separate direct enumeration of labeled subsets for the six-individual example. It checks all six expected-diversity differences, affine dependence on the cherry terminal length at five rational values, and a weakly resolved nonstar example. Every legal positive-integer donor/recipient choice for population sizes at most five, every depth, and every set partition of species is checked for nonnegative cut change. These tests are finite sanity checks; the unrestricted theorem rests on the layer concavity argument and the two-draw and penultimate-draw identities in `RESULT.md`.

The independent scientific audit is not yet performed. No empirical field validation, prior-publication certification, or results for sampling models outside the stated assumptions are asserted.
