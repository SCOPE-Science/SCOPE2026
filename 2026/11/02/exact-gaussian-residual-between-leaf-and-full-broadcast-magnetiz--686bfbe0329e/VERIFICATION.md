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

The standalone `checker.py` is executable using only Python's standard library. It exhaustively enumerates every recursive parent-choice list and every nonzero-probability broadcast-sign sequence for orders 2 through 7 at seven distinct rational transmission means. It uses `fractions.Fraction` throughout, tests probability normalization, all-spin mean, leaf-spin mean, centered residual, finite residual second moment, uncolored leaf count, and (for smaller orders) every next-step conditional first and second moment by direct branch enumeration. Replayed on the embedded source, it passes **5,622 exact rational assertions**.

The infinite Gaussian limit is supported by a written martingale argument, the law of large numbers for leaf counts and deterministic limiting quadratic variation, not by the finite checker. In the regime \(t>1/2\), the full-spin martingale has summable square increments and its limit is independent of the stably converging residual Gaussian. At \(t=1/2\) no such independence assertion is made.

Independent mathematical auditing and definitive source-priority verification have not been performed.
