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

# Reproducibility and verification

Run `python checker.py` with Python 3 and no third-party packages. The program enumerates every codeword in the stated construction for \(4\le n\le16\), checks every ordered codeword pair (including a word paired with itself) and every proper prefix/suffix length, and compares the union of all cyclic rotations with all primitive length-\(n\), weight-three words. For \(4\le n\le100000\), it also checks the polynomial closed-form count identity by integer arithmetic.

The execution completed successfully with the final line `PASS: exhaustive word and overlap checks through n=16; arithmetic count n=4..100000`. For lengths \(4\) through \(16\), the code sizes were \(1,2,3,5,7,9,12,15,18,22,26,30,35\). For lengths divisible by three, the checker independently found exactly \(n/3\) nonprimitive weight-three words; otherwise it found none.

These finite checks cannot establish the universal quantifier; the all-length proof is in `RESULT.md`. No outside verifier has been used and no independent review or validation is asserted.
