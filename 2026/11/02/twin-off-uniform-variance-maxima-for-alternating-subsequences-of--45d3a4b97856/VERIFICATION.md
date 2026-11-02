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

# Reproducibility and scope of the checks

Run `python VERIFY.py` in a Python 3 environment with SymPy installed. The script verifies all six weighted local-overlap probabilities by enumerating the \(2!\) through \(5!\) Mallows-ranked permutation patterns. It checks, with exact symbolic rational arithmetic, the variance's linear and constant coefficients, the factorized derivative, reciprocal identities, and the uniform specialization. It then computes the longest descent-first alternating subsequence by an independent dynamic programming algorithm on every permutation through eight elements, and compares exact Mallows-weighted means and variances with the stated formulas at \(q=1/3,1/2,1,2,3\) for sizes four through seven, and \(q=1/2,1\) for size eight.

Observed output: `PASS: 110,195 exact assertions; n=4..8, and 13 symbolic identities`.

The all-size claim is not established merely by these finite tests. Its mathematical proof uses the canonical local-extrema representation, disjoint-block independence, finite overlap enumeration, and the reciprocal polynomial's two-positive-root classification. No numerical optimization is used to prove uniqueness. The approximate root and maximum are supplementary numerical values.

Independent audit: not performed.
