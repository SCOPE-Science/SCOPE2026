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

The mathematical proof is self-contained in `RESULT.md`. It uses weak sequential compactness of the Hilbert unit ball, an explicitly constructed Riesz subsequence, and standard Hilbert numerical-radius estimates; no computational enumeration substitutes for these infinite-dimensional statements.

Execute `python3 checker.py` with NumPy installed to reproduce 13,041 deterministic finite assertions. The executable checks square-zero witnesses in complex finite-dimensional matrices, left-singular norming vectors, the sharp \(2\times2\) identity case, and scalar-target diagnostics. It does not certify historical novelty or the existence of Riesz subsequences in arbitrary Hilbert spaces.

Independent audit remains not performed. The published-source comparison and remaining risk of an inaccessible unpublished reference are documented in `REVIEW.md` and `AUDIT.json`.
