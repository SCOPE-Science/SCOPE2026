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

Execute `python3 checker.py` from the directory containing this file and compare stdout byte-for-byte with `CHECK_OUTPUT.txt`. It uses Python 3 standard library only, without external datasets or dependencies. Direct enumeration chooses every placement of the \(A\) occurrences of \(a\), counts scattered \(ab\) pairs, and independently scans whether \(a b^t a\) is a scattered subsequence. Its proposed-polynomial calculation uses an exact integer recurrence for Gaussian coefficients.

The finite test checks 252 parameter triples, 3,354 coefficients and 320 restricted-partition chamber instances, and prints illustrative exact probabilities. Integer arithmetic and assertions avoid tolerance uncertainty. These bounded computations cannot imply the theorem for infinitely many parameters; the proof in `RESULT.md` is the infinite argument, including the restricted-partition asymptotic whose analytic ingredients are cited there.

Independent audit has not been performed; no claim of external certification is made.
