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

Run the standalone standard-library script with `python3 verify_subquorum.py`. It enumerates canonical partial colour partitions, checks each coloured vertex's majority among the coloured closed neighbourhood, computes the maximum-colour set, and tests the proposed structural list and count. It does **not** treat numerical enumeration as an infinite proof.

Observed output:

```
VERIFY_OK profiles=66 classified_optimal_unlabeled=629 smallest_part=1 maximum_order=10
EXAMPLE (3, 1) normalized=4 named=24
EXAMPLE (3, 3) normalized=26 named=156
EXAMPLE (3, 3, 3) normalized=75 named=450
EXAMPLE (4, 3, 3) normalized=1 named=24
EXAMPLE (4, 4, 1) normalized=2 named=48
EXAMPLE (5, 5) normalized=2 named=240
```

Every integer partition of orders four through nine with at least two nonempty parts and a part of size at least three is tested. Six further order-ten profiles are tested, including both multi-triple and multi-maximum-part cases. The original proof covers all finite orders and all numbers of multipartite parts under the stated hypotheses. No independent mathematical audit is claimed.
