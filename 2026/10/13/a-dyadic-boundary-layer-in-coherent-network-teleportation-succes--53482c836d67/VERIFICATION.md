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
# Verification

The claim is proved analytically from the published success-probability expression. The critical steps checked are:

1. The hyperbolic form simplifies to
\[
P_m(x)=\frac12\frac{1+e^{-2(2a-1)x}}{1+e^{-2ax}}.
\]
2. The derivative after \(q=e^{-2x}\) has exactly one zero because
\[
F_a'(q)=(a-1)(2a-1)(q^{a-2}+q^{2a-2})>0.
\]
3. The rescaled critical equation converges to \(u^2+2u-1=0\), selecting \(u=\sqrt2-1\) in \((0,1)\).
4. The boundary scaling \(x=t/2^m\) gives the explicit limiting profile, while fixed \(x>0\) gives \(1/2\).
5. The exact inequality \(P_m(x)\le1/2\) reduces the uniform error to the minimum depth.

The included `verify_boundary_layer.py` evaluates the source and simplified formulas independently on a finite grid, locates the unique finite-size critical point by bisection, and checks convergence toward the analytic constants. The replay is finite and is not used to establish the infinite limits.

Scientific limit: the analysis begins from the source's Eq. (18); it does not independently validate the entire physical derivation of that equation.
