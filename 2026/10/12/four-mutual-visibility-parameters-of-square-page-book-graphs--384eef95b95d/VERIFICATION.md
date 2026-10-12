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

The checker constructs each square-page book, computes all-pairs distances, enumerates the internal-vertex masks of every shortest path, and tests mutual, outer, dual, and total visibility directly.

For every \(2\le r\le7\), every vertex subset is tested. The program verifies value \(2r\) for all four variants and verifies that the common maximum is unique and consists of all non-spine page vertices.

Recorded output:

```text
VERIFY_OK
book_parameters_checked = 6
subset_variant_trials = 436800
pair_visibility_variant_checks = 349440
parameters r = 2..7
all four visibility numbers equal 2r
the common maximum set is unique and equals the 2r internal page vertices
all independent mutual-visibility numbers equal r+1
the two maximum independent sets match the theorem
```

The independent-mutual-visibility lines are an additional sanity check and are not part of the claimed theorem. Finite computation is corroborative only.
