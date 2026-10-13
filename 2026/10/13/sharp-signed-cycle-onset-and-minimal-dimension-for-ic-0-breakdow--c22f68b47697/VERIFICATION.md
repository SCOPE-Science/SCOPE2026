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
The proof is analytic. The checker replays exact special cases and the conditioning identity.

For
\[
A(t)=
\begin{pmatrix}
1&-t&0&t\\
-t&1&-t&0\\
0&-t&1&-t\\
t&0&-t&1
\end{pmatrix},
\]
IC(0) in the natural order has squared pivots
\[
q_1=1,
\qquad
q_2=1-t^2,
\]
\[
q_3=\frac{1-2t^2}{1-t^2},
\qquad
q_4=
\frac{(1-t^2)(1-3t^2)}
{1-2t^2}.
\]

The embedded `verify.py` checks with exact rational arithmetic that:

1. at \(t=1/2\),
\[
(q_1,q_2,q_3,q_4)
=
\left(1,\frac34,\frac23,\frac38\right);
\]

2. at \(t=2/3\),
\[
(q_1,q_2,q_3,q_4)
=
\left(1,\frac59,\frac15,-\frac53\right);
\]

3. scaling by three yields the Kershaw sequence
\[
\left(3,\frac53,\frac35,-5\right);
\]

4. the fourth-pivot numerator is exactly zero at
\[
t^2=\frac13;
\]

5. high-precision decimal arithmetic verifies
\[
\frac{1+\sqrt{2/3}}
{1-\sqrt{2/3}}
=
5+2\sqrt6.
\]

The all-\(n\le3\) safety theorem is proved from positive principal minors and is not established by enumeration.

Unproved limits include a global condition-number threshold over all four-dimensional SPD patterns, reordered IC(0), shifted or modified incomplete Cholesky, threshold dropping, and finite-precision breakdown.
