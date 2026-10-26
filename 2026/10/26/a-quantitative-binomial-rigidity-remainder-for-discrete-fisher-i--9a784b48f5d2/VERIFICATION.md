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
The independent-audit channel remains unperformed. Scientific reproducibility rests on the full elementary proof in `RESULT.md` and exact rational calculations in `verify_stam_stability.py`.

Run `python verify_stam_stability.py` using standard Python. Expected successful output: `PASS: 506 exact-rational configurations, including full conditional-variance identity, sharp equality, stability, and quadratic onset.`

The program checks 400 variable-law configurations, 100 binomial equality configurations, and six perturbations. It explicitly compares the global deficit to the complete pairwise conditional-variance sum and to the adjacent-fiber lower bound, without floating-point tolerance. It does not certify any universal quantified statement by enumeration: the written proof does that. The log-ratio/total-variation step is established analytically in `RESULT.md`, subject to the stated positive-mass and small-deficit conditions.
