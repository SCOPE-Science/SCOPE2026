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

The model has the triangular form
\[
\dot C=f(C,B),\qquad
\dot B=g(C,B),\qquad
\dot z=H(C,B).
\]
Because no right-hand side contains \(z\), replacing \(z(t)\) by \(z(t)+c\) leaves all three differential equations unchanged. This is an exact identity, not a linear approximation.

At a cell equilibrium with
\[
H(C_*,B_*)=0,
\]
every value of \(z\) gives a full equilibrium. A nearby equilibrium obtained by changing \(z\) alone never approaches the original point, which directly excludes local asymptotic stability of that point.

For a \(T\)-periodic cell orbit,
\[
z(t+T)-z(t)
=
\int_t^{t+T}H(C(s),B(s))\,ds.
\]
The integrand is \(T\)-periodic, so the integral is independent of \(t\) and equals
\[
\Delta=
\int_0^T H(C(s),B(s))\,ds.
\]
Repeating the identity yields
\[
z(t+nT)=z(t)+n\Delta.
\]
Therefore \(\Delta=0\) is both necessary and sufficient for the full trajectory to be \(T\)-periodic.

The motivating publisher PDF was inspected directly. It prints equation (2.3) with no \(z\)-dependence and explicitly states that equation (2.3) is isolated before the stability analysis of equations (2.1) and (2.2). The proof therefore applies to the actual published system.

No numerical experiment is needed for the theorem, and no finite simulation is used as evidence of an infinite-time claim.
