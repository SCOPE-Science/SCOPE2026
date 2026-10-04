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

The proof was checked by recomputing the support-spectrum reduction, the area formula, the curvature-density transformation, and the Fejer--Riesz coefficient relations. The scalar objective becomes
\[
J(u)=\frac{80u-156u^2}{15}
=\frac{80}{117}-\frac{52}{5}\left(u-\frac{10}{39}\right)^2,
\]
so the unique scalar optimizer is \(u=10/39\), with \(J=80/117\) and area factor \(1-J/2=77/117\).

For the equality support, direct differentiation gives
\[
p_*+p_*''=\frac{\Lambda}{3}\left(1-\frac{4\sqrt{190}}{39}\cos(2\theta)+\frac{20}{39}\cos(4\theta)\right),
\]
and the identity \(\cos(4\theta)=2\cos^2(2\theta)-1\) factors this as a nonnegative square.

The bundled `verify.py` replays these exact rational identities and checks the trigonometric cancellations numerically. Sampling is not used to establish nonnegativity or global optimality; both are proved algebraically.

Unproved limits: no claim is made about support functions with Fourier modes of degree above \(4\), nor about the unrestricted least-area problem.
