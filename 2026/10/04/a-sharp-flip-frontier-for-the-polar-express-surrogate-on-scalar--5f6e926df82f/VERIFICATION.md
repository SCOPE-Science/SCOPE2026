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

The proof first rescales the scalar quadratic iteration to the dimensionless map
\[
T_\tau(u)=u\left[1-\frac{\tau}{(1+|u|^4)^{1/4}}\right].
\]
Global convergence for \(0<\tau\le2\) follows from strict contraction of the magnitude at every nonzero state. Local series expansions prove the fifth-order matched step and the critical \(k^{-1/4}\) law. The postcritical two-cycle is solved exactly and its two-step derivative is evaluated in closed form.

`artifacts/verify_polar_surrogate_scalar.py` checks exact cycle identities and derivatives, representative global contraction inequalities, the fifth-order coefficient, and the critical asymptotic constant.

The computational replay is finite and is not used as a proof of the all-parameter claims. Matrix polynomial iterations, pre-normalized practical updates, stochastic gradients, and noncommuting multidimensional modes are outside scope.
