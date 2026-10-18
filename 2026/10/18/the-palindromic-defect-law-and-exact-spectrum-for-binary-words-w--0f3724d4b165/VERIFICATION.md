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

Run `python3 verify.py` from a directory containing this file and `verify.py`. Only Python 3 standard-library modules are used.

The program independently enumerates all binary words with exactly three ones for lengths \(3\) through \(34\). For each word it discovers distinct palindromic substrings by centre expansion, compares the observed defect with the analytic four-run formula, and checks the exact coefficient in every possible positive-defect generating series. Further exact-integer checks compare two independent counting expressions for the total non-rich count through length \(500\). Expected marker: `ALL_CHECKS_PASS`.

The unrestricted statement is mathematically proved by the palindrome-family count and the formal generating-function manipulations in `RESULT.md`; the finite tests check implementation and low-length boundary behavior but cannot prove all lengths or bibliographic priority. Independent audit was not performed.
