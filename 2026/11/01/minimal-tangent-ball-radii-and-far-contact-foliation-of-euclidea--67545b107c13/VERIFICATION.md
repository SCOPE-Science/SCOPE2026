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

The exact-rational program `verify.py` was run from this package's source, producing:

`PASS: 2023 exact-rational checks; analytic proof required for all dimensions/parameters.`

The tests cover rational sphere-parameter samples for semiaxis lists `(5,3)`, `(5,3,2)`, `(5,5,2)`, `(7,5,3,2)` and `(2,2,2)`; boundary-containment Rayleigh inequalities; equalities under reflection in a maximal eigendirection; positive pointwise curvature gaps when the top eigenvalue is simple; and near-equatorial sequences whose Rayleigh quotients approach, without attaining, the top eigenvalue. All universal cases are established analytically in `RESULT.md`, not by sample counts.

The central identity can be independently checked symbolically: for unit parameter vectors \(u,v\), \(2\langle u,u-v\rangle=\|u-v\|^2\). Consequently the boundary sphere containment condition becomes a Rayleigh inequality with largest eigenvalue \(a^2\); the normal projection and classification follow algebraically.

No independent audit or external verification has been performed. The 2014 global ellipsoid threshold is a known result; the claimed contribution is the sharp pointwise profile and complete far-contact classification.
