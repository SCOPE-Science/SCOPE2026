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
The universal theorem is analytic. The checker replays the threshold identities and exact witness.

The sharp spread parameter is
\[
\delta_*^2
=
\frac{97-26\sqrt{13}}{27},
\]
with
\[
\kappa_*
=
\frac{1+\delta_*}{1-\delta_*}.
\]
The checker verifies numerically at high precision that
\[
9\kappa_*^4+\kappa_*^3-43\kappa_*^2+\kappa_*+9=0
\]
and that
\[
\kappa_*
=
2.0639445610119587707\ldots.
\]

For the exact witness
\[
A=
\begin{pmatrix}
1&1/2\\
1/2&1
\end{pmatrix},
\qquad
g=
\begin{pmatrix}
1\\
-9/10
\end{pmatrix},
\]
the checker verifies that coordinate \(1\) is the unique GSL choice, that exact coordinate minimization produces
\[
g^+
=
\begin{pmatrix}
0\\
-7/5
\end{pmatrix},
\]
that the objective decrease equals
\[
1/2,
\]
and that
\[
\frac{\|g^+\|_2^2}{\|g\|_2^2}
=
\frac{196}{181}>1.
\]

It also checks representative matrices just below and above the analytic frontier against the fixed-matrix condition
\[
q^2+2qs\le1.
\]

Finite replay is corroborative only. The all-matrix threshold follows from the constrained minimization in `RESULT.md`.

Unproved limits include dimensions three and higher, block rules, approximate GSL selection, inexact coordinate minimization, proximal variants, and finite-precision effects.
