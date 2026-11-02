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

# Algebraic and analytic verification

Run `python verification/check.py` with SymPy installed. The executable asserts the exact fold identities, nonzero fold curvature, eigenvalue signs, four algebraic center-manifold coefficient equations, and three simple equilibrium roots at the paper's baseline inflow. It prints the algebraic normal-form values. The global positive-orbit convergence, separatrix geometry, and asymptotic constant-existence claims are analytical arguments in `RESULT.md`, not certified by the finite symbolic checks. The symbolic check is a self-review calculation; no independent scientific audit or validation has been performed.
