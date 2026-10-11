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

The verification target is the exact disease-free codimension-two boundary of the printed multiple-exposure planar epidemic system.

Checks performed:

1. Reconstructed the translated vector field directly from the printed equations at \(\beta_1=d\rho/A\) and \(\beta_0=d\rho^2/A^2\).
2. Solved the center-manifold invariance equations through cubic graph order and obtained \(a_1=-\rho/d\), \(a_2=0\), and \(a_3=\rho^3(d-\rho)/(A^2d^2)\).
3. Substituted the graph into the infection equation and checked the cubic coefficient \(-\rho^3/A^2\) and quartic coefficient \(\rho^4(d-\rho)/(A^3d)\).
4. Checked that the endemic-equilibrium polynomial reduces to a positive multiple of \(I^2\), so no positive equilibrium exists at the exact boundary.
5. Checked the algebra converting the reduced coefficients into the leading and subleading time-asymptotic constants.
6. Rechecked boundedness from \(\dot S+\dot I=A-dS-\rho I\le A-d(S+I)\).

The global convergence step is an analytic planar-dynamics argument, not a finite computation. The checker verifies the algebraic premises but does not substitute for the Poincaré–Bendixson/index proof. No independent audit has been performed.
