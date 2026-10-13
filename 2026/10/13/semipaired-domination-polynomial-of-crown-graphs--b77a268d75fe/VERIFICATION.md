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

The checker constructs \(\operatorname{Cr}_n\) for \(3\le n\le8\). For every vertex subset, it tests domination from the graph adjacency relation. For every dominating set of even cardinality, it builds the partner graph whose edges join selected vertices at crown-graph distance at most \(2\) and tests for a perfect matching by exact search. It independently compares the full cardinality histogram, minimum value, minimum-set count, and total-set count with the theorem.

Recorded output:

```text
VERIFY_OK
n=3: gamma_pr2=4, minimum_sets=15, total_semipaired_sets=16, histogram={4: 15, 6: 1}
n=4: gamma_pr2=4, minimum_sets=62, total_semipaired_sets=91, histogram={4: 62, 6: 28, 8: 1}
n=5: gamma_pr2=4, minimum_sets=160, total_semipaired_sets=416, histogram={4: 160, 6: 210, 8: 45, 10: 1}
n=6: gamma_pr2=4, minimum_sets=345, total_semipaired_sets=1819, histogram={4: 345, 6: 912, 8: 495, 10: 66, 12: 1}
n=7: gamma_pr2=4, minimum_sets=651, total_semipaired_sets=7652, histogram={4: 651, 6: 2905, 8: 3003, 10: 1001, 12: 91, 14: 1}
n=8: gamma_pr2=4, minimum_sets=1120, total_semipaired_sets=31539, histogram={4: 1120, 6: 7616, 8: 12854, 10: 8008, 12: 1820, 14: 120, 16: 1}
vertex_subsets_checked = 87360
semipaired_sets_checked = 41533
all semipaired dominating sets were exactly even dominating sets of size at least four
```

The computation checks \(87{,}360\) vertex subsets and identifies \(41{,}533\) semipaired dominating sets over the tested orders. The finite computation is corroborative only; the arbitrary-order theorem follows from the analytic domination classification and complete-graph-minus-a-matching partner argument.
