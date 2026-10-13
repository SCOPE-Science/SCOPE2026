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

# Verification of the covariance identity

Running `python verify.py` with the standard library yielded:

```
PASS: checked 46233 permutations over n=1..8
PASS: checked 120 exact root-split/mixed-moment recurrences
PASS: asymptotic illustrations at n=200000: cov/n=-0.2898106666, corr=-0.1339673251
Finite checks are not proofs of the infinite-domain conclusions.
```

The program computes Quicksort comparison counts recursively, constructs pointer-based search trees independently, checks strict upper records, compares exact rational mixed moments to \(3n+H_n-2(n+1)H_n^{(2)}\), checks the two marginal variance formulas, and independently evaluates the root-split total-covariance recurrence in fractions for the first \(120\) sizes. Floating-point checks at large size illustrate the leading asymptotic coefficients and are not rigorous error certificates.

The all-size identity is proved by finite harmonic-sum algebra and the covariance recurrence in `RESULT.md`. Its strict sign is proved by a reflected-split rearrangement argument. The covariance and correlation limits use standard harmonic expansions and established marginal moment formulas. The checks do not claim a full joint distribution, independence, or exhaustive historical priority. Independent audit has not been performed.
