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
# Verification

The probability law is represented by exact integer masses summing to \(86\). The verification script generates all finite upper sets from the product order rather than hard-coding the NRD inequalities. It then enumerates all disjoint nonempty output/conditioning coordinate blocks and all comparable conditioning values.

The enumeration contains \(74\) formal upper-set comparisons. Exactly \(64\) have positive mass on both conditioning values and hence belong to the conditional stochastic-order definition. Every applicable cross-product slack is nonnegative; \(57\) are positive, \(7\) are zero, and the smallest positive integer slack is \(6\).

The NRTD witness is checked separately and exactly:
\[
\Pr(X_1=1\mid X_3\ge1)=\frac7{24},\qquad
\Pr(X_1=1\mid X_2=1,X_3\ge1)=\frac25,
\]
with cross-product difference \(-13\).

Reproduce with `python3 verify_sparse_nrd.py`; a successful run ends with `VERIFY_OK`.

The verification establishes the displayed seven-atom example only. It does not prove that smaller supports are impossible and does not use failed searches, timeouts or random sampling as mathematical evidence.
