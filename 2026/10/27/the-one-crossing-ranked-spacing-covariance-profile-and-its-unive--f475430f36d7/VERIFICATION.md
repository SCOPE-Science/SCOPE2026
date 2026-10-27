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
# Reproducible checks

Execute `python3 verify.py` with Python 3.9 or newer. The script independently sums all first-, second- and third-order monomials of a uniform Dirichlet vector using factorial moment rules, then compares the results with the claimed harmonic covariance formula for every rank and dimension 2 through 12. It checks the exact mean of each ranked gap, total quadratic mean, zero-sum of all rank covariances and unique sign transition. It also checks the predicted large-rank fraction at four finite dimensions, only as a numerical sanity check. Observed: PASS, 279 checks.

The proof in RESULT.md is needed for all-dimensional claims and the limit; finite verification is not an infinite certificate. Historical novelty has not been independently audited. No external certification or expert validation is claimed.
