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
Run `python3 verify.py` with Python 3 standard library only. It constructs all distinct scattered subsequences by literal increasing-index combinations and retains exactly the palindromic targets, independently of the greedy proof. It compares those literal sets with all predicted exact length counts. A separate membership loop checks literal inclusion of each generated short candidate palindrome against the sharp cost criterion; a different formal-power-series computation compares coefficients to the closed binomial formulas.

Actual output from the supplied code:

`VERIFY_OK literal_parameter_cases=49 literal_palindromes=3086 palindrome_membership_tests=67121 exact_formal_coefficients=50932 q=3..9 k=1..34 all_prefixes=yes`

The literal host cases include partial final periods of every permitted length for the tested alphabet sizes. Formal coefficient tests include all \(3\le q\le9\), \(1\le k\le34\), and \(0\le s<q\). These tests establish finite consistency only. The infinite statement follows from the proof in RESULT.md, and no independently performed scientific audit is asserted.
