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
Write sensitivity and specificity as
\[
s=\frac{TP}{P},
\qquad
c=\frac{TN}{N-P}.
\]
Then
\[
B=\frac{s+c}{2},
\qquad
G^2=sc,
\qquad
G^2=B^2-\frac{(s-c)^2}{4}.
\]

The embedded `verify_balanced_accuracy_gmean_boundary.py` enumerates every positive-cell binary confusion matrix through total eleven, retains exactly those satisfying
\[
B>\frac12,
\]
and compares every unordered pair at common prevalence using exact rational arithmetic.

It verifies no strict reversal for
\[
N\le10,
\]
the first weak-only disagreement at
\[
N=8,
\]
and exactly six strict reversals at
\[
N=11.
\]

It also verifies global class-label complement symmetry and the determinant identity
\[
s+c-1
=
\frac{TP\,TN-FP\,FN}{P(N-P)}.
\]

Run:

`python3 verify_balanced_accuracy_gmean_boundary.py`

The first output line must be:

`VERIFY_OK`
