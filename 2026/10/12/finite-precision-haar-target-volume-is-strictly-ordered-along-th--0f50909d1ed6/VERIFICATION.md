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

The exact source expression checked is
\[
V_a(c)=\frac{A(a)-B(a)\cos(2c)+C(a)\cos(4c)}{2\pi},
\]
with the controlled-edge domain \(0\le a\le c\le\pi/2\). Symbolic differentiation gives exactly
\[
\frac{\partial V_a}{\partial c}=\frac{\sin(2c)}{\pi}\bigl(B(a)-4C(a)\cos(2c)\bigr).
\]

For \(t=\tan(a/2)\), exact half-angle reduction gives
\[
C(a)=\frac{48t^2(1-t^2)}{(1+t^2)^3}\bigl(2t-2\arctan t\bigr)>0
\]
and
\[
B(a)-4C(a)=\frac{48t^2}{(1+t^2)^3}F(t),
\]
where
\[
F(t)=6(1-t^2)\arctan t+8t^3-6t.
\]
With
\[
G(t)=2t^3+t-(1+t^2)\arctan t,
\]
the two exact derivative identities are
\[
F'(t)=\frac{12t}{1+t^2}G(t),
\qquad
G'(t)=2t\bigl(3t-\arctan t\bigr).
\]
For \(t>0\), \(3t-\arctan t>0\), and \(F(0)=G(0)=0\). Hence \(B(a)>4C(a)>0\) throughout \(0<a<\pi/2\). Combining this with \(\sin(2c)>0\) for \(c<\pi/2\) proves the strict derivative sign over the entire admissible interior.

The proof was algebraically replayed from these formulas. The source page containing Eq. (48) and its domain was visually inspected. No floating-point threshold, random search, finite grid, or unproved asymptotic is used as a certificate.

Limits: the conclusion applies to the normalized Haar coordinate-cube target in the cited convention and only to the controlled-gate edge. It does not certify an ordering for arbitrary physical control errors or alternative target geometries.
