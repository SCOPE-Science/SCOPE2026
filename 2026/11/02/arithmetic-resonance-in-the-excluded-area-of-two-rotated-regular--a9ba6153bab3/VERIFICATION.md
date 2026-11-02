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

# Reproducible checks

The theoretical identities come from the convex mixed-area edge-support formula, the exact trigonometric finite grid sum, and an analytic probability pushforward. Numerical verification is a diagnostic, not proof for all orders, radii or angles.

Run `python verify.py` from the extracted package with Python 3, NumPy, and SciPy installed. The program constructs every pairwise vertex sum, obtains the convex hull via Qhull and compares area against the derived formula for 3,888 deterministic pseudorandom configurations over orders from 3 through 20. It also independently verifies 28 extremizing boundary configurations, six midpoint-quadrature moment profiles and five previously published fixed-orientation table entries. The final row's embedded verifier must be extracted and executed before relying on reported checks. All evaluations use finite double-precision arithmetic; the exact proof is in RESULT.md.

Independent audit status: not performed.
