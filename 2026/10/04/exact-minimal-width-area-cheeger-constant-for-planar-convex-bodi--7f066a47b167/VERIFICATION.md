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

The proof has no computational premise.

For any admissible set \(X\), let
\[
K=\overline{\operatorname{conv}}(X).
\]
Then
\[
\omega(K)=\omega(X),
\qquad
A(X)\le A(K).
\]
If \(u\) is a minimum-width direction and \(v\perp u\), the orthogonal bounding rectangle gives
\[
A(K)\le w_u(K)w_v(K)
=
\omega(X)w_v(K)
\le
\omega(X)D(\Omega).
\]
This verifies the universal lower bound.

For the upper bound, a diameter segment of length \(D(\Omega)\) and any interior point at perpendicular height \(h\) span a triangle contained in \(\Omega\). At height \(s\), its section parallel to the diameter has length
\[
D(\Omega)\left(1-\frac{s}{h}\right).
\]
Integrating from \(0\) to \(t\) gives
\[
D(\Omega)t\left(1-\frac{t}{2h}\right).
\]
The corresponding ambient slice lies in a strip of width \(t\), so its quotient is at most
\[
\frac{1}{D(\Omega)\left(1-\frac{t}{2h}\right)},
\]
which tends to \(1/D(\Omega)\).

For nonattainment, equality in the full lower-bound chain would force a positive-width convex hull to fill an orthogonal rectangle with side lengths \(\omega(X)\) and \(D(\Omega)\). That rectangle has diagonal
\[
\sqrt{D(\Omega)^2+\omega(X)^2}>D(\Omega),
\]
contradicting containment in \(\Omega\).

No finite experiment, timeout, or numerical approximation is used as evidence for the theorem.
