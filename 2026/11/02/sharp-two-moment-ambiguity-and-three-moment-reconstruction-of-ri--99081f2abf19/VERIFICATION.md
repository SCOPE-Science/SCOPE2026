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

# Reproduction and boundaries

Use Python 3 to execute `python3 verify_torus.py` from the unpacked result directory. No third-party dependencies are required. The checks actually executed in this package returned:

`VERIFY_OK independent_angle_moments=30 rational_and_inverse_checks=274`

The script exactly checks cleared-denominator polynomial identities for the normalized fourth moment and the sixth-minus-six-times-fourth moment, their endpoint and transition values, the rational two-moment collision, and exact feasibility of the collision's squared radii. For ten positive embedded-ring geometries it integrates the two independent surface coordinates by a 64-point periodic trapezoid rule in each angle, using a direct angular-difference average. The resulting 30 numerically integrated moments agree with their separate analytic formulas to specified floating tolerances. It also tests rational representatives of the ambiguity involution and an inverse inequality.

These are finite diagnostic computations. The theorem for all positive real \(0<r<R\), its uniqueness, and optimality are established by the algebraic proof in `RESULT.md`. No programmatic search over parameters is treated as an exhaustive proof. No independent human verification or historical-priority certification has been performed.
