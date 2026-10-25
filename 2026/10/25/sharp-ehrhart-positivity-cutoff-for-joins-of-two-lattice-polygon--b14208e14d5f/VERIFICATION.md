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

# Reproducibility and limits

Use \(\texttt{python3 verify.py}\), requiring Python 3 and standard-library modules only. The verifier constructs coefficient vectors two ways (Ehrhart-numerator binomial expansion and convolution of Pick Ehrhart counts with independent forward-difference interpolation), checks six test parameter tuples, and exhaustively evaluates every eligible integer Pick-data tuple with normalized-volume product at most \(168\) in a conservative superset of actual polygon pairs. This includes **14,438** states strictly below the cutoff and **14,838** through the cutoff. It confirms strict coefficient positivity in the lower range, a single offending Ehrhart-data tuple at the boundary, and two realizable, different negative-coefficient types.

Actual execution output:

```text
EXACT_OK below_168_states=14438 min_U=5 min_V=45 upto_168_states=14838 unique_bad=(12, 14, 0, 0, -4, 142) coeff_linear=-1/15 quadratic_only=-1/24 independent_convolutions=6
```

The proof of the general sign criterion is symbolic; the bounded exhaustive calculation is invoked only for the sharp finite-volume minimum. The verifier uses exact integers/rationals and performs no extrapolation to larger normalized volumes. No external or independent audit has been performed. Unindexed prior literature remains a priority risk.
