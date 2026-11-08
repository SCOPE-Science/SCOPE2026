---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PO is equivalent to assigning each good to an approver: otherwise transfer to an approver gives Pareto improvement; supported allocations maximize sum utility. Under binary values and supported assignments, EQX is exactly max_i u_i-min_i u_i<=1, which implies EFX by removing an approved good from any holder’s bundle. Because each agent approves two goods, utilities are 0,1,2; the range condition implies a matching saturates either all agents (u>=1) or all goods (u<=1), and such matchings construct the allocation. Edge-to-vertex injections exist in a connected multigraph iff e<=v (tree/unicyclic orientations); vertex-to-edge injections iff e>=v (spanning unicyclic subgraph). Thus mixed e<v and e>v components are the sole obstruction. Lower bounds four multigraph agents and six simple-edge agents follow from minimum multicyclic component edge count plus separate tree; explicit witnesses attain them. Independent enumerator tested all 1296 ordered four-edge profiles using four goods against all supported allocations.

## originality

PASS

Best-of-knowledge originality of the precise final result is retained after direct scope/implication comparisons and meaningful reading, with identified prior machinery and explicit inaccessible-source risks. No failed search is treated as a novelty proof.

## value

PASS

Provides a graph-theoretic forbidden-component classification, linear-time direct construction and sharp 4-versus-6 agent boundary for a natural restriction of simultaneous efficiency, envy and equitability fairness. The structural cycle-rank explanation goes beyond merely running a known generic fair-division algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
