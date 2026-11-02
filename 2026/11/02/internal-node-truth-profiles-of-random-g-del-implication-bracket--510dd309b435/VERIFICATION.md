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

# Reproducible finite checks and analytic boundary
Run `python3 checker.py` using only the Python standard library. It exhaustively compares every ordered internal-child pair for \(m=2,3\) and \(1\le n\le6\), and for \(m=4\) and \(1\le n\le5\). The test reconstructs all Catalan trees, enumerates all leaf assignments, and compares each resulting multiset against a separate recurrence for the marked-node generating series. Expected final output: `ALL_CHECKS_OK 158`. The critical Boolean child and internal false values are checked against their radicals. Numerical tests or finite enumeration cannot validate a universal limit; the latter is proved via explicit factorial-moment formulas and an Euler-limit argument in the manuscript. No independent audit has been performed.
