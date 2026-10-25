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
# Verification record
The standalone `verify.py` uses only the Python standard library and exact `fractions.Fraction` arithmetic. It exhaustively enumerates the \((2n-1)!!\) uniform matchings, every subset of \(k\) marked pairs, and all induced rank patterns for each \(1\le n\le5\), \(1\le k\le n\). It checks the empirical conditional means against the exact formula and independently sums chord-type counts for the covariance formula for \(2\le n\le5\). A direct execution from this extracted package reports PASS for all five sizes.

Verification is a finite independent computational cross-check, not an exhaustive check for all positive integers. The proof in RESULT.md establishes the all-parameter assertion using uniform residual pairing and exchangeable gaps. The source-comparison and priority assessment remain nonexhaustive. No external audit or independent scientific validation has been performed.
