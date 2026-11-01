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
# Verification and limits

The executable `verify_symmetric_fixed_rips.py` performs four independent classes of finite checks. It reconstructs all binary words and maximal inter-orbit Hamming distances, verifies the weight-orbit graph against the banded bipartite model for all scales in dimensions up to ten, checks each local neighborhood-dominance fold for 400 choices of band parameters, and computes reduced mod-two homology from actual face-boundary matrices in 105 cases through dimension fourteen. It additionally checks the core generator maps across 4,950 scale transitions for dimensions up to one hundred, including the complete barcode-threshold inequalities.

Expected stdout:

```
PASS: 55 raw Hamming-orbit scale comparisons (n <= 10)
PASS: 400 independently checked dominated-vertex deletion sequences
PASS: 105 reduced mod-two chain-homology computations (n <= 14)
PASS: 4950 transition/core-map checks (n <= 100)
PASS: all barcode-threshold comparisons (n <= 100)
Example: n=30 gives reduced H_1 interval [20,24).
Finite checks do not replace the all-parameter proof.
```

No finite enumeration proves the universal claim. The general integral classification and inclusion maps follow from the explicit orbit-triangulation, graph fold, and degree arguments in `RESULT.md`. No independent external audit or validation is claimed.
