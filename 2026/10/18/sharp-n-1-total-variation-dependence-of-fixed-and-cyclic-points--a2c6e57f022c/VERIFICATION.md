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

The mathematical derivation is in `RESULT.md`. The accompanying `verify.py` uses only the Python standard library; run `python verify.py` in the directory containing it.

The execution completed 231 finite/exact assertions plus one numerical limiting-constant consistency check. Exact checks enumerate all \(n^n\) endofunctions for each \(1\le n\le6\), compare the joint law with the rooted-forest/rencontres factorization, and check the marginals, covariance, and total variation against independently enumerated outcomes. The numerically evaluated finite sum serves only as a check of the algebraic constant.

The unbounded argument relies on the rooted-forest enumeration, the alternating Taylor remainder, dominated convergence with the summable bound \(nq_{n,k}\delta_k\le k\delta_k\), and a summable binomial-to-Poisson mass expansion. No finite enumeration establishes the limit. Historical priority and independent verification have not been established here.
