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

# Reproduction and verification

Run `python verify.py` with Python 3 (standard library only). The checker compares the exact two-level pivot-count mass formula against a separately programmed rational finite-state sequential-pivot recursion. It also verifies normalization, exact expected count and variance and leading critical-window mean centering for numerical cases. On the prepared package, all **1,383** exact-rational identities and asymptotic-centering checks passed.

The code tests exact finite formulas for \(2\le n\le10\), \(1\le r<n\), and \(a\in\{2,3,4,7\}\), and checks representative large dimensions. These finite checks do not establish the infinite-rank Gaussian limit. Its proof uses the exponential-race construction, uniformly bounded variance of the centered high-clock maximum, and conditional binomial central limit theory. No independent audit has been performed.
