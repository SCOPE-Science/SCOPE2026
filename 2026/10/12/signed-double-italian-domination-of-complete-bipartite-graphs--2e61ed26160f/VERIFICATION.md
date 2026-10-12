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

The checker represents each bipartition side by the counts of labels \(-1,1,2,3\). For every side state it computes the total label sum, the positive-label sum, and the exact multinomial multiplicity.

For a state pair it then applies the original signed double Italian requirements directly: every label must satisfy its closed-neighborhood inequality, every occurring label \(-1\) must see positive neighbor sum at least \(3\), and every occurring label \(1\) must see positive neighbor sum at least \(2\). No closed-form theorem is used to decide feasibility.

It exhausts all side-state pairs for
\[
2\le m,n\le12.
\]

Recorded output:

```text
VERIFY_OK
complete_bipartite_instances_checked = 121
side_state_pairs_checked = 3294225
minimum_labelings_counted_across_instances = 9100528918
all minima matched the piecewise formula for 2 <= m,n <= 12
```

The finite computation is corroborative only. The all-parameter theorem follows from the symbolic side-sum proof in `RESULT.md`.
