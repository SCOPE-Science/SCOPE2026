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
For two positive household incomes with fixed total \(S\), write their absolute gap as
\[
d.
\]
Their product is
\[
\frac{S^2-d^2}{4},
\]
so both Gini inequality and the \(\epsilon=1\) Atkinson index increase with \(d\).

For three sorted incomes
\[
a\le b\le c,
\qquad
a+b+c=S,
\]
the exact ranking quantities are
\[
R=c-a
\]
for Gini and
\[
P=abc
\]
with reversed order for Atkinson.

The embedded `verify_gini_atkinson1_boundary.py` enumerates every positive sorted integer triple for
\[
3\le S\le11
\]
and every unordered pair.

It verifies strict-reversal counts
\[
0,0,0,0,0,0,0,0,1.
\]

It verifies the first weak-order split at total
\[
S=9
\]
for
\[
(1,4,4)
\quad\text{versus}\quad
(2,2,5),
\]
which tie under Gini but have products \(16\) and \(20\).

It verifies the unique first strict reversal at total
\[
S=11
\]
for
\[
(1,5,5)
\quad\text{versus}\quad
(2,2,7),
\]
with Gini values
\[
\frac8{33}
\quad\text{and}\quad
\frac{10}{33}
\]
and products
\[
25
\quad\text{and}\quad
28.
\]

Run:

`python3 verify_gini_atkinson1_boundary.py`

The first output line must be:

`VERIFY_OK`

The finite enumeration is exhaustive for the stated integer boundary. The two-household equivalence and three-household range-product criterion are proved symbolically in the result text.
