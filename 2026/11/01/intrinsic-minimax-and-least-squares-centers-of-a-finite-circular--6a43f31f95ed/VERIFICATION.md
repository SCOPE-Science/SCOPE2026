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

# Verification of intrinsic cone center theorem

The complete continuum claim is proved analytically in `RESULT.md`. In particular, the developed-geodesic argument bounds all winding paths; the farthest target lies at the apex or antipodal rim; all center-radii transitions and equality cases follow by convexity; and the sharp radius/diameter ratio follows from a four-branch explicit formula.

## Executed finite checks

Running `python3 verify_cone_center.py` from the accompanying files succeeds with:

```
Isolated center-coincidence cone ratios: 0.2030336599850761 0.30793382365128746
PASS: 2,857,130 counted finite checks; 66 cone ratios; 0 numerical failures
Maximum target-grid discrepancy: 0.0
Sharp ratio attained at t=1/3: 0.8660254037844386
```

The script also quadratures the original squared-distance integral and compares it with the derived Fréchet quadratic at sampled source radii and cone opening parameters. Its grids contain 301 source radii per shape, 32 slant targets and 33 angle targets in repeated trials, plus 9,999 further shape parameters for the sharp upper ratio. The root calculations use deterministic bisection. All assertions passed.

## Scientific scope and unverified limits

The finite tests do not prove universal geodesic minimality, extrema, uniqueness of both coincidence roots, or historical priority; these are supplied by the analytic proof and source comparison respectively. No independent audit has been performed. The cone's base disk is excluded; a different intrinsic metric would require a new proof.
