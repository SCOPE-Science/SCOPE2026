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
The universal proof is analytic. This file records replay checks for its algebraic consequences.

For a unit secant direction, put
\[
q=s^{\mathsf T}Hs.
\]
The sharp endpoint moment bound is
\[
m^2\le(q-1)(\kappa-q).
\]
At equality the active \(2\times2\) BFGS block has determinant \(q\) and trace
\[
\kappa+2-\frac{\kappa}{q}.
\]
The normalized trace is maximized at
\[
q_*=\frac{3\kappa}{\kappa+2}.
\]

The resulting worst condition number is
\[
\Gamma(\kappa)
=
\frac{
\left[
(\kappa+2)^{3/2}
+
(\kappa-1)\sqrt{\kappa+8}
\right]^2
}{
27\kappa
}.
\]

The embedded `verify.py` checks exact rational identities for several values of \(\kappa\), confirms the optimizer \(q_*\), compares the closed form with the eigenvalue ratio obtained from trace and determinant, and replays the exact \(\kappa=4\) example with
\[
\operatorname{tr}(B_1)=4,
\qquad
\det(B_1)=2.
\]

Finite replay is corroborative only. The all-dimension supremum follows from the spectral second-moment inequality and the explicit endpoint construction in `RESULT.md`.

Unproved limits include arbitrary initial scalar scaling, multiple updates, finite precision, nonquadratic secant pairs, and structurally restricted Hessian classes.
