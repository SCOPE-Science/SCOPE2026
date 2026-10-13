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
Write positive integer species abundances as
\[
n_i=1+y_i,
\qquad
\sum_i y_i=r.
\]

At fixed richness and total abundance, Berger–Parker ranking is exactly ranking by
\[
M(y)=\max_i y_i,
\]
while Simpson concentration is exactly ranking by
\[
Q(y)=\sum_i y_i^2.
\]

The embedded `verify_berger_parker_simpson_boundary.py` enumerates every integer partition of
\[
0\le r\le8
\]
and compares every unordered pair using exact integer arithmetic.

It verifies strict-reversal counts
\[
0,0,0,0,0,0,0,0,4.
\]

The universal first-layer witness is excess
\[
(1,2,5)
\]
versus
\[
(4,4),
\]
which restores to
\[
(1,\ldots,1,2,3,6)
\]
versus
\[
(1,\ldots,1,5,5).
\]

For three species this is
\[
(2,3,6)
\]
versus
\[
(1,5,5).
\]

The script verifies fixed-richness first-layer counts
\[
1,2,3,4
\]
for
\[
k=3,4,5,\ge6,
\]
checks the universal witness through \(k=100\), and confirms that the population and finite-sample Simpson formulas induce identical fixed-total rankings.

Run:

`python3 verify_berger_parker_simpson_boundary.py`

The first output line must be:

`VERIFY_OK`

The all-\(k\) claim does not rely on the finite \(k\le100\) replay. It follows because zero excess coordinates leave both \(M\) and \(Q\) unchanged.
