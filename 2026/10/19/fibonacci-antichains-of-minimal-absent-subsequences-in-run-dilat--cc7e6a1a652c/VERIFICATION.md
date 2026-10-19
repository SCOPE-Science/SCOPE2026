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

The accompanying Python 3 program `verify_mas_fibonacci.py` checks the finite consequences of the theorem using two distinct implementations. The direct construction explicitly builds distinct scattered subsequences and tests every single-letter deletion of each absent candidate; the alternative uses the greedy pair-state transition criterion. Both agreed for every tuple of two- or three-letter runs with 2–6 runs (124 cases), including terminal-letter counts and complementation. The transition implementation also tested 24 further nonuniform cases, with at most 25 runs and individual lengths between 2 and 14. The run-specific mathematical induction in RESULT.md supplies the arbitrary-parameter proof; finite tests do not establish the infinite result or originality.

Execution command: `python3 verify_mas_fibonacci.py`.
Expected output: `ALL_FIBONACCI_RUN_MAS_CHECKS_PASSED independent_direct_cases 124 nonuniform_large_run_cases 24`.

Publication-index comparisons do not eliminate the possibility of an equivalent historical result. No independent scientific audit has been performed.
