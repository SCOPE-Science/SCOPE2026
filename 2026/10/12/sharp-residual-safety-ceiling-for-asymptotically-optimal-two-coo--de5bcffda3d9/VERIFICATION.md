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
The universal theorem is analytic. The checker replays exact and high-precision consequences of the formulas.

For
\[
\rho=\frac45,
\qquad
s=\frac35,
\]
the residual-safe ceiling is
\[
\omega_{\mathrm E}
=
\frac{30}{31},
\]
whereas the asymptotically optimal SOR parameter is
\[
\omega_{\mathrm{opt}}
=
\frac54.
\]
At
\[
\omega=\frac54,
\]
the completed-sweep residual matrix is
\[
R=
\begin{pmatrix}
3/4&-1\\
1/4&-1/4
\end{pmatrix}.
\]
The incoming residual
\[
(0,1)^{\mathsf T}
\]
is mapped to
\[
(-1,-1/4)^{\mathsf T},
\]
so the squared Euclidean residual ratio is
\[
17/16.
\]

The embedded `verify.py` also checks the determinant factorization of
\[
I-R^{\mathsf T}R
\]
at several rational Pythagorean values, and confirms at high precision that
\[
\omega_{\mathrm E}
=
\omega_{\mathrm{opt}}
\]
when
\[
\rho^2=\frac12,
\qquad
\kappa=3+2\sqrt2.
\]

Finite replay is corroborative only. The exact all-\(\omega\) safe interval follows from the positive-semidefinite criterion proved in `RESULT.md`.

Unproved limits include a robust unequal-diagonal two-dimensional frontier, higher-dimensional SOR, alternative orderings, block methods, SSOR, and finite precision.
