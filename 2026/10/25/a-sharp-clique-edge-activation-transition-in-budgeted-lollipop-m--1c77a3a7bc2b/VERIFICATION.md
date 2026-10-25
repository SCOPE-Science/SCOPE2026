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

# Reproducibility and scope

Run `python verify.py` using Python 3 and NumPy. The checker constructs the full weighted Laplacian and its quotient certificate for every integer \(2\le k\le60\), then checks total edge-rate budget against the exact target, the unit second eigenvalue, its expected multiplicity, and the axial positive-semidefinite matrix. All 59 cases passed at tolerance \(10^{-10}\) or smaller. The general exact theorem is proved analytically in RESULT.md, including a sum-of-squares identity; these finite tests are not a proof outside their checked range.

No independent audit or external formal proof certificate has been performed. The literature comparisons concern scientific coverage, not a claim of formal uniqueness within all literature.
