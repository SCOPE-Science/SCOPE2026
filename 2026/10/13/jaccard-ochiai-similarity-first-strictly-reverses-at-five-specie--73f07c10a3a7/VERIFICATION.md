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
For a normalized Venn signature
\[
(a,b,c),
\qquad
a>0,\quad b\le c,
\]
define
\[
u=\frac{b+c}{a},
\qquad
v=\frac{bc}{a^2}.
\]

Then
\[
J=\frac1{1+u}
\]
and
\[
O^2=\frac1{1+u+v}.
\]

The embedded `verify_jaccard_ochiai_minimal_reversal.py` independently constructs all signatures through the first boundary in two ways:
- integer Venn-count enumeration;
- all nonempty subset pairs of a finite species universe followed by canonical Venn reduction.

It verifies exact signature counts
\[
1,\ 3,\ 7,\ 13,\ 22
\]
through gamma-richness bounds \(1\) to \(5\), weak-order mismatch counts
\[
0,\ 0,\ 1,\ 5,\ 12,
\]
and strict-reversal counts
\[
0,\ 0,\ 0,\ 0,\ 1.
\]

The unique first strict reversal is
\[
(1,0,4)
\quad\text{versus}\quad
(1,1,2),
\]
with
\[
J=\frac15,\frac14
\]
and
\[
O^2=\frac15,\frac16.
\]

The replay also verifies the exact ordering-key criterion on every checked pair and checks the structural family
\[
(1,0,r+2)
\quad\text{versus}\quad
(1,1,r)
\]
for every integer \(2\le r\le500\).

Run:

`python3 verify_jaccard_ochiai_minimal_reversal.py`

The first output line must be:

`VERIFY_OK`

The algebraic criterion and infinite family are proved in `RESULT.md`; the finite replay is the exhaustive certificate for the sharp first boundary.
