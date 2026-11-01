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

# Reproducibility
Run `python CHECK.py` with SymPy installed. The checker creates exact coefficient matrices for nine admissible rational parameter triples, checks their exact symbolic ranks, verifies three formal numerator expansions, and computes the determinant of the complete generic coefficient matrix as \(32\beta^3(\beta-2)\). The reproduced calculation is finite and algebraic, not an infinite completeness certificate. Universal correctness comes from the geometric section formula and parity/rank argument in `RESULT.md`.

The external section-function theorem and symmetric precursor were inspected as literature comparisons, not as substitutes for reconstructing the present rank argument. Full classification is limited to the stated axial family. Independent mathematical validation has not been performed.
