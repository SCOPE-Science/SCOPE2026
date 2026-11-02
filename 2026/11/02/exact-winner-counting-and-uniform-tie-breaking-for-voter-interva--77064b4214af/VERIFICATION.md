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

The standalone `verify.py` uses inclusive one-based interval endpoints, distinct labeled input candidates, exact integer score comparisons, binomial multiplicities, and an independently expressed brute-force baseline.

The command `python verify.py` passed **1,167,656 exhaustive labeled profile/cardinality cases**, **5,000 seeded nonnegative-weighted random cases**, and **7,000 conditional-uniform sampler choices** on an explicitly checked seven-winner instance. It checks that all samples lie in the exact optimal set and that all seven optimum committees are reachable. The program does not assert statistical independence or prove sampling uniformity by finite observation; the proof of exact uniformity follows instead from the count-weighted path decomposition and unbiased integer sampling.

The proof treats repeated supports, strict containments, empty approvals, zero weights, zero committee size and exact cardinality. Bounds are polynomial in the encoded input size (including rational-weight bit length); the explicit operation count uses a unit-cost rational/integer arithmetic convention. No search result or finite computation proves originality or independent validation.
