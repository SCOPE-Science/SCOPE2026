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
The universal proof is analytic. This file records replay checks for the exact identities.

For
\[
A=
\begin{pmatrix}
a&c\\
c&b
\end{pmatrix},
\qquad
p=\frac{|c|}{a},
\qquad
q=\frac{|c|}{b},
\]
diagonal-proportional randomized Gauss-Seidel has conditional expected residual matrix
\[
M
=
\frac1{p+q}
\begin{pmatrix}
p(1+pq)&-2pq\\
-2pq&q(1+pq)
\end{pmatrix}.
\]
The proof factors
\[
\det(I-M)
=
\frac{pq}{(p+q)^2}
(pq-p-q-1)(pq+p+q-1).
\]

The embedded `verify.py` checks exact rational instances of this identity and replays
\[
A=
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix},
\qquad
r=(1,-1)^{\mathsf T},
\]
for which both coordinate choices give squared residual norm \(9/4\) from an incoming squared norm \(2\).

It also checks the equal-diagonal family formula
\[
\frac{\mathbb E\|r^+\|_2^2}{\|r\|_2^2}
=
\frac{2\kappa^2}{(\kappa+1)^2}
\]
at rational condition numbers.

Finite replay is corroborative only. The all-orientation threshold
\[
\kappa\le1+\sqrt2
\]
is established by the analytic rotation reduction in `RESULT.md`.

Unproved limits include higher dimensions, alternative sampling laws, delayed or asynchronous updates, finite precision, block coordinates, and multi-step path maxima.
