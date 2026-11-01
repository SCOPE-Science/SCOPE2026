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

Execute `python verify.py` in the same directory. The program uses SymPy to perform exact operations in \(\mathbb Q(\sqrt2)\) and NumPy for an independent numerical orientation diagnostic. The exact tests construct all 56 triple determinant signs, check pairwise-general-position of the eight great circles, enumerate exactly 58 sign chambers from local intersection quadrants, and compute section side counts from the 16 explicitly listed polyhedral edges. The chamber completeness uses the independent topological formula \(8\cdot7+2=58\). The expected count follows analytically from one-edge angular crossing probability, so no area quadrature is needed. The code also verifies that the physical antiprism vertices are cospherical and all listed edges have equal length.

The separate 250,000-sample normal-orientation simulation provides a non-probative numerical diagnostic only. Exhaustive finite sign computation establishes the combinatorial assertion. The identity for Haar crossing probability is proved in RESULT.md. The program does not independently prove the mathematical universality of great-circle arrangement theory and does not constitute an independent external audit.
