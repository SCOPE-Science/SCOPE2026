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

# Verification notes

The script `palindrome_checker.py` requires standard Python 3 only and can be run with `python palindrome_checker.py`. It verifies the exact digit-prefix formula directly against independently enumerated palindromes over nine bases and five thousand integers per base, and tests exact rational ordering chambers, total mass, and the two-variable integral formula. Its completed output was:

```
CERTIFICATE_PASS exact_count_and_volume_comparisons 45082
example_two_three_log_density 0.3154648767857287
three_base_order_probabilities_for_uniform_scales_1_3_4 [((0, 1, 2), '17/36'), ((0, 2, 1), '19/72'), ((1, 0, 2), '5/36'), ((1, 2, 0), '1/72'), ((2, 0, 1), '7/72'), ((2, 1, 0), '1/72')]
```

The finite enumeration does not establish the infinite limiting distribution. The latter follows from the prefix formula, the weighted Weyl criterion for rationally independent reciprocal logarithms, zero measure of tie hypersurfaces, and the Gelfond--Schneider independence argument for the explicit family. These standard mathematical inputs are invoked as theorems, not computationally certified. The displayed three-base rational test uses *integer uniform scales* as a check on the integral routine and is not a claim that \(\log b_i\) have those integer values.
