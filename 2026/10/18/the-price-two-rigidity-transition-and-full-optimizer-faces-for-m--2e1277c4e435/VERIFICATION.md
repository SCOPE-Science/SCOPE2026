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

# Reproducibility and verification

Run `python verify_matching.py` with Python 3, NumPy and SymPy available. The program constructs independently weighted Laplacians from edge assignments and checks the budget and the formula for the spectral gap; verifies eigenvector equations and a genuine nonuniform optimal family; checks the critical face with positive matching conductance; and tests random feasible competitors. The observed output during review was:

`PASS: 203 exact symbolic/rational identities and numerical spectral/budget/upper-bound checks`

These checks are finite sanity tests. The all-dimensions upper bounds, necessity and sufficiency of all equality conditions, uniqueness, and affine dimensions follow from the explicit analytic proof in `RESULT.md`. No independent audit or external proof certification has occurred.
