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
# Reproducible checks

Run `python3 verify.py`. The script uses only Python's standard library, computes every payoff-induced resistance with rational arithmetic, verifies five rational parameter choices for both minimum barrier formulas, checks the degree-weighted potential identity on every unilateral flip of all eight action profiles, and enumerates all six-state directed in-trees at \(\theta=9/10\). Its output includes `EXACT_VERIFY_OK`, the six minimal exponent/coefficient pairs, and the \(2/5\), \(3/5\) critical limits.

The exact open-interval theorem additionally requires the analytic first-crossing lower bounds and explicitly exhibited attaining in-trees in `RESULT.md`. Finite sampled parameters cannot establish the continuum of allowed \(\theta\). No external human or independent audit has been performed.
