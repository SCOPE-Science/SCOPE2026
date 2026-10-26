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
# Verification of the bounded-height four-run polynomial

The standalone `verify_piecewise.py` was run directly. It implements greedy subsequence matching and breadth-first searches for the first subsequence introduced by inserting each binary symbol at each cut. This independently verifies the individual-word height formula using the published one-insertion theorem, without using the run-block distance recurrence in the research proof. Small direct subsequence-set tests confirm the automata-distance computation.

Command: `python3 verify_piecewise.py`

Observed output: `VERIFY_OK four_run_bfs=4096 height_polynomials=9 length_extrema=22 direct_subword_pairs=8192`

The four-run loops cover all positive parameter quadruples with each entry at most eight. The polynomial enumeration is checked at heights three through eleven, and the numerical extremal statements at lengths four through twenty-five. The direct-subsequence check covers \(8192\) one-symbol insertions of short binary words. These are finite experiments. They do **not** by themselves prove the formula for unbounded runs or all height thresholds. The infinite argument uses the cited Simon-congruence distance formulas and algebraic independence of the opposite-run pairs. No independent external audit was conducted.
