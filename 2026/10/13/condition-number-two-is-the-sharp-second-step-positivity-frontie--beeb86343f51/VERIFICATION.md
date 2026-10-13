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
The universal proof is analytic.

With
\[
m_j=\sum_i b_i^2\lambda_i^j,
\]
the second-step GMRES normal equations imply
\[
c=
\frac{m_1m_3-m_2^2}{m_2m_4-m_3^2},
\qquad
\frac ac=
\frac{m_1m_4-m_2m_3}{m_1m_3-m_2^2}.
\]
The exact pairwise identities
\[
m_1m_3-m_2^2
=
\sum_{i<j}
b_i^2b_j^2\lambda_i\lambda_j(\lambda_i-\lambda_j)^2
\]
and
\[
m_1m_4-m_2m_3
=
\sum_{i<j}
b_i^2b_j^2\lambda_i\lambda_j(\lambda_i-\lambda_j)^2
(\lambda_i+\lambda_j)
\]
show that \(a/c\) is a weighted average of active pair sums.

Hence
\[
\frac ac\ge2\mu.
\]
Because
\[
(x_2)_i
=
cb_i\left(\frac ac-\lambda_i\right),
\]
condition number at most \(2\) is sufficient for universal componentwise nonnegativity.

For every \(\kappa>2\), the three-point family in `RESULT.md` makes the top coordinate negative whenever
\[
0<\delta^2<
\frac{(\kappa-2)^3}
{\kappa^4+16(\kappa-1)^2}.
\]

The embedded `verify.py` checks the moment pair expansions on exact rational datasets and replays the concrete witness
\[
A=\operatorname{diag}\left(1,\frac32,3\right),
\qquad
b=\left(1,1,\frac1{20}\right)^{\mathsf T}.
\]
It verifies
\[
a=\frac{833}{545},
\qquad
c=\frac{306}{545},
\qquad
(x_2)_3=-\frac{17}{2180}.
\]

Finite calculations corroborate the formulas but do not replace the universal proof.

Unproved limits include later iterations, arbitrary SPD coordinate bases, general Stieltjes matrices, restarted or preconditioned variants, and finite precision.
