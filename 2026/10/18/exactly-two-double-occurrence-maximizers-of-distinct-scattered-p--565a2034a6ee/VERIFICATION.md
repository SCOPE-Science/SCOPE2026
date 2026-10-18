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

# Verification and reproducibility

`check_scattered_palindromes.py` is a self-contained Python 3 program using only the standard library. Execute `python3 check_scattered_palindromes.py` in the folder containing it.

A direct subsequence-set enumerator and a different interval/support enumerator are compared for every pairing of \(2q\) positions, with \(1\le q\le5\), producing respectively \(1,3,15,105,945\) pairings. Counts and length histograms coincide for all cases, and only the stated canonical words attain \(2^{q+1}-2\). Independent second-half-permutation scans additionally cover every tail at \(q=6,7\), testing \(720\) and \(5040\) permutations. The checker also verifies the exact length-spectrum identities for both forms through \(q=5\).

All listed tests completed successfully, ending with `ALL_SCATTERED_PALINDROME_CHECKS_PASSED`. They are finite tests, not a certificate for infinitely many alphabet sizes. The proof in RESULT.md supplies the universal interval-nesting argument and complete equality classification. No independent audit has been performed.
