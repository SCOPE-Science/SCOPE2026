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

The symbolic proof establishes that a set power dominates a spider exactly when it contains the center or meets at least all but one arm. The generating polynomial follows by separating center-containing sets from center-free sets that meet all arms or exactly all but one arm.

The included checker independently constructs each spider as an adjacency list and simulates the domination step and subsequent forcing process from the definition. It then compares every subset with the structural characterization and the full coefficient vector. A second exact-rational routine checks the finite arm-balance extremal census at three positive activities.

Recorded output:

```text
VERIFY_OK
spider_types_bruteforced = 432
vertex_subsets_checked = 483024
extremal_part_shapes_checked = 1392
extremal_evaluations_per_shape = 3
```

The finite computations are corroborative only. The all-orders characterization and the extremal theorem for every real \(x>0\) rest on the symbolic proof and strict transfer identities.
