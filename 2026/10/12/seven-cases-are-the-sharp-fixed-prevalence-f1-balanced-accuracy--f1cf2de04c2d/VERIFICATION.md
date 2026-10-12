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
For fixed total \(N\) and positive count \(P\), write
\[
a=TP,
\qquad
b=FP.
\]

Then
\[
F_1=\frac{2a}{P+a+b}
\]
and
\[
B=\frac12\left(1+\frac aP-\frac b{N-P}\right).
\]

The embedded `verify_f1_balanced_accuracy_boundary.py` enumerates every strictly positive confusion matrix for totals
\[
4\le N\le7
\]
and every admissible prevalence.

It verifies:
\[
N\le5:
\]
complete weak-order agreement;

\[
N=6:
\]
one weak-only disagreement and no strict reversal;

\[
N=7:
\]
exactly three strict reversals.

It also verifies the exact rational values for all three first-layer pairs and the scaling persistence of the \(P=3\) witness.

Run:

`python3 verify_f1_balanced_accuracy_boundary.py`

The first output line must be:

`VERIFY_OK`

All comparisons use exact rational arithmetic.
