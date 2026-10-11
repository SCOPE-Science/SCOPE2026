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

The source reduction for the complex exponential class is
\[
T_6(1)=D^2,
\qquad
D=
\frac{
(4-s)^2-w^2
}{16},
\]
where
\[
s=v_1^2,
\qquad
w=v_2,
\qquad
|w|\le1-|s|.
\]

Set
\[
t=|s|.
\]
Then
\[
16|D|
=
\left|
(4-s)^2-w^2
\right|
\ge
|4-s|^2-|w|^2.
\]
The coefficient constraint and the ordinary triangle inequality give
\[
|4-s|^2-|w|^2
\ge
(4-t)^2-(1-t)^2
=
15-6t.
\]
Since
\[
0\le t\le1,
\]
\[
15-6t\ge9.
\]
Therefore
\[
|D|\ge\frac9{16}
\]
and
\[
|T_6(1)|\ge\frac{81}{256}.
\]

For equality, the last inequality forces
\[
t=1.
\]
Then
\[
w=0,
\]
and equality in
\[
|4-s|\ge4-|s|
\]
forces
\[
s=1.
\]
Thus
\[
v_1=\pm1.
\]
Schwarz's lemma gives
\[
v(\zeta)=\pm\zeta.
\]
Conversely these two maps give
\[
D=\frac9{16}
\]
and hence equality.

The source proves the complementary sharp upper bound
\[
|T_6(1)|
\le
\frac{625}{256}.
\]

A large random sample of admissible pairs
\[
(s,w),
\qquad
|w|\le1-|s|,
\]
was evaluated only as a consistency check and approached the lower endpoint from above. The proof is exact and does not rely on numerical sampling.
