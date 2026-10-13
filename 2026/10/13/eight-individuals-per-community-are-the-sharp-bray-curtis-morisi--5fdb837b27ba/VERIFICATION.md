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
For equal census totals \(N\), Bray–Curtis similarity is
\[
B(x,y)=\frac{\sum_i\min(x_i,y_i)}{N},
\]
and Morisita–Horn similarity is
\[
H(x,y)=\frac{2\sum_i x_i y_i}{\sum_i x_i^2+\sum_i y_i^2}.
\]

The embedded `verify_bray_morisita_horn_boundary.py` generates every positive integer abundance vector for every
\[
2\le k\le N\le8.
\]

Community comparisons are quotiented only by joint species relabeling and by swapping the two communities. Every unordered pair of canonical comparison types with common \(N,k\) is then checked using exact rational arithmetic.

The strict-reversal counts by total are
\[
0,0,0,0,0,0,1
\]
for
\[
N=2,3,4,5,6,7,8.
\]

The unique first reversal is
\[
(1,1,2,4)\ \text{versus}\ (1,4,2,1)
\]
against
\[
(1,1,3,3)\ \text{versus}\ (3,3,1,1).
\]

Run:

`python3 verify_bray_morisita_horn_boundary.py`

The first output line must be:

`VERIFY_OK`

The recurrence under common scaling follows directly from homogeneity and is separately replayed for scaling factors through \(50\).
