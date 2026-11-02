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

Run `python verify_weighted_tripartite_edge.py` with NumPy installed according to `requirements.txt`. The standalone checker constructs the weighted powered-distance matrices directly and verifies their critical eigenvalues and kernel dimensions for 95 choices of graph size and stretched edge length. It also checks 52 exact rational adjacency quadratic identities and the cubic sensitivity coefficient numerically.

```
FULL_WEIGHTED_METRIC_THRESHOLD_AND_SIMPLE_KERNEL_OK 95
EXACT_RATIONAL_WEIGHTED_QUADRATIC_FORM_OK 52
CUBIC_WEIGHTED_EDGE_SENSITIVITY_OK
ALL_WEIGHTED_TRIPARTITE_EDGE_CHECKS_OK
```

These finite checks corroborate, but do not prove, the universal spectral reduction or the asymptotic limit. The formulas and strictness are proved analytically in `RESULT.md`. No independent scientific audit has been performed.
