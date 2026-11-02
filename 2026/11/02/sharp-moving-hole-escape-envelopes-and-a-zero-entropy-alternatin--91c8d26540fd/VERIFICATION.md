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

## Direct mathematical checks
The analytic proof in `RESULT.md` uses exact binary coding, 2-by-2 transfer matrices, monotone integer recurrences, finite-dimensional Perron–Frobenius theory and a direct phase transformation for alternation.

`python CHECK.py` completed with 1023 exact matrix-versus-brute-force/equality comparisons, 2046 finite periodic spectral comparisons, and rational finite-horizon probability checks. Those tests verify implementation only, not unbounded quantifiers.

## Limits
No independent audit has been performed. Existing literature may contain an equivalent consequence of broader switched nonnegative-matrix results not identified in the inspected sources. The infinite-time claims rely on the supplied proof, not experimental extrapolation.
