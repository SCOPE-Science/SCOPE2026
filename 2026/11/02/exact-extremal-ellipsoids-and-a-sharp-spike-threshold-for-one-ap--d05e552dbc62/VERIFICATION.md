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

# Reproducibility and scope of verification

Run the included standalone `verify_pointed_ball_ellipsoids.py` with Python 3 and NumPy installed. It evaluates all contact and parameter equations as floating-point assertions, verifies positive-semiaxis formulas and cone containment, and compares 3,001 radial sections of each candidate with the exact sphere-plus-cone boundary. It also verifies 3,001 spherical latitudes against the enclosing ellipsoid.

Observed output: `PASS: 320 dimension/spike configurations`; smallest sampled radial difference \(-2.22\times10^{-16}\), maximum sampled outer-constraint excess \(2.22\times10^{-16}\). Round-off at the displayed level is expected. The analytic arguments in `RESULT.md` establish all-dimensional and all-real-parameter claims. This script is not a formal proof or an exhaustive discretization. Independent audit has not been performed.
