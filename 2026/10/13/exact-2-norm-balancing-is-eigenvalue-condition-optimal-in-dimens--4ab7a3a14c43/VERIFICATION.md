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
The universal statements are proved analytically in `RESULT.md`. The finite checker replays exact identities for the displayed three-dimensional family.

For
\[
B_t=
\begin{pmatrix}
t+1&t&1\\
t&t+1&1\\
1&-1&2t+2
\end{pmatrix},
\]
the characteristic polynomial is
\[
(\lambda-1)(\lambda-(2t+1))(\lambda-(2t+2)).
\]
At
\[
\lambda_t=2t+2,
\]
the right and left eigenvectors
\[
x=(1,1,1)^{\mathsf T},
\qquad
z=
\left(
\frac1{2t+1},
-\frac1{2t+1},
1
\right)^{\mathsf T}
\]
satisfy
\[
z^{\mathsf T}x=1.
\]

The squared condition numbers are
\[
\chi(\lambda_t,B_t)^2
=
\frac{3(4t^2+4t+3)}{(2t+1)^2},
\]
and
\[
\chi(\lambda_t,A_t)^2
=
\frac{(2t+3)^2}{(2t+1)^2}.
\]
Their difference is
\[
\frac{8t^2}{(2t+1)^2}.
\]

The checker also verifies
\[
\|A_t\|_{\mathrm F}^2-\|B_t\|_{\mathrm F}^2
=
\frac{8t^2}{2t+1}
\]
for representative rational parameters and reconstructs the \(t=1\) condition-number values through exact squared quantities.

Finite replay is corroborative only. The all-\(2\times2\) minimization rests on the explicit condition-number formula and arithmetic-geometric mean inequality.

Unproved limits include the globally largest possible harmful factor in dimension three, finite-precision power-of-two balancing, and eigenvector or invariant-subspace conditioning.
