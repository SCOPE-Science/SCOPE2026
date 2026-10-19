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

Run `python3 verify.py` (Python 3 standard library; no dependencies) from the extracted directory. This program independently enumerates every word over paired binary and quaternary alphabets at stated short lengths, across multiple stem sizes and loop minima. It computes exact rational first and second moments directly from the full sample space, then compares them with the formulas in `RESULT.md`. An unrelated parity-union-find method checks the number of independent complement equations for every sampled pair of distinct candidate stems, including both coincident- and distinct-center pairs.

These checks are finite sanity checks, not an infinite proof. The symbolic all-parameter proof of the covariance classification and variance identity is in `RESULT.md`. Probability distribution, folding energetics, nonuniform alphabet probabilities, and first-publication priority are not certified by this finite program.
