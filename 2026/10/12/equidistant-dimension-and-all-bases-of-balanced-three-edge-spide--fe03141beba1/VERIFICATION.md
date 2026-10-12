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

The checker constructs the balanced three-edge spider \(T_q\), computes all-pairs shortest-path distances by breadth-first search, and tests the distance-equalizer definition directly.

For every \(q\in\{3,4,5,6\}\), it enumerates every vertex subset of cardinality at most \(2q\). It verifies that no smaller subset is a distance-equalizer set, enumerates every size-\(2q\) equalizer, and compares that complete family with the predicted \(q+1\) bases.

Recorded output:

```text
VERIFY_OK
parameters_q_checked = [3, 4, 5, 6]
subset_trials_size_at_most_2q = 547090
minimum_bases_checked = 22
all smaller sets failed
all minimum sets matched the q+1 structural bases
```

The finite enumeration is corroborative only. The universal statement for all \(q\ge3\) follows from the bipartite-class dichotomy and the unique-midpoint proof.
