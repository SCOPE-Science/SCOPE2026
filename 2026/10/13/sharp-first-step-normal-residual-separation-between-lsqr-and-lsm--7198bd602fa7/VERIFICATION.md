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
The universal theorem is analytic. The checker replays exact rational instances of both first-step minimizers.

For
\[
A=\operatorname{diag}(1,3),
\qquad
b=(3,1/3)^{\mathsf T},
\]
one has
\[
g=A^{\mathsf T}b=(3,1)^{\mathsf T}.
\]
The first LSQR and LSMR line-search coefficients are
\[
t_Q=5/9,
\qquad
t_M=1/5.
\]
The checker verifies
\[
\frac{\|A^{\mathsf T}r_Q\|_2^2}{\|A^{\mathsf T}b\|_2^2}
=
\frac{16}{9},
\]
and
\[
\frac{\|A^{\mathsf T}r_M\|_2^2}{\|A^{\mathsf T}b\|_2^2}
=
\frac{16}{25}.
\]
Therefore
\[
\frac{\|A^{\mathsf T}r_Q\|_2}{\|A^{\mathsf T}r_M\|_2}
=
\frac53,
\]
which equals the sharp condition-number factor
\[
\frac{3^2+1}{2\cdot3}.
\]

The checker repeats the equality-family identities for several rational \(\kappa>1\). Finite replay is corroborative only; the all-matrix upper bound follows from the spectral secant argument in `RESULT.md`.

Unproved limits include later Krylov iterations, rank-deficient extensions, damping, preconditioning, and finite-precision loss of orthogonality.
