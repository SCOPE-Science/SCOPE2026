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

# Verification of the slow-return telegraph theorem

The complete standalone program `verify.py` can be run with Python and installed `mpmath`, `scipy`, and `numpy` packages; no input files or external services are required. Its analytical checks reproduce the previously published exact expression using two independent hyperbolic forms, verify the positive real cubic threshold, test strict convexity numerically at representative parameters, compare series coefficients at small alarm rates, and numerically locate global large-return-cost optimizers in each of the three regimes.

An additional check integrates the killed telegraph resolvent over both the negative and positive half-lines to obtain the expected return distance from first principles. Three independent event-driven simulations, each containing 42,000 complete first-passage trajectories including time spent returning, yielded relative errors approximately 0.001945, 0.005473, and 0.001504 against the exact mean. All 70 program comparisons passed in the recorded execution.

The proof uses the explicit absolutely convergent power series for the return-cost factor and the global localization argument; finite numerical tests are not substituted for strict convexity, uniqueness, or asymptotic statements. Simulation discrepancy is sampling error, not an exact error bound. Reproducing the source renewal model assumes telegraphic reversals, memoryless alarms, no new alarm or absorption while returning, and independent symmetric reinitialization after each return.
