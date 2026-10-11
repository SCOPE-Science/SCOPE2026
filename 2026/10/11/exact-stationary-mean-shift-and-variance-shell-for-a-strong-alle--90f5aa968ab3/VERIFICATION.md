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

The proof is analytic. Its critical checks are:

1. On compact support inside \((0,\infty)^2\), invariance permits averaging the derivatives of \(\log x\) and \(\log y\).
2. The predator stationarity equation and \(x_*=\sigma/(\omega-\sigma\eta)\) give
\[
\int\frac{x-x_*}{1+\eta x}\,d\mu=0.
\]
Splitting \(x=x_*+(x-x_*)\) inside the resulting algebra gives the exact nonnegative defect
\[
\bar x-x_*=\eta\int\frac{(x-x_*)^2}{1+\eta x}\,d\mu.
\]
3. The prey per-capita polynomial is exactly quadratic, so
\[
\int(1-x)(x-\alpha)\,d\mu=(1-\bar x)(\bar x-\alpha)-\operatorname{Var}_\mu(x),
\]
which yields the second identity after averaging \(d(\log x)/dt\).
4. Equality in the first defect forces \(x=x_*\) on the invariant support, and invariance of that support then forces \(y=K(1-x_*)(x_*-\alpha)\), leaving only the coexistence-equilibrium Dirac measure.

The supplementary `verify.py` uses exact rational arithmetic to check the source numerical specialization and representative exact algebraic instances. It is a consistency check only; the general theorem is established by the symbolic argument above.

Limits: no assertion is made for invariant measures that charge an axis, noncompact invariant measures, or transient trajectories. The literature comparison retains a residual risk for prior appearances of the generic Holling-II mean-bias ingredient; no inspected source covered the paired source-specific claim.
