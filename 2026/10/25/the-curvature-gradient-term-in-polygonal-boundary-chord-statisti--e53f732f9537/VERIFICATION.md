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

# Verification notes

The analytic proof in `RESULT.md` supplies the all-curves assertion. To reproduce deterministic numerical checks with no external packages, run `python3 verify.py` from the directory containing this file.

`verify.py` constructs the exact support-function ovals with \(\rho_p(\theta)=1+\frac12\cos(p\theta)\) and places polygon vertices at equal curve arclength using Newton inversion of \(s=\theta+\sin(p\theta)/(2p)\). Exterior angles are computed using `atan2` of adjacent polygon edge vectors. For mode \(p=2\), the estimates of the second asymptotic coefficient at edge counts \(64,128,256,512,1024\) converge toward approximately \(7.0356815386\); for mode \(p=3\), they converge toward approximately \(-71.6528619849\). The terminal absolute errors are below \(0.03\) in both cases. The program also checks two periodic-integral formulas and the circle expansion through its exact regular-polygon expression; it prints `VERIFY_OK` if all checks pass.

Finite examples neither prove the uniform Taylor remainder nor establish a literature-priority claim. The exact wedge identity, center-edge directional series, periodic quadrature, and closed-curve integration by parts are proved in the result. Independent scientific audit has not been performed.
