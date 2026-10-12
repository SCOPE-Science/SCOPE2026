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

The self-contained verifier is `verify.py`. Run `python3 verify.py` with standard Python 3. It constructs 15 deterministically seeded positive rational ultrametric rooted binary trees for each tip count from two to seven, then independently calculates optimal normalized Rao weights by exact Gaussian elimination on the shared-ancestry covariance matrix. It checks agreement with a separate exact electrical-conductance recursion, every cardinality knapsack optimum against exhaustive subset search, and every strict seeded marginal comparison in those test instances.

Actual checked output:

```text
VERIFY_OK direct_KKT_vs_conductance=3690 knapsack_optima=405 strict_marginal_triples=83970
```

The proof in `RESULT.md` covers all positive-length ultrametric rooted binary trees. The finite verifier does not establish the unrestricted theorem on its own. The computed weights are exact rational values; no numerical optimization tolerance is involved. Positive-length and ultrametric assumptions are material. Theoretical novelty is subject to the literature risks described in `REVIEW.md`.
