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

# Reproducibility checks

Execute `python verify.py` using standard Python. The program enumerates all unordered approval profiles with \(n-2\) voters and two abstainers for each \(3\le n\le12\) using seven nonempty ballot masks, with exactly \(28\binom{n+4}{6}\) cases at each \(n\). It uses the exact greedy marginal-score identity and integer Kelly inequalities, never floating-point comparisons.

Expected failures are zero for \(3\le n\le11\) and six at \(n=12\). Six candidate permutations of the explicit representative give all cases. The script separately checks the witness and every minimal case with an independent fraction-valued PAV marginal-score evaluator. The proof of extension to larger electorates is algebraic and does not rely on testing finitely many larger populations.

These checks only verify this exact ballot-size, committee-size, coalition-size and tie-handling domain. Independent audit has not been performed.
