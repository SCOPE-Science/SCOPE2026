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

The analytical arguments appear in `RESULT.md`. The single executable file is `verify.py`, which requires Python 3 and the standard library only. Execute `python verify.py` from the directory containing the extracted files; no network access or external data are needed.

Checks performed on the exact file included in the package: independent convex-hull edge reconstruction by supporting planes at four heights; independent intersection-point and planar-convex-hull construction for 3,600 sampled plane normals at three heights; exact threshold-side-count correspondence; agreement between the spherical area integral, a separate edge-angle expectation calculation, and a midpoint angular quadrature at seven heights; equal-edge regularity calculation; sharp thin/tall constants; and three seeded isotropic-normal experiments using 180,000, 120,000 and 120,000 normals. These computations all passed.

The numerical studies test implementation consistency but cannot certify statements for all real heights or an infinite set of orientations. The sign-threshold table and analytic spherical integral in `RESULT.md` are the proof for the complete domain. Historical novelty is not certified by a finite literature search. Independent mathematical review has not been performed.
