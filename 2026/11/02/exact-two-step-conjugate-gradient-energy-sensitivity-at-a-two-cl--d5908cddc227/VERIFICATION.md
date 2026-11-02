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

# Verification of the two-cluster two-step CG coefficient

The analytical proof appears in `RESULT.md`. The local `VERIFY.py` file contains complete, standard-library-only exact-rational verification code, including the CG moment normal equations, their first derivatives, the derivative residual, the blockwise orthogonal projections, the announced coefficient, and two rank-two sharpness examples.

Running `python3 VERIFY.py` completed with PASS for 560 seeded rational perturbation configurations over block dimensions \((1,1),(2,1),(1,2),(2,2),(3,2),(2,3),(3,3)\). The direct solver also checked exact rational two-step CG errors for a three-mode case with coefficient \(9/2048\) at perturbations \(t=1/100,1/1000,1/10000\). Their ratios of squared error to \(t^2\) respectively were approximately \(0.0043940642901\), \(0.0043944853816\), and \(0.0043945266714\), approaching \(9/2048=0.00439453125\).

For a purely cross-block perturbation the checker found an identically zero first-order coefficient and positive direct squared errors scaling as \(t^4\). No numerical test is used as a proof of the all-dimensional or asymptotic assertion, and no independent audit has been performed.
