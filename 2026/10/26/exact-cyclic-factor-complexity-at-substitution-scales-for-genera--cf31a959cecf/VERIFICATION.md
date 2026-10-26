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

# Reproducible checks and limits

Run `python verify.py` with Python 3 standard library in the same directory as `counts.csv`. The verifier independently generates the infinite word's finite factors from two higher substitution levels and reconstructs them by neighboring-level block concatenations. It calculates rotation classes by Booth's minimum-rotation algorithm and, for short lengths, independently by exhaustive rotation comparison. It checks all one-count classes and the exact consecutive-one gap formula.

The verified cases are \(3\le q\le7\), \(0\le k\le4\), and \((q,k)=(3,5),(3,6),(3,7),(4,5)\). The output table contains 29 parameter rows. These calculations are finite consistency tests, not a substitute for the all-base, all-level proof. No independent scientific audit or external mathematical validation is claimed.
