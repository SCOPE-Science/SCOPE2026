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
For balanced arm size \(m\), each admissible table is an integer pair
\[
(t,c)
\]
with
\[
1\le t<c\le m-1.
\]

The embedded `verify_arr_rrr_minimal_reversal.py` computes
\[
\mathrm{ARR}=\frac{c-t}{m},
\qquad
\mathrm{RRR}=\frac{c-t}{c},
\qquad
\mathrm{NNT}=\frac{m}{c-t}
\]
using exact rational arithmetic.

It verifies admissible-table counts
\[
0,\ 1,\ 3,\ 6,\ 10
\]
for arm sizes
\[
2,\ldots,6
\]
and strict-reversal counts
\[
0,\ 0,\ 0,\ 0,\ 2.
\]

The first-layer reversing pairs are exactly
\[
(1,2)\ \text{versus}\ (3,5)
\]
and
\[
(1,3)\ \text{versus}\ (2,5).
\]

For the displayed witness,
\[
\mathrm{ARR}=\frac16,\frac13,
\qquad
\mathrm{RRR}=\frac12,\frac25,
\qquad
\mathrm{NNT}=6,3.
\]

Run:

`python3 verify_arr_rrr_minimal_reversal.py`

The first output line must be:

`VERIFY_OK`

The persistent all-\(m\) family is also replayed through \(m=500\), while its universal validity follows from the symbolic inequality
\[
\frac2{m-1}<\frac12
\]
for every integer \(m\ge6\).
