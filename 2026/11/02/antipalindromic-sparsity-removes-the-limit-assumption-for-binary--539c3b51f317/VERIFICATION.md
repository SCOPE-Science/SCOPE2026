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
# Verification evidence and limits

The exact Python 3 checker `check_antipalindromic_derivative.py` can be executed with `python3 check_antipalindromic_derivative.py`. Its recorded output is `check_antipalindromic_derivative_output.txt`. It tests the binary derivative-palindrome implication and multiplicity bounds on all finite binary strings through length 11; it also checks the finite Burnside formula on the group closure of all factor languages through length 9 and verifies factor inequalities for prefixes of the Thue–Morse and Fibonacci words. It does not establish limiting behavior or aperiodicity of infinite strings. Those steps are proved symbolically in RESULT.md, conditional only on Shallit's published theorem. Independent mathematical audit has not been performed.
