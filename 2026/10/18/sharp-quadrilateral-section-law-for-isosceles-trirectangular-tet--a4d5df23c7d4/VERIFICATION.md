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

The source package includes `check_profile.py`, which directly integrates edge crossing lengths and directional widths on a deterministic spherical grid for five right-tetrahedron aspect ratios and compares with the closed formula. It also tests the expected monotonicity numerically over a finite grid and the two degenerate limits. These numerical samples do not prove strict monotonicity for all positive parameters: the exact derivative proof in `RESULT.md` supplies that step.

The general polyhedral mean-width identity is used as a standard geometric theorem; the proof checks its normalization against the unit cube. The six edge lengths and the three non-right exterior dihedral angles are explicitly derived. There is no external or independent audit, and historical priority remains subject to further review.
