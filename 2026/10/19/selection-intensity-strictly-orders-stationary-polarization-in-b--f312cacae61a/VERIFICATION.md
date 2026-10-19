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

All required computations can be reproduced from `verify_stationary.py` using `python3 verify_stationary.py` (Python standard library only).

The checker independently enumerates both focal-strategy hypergeometric payoff sums for all \(3\le N\le13\), all \(2\le n<N\), and compares against the derived linear payoff-gap identity. At three representative positive exploration rates and three return regimes, it forms exact-rational transition probabilities by choosing intensities such that \(\exp(w|\kappa|)\) is \(1,2,3,5\), builds the full stationary law with detailed-balance products, and tests normalization, reflection, balance and the strict ordering of all adjacent polarizations and nontrivial tails. Where \(\kappa=0\), it tests exact invariance. Each calculation is rational; no finite-precision tolerance is involved.

Observed output:

```
PASS: hypergeometric/payoff identities 3432
PASS: stationary distributions and balance 2376
PASS: strict ordering inequalities/equalities 14139
PASS: exact-rational finite verification complete
```

The complete proof of the unbounded quantifiers appears in `RESULT.md`; a finite checker cannot establish an all-population theorem by itself. No independent scientific validation was performed. Source publication priority remains subject to outside review.
