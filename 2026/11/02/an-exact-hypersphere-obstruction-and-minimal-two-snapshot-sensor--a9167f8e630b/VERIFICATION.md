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

# Verification of the Gaussian-puff sensor theorem

All general assertions are proved analytically in `RESULT.md`. To reproduce the finite checks, run `python3 checker.py` in this directory; it requires only Python 3 standard-library modules.

The checker verifies with exact rational arithmetic that the illustrative three-point array is cospherical, that the fourth sensor breaks cosphericity, and that the sphere-inversion map rescales *every* squared source-to-sensor distance exactly. It also checks identical log-concentration time profiles, mirrors across a line, and 1,200 deterministic randomized two-snapshot reconstructions of source position, positive diffusivity, release time, and positive mass. All 6,036 assertions passed during preparation. The exact four-sensor design determinant is 8.

Finite checks do not prove global identifiability or rule out coverage by previous mathematical literature. These conclusions rest respectively on the written rank-and-inversion proof and the cited comparison, which retains explicit historical-priority risks. There has been no independent audit.
