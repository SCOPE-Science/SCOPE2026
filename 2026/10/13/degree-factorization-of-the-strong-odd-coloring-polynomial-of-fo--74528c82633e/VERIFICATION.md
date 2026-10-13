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

# Reproducible verification

Run `python3 verify.py` with Python 3's standard library. The checker implements the actual proper strong-odd condition on every vertex using local counts and independently evaluates the coefficient-extraction local factors with exact rational arithmetic; it does not use the theorem's recurrence inside the direct coloring predicate.

A completed run printed:

```
VERIFY_OK
full_brute_vs_product_comparisons 4516
full_brute_total_accepted_assignments 297098
closed_3_color_all_labeled_trees 18248
largest_brute_tree_order 9
series_vs_direct_local_factors 50
local_factors_q3_degrees_1_to_12 [1, 1, 1, 4, 1, 16, 1, 64, 1, 256, 1, 1024]
```

The exact proof in RESULT.md uses a bijection for arbitrary finite forests and palette sizes \(q\ge2\). Computer enumeration tests only finite instances and cannot establish all-order validity or mathematical originality. No independent audit has been performed.
