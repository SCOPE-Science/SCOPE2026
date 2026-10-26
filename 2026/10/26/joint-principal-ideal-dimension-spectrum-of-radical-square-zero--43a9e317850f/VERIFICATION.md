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
# Verification

The proof uses exact basis products in the radical-square-zero quiver algebra and a disjoint count of scalar-zero sets and nonzero-arrow supports. This is a uniform algebraic proof for every finite quiver and every finite field, not an extrapolation from experiments.

Running the standalone `verify_principal_ideal_ranks.py` with Python 3 constructs multiplication matrices from the original basis equations, computes their two ranks by field Gaussian elimination, and compares the complete bivariate rank histogram with the independent support-strata sum. A replay before packaging returned `VERIFY_OK_PRINCIPAL_RANK_BIVARIATE 56 finite-field graph configurations` and `VERIFIED_ORIENTATION_STAR_PATH F2 3-vertex marginal counts`. The tests cover fields of sizes 2, 3 and 4, including loops, parallel arrows, a directed cycle, different connectedness patterns, and three orientations of the three-vertex path.

The displayed formulas are ordinary rank distributions of algebra elements. No claim is made about the distribution of distinct ideal isomorphism classes. Neither numerical testing nor source searches establish historical uniqueness or constitute independent validation.
