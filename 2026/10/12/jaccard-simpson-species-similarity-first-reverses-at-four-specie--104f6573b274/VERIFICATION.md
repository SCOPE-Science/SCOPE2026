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
The proof reduces both similarities to exact monotone functions of two mismatch ratios.

After normalizing site labels so that
\[
b\le c,
\]
\[
S=\frac{1}{1+b/a},
\qquad
J=\frac{1}{1+(b+c)/a}.
\]

Therefore two signatures reverse exactly when
\[
\left(
\frac{b}{a}-\frac{B}{A}
\right)
\left(
\frac{b+c}{a}-\frac{B+C}{A}
\right)
<0.
\]

The embedded `verify_jaccard_simpson_minimal_reversal.py` checks this criterion against direct exact-fraction comparisons for every normalized Venn signature through gamma richness \(8\).

It verifies signature counts
\[
1,\ 4,\ 9,\ 17
\]
through gamma richness \(1,2,3,4\), strict-reversal counts
\[
0,\ 0,\ 0,\ 3,
\]
and exactly the three first-layer pairs
\[
(1,0,2)\leftrightarrow(2,1,1),
\]
\[
(1,0,3)\leftrightarrow(1,1,1),
\]
and
\[
(1,0,3)\leftrightarrow(2,1,1).
\]

It also checks the structural family
\[
(1,0,r)\leftrightarrow(r,1,1)
\]
for every integer
\[
2\le r\le500.
\]

Run:

`python3 verify_jaccard_simpson_minimal_reversal.py`

The first output line must be:

`VERIFY_OK`

The infinite family and general reversal criterion are proved algebraically in `RESULT.md`; the finite replay is a consistency check and an exhaustive certificate for the sharp first boundary.
