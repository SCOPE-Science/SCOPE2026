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
# Verification of the forest likelihood-ratio boundary

The accompanying `verify_forest_orders.py` is self-contained standard-library Python. Execute `python verify_forest_orders.py` to independently reproduce the exact finite checks.

The verifier enumerates all edge subsets of the complete graph on \(n\le6\) labeled vertices, accepts only acyclic graphs, obtains unrooted component counts directly, and obtains root-marked counts by multiplying the component sizes. It verifies the analytic Cayley and forest decomposition formulas against these independent enumerations, checks root-marked cross-product likelihood-ratio inequalities for \(n\le41\), checks the unrooted two-component exact formula through \(n=84\), and verifies two-versus-three incomparability for \(5\le n\le54\). All rational values use `fractions.Fraction`, with no numerical tolerance.

The actual run completed successfully with 391,322 exact assertions. This finite evidence does **not** certify the infinite-family claim independently: that claim is proved by the exact finite-difference and likelihood-ratio identities in `RESULT.md`. No external independent audit or expert validation has been performed.
