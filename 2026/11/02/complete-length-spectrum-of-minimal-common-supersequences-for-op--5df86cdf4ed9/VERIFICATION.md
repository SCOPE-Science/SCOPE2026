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

# Reproducibility and limits

Run `python verify.py` from the extracted package directory. It requires only the Python 3 standard library and performs direct subsequence, single-deletion and constructive-family checks.

Unrestricted enumeration of **every** binary word of lengths from \(2m\) through \(4m\) matches the theorem's family for \(m=1,2,3,4\). For \(m=5\), every word having exactly \(2m\) occurrences of one binary symbol and between \(m\) and \(2m-1\) of the other is checked. The independent proof establishes that this restriction contains all possible minimal common supersequences. The output is recorded in `verification_output.txt`; it reports `ALL CHECKS PASS`.

All infinite-parameter assertions, the exact characterization and the asymptotic law depend on the mathematical proof in `RESULT.md`. The exhaustive calculations are corroborating evidence and are not an exhaustive search over all word lengths or parameters. No independent mathematical audit has been performed.
