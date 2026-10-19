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

# Verification record

Run `python3 verify.py` from the directory containing the supplied file. The script needs Python 3 only. In the reported execution, **2,932 numerical assertions passed**. They cover the exact second/fourth generator balances, admissible fourth-moment envelopes, the critical-root formula and derivative regimes, optimal binary radii, large-radius limiting behavior, critical scaling, and direct regeneratively sampled trajectories for three parameter sets.

The simulated stationary samples draw exponential backward ages and independently reset position and fair spin, evolve the telegraph dynamics over the last-reset interval, and evaluate the terminal position exactly between flips. Monte Carlo tolerances account for finite sampling and do not establish infinitude-wide statements. Strict global minimization over all centered fourth-integrable reset laws, uniqueness, nonattainment above threshold, and the divergence exponent come exclusively from the fully stated algebraic proof in RESULT.md.

Source comparisons for priority are described in REVIEW.md and the structured scientific assessment. No independent audit or external certification has been performed.
