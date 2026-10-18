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

The exact rational checker `verify.py` was executed against the public algorithmic specifications. It performed 12,006 exact finite transition/normalization/detailed-balance/stationary-moment/polynomial-factorization checks with residual exponents two, four, and six, and 54 exact two-level outlier checks. It printed PASS. No external independent audit or numerical infinite-dimensional certification was performed.

The full mathematical proof of the all-size rank/inertia statement is the Vandermonde and symmetric-block congruence in `RESULT.md`. Finite tests do not establish its universally quantified components. The sharp skewness/bias classification follows from the two-level constrained extremum calculation; the checker tests representative exact values, not exhaustively all datasets. The claim is limited to unit scalar rows and exact projections.
