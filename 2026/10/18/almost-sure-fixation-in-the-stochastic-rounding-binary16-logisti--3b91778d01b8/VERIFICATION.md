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

# Reproduction and limits

With Python 3, execute `python3 verify.py`. It uses only standard-library arbitrary-precision rational arithmetic and an exhaustive binary16 code range. It checks exact state decoding, strict sorting, bracketing/positive probabilities, every transition, the complete SCC decomposition, terminal classes, reachability sets, and a shortest-path statistic. Expected output reports `states 15361`, `edges 30623`, `reach_zero 15359`, `reach_three_quarters 46`, `both 44`, `only_zero 15315`, `only_three_quarters 2`, `max_shortest_absorption_path 23`, and `PASS`.

No data files, random seeds, numerical tolerances, mathematical packages or proprietary operations are required. The finite computation is exhaustive over exactly the specified binary16 state set, but it is not a claim about other number formats or arithmetic-operation orderings. All asymptotic stochastic claims then follow from the elementary finite-chain recurrent-class theorem; the checker does not simulate an infinite random trajectory. No independent audit was conducted.
