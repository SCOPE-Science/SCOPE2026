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

# Reproduction and verification

Run `python3 check_hom_r5.py` using Python 3.9 or later; no dependencies are required. The script builds the entire directed Hom regular CW complex at lengths three through ten; verifies every cell is a nonadjacent-swaps cube with constant winding count, and checks exact face counts against the particle-configuration model. It calculates boundary ranks over both \(\mathbf F_2\) and \(\mathbf F_3\) and compares all Betti numbers with the circle-and-point predictions. It reports `ALL_CHECKS_PASSED` if every assertion succeeds.

The general all-length proof uses the explicit covering map, the standard graph-configuration deformation retraction, the known circle homotopy type of unordered configurations on a circle, and the computed primitive covering monodromy. The finite checks are corroboration rather than a proof for arbitrary length; no independent audit is claimed.
