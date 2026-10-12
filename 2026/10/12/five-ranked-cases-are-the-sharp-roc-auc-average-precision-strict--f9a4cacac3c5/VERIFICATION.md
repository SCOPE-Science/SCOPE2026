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
If the positive cases occupy ranks
\[
1\le r_1<\cdots<r_P\le N
\]
and
\[
Q=N-P,
\]
then empirical ROC-AUC is
\[
A
=
1-\frac1{PQ}\sum_{j=1}^{P}(r_j-j),
\]
while classical average precision is
\[
\mathrm{AP}
=
\frac1P\sum_{j=1}^{P}\frac{j}{r_j}.
\]

The embedded `verify_auc_average_precision_boundary.py` enumerates every binary ranking with both classes present for
\[
2\le N\le5.
\]

It verifies:
\[
N\le3:
\]
complete weak-order agreement;

\[
N=4:
\]
exactly one weak-only disagreement and no strict reversal;

\[
N=5:
\]
exactly two strict reversals across all prevalences.

Run:

`python3 verify_auc_average_precision_boundary.py`

The first output line must be:

`VERIFY_OK`

All metric values and comparisons use exact rational arithmetic.
