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

# Verification record

The proof is analytic and self-contained in `RESULT.md`: the exact supporting-plane normals, the comparison of polar and lateral distances, and the derivative-critical-point inequality establish the claim for the stated full domain. The standalone script `check_antiprism.py` independently constructs the polytope and calculates the facet-distance minimum for 245 configurations using SciPy; it also evaluates 300,000 sampled spherical directions and checks 25 local optimal heights.

Command: `python check_antiprism.py` with Python 3, NumPy and SciPy.

Observed standard output: `ANTIPRISM_SPHERICAL_COVERING_OK facet_comparisons 245 samplings 300000 optimal_profiles 25`

Finite checks cannot replace the universal symbolic proof, and no independent mathematical audit or external certification was performed. Prior-work checks and unresolved historical-priority risks are detailed in `REVIEW.md` and `AUDIT.json`.
