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

The algebraic proof follows by expanding the three nonzero commutator blocks, computing the image of the remaining tensor coordinate in two exhaustive cases, and counting pairs of vectors by rank and zero status. No symbolic computation is needed for the general theorem.

Run `python3 artifacts/check.py` with Python 3.8 or newer, without external dependencies. The script uses an independently constructed path-product multiplication table and modular Gaussian elimination; it then compares each exact class-size histogram coefficient to the theorem and tests three small Burnside commuting-pair totals. It prints `FOUR_VERTEX_QUIVER_CLASS_SPECTRA_CHECKS_PASSED cases=10 independent_adjoint_matrices=10963` on success. The complete observed results are in `artifacts/checker_output.txt`.

The script checks only the listed prime fields and finite dimensions. The theorem covers all prime powers and all positive outer dimensions by a separate written proof. Access to the complete 2025 four-block character paper was unavailable; an equivalent or stronger element-spectrum claim there is not ruled out.
