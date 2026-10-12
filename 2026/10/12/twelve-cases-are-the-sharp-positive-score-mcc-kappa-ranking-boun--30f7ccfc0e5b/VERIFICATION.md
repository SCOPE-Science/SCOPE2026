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
For a binary confusion matrix define
\[
P=TP+FN,
\qquad
Q=FP+TN,
\qquad
R=TP+FP,
\qquad
S=FN+TN,
\]
and
\[
\Delta=TP\,TN-FP\,FN.
\]

Then
\[
M=\frac{\Delta}{\sqrt{PQRS}}
\]
and
\[
\kappa=\frac{2\Delta}{PS+QR}.
\]

The embedded `verify_mcc_kappa_positive_boundary.py` enumerates every strictly positive binary confusion matrix with positive determinant through total
\[
N=12.
\]

Within every common \((N,P)\) layer it compares all unordered classifier pairs exactly. MCC comparisons are made by cross-multiplying squared algebraic quantities, so no floating-point ordering is used.

The verifier checks complete weak-order agreement through nine cases, the first weak-only split at ten cases, no strict reversal through eleven cases, and exactly two complement-related strict reversals at twelve cases.

Run:

`python3 verify_mcc_kappa_positive_boundary.py`

The first output line must be:

`VERIFY_OK`
