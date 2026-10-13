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

For the equality family
\[
A=\operatorname{diag}(1,\kappa),
\qquad
d=(\kappa,1)^{\mathsf T},
\]
the minimal-residual smoothing projection is
\[
P_d
=
\frac12
\begin{pmatrix}
1&-\kappa\\
-1/\kappa&1
\end{pmatrix}.
\]
It is idempotent and rank one. Therefore its unique nonzero singular value equals its Frobenius norm,
\[
\|P_d\|_2
=
\frac{\kappa^2+1}{2\kappa}.
\]

For
\[
e=(1,-\kappa)^{\mathsf T},
\]
the checker verifies
\[
\eta_*=\frac{\kappa^2-1}{2\kappa}
\]
and equality in the Euclidean error bound.

At
\[
\kappa=3,
\]
the exact ratios are
\[
\frac{\|e^+\|_2}{\|e\|_2}
=
\frac53,
\qquad
\frac{\|Ae^+\|_2^2}{\|Ae\|_2^2}
=
\frac{25}{41}.
\]

Finite replay is corroborative only. The global maximization over every SPD matrix of condition number \(\kappa\) follows from the spectral endpoint inequality proved in `RESULT.md`.

Unproved limits include direction restrictions imposed by a particular primary solver, nonsymmetric systems, weighted or block residual smoothing, and finite-precision residual gaps.
