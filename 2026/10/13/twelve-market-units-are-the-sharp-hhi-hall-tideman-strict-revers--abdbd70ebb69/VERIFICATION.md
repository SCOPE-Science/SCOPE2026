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
For a positive-integer market profile of total \(N\), define
\[
Q=\sum_i n_i^2.
\]

After sorting the profile in descending order
\[
d_1\ge\cdots\ge d_k,
\]
define
\[
R=\sum_{i=1}^k i d_i.
\]

Then
\[
H=\frac{Q}{N^2}
\]
and
\[
\mathrm{HTI}=\frac{N}{2R-N}.
\]

Thus, at fixed \(N\), HHI increases with \(Q\), while Hall–Tideman decreases with \(R\).

The embedded `verify_hhi_hti_boundary.py` generates every positive integer profile for
\[
2\le N\le12,\qquad 2\le k\le N,
\]
in two independent ways and checks all
\[
762
\]
within-\((k,N)\) unordered pairs.

It verifies weak-order agreement through \(N=9\), the unique tie split at \(N=10\), no strict reversal through \(N=11\), and exactly one strict reversal at \(N=12\):
\[
(1,2,4,5)
\quad\text{versus}\quad
(2,2,2,6).
\]

Run:

`python3 verify_hhi_hti_boundary.py`

The first output line must be:

`VERIFY_OK`

All classification comparisons use exact integers or rational numbers.
