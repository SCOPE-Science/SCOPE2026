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

The finite absorbing-chain check `python checker.py` passed on sizes 3 through 9 for both neighbor-only and self-sampling update rules. The independent rational Gaussian elimination and the direct backward-difference recurrence agree exactly. Floating-point size checks through 200,000 agents are consistent with the limit \(8.215284066486\ldots\) at an initially all-inferior population, with the distinct threshold-initialization constant and the above-threshold \(n\log n\) law.

The proof in RESULT.md, not the finite tests, supplies the infinite-population conclusion. The crucial checks are the exact ratio \(8k(n-k)/((n-1)^2+8k^2)\), the quadratic vanishing of the ratio defect at \(k/n=1/4\), the rescaling of log products to a cubic potential, a summable tail envelope, and the gamma integral evaluation. The original update samples neighbors excluding the updating agent; the comparison process with self-sampling is not substituted for it in the final claim.
