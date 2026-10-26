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

The supplied `verify.py` independently enumerates valid length-four palindrome windows of each receiver, removes the latter two symbols and deduplicates the resulting parents. Separately it computes the maximal-run formula and the coefficients of the claimed rational generating function by exact integer-polynomial recurrence. It compares these three definitions word by word and checks complete population histograms, the previously known maximum, and the mean.

Exhaustive finite domains: \(q=2\), lengths 4–12; \(q=3\), lengths 4–9; \(q=4\), lengths 4–8; \(q=5\), lengths 4–7; 222,456 received words altogether. The recorded execution ended `VERIFY_OK`. The full rational identity is proved symbolically by the run transition matrix in `RESULT.md`. The asymptotic variance and Gaussian limit are proved by the analytic pole argument there, not inferred from the finite tests.

The independent-audit channel has not been performed. No claim of an independent certification, peer review, formal proof assistant or exhaustive infinite testing is made.
