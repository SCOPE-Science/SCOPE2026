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

# Verification details

The identity \(H_a=M_{F_a}\) is a direct consequence of Plancherel applied in the unbounded frequency variable; it does not assume pointwise convergence for arbitrary \(L^2\) input. The defining primitive can be differentiated explicitly and the density integrates to one. Uniqueness of the outer root follows from strict monotonicity of \(a\coth(at)-t\), whereas uniqueness of the optional inner root follows from strict concavity of \(a\tanh(at)-t\). For \(a>1\), the envelope derivative is strictly positive because the density decreases on \((1,\infty)\). The min/max and sixfold spectral fiber statements follow from these derivative signs. Monotonicity plus change of variables proves the absence of singular spectral components.

`checker.py` performs floating-point consistency checks of the special-function formula and stationary equations, numerically brackets the critical width, and checks representative monotonicity and multiplicity regimes. It is included to reproduce numerical constants and catch arithmetic errors. It is not an infinite-dimensional proof. The analytic proof handles all positive widths and every spectral level outside the finitely many branch-boundary values.

Publication priority beyond the cited and inspected sources has not been independently certified. Independent mathematical validation has not been performed.
