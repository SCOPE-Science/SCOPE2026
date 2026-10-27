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

# Finite checks and scientific limits

Run `python verify.py` with Python 3 standard library after extracting the seven included files. The checker builds the five-cycle, Petersen graph and Clebsch graph directly; verifies graph regularity and the exact strongly regular identity; compares nonedge squared-Laplacian entries with the expected common-neighbor count; computes the scalar temporal peak and threshold; and reconstructs sampled exponential matrices by independent spectral projections, comparing every absolute row sum with the proposed formula. It passed 7,190 assertions in the recorded execution. The exact integer algebraic checks are rigorous for those three finite instances, while floating comparisons at selected times are diagnostic only. General correctness rests on the complete symbolic proof in RESULT.md, not on the finite test set.

The strongest related published general three-spectrum positivity result already covers the qualitative half-ray structure. Its accessible scientific summary was compared by implication; full text was not available. Consequently the novelty claim is restricted to exact family-specific amplification and peak formulas, and an independent literature audit remains outstanding.
