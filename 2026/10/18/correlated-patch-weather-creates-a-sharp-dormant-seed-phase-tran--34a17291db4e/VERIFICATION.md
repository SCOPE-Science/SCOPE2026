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

Run `python3 verify_beta_dormancy.py` with Python 3 standard library. The program evaluates beta-binomial masses independently of the analytical proof, confirming 100 finite-k exact critical first-order equalities for `Beta(2,1)` with survival 1 and favorable yield 2, 71 exact-rational two-sided brackets consistent with the noncritical `Beta(2,1)` asymptotic, and 35 exact arcsine Beta(1/2,1/2) finite-k derivative signs. The command prints `PASS: 100 exact critical identities, 71 exact two-sided brackets, 35 arcsine signs`.

The proof, rather than this test suite, establishes universal uniqueness, the inverse moment phase criterion, strictly decreasing optima, and the Gamma-ratio asymptotic. No numerical experiment establishes the universal claim. The general critical-rate problem and non-scalar ecological extensions are not proved. Source-level originality remains limited by inaccessible complete 1988 material.
