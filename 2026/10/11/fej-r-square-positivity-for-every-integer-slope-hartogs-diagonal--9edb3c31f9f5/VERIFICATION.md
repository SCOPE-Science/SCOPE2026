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

The principal certificate is the algebraic Fourier-coefficient identity in `RESULT.md`. Each coefficient is computed directly from the normalized five-part Bergman numerator in Edholm–Mathew [1]. The equality is a symbolic identity for every integer \(d\ge1\); no floating-point root plot or finite sweep is required for the theorem.

The packaged script `check_integer_hartogs.py` (Python 3 standard library only) was executed from its actual package path. It reconstructs the polynomial by four independent exact-integer methods for each of the 500 values \(2\le m\le501\): Edholm–Mathew's five numerator pieces, Edholm's earlier two-polynomial formula, the derived closed coefficient list, and the two Fejér autocorrelation lists. All comparisons, degree tests, and palindromicity tests passed.

These finite executions only test algebraic transcriptions for finitely many parameters. They do not independently prove the infinite family. The written proof treats all \(m\ge2\). Only same-model scientific review has been performed; independent audit remains not performed.
