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

# Verification of the mathematical claim

Run `python verify.py` with Python 3 and SymPy. The script computes the quotient traces as exact rational functions in symbolic \(m\) and \(\kappa\), factors the four gap identities, and checks that the proposed formulas coincide identically. It then independently builds the unweighted bridge-barbell Laplacian and verifies 60 exact-rational full-matrix orbit cases for \(m=3,4,5,6\) and \(\kappa=1/3,1,7/2\).

The proof in `RESULT.md` supplies the all-parameter conclusion using strictly positive factors; the finite direct tests check the formula and its boundary case but are not an infinite proof. All numerical or finite calculations are reproducible using only the packaged script. Equal gains and unit edge weights are essential assumptions. No independent validation is claimed.
