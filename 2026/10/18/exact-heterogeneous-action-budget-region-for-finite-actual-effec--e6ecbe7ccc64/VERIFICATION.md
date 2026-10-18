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

# Verification

The standard-library script `verify.py` was executed against its own standalone action-profile semantics. The output was:

```
VERIFY_OK slices=15920 games=1152 action_profiles=305424 budgets=21760 strict_example=(3,4,4)
```

It exhaustively checked coordinate-fixed slice surjectivity on all budget tuples with two to five agents and budgets one through four. It rebuilt actual-effectivity families from random finite deterministic games, applied all selected feasible heterogeneous action vectors, and compared the families exactly. The direct product-capacity identity and strict asymmetric example were also tested. These are reproducibility checks for a separately provided mathematical proof. The script neither proves arbitrary parameter cases nor validates scientific priority. An independent audit has not been performed.
