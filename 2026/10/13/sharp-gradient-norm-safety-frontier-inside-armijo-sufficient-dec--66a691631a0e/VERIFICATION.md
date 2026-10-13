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
The universal theorem is analytic. The checker replays exact rational consequences.

For
\[
\sigma=\frac14,
\qquad
\kappa=4,
\qquad
s_0=1,
\]
the sharp scaling gives
\[
A=
\operatorname{diag}
\left(
\frac{15}{16},
\frac{15}{4}
\right).
\]
With
\[
x=
\begin{pmatrix}
32/15\\
4/15
\end{pmatrix},
\qquad
b=0,
\]
the gradient is
\[
g=
\begin{pmatrix}
2\\
1
\end{pmatrix}.
\]
The unit trial is accepted at Armijo equality:
\[
f(x^+)-f(x)
=
-\frac54
=
-\sigma\|g\|_2^2.
\]
The new gradient is
\[
g^+
=
\begin{pmatrix}
1/8\\
-11/4
\end{pmatrix},
\]
and
\[
\frac{\|g^+\|_2^2}{\|g\|_2^2}
=
\frac{97}{64}.
\]

The checker also verifies for several exact rational parameter pairs that the sharp endpoint formula is nonexpansive exactly when
\[
\sigma
\ge
\left(
\frac{\kappa-1}{\kappa+1}
\right)^2.
\]

Finite replay is corroborative only. The all-dimensional spectral-moment bound and interval maximization are proved in `RESULT.md`.

Unproved limits include Wolfe-type line searches, nonquadratic strongly convex objectives, preconditioned directions, and finite-precision acceptance behavior.
