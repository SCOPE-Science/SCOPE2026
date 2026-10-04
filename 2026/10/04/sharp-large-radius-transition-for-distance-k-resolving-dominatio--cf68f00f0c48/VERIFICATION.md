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

The checker constructs each balanced spider from its adjacency list, computes all-pairs shortest-path distances, and tests resolving sets by direct distance-vector uniqueness and distance-\(k\) domination by direct radius checks.

It independently enumerates all resolving sets of size \(q-1\), verifies that they contain one noncentral vertex on exactly \(q-1\) arms, checks that no smaller set satisfies both properties in the theorem range, and compares the complete minimum-set list for \(k\ge L+1\) with the depth-threshold counting formula.

Recorded output:

```text
VERIFY_OK
parameter_pairs_checked = 12
theorem_values_checked = 84
minimum_sets_checked = 47855
candidate_sets_checked_below_or_at_metric_threshold = 149125
parameters q = 3..5, L = 2..5
all direct resolving and distance-k domination tests matched the phase formula
all size-(q-1) resolving sets matched the one-vertex-per-q-1-arms structure
all k >= L+1 minimum-set counts and depth-threshold classifications matched
```

The finite computation is corroborative only. The theorem for arbitrary \(q\ge3\), \(L\ge2\), and \(k\ge\lceil L/2\rceil\) follows from the proof.
