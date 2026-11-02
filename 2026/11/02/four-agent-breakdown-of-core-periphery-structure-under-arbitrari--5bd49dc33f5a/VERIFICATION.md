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

The accompanying `verify.py` independently rebuilds Katz centralities from each finite adjacency matrix using exact rational Gaussian elimination. It enumerates all unilateral sponsorship replacements in the specified four-player profile at seven admissible rational attenuations, testing both an interior strict equilibrium and the minimal-ratio weak equilibrium: 392 unilateral comparisons passed. It also evaluates the rational benefit differences, eight triangle orientations' necessary cost bounds, and the three-player obstruction at those attenuations. The universal statements follow from the explicit algebra and walk-count argument in RESULT.md; finite checking alone does not certify them. No external or independent audit was performed.
