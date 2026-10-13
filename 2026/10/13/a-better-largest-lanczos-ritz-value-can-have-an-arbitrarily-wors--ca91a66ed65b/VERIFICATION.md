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
The analytic proof is in `RESULT.md`. The standalone checker replays exact algebra and one high-precision finite witness.

For
\[
\varepsilon=\frac1{10},
\]
the first squared Ritz residual is exactly
\[
\frac{281}{40401}.
\]
The two-step generalized Ritz polynomial is exactly
\[
2810\theta^2-7611\theta+4882.
\]
The checker selects its larger root, reconstructs the corresponding generalized eigenvector from the exact Gram and projected matrices, normalizes the physical Ritz vector, and evaluates its residual.

The resulting numerical values are approximately
\[
\rho_\varepsilon=1.054726368159204,
\qquad
\|r^{(1)}_\varepsilon\|_2=0.083398281662887,
\]
\[
\theta_\varepsilon=1.665207655517674,
\qquad
\|r^{(2)}_\varepsilon\|_2=0.449903178976340.
\]
Thus the finite residual ratio exceeds
\[
5.39
\]
while the largest Ritz value moves toward \(2\).

The checker also verifies the limiting generalized pencil exactly:
\[
G_0=
\begin{pmatrix}
2&-1\\
-1&2
\end{pmatrix},
\qquad
H_0=
\begin{pmatrix}
2&-1\\
-1&3
\end{pmatrix}.
\]
Its generalized eigenvalues are \(1\) and \(5/3\). The coefficient vector \((1,2)^{\mathsf T}\) produces the physical vector \((-1,1,2)^{\mathsf T}\), and its normalized residual at \(5/3\) has exact squared norm \(2/9\).

Finite replay is corroborative only. The divergent ratio, strict variational improvement, and dimension-three minimality are proved analytically.

Unproved limits include higher Krylov dimensions, restarted methods, finite precision, and any typical-case distribution of residual spikes.
