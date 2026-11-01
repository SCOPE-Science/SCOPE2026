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

The exact proof uses the graph nodal mass matrix, explicit inverse-column coefficients, elementary integration of absolute affine functions and two positive-coefficient polynomial identities. These objects are specified in `RESULT.md`. Run `python verify_split_spline.py` with SymPy at least version 1.10 to reproduce the exact-rational calculations.

The executed checker returned `EXACT_INDEPENDENT_MASS_INVERSES_AND_KERNEL_INTEGRALS_OK 72`, all-parameter positivity certificates for both signs of the other-clique inverse coefficient, `EXACT_TWO_THRESHOLD_AND_LIMIT_IDENTITIES_OK`, and `ALL_SPLIT_METRIC_GRAPH_P1_PROJECTION_CHECKS_OK`.

Finite matrix instances are supplementary diagnostics; the two symbolic coefficient checks establish universal algebraic comparisons. The universal theorem also depends on the explicit kernel representation and positivity of the mass matrix, proved in `RESULT.md` independently of any finite run. No independent scientific audit or external certification has been performed.
