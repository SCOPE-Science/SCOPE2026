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

# Verification record

The accompanying `verify.py` was executed from its packaged source as a standalone Python program. It returned:

```
PASS projected-flow selection trials 384
PASS instances 2405 rational equilibrium checks 88985
PASS balanced example ('5/12', '5/6') ('2/5', '4/5')
```

The checker enumerates pairs of strictly positive target vectors of lengths at most three and common integer total at most nine. It constructs exact rational below-threshold equilibrium candidates using capped-demand inversion and at/above-threshold candidates using the proposed interval parameterization, then independently verifies every individual capped fixed-point equation and aggregate matching-volume identity. The numerical trajectory trials apply the projected homogeneous aggregate vector field over finite time and compare with the predicted clipped-initial-imbalance limit. Exact calculations were independently checked for the heterogeneous two-by-two example and the interior Jacobian eigenvalues.

Finite arithmetic checks do not prove uniqueness, global convergence, or the asymptotic derivative statement. Those follow from the explicit monotonicity, boundary, and flow arguments in `RESULT.md`. The empirical selection trials use numerical discretization and are not a proof of the limiting statement. Unrestricted heterogeneous trajectory convergence is not claimed. Historical novelty and scientific completeness have not been independently validated.
