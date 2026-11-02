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

# Reproducibility and limits

Run `python verify_cycle.py` with a standard Python installation. It performs exact rational checks of the full-graph edge-gradient intertwining for ten conductance ratios; independently evaluates forty full vertex heat kernels using stochastic uniformization; tests all six norming extreme gradients; checks the conductance-side winning edges and the sharp limiting witness.

The Poisson-tail truncation uses the explicit ratio bound of at most one half once the truncation index exceeds twice the Poisson parameter. Decimal arithmetic is high precision but is not itself an interval-arithmetic proof. The continuum of conductance ratios and positive times, the strict maximizer classification, and the sharp bound are proved analytically in `RESULT.md`.

Self-review of the claim has passed. Independent scientific audit has not been performed. The comparison with published literature may miss unindexed equivalent computations.
