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
# Reproducibility and boundaries

The standalone `verify.py` uses its own implementations of modular Gaussian elimination and graph maximum matching. Its `predict_distribution` classifies supports via the matching-essentiality condition; `direct_distribution` enumerates all edge weights and computes ranks from actual alternating matrices. Run `python3 verify.py` (Python standard library only).

Direct complete field enumerations passed on a four-cycle, attached-leaf, attached-two-edge-path, two-leaf attachment, and odd-cycle examples in characteristics two, three, and five. Additionally, 12 separately generated connected unicyclic graphs with 7–8 vertices and varying cycle lengths passed exhaustive enumeration over the three-element field. Totals were 29 complete graph/field configurations. The 4-cycle with a two-edge pendant path at field order three gave half-rank counts (1, 56, 384, 288), and the induced character counts (729, 4536, 3456, 288) satisfy the dimension-square identity for group order 3^12.

The verifier is finite and does not establish the universal theorem, which rests on the proof in `RESULT.md`. The script is not an external or independent mathematical audit. Algebraic closure, formal Lean certification, and publisher access are not claimed. Remaining priority risk: the full Gong–Xu 2012 paper was not inspected.
