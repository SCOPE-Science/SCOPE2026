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

Run `python verify.py` in a standard Python 3 interpreter. The checker uses only `fractions` and `itertools` and reports `VERIFY_OK rational_parameters=359 12_dual_vertices=True exact_norm_radius=True`. It constructs all dual extreme points at 359 rational parameters, checks the displayed light/heavy functional decompositions as exact rational identities, and independently evaluates the two rank-one operators' quotient norms and numerical radii by explicit dual-vertex maximization.

The analytic argument in `RESULT.md` proves the formula for all real parameters and handles endpoint degeneracies separately. The finite checks are not a proof for the continuum, and no machine-checked formal certificate or independent review is claimed.
