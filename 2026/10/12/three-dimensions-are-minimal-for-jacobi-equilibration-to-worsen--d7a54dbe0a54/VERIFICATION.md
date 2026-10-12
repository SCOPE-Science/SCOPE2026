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
The proof is analytic. The checker replays exact special cases and selected consequences.

For
\[
A=
\begin{pmatrix}
a&c\\
c&b
\end{pmatrix}>0,
\]
the proof uses
\[
q^2-\rho^2
=
\frac{(a-b)^2(ab-c^2)}{ab(a+b)^2},
\qquad
\rho=\frac{|c|}{\sqrt{ab}}.
\]
The embedded `verify.py` checks this identity for several exact rational SPD matrices.

For the three-dimensional family
\[
A_\kappa
=
I+\frac{\kappa-1}{9}uu^{\mathsf T},
\qquad
u=(1,-2,-2)^{\mathsf T},
\]
the checker verifies the rank-one spectral identity and evaluates the closed equilibrated condition-number formula at representative values.

At \(\kappa=10\), it uses exact arithmetic for
\[
A=
\begin{pmatrix}
2&-2&-2\\
-2&5&4\\
-2&4&5
\end{pmatrix}
\]
and confirms the generalized-eigenvalue data corresponding to
\[
\frac15,
\qquad
\frac{7-2\sqrt6}{5},
\qquad
\frac{7+2\sqrt6}{5}.
\]

Finite replay is corroborative only. The universal \(2\times2\) theorem and the all-\(\kappa>1\) counterfamily are established symbolically in `RESULT.md`.

Unproved limits include the globally largest possible Jacobi-induced condition-number deterioration in three or higher dimensions and analogous questions for other scaling norms.
