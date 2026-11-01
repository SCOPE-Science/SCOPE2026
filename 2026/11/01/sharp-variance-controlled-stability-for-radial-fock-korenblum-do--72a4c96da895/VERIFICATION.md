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
# Verification of the sharp variance gap

The analytical proof in `RESULT.md` verifies each implication: rationality and Schur boundedness of the exterior quotient; the moment-weighted shift contraction; exact norm defect splitting; strict Cauchy–Schwarz; and the explicit equality witnesses for every fixed Schur constant. In particular, the proof covers infinitely many monomial orders and all admissible radial densities; no finite test is interpreted as an exhaustive infinite proof.

`CHECK.py` is a standalone Python standard-library script. It evaluates moment-ratio bounds and the exact quadratic witness identity in Gaussian, gamma, annular and a nonmonotone mixed-gamma weight; selected higher-degree Möbius pairs are checked by independent polynomial coefficient norms. Run it with `python3 CHECK.py`. It is supplementary, not independent certification. There is no claim for a direct sharp distance between function pairs and the extremal family.
