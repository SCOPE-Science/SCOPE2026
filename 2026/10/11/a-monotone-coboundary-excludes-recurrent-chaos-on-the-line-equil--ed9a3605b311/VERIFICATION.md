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

The claimed identity is checked in two independent ways inside this package.

First, direct differentiation gives
\[
\dot H
=g\bigl(mx^2-(1+m)xy\bigr)
+g(1+m)x(y-x)
=-g x^2.
\]
No limiting argument or numerical integration is used.

Second, `verify.py` expands the monomials coefficient-by-coefficient using only the Python standard library. It checks that every \(gmx^2\), \(gxy\), and \(gmxy\) term cancels except \(-gx^2\). It also checks the published specialization
\[
\frac{g(1+m)}{2r}=\frac{126}{61}
\]
for \((m,r,g)=(1.1,6.1,12)\), and evaluates the printed vector field at the source's origin initial condition to confirm that it is exactly zero.

The invariant-measure step uses only the standard generator identity for a compactly supported invariant probability measure and the nonnegativity of \(x^2\). The recurrent-point step uses monotonicity of \(H\) and continuity under returns.

Limits: no claim is made about parameter regimes outside \(k_1=0\), \(k_2=g\), \(k_3=0\); no finite simulation is treated as proof of infinite-time behavior; and no claim is made that every bounded complete non-equilibrium trajectory is impossible.
