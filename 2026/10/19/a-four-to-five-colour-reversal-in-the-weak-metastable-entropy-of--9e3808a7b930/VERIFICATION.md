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

Run `python verify.py` with Python 3's standard library. The script independently evaluates the energy advantage of every recolouring of every labelled word of length 3–7 for \(q=4\) and \(q=5\), and checks the results against exact transfer-matrix and winding-state recurrences. The exhaustive range is finite; the general formulas and entropy limits follow from the proof in RESULT.md rather than from extrapolation.

One-site energy comparisons use ordinary floating-point cosine values with tolerance \(10^{-9}\). For these fixed alphabets the possible energy gaps between genuinely unequal candidate local scores exceed the tolerance; neutral alternatives are treated as allowed. The integer transfer counts involve no floating-point approximation. At lengths 8–16, only the exact integer count formulas are evaluated, without claiming that all spin configurations were exhaustively enumerated.

This package carries a self-review, not an independent verification. Independent audit and external validation have not been performed.
