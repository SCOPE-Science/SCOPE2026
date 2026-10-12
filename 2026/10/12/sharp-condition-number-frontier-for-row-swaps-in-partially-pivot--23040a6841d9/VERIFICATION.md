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
The universal theorem is analytic. The standalone checker replays exact and high-precision consequences.

For the rational witness
\[
A_9=
\begin{pmatrix}
18&24\\
24&82
\end{pmatrix},
\]
the checker verifies
\[
\operatorname{tr}(A_9)=100,
\qquad
\det(A_9)=900.
\]
Hence the characteristic polynomial is
\[
\lambda^2-100\lambda+900
=
(\lambda-10)(\lambda-90),
\]
so
\[
\kappa_2(A_9)=9.
\]
The first multiplier is exactly
\[
\frac{24}{18}
=
\frac43>1,
\]
which forces partial pivoting to interchange the first two rows.

The checker also evaluates
\[
\kappa_*=3+2\sqrt2
\]
at high precision and verifies
\[
\frac{\kappa_*-1}{2\sqrt{\kappa_*}}=1.
\]
For the representative safe value
\[
\kappa=4,
\]
it verifies the sharp upper bound
\[
\frac{\kappa-1}{2\sqrt\kappa}=\frac34<1.
\]

Finite replay is supporting evidence only. The all-dimension result follows from the Schur-complement spectral enclosure and the exact \(2\times2\) optimization in `RESULT.md`.

No claim is made about floating-point comparisons near a tie, scaling-invariant pivot policies, sparse permutations, or pivoting strategies other than classical scalar partial pivoting.
