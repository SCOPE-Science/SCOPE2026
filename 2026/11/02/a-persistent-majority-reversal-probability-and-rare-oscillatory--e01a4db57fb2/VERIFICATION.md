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

Run `python3 check_majority.py` in the directory containing this file and the verifier. The script uses Python's standard library only. It reconstructs the strict-majority/tie-retention update directly from adjacency data on every labelled binary state for \(1\le n\le5\), then checks the full first-periodic-entry-time and eventual-period table against the independent shore-count map and its binomial multiplicities.

It additionally checks the all-parameter finite sum and orbit/fixed-state formulas for each \(1\le n\le30\), as well as the numerical values of the two explicit asymptotic constants. The output is `check_output.txt`, ending with `BALANCED_TRIPARTITE_MAJORITY_CHECK_OK`.

These experiments exhaust only the specified finite sizes. The general theorem is established by the complete zero/one/two/three-tie case split and the probabilistic limit calculations in `RESULT.md`. The exact finite sum is part of the mathematical proof; the code is supplementary validation rather than infinite certification. Independent audit was not performed.
