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

The analytic verification reconstructs the circulant Jacobian, positive-frequency characteristic polynomial \(\lambda^2+(a+1-i)\lambda-i\), positive-real-square-root branch, quadratic frequency locus and monotonicity. Differentiating the locus gives the unique strictly increasing quintic \(4v(1-v)^4+3v-2\). Because its derivative has a positive lower bound on \([0,1]\), the rational sign bracket is a rigorous global root isolation, not a finite-search argument.

Run `python3 verify.py` with standard-library Python. It recomputes exact rational signs at \(654193/10^6\) and \(654194/10^6\), the two exact endpoint polynomial identities, a monotonicity bound, the algebraic optimum, and the characteristic residual for the coupled Fourier block. A finite grid of off-optimum rates is only a cross-check and is not proof of the global optimization theorem.

No simulation or checker validates stochastic fixation, nonlinear global relaxation rates, arbitrary relative active/dormant frequencies, or independent peer review. Numerical values are approximations to the unique algebraic quantities defined in the proof.
