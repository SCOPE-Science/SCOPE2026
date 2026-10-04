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

The proof reduces the definition to arm counts: a geodesic in a spider uses one arm or two arms, so the exact necessary and sufficient constraints are \(a_i\le 2\) and \(a_i+a_j\le 2\) for distinct arms. These constraints are equivalent to the two patterns stated in the finding.

The included checker does not use that characterization. It constructs each spider as a graph, reconstructs unique shortest paths, tests every edge subset directly against the requirement that no geodesic contain three selected edges, and independently tests inclusion-maximality.

Recorded output:

```text
VERIFY_OK
spider_types_checked = 432
edge_subsets_checked = 241512
arm_lengths = 1..4, total_edges <= 10, number_of_arms = 3..5
```

The finite computation is corroborative only. The theorem for arbitrary positive arm lengths follows from the symbolic proof.
