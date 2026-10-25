---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Bounded g permits Gaussian differentiation: DF(0)=delta I+a u^T, not in general symmetric. The two nonzero eigenvalues of sym(a u^T) are (u·a ± ||u|| ||a||)/2, so the lower one is -delta_*. Since g(0)=0, f(tw)=delta t² ||w||²/2+o(t²), and F(tv)=tJv+o(t), hence the fixed-step gain has strictly positive leading coefficient delta t²[-h v^T Jv +(h²/2)||Jv||²] for every h>0 if the least symmetric eigenvalue is negative. Positive symmetric part gives uniform local descent directions. For g(s)=s² exp(-s²/2), u=(1,10), delta=.001, independently computed v=(-9.9,1) yielding v^T Jv=-.1524893230 and delta_*=.156921249228332. The displayed rational comparisons certify sign without floating point. Equality delta=delta_* is explicitly not classified beyond quadratic order.

## originality

PASS

The nonlocal coordinate-by-coordinate Gaussian derivative is a known optimization operator, but the inspected primary convergence analysis controls distance to a neighborhood, not monotone objective descent. The exact rank-two local negative-curvature threshold and every-fixed-step uphill witness are distinct mathematical assertions.

## value

PASS

The sharp criterion separates provable local descent directions from unavoidable local ascent even for a globally smooth strongly convex objective. It diagnoses a structural obstruction to naive fixed-step monotonicity assurances for a named, nonconservative smoothing method and provides an analytic bounded-curvature explicit witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
