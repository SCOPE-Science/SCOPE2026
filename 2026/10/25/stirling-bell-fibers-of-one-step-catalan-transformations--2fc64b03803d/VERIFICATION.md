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

The standalone `verification/check_fibers.py` enumerates every valid nested-set \(N\)-tableau for \(1\leq n\leq8\). For each tableau it computes the transformation by successive application of generator maps in the top-to-bottom row word, independently of any full-core implementation. For every subset \(S\) it compares the resulting row-count profile against the Stirling recurrence, checks the total \(B_{n+1}\) of tableaux, and checks that exactly \(\binom{n+1}{2b}\) subsets have \(b\) maximal runs.

Observed total tableau counts for \(n=1,\ldots,8\): \(2,5,15,52,203,877,4140,21147\). All tests succeeded and the checker printed `VERIFY_OK`.

The enumeration is exhaustive **only in those finite ranks**. It is not an exhaustive proof for all \(n\), and no independent audit or external certification has been performed. Universal correctness rests on the constructive restricted-growth bijection in `RESULT.md`.
