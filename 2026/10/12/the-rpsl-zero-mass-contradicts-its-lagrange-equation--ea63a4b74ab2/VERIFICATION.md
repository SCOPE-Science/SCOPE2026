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
The RPSL construction defines
\[
\psi(u)=u g(\psi(u)).
\]
At \(u=0\),
\[
\psi(0)=0.
\]
Thus its generating series has no zero-degree probability.

Lagrange inversion gives
\[
p_n=\frac1n[z^{n-1}]g(z)^n,\qquad n\ge1.
\]
For
\[
g(z)=c+(1-c)\left(\frac{1-\theta}{1-\theta z}\right)^\gamma,
\]
the offspring mean is
\[
m=g'(1)=\frac{(1-c)\gamma\theta}{1-\theta}.
\]
The finite coefficient mass is the smallest fixed point
\[
q=g(q).
\]
It equals one when \(m\le1\) and is below one when \(m>1\).

At \((\gamma,\theta,c)=(1.5,0.4,0.3)\),
\[
m=0.7,\qquad g(0)=0.625331\ldots,
\]
so the positive coefficients already have total mass one and the source's added zero atom would raise the total above one.

The included checker computes Lagrange coefficients from the actual generator, accumulates them in a subcritical example, and compares them with the extinction fixed point in a supercritical example. The phase theorem itself is analytic.
