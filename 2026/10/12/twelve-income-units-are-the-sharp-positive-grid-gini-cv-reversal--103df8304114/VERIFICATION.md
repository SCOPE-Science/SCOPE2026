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
For fixed household count \(n\) and fixed total income \(S\), define
\[
D(x)=\sum_{i<j}|x_i-x_j|
\]
and
\[
Q(x)=\sum_i(nx_i-S)^2.
\]
Then
\[
G(x)=\frac{D(x)}{nS}
\]
and
\[
V(x)^2=\frac{Q(x)}{nS^2}.
\]
Thus exact integer comparison of \(D\) and \(Q\) is sufficient.

The embedded `verify_gini_cv_integer_boundary.py` generates every nondecreasing positive integer partition for every
\[
2\le S\le12
\]
and every admissible household count.

It compares every unordered pair within the same \((n,S)\) slice. The total number of comparisons through the sharp layer is
\[
762.
\]

It verifies zero strict reversals for
\[
S\le11
\]
and exactly one at
\[
S=12,
\]
namely
\[
(1,2,4,5)
\quad\text{versus}\quad
(2,2,2,6).
\]

It also verifies the unique first weak-order disagreement at total \(10\), checks the displayed Gini and squared-CV fractions exactly, and replays the two-household identity.

Run:

`python3 verify_gini_cv_integer_boundary.py`

The first output line must be:

`VERIFY_OK`

The lower cutoff is exhaustive rather than inferential: positivity implies \(n\le S\), so every admissible profile below the claimed total is explicitly included.
