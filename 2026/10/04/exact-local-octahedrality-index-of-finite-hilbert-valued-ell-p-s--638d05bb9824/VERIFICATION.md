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

The claimed constant is checked from the defining infimum-supremum geometry, without numerical approximation.

For \(1\le p\le2\), two inequalities meet exactly. The universal witness uses a coordinate of size at most \(n^{-1/p}\) and an orthogonal unit direction. The sharp obstruction is the balanced vector with all coordinate norms \(n^{-1/p}\). Concavity of the Hilbert squared-norm expression and convexity on the coordinate-mass simplex reduce the obstruction to a simplex vertex, giving exactly
\[
1-\frac1n+\left(1+n^{-2/p}\right)^{p/2}
\]
after taking the \(p\)-th power.

For \(p\ge2\), an orthogonal vector of the same coordinate norms gives both distances exactly \(\sqrt2\). Conversely, testing at a one-coordinate vector reduces the smaller signed distance to the scalar inequality
\[
(1+t^{2/p})^{p/2}+1-t\le2^{p/2},\qquad0\le t\le1,
\]
whose left side is increasing.

Boundary checks: at \(p=2\), the first branch equals \(\sqrt2\) for every \(n\); at \(n=1\), both branches equal the Hilbert value \(\sqrt2\). No computation is being used as a substitute for an infinite or asymptotic proof.
