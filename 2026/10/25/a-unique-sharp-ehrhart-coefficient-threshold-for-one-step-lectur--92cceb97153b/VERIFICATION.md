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

Run `python3 verify.py` from the directory containing this file and the script. The script requires Python 3 and no third-party package.

The checker independently enumerates integer points by slicing at the last coordinate, compares the exact binomial-sum formula at integer dilations, interpolates entire Ehrhart polynomials over the rational numbers, and checks the coefficient extracted from the quartic. It examines dimensions \(5\) through \(9\), six parameter choices per dimension, and every interpolation node from zero through the dimension. It additionally checks first-negative integer boundaries and exact coefficient signs in dimensions \(5\), \(6\), \(7\), \(8\), \(9\), \(10\), \(20\), \(50\), \(100\), and \(250\).

Expected output:

`VERIFY_OK exact_counts=240 dim5to9_a6 beta5to9=16,19,23,27,31 sign_pattern_n5to250`

The infinite sign-change and dimension-asymptotic conclusions are proved analytically in `RESULT.md`; the finite checker alone cannot establish either one. No external audit is included.
