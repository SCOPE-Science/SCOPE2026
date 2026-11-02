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

The full mathematical argument is in `RESULT.md`. Every pair type of the explicit embedding is enumerated. The positivity of its Gram matrix follows from its given orthogonal coordinate realization; no numerical semidefinite test is used to justify the infinite assertion.

Run `python verify.py`. In this environment the ordinary standalone Python interpreter reported:

`TREE_DEPTH2_CHECK_OK cases=256 exact_pair_inequalities=1889536 binary_depth2_squared_distortion=81/56 limiting_squared_distortion=8/3`

The independent finite-distance calculation uses `fractions.Fraction` and reconstructs all pairwise distances for 256 integer parameter pairs; this is not an exhaustive calculation for arbitrary integer parameters, and it does not independently certify the analytic proof. The symbolic monotonicity and equality rigidity arguments are supplied in the theorem text. No independent external mathematical audit or expert certification has been performed.
