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

## Direct checks
`check.py` uses independently evaluated numerical integration and a positive-series representation over 25 contrast/frequency settings. It solves the curvature-based critical equation at five contrasts and verifies the first weak-cooling correction at three contrasts. The program ran successfully before packaging.

## Mathematical limits
Numerical tests cannot certify a unique root for every contrast or an infinite-series equality. Those are handled by the exact Gaussian identity, the globally positive cubic derivative, the single sign change in the curvature and a tilted-Laplace-ratio argument. The theorem does not identify cycle endpoint divergence with device entropy production.
