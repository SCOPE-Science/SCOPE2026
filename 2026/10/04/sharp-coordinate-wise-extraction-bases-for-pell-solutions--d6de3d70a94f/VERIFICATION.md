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

The theorem is established by the exact inequalities in RESULT.md. The finite replay is corroborative rather than the basis of the infinite claim.

`verify.py` uses only Python's standard library. It computes fundamental Pell solutions by continued fractions for every nonsquare \(2\le d<200\) with \(X_1\le50\). For each of the \(54\) resulting Pell equations it performs the following checks:

- every base \(2X_1\le b<b_X\) fails the \(X\)-formula by \(n\le2\);
- every base \(2X_1\le b<b_Y\) fails the \(Y\)-formula by \(n\le2\);
- each threshold and the next two bases reproduce the corresponding coordinate for \(1\le n\le8\).

The exact replay output is:

`VERIFY_OK pell_cases=54 below_x=67240 below_y=8682 threshold_checks=2592`

The finite range contains \(67{,}240\) sub-threshold \(X\)-base checks and \(8{,}682\) sub-threshold \(Y\)-base checks. It does not certify any untested \(d\), \(b\), or \(n\); those are covered by the symbolic proof.

Scientific limits: this verifies the stated base thresholds only for the fixed generating-function formulas. It does not compare all possible arithmetic expressions for Pell coordinates.
