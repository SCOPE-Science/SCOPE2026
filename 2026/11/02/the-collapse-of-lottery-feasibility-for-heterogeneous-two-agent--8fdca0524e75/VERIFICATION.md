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

# Reproducibility

The embedded `verify.py` is a standalone Python 3 checker using exact `fractions.Fraction` arithmetic. The script independently enumerates all assignments of at most eight labeled chores and all positive rational weights \(p=A/B\) with \(2\leq B\leq9\), tests fractional Pareto optimality from minimum achievable total cost, direct weighted comparisons including zero-cost-item removals, and the lottery's feasible expected common-chore-count interval. It compares deterministic WEF counts with the explicit binomial formula and validates equivalence of deterministic and randomized feasibility. Invocation: `python verify.py`.

Observed output: `VERIFY_OK cases=16200 allocations=2211840 wefx_supports=133848`. Another separate closed-form checker independently passed 54,450 tuples. No computational timeout or approximate comparisons are used. The full infinite-domain result depends on the five-step analytical proof in RESULT.md, not exhaustive finite checking. No independent audit was performed.
