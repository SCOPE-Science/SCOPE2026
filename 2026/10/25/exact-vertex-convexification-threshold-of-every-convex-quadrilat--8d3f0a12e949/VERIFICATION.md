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

# Scientific verification

The exact proof reduces the normalized vertex-translate inclusion to the maximum of the minimum of two explicitly piecewise-affine gauges on a fixed rectangle. It computes four quadrant maxima and an explicit uncovered point for every subcritical \(\lambda\) at least one. Supporting edge geometry excludes \(\lambda<1\).

Run `python verify.py` using only the Python standard library. The script partitions the rectangle at all breakpoints, enumerates exact rational cell corners and intersections of the two affine branch surfaces, and compares the resulting exact maxima for 36 rational shapes. On execution it printed:

`PASS: 36 affine-shape pairs checked using exact rational polyhedral subdivision.`

The script's check is finite; the universal exact formula rests on the analytic proof in `RESULT.md`. No external, third-party, formal or independent validation is claimed.
