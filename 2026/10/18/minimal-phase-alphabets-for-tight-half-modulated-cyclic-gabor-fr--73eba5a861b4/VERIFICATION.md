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

The proof derives the exact block spectrum directly from character orthogonality, then proves an if-and-only-if moving-sum cancellation lemma and the phase-alphabet classification by parity and cubic-root real parts. No finite search or external computation is used to establish the universal assertion.

The accompanying standalone `CHECK.py` uses Python 3 and NumPy. Execute `python CHECK.py` in the directory containing the file. The recorded run checked 210 tight constructions across even dimensions 2 through 40, 95 independent full-frame spectral comparisons, and 168 exhaustive small-dimensional phase-alphabet cases. This is supporting finite evidence only. All bounds and quantifiers for arbitrary even dimension and admissible translation count are covered by the analytic proof in `RESULT.md`.

Independent validation has not been performed. Priority remains limited by the inspected accessible literature; relevant unindexed earlier work could exist.
