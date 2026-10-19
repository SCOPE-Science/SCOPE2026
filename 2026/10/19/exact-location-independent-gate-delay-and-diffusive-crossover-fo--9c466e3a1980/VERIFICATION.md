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

Run `python3 verify_antiphase.py` using Python 3 standard library. This builds transient rate matrices from edge-jump and gate-flip transitions independently of the closed formula, solves the linear mean-hitting-time systems in exact rational arithmetic, and cross-checks the rational three-term recurrence. The checks cover every integer \(1\le N\le13\) at positive rates \(1/7\), \(1/2\), \(1\), \(5/2\) and \(4\), all starting sites, for 520 rational comparisons. The script also checks nine sample diffusive-scaling convergence values and 24 sample rate-monotonicity inequalities. One completed run returned `CHECK_OK exact_source_state_comparisons=520 diffusive_checks=9 monotonic_checks=24`.

These finite verifications do not certify the global theorem. The global argument is the analytic decoupling of the backward equations, the exact reflecting-boundary constant, and direct asymptotic and derivative inequalities in `RESULT.md`. For any rational input, the recurrence gives exact values without rounding. The continuous hyperbolic formula is evaluated numerically only as a secondary check.

The theorem assumes a uniform initial gate state; a fixed gate state would have an additional spatially antisymmetric term. This is not validated for asymmetric switching or site-biased random walks.
