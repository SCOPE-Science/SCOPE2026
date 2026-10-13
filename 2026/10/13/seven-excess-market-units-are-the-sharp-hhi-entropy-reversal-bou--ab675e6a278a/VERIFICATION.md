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
For a fixed number of firms \(k\), write each positive integer market size as
\[
n_i=1+y_i
\]
with
\[
\sum_i y_i=r=N-k.
\]

At fixed \(k\) and \(r\), Herfindahl ranking is exactly ranking by
\[
Q(y)=\sum_i y_i^2.
\]

Entropy satisfies
\[
E
=
\log N
-
\frac1N
\log W(y),
\qquad
W(y)=\prod_i(1+y_i)^{1+y_i},
\]
so smaller entropy is exactly larger \(W(y)\).

The embedded `verify_hhi_entropy_excess_boundary.py` enumerates every integer partition of each excess total
\[
0\le r\le7
\]
and compares every unordered pair using exact integers.

It verifies strict-reversal counts
\[
0,0,0,0,0,0,0,1.
\]

The unique first reversing excess pair is
\[
(3,4)
\]
versus
\[
(1,1,5).
\]

After restoring the mandatory one unit per firm, this gives
\[
(1,\ldots,1,4,5)
\]
versus
\[
(1,\ldots,1,2,2,6).
\]

For the three-firm witness,
\[
(1,4,5)
\]
has Herfindahl numerator \(42\) and entropy product \(800000\), while
\[
(2,2,6)
\]
has Herfindahl numerator \(44\) and entropy product \(746496\).

Run:

`python3 verify_hhi_entropy_excess_boundary.py`

The first output line must be:

`VERIFY_OK`

The finite script also reconstructs and checks the theorem for every
\[
3\le k\le100.
\]
The proof for all \(k\ge3\) is symbolic: padding an excess partition by zeros changes neither \(Q\) nor \(W\).
