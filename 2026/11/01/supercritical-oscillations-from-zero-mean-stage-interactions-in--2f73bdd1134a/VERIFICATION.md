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

# Reproducibility checks

Run `python verify_stage_hopf.py` from the extracted package, with Python 3 and SymPy installed. The program derives both exchange-block Jacobians directly from the four-variable vector field, compares their exact characteristic polynomials, restricts the nonlinear flow to the invariant exchange-symmetric plane, computes the canonical planar first Lyapunov coefficient, and verifies the four-dimensional characteristic factorization. It also checks the exact \((u,d,w)=(3,6,14)\) witness and 20 rational parameter cases. In the original package review the program printed:

`PASS: symbolic identities, full Jacobian, exact Hopf coefficient, and 20 rational cases`

The decisive infinite-parameter signs are analytic: \(d>u+2\) and \(u>2\) make the noncritical block Hurwitz and the Hopf frequency real, while \(\ell_1=-du/[4(u+2)]<0\) and the crossing derivative \(1/2\) establish the nondegenerate supercritical bifurcation. Finite samples are checks of implementation only. The standard local Hopf and hyperbolic persistence theorems establish small-amplitude orbit existence and transverse stability; the checker is not an independent proof of those theorems. No independent scientific audit has been performed.
