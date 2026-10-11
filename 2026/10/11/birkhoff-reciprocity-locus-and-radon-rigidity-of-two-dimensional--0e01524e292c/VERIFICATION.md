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

For \(0<t<1\), define
\[
x_t=(1,t),\qquad a=\omega t^{q-1},\qquad y_t=(a,-1).
\]
Because \(1<q<\infty\), both points lie in smooth sectors. The derivative of \(N_{\omega,q}^q\) at \(x_t\) is proportional to
\[
(1,\omega t^{q-1}),
\]
so its pairing with \(y_t\) vanishes. Hence \(x_t\perp_B y_t\).

At \(y_t\), the second coordinate has larger magnitude and the derivative is proportional to
\[
(\omega a^{q-1},-1).
\]
Thus
\[
y_t\perp_B x_t
\iff \omega a^{q-1}=t
\iff \omega^q t^{(q-1)^2}=t
\iff \omega^q t^{q(q-2)}=1.
\]
No numerical approximation enters this equivalence.

For \(q>2\), the left side is strictly below \(1\) on \(0<t<1\). For \(q=2\), it is \(\omega^2\), so reciprocity for every smooth direction occurs exactly at \(\omega=1\). For \(1<q<2\) and \(0<\omega<1\), there is exactly one solution,
\[
t=\omega^{1/(2-q)}.
\]
When \(\omega=1\) and \(q<2\), the solution moves to the boundary \(t=1\), so no interior smooth parameter is reciprocal.

A Radon plane requires symmetry for every Birkhoff-orthogonal pair. Therefore each non-Euclidean parameter is ruled out by an explicit smooth one-way pair. At \((\omega,q)=(1,2)\), the Lorentz norm equals the Euclidean norm exactly, so symmetry holds globally.

Limits: the nonsmooth exponents \(q=1\) and \(q=\infty\) are outside the theorem. Axial and diagonal seam pairs are not classified because they are unnecessary for the iff Radon conclusion.
