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

Run `python checker.py` with Python 3 and the public `mpmath` package. The program executes 294 numerical consistency assertions in dimensions 3, 4, 5, 7, 10 and 25, across cutoffs below, at, between and above the two theoretical thresholds. It compares five directly integrated eigenvalues with analytic boundary differences and verifies the multiplicity-weighted trace identity. `verification_output.txt` records the output from one completed run.

The exact five-sector decomposition, normalization, monotone-likelihood-ratio comparisons, polynomial boundary factorizations, and sharp stability follow from the proof in `RESULT.md`, not from finite tests. The checker is evidence of arithmetic consistency only and cannot establish an all-dimensional theorem or publication priority. Independent audit has not been performed.
