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
The structural proof is analytic and the finite grid statement is exhaustive.

For two parties, every discrepancy vector has the form
\[
(x,-x),
\]
so
\[
L=G=|x|.
\]

For three parties, after permutation and global sign,
\[
d=(a,b,-a-b),
\qquad a,b\ge0.
\]
Putting
\[
L=a+b,
\qquad h=|a-b|,
\]
gives
\[
G^2=\frac{3L^2+h^2}{4}.
\]
This identity yields both the sharp band
\[
\frac{\sqrt3}{2}L\le G\le L
\]
and the exact reversal criterion.

The embedded `verify_lh_gallagher_three_party_boundary.py` enumerates every positive three-part vote composition and every positive three-part seat composition for each common denominator
\[
3\le N\le11.
\]
It deduplicates the induced labeled discrepancy vectors and compares every unordered pair using exact rational arithmetic.

The realizable-vector counts are
\[
1,7,19,37,61,91,127,169,217,
\]
and the strict-reversal counts are
\[
0,0,0,0,0,0,0,0,36.
\]

At \(N=11\), every reversing pair is, up to party permutation and swapping votes with seats, the pair
\[
(7,-7,0)
\]
and
\[
(-8,4,4).
\]

Run:

`python3 verify_lh_gallagher_three_party_boundary.py`

The first output line must be:

`VERIFY_OK`
