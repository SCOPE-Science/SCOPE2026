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
For a sorted citation vector
\[
c_1\ge\cdots\ge c_n\ge0,
\]
the verifier computes
\[
h=\max\{r:c_r\ge r\}
\]
and
\[
g=\max\left\{r\le n:\sum_{i=1}^{r}c_i\ge r^2\right\}
\]
using exact integer arithmetic.

The embedded `verify_h_g_equal_total_boundary.py` confirms the universal inequality
\[
h\le g
\]
on a broad finite replay, exhaustively enumerates the unrestricted first boundary, and obtains exactly three four-paper nine-citation profiles with
\[
(h,g)=(1,3)
\]
and exactly five with
\[
(h,g)=(2,2).
\]
Thus it recovers exactly fifteen cross-pair reversals.

It also verifies the positive-citation boundary at
\[
n=4,
\qquad
C=10,
\]
with exactly two unordered reversal pairs, and checks zero-padding invariance through one hundred papers.

Run:

`python3 verify_h_g_equal_total_boundary.py`

The first output line must be:

`VERIFY_OK`

The impossibility below nine citations and the necessity of four papers at the nine-citation layer are proved symbolically in `RESULT.md`; finite replay is not used to infer an infinite claim.
