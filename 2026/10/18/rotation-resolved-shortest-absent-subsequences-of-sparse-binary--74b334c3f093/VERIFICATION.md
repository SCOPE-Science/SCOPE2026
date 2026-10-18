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

Run `python3 verification/verify_circular_sas.py` with Python 3. The standalone checker independently enumerates all binary length-\(k+1\) candidates and tests subsequence inclusion for 501 zero-gap necklaces with \(2\le k\le8\), totaling 8,890 indexed cuts. A separate next-occurrence dynamic program checks smaller subcases and computes Fibonacci rotation counts through substitution level \(11\), with substitution generation cross-checked against the word-concatenation recursion.

Observed output:

`VERIFY_OK binary_gap_necklaces=501 rooted_cuts=8890 fibonacci_m3_to11=9`

The executable calculation validates only its stated finite ranges. The all-length, all-parameter statements are proved in `RESULT.md`. Scientific originality is assessed against identified sources without claiming exhaustive coverage or independent audit.
