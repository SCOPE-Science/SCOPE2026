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

Run `python3 verify.py` using only the Python standard library. The checker evaluates two algebraically distinct rational covariance representations and their sign predictions over the stated finite test ranges, confirms the explicit \(n=6,r=3/10\) positive witness and zero boundaries, computes independent circular-grid mixed moments directly from two-point positions, and exhaustively enumerates all vertex configurations for selected small periodic discrete grids. Expected output:

```
OK: 653 rational/checker assertions
```

**Proof boundaries:** The enumerated/discretized configurations are finite checks, not a proof for all real radii or all graph sizes. The all-size continuous theorem is verified mathematically by the conditional-uniform-arc density integral and quadratic/linear sign analysis in `RESULT.md`. The independent historical-priority comparison is limited to the cited accessible primary full texts and targeted searches; an external audit has not been performed.
