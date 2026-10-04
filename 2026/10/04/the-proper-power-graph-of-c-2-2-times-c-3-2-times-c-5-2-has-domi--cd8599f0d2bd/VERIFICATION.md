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

The standalone `verify.py` checks the exact finite reduction and lower-bound certificate. It reconstructs all \(139\) nonempty partial assignments in coordinate alphabets of sizes \(3,4,6\), builds the complete comparability graph, checks the explicit dominating family of size \(11\), and exhaustively rules out a dominating family of size at most \(10\) by branch-and-bound. The search uses only a maximum-new-coverage lower bound for pruning and memoizes a state only after all of its branches fail.

Observed output:

```text
VERIFY_OK
group_order=900
proper_power_vertices=899
cyclic_subgroup_types=139
dominating_witness_size=11
no_dominating_family_size_10=true
branch_nodes=1022864
```

The computation proves this finite claim only; it does not certify a formula for larger prime sets or higher Sylow ranks.
