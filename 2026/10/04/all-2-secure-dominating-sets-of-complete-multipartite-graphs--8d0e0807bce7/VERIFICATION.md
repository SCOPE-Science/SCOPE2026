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

The symbolic proof reduces 2-secure domination to the number of selected defenders outside each part. The exact threshold is one outside guard for one omission, two guards for two omissions, and three guards for three or more omissions.

The included checker is definition-level. It reconstructs every complete multipartite graph of orders two through ten, tests domination directly, and for every pair of distinct attacked vertices searches ordered pairs of distinct defenders in the required closed neighborhoods. It does not use the structural criterion to decide feasibility.

Recorded output:

```text
VERIFY_OK
multipartite_types_checked = 128
vertex_subsets_checked = 64916
orders = 2..10
definition-level two-attack test matched the structural criterion
all enumerator coefficients matched
```

The checker also compares every observed size coefficient with the closed coefficient formulas. The finite computation is corroborative only; the theorem for arbitrary part sizes follows from the proof.
