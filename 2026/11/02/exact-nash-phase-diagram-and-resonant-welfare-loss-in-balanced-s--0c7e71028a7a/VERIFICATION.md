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

The standard-library script `verify.py` was run successfully. It enumerated 533,660 complete partition/parameter cases, compared a direct strict unilateral-deviation tester against the theorem's structural condition, and observed 6,215 stable partition incidences. Direct additive-payoff welfare evaluations agreed with the independent quadratic identity, and both the exact count and extrema agreed for all tested parameters. Separate integer enumeration tested the labeled-count formula through population size 11 per type.

The script uses rational parameters to avoid floating-point threshold errors. It does not certify claims for arbitrary real parameters or infinitely many population sizes: these are established by the proof in `RESULT.md`. No independent audit is claimed. Run `python verify.py` with Python 3.9+.
