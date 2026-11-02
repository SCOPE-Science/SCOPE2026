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

The standalone `verify.py` has no external dependencies and runs under Python 3. The invocation is `python3 verify.py` from the extracted file directory.

The test directly creates circular words from each run-length tuple, enumerates every pair of positive shifts shorter than the displayed period, and compares literal failed phases against the closed expression. It then checks the complete set of qualifying pairs, each finite delay-budget count, the uniqueness of the minimum-maximum-delay pair, and equivalence with finite words consisting of two periods. A primitive-period repeated-letter counterexample illustrates the necessity of the distinct-letter hypothesis.

Executed successfully on the embedded script content:

`VERIFY_OK cases=2537 shift_pairs=157381 delay_budgets=28563 two_period_checks=157381 mismatch_phase_evaluations=1368760 distinct_run_assumption_counterexample=00101`

The tests cover a finite parameter set and do not constitute a proof for arbitrary run lengths or alphabet sizes. The complete proof is in `RESULT.md`. External independent validation has not been performed.
