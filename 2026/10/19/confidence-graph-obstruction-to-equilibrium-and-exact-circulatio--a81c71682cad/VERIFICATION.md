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

# Computational and analytic verification

The supplied standalone `verify.py` is the entire computational dependency. Running `python3 verify.py` with standard Python 3 prints a successful count of 1479 exact rational comparisons and numerical maximizer \(p_*=0.291984797141795\), with entropy-production rate \(0.064719539702587\).

The program constructs labeled-state transition generators from the specified q-neighbor sampling rule; verifies the graph-uniform three-configuration witness across multiple social graphs and unanimity sizes; independently checks detailed balance for the complete confidence relation at \(q=1\); and constructs the six-state count-chain generator, its exact stationary distribution, the two triangle currents, and entropy production at three rational noise parameters. It also solves the derived critical-point equation numerically by bisection.

Analytical certification uses the exact rate-product mismatch, direct detailed-balance ratios, finite stationary balance equations and explicit signs in the derivative calculation. The checker does not search all graphs or all real noise values, and finite experiments are not a proof of generality. A separate independent mathematical audit has not yet been performed. Related literature coverage may be incomplete, particularly general results on reversibility of noisy interacting particle systems.
