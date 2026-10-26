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

The analytic certificate is the stationary Lyapunov trace identity, the exact mixed derivative of the weighted inverse trace, inverse-positivity of grounded Laplacians, and the large-grounding necessity construction. The two-follower rational example and the sharp correlation boundary are given as closed formulas in RESULT.md.

The standalone `verify.py` uses standard-library exact fractions and checks rational parameter grids, a strictly positive-definite negatively correlated counterexample, and selected finite instances of monotonicity and supermodularity. Execution passed 8,686 exact-rational assertions. Finite tests do not establish a theorem with universal quantifiers; that work is done by the proof.

Independent scientific audit has not been performed. The code does not check all graphs, does not prove literature priority, and does not address changes of the noise covariance upon interventions.
