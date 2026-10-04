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
The classification proof is analytic.

For
\[
p(\lambda)=\lambda^2-T\lambda+D,
\]
the checker independently verifies the exact source-model witness
\[
a=12,\quad b=8,\quad c=1,\quad d=4,\quad e=1,\quad f=8,\quad
\alpha=\frac1{10},\quad\beta=1.
\]
It reconstructs
\[
(H^*,P^*)=\left(1,\frac{79}{10}\right)
\]
and
\[
J^*=
\begin{pmatrix}
-5&-\frac12\\[2mm]
\frac{79}{5}&1
\end{pmatrix}.
\]
Thus
\[
T=-4,\qquad D=\frac{29}{10},
\]
and
\[
\lambda_{\pm}=-2\pm\sqrt{\frac{11}{10}}.
\]

The script verifies that the source's source predicate and saddle predicate both hold, while exactly one multiplier lies inside the unit circle.

It also verifies
\[
p(1)=\frac{79}{10}>0,\qquad p(-1)=-\frac1{10}<0,
\]
matching the independent standard polynomial saddle test inspected in related literature.
