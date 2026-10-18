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

The accompanying `verify_closed_five_runs.py` uses a direct set of distinct nonempty factors and, for each factor, tests every nonempty proper border by locating all occurrences of the candidate border. A factor is counted precisely if a proper border occurs at just its initial and final positions; one-letter factors are counted by convention. This is a definition-level computation, independent of the mathematical run-family enumeration.

Run with `python3 verify_closed_five_runs.py`; observed output:

`ALL_FIVE_RUN_CLOSED_FACTOR_CHECKS_PASSED cases 9592 maximum_cartesian_length 20 sharp_family_parameters 10`

The tests cover every five-tuple with all run lengths between one and four, every composition of lengths five through eighteen into five positive parts, and ten exact evaluations on the asymptotically sharp construction. Source-file execution from the actual packaged code is required for reproducibility. Exhaustive finite tests do not establish correctness for unbounded run lengths; the complete proof is in `RESULT.md`.

The work was assessed for mathematical correctness, literature overlap and value in the self-review; no independent mathematical audit or external certification has taken place.
