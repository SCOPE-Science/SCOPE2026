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

The verifier `artifacts/verify.py` uses Python's standard library only.

It first reconstructs
\[
R_1=113322\cdot157=17791554,
\qquad
c_1=797\cdot157-113322=11807.
\]
It then applies the proved inequalities to enumerate every prime \(q\) and \(r\) that could occur in a four-prime filling with least prime \(157\). For each pair it evaluates the uniquely forced rational completion
\[
s=\frac{R_2r+1}{c_2r-R_2}.
\]

The verifier records \(375\) admissible prime values of \(q\), \(242779\) admissible prime values of \(r\), and exactly one integral completion. That completion is
\[
(1979,10093,16879).
\]
It finally verifies primality from the same sieve and checks the original filling identity exactly.

The verification proves only the finite branch stated in the theorem. It does not search or certify four-prime fillings with a least prime other than \(157\).
