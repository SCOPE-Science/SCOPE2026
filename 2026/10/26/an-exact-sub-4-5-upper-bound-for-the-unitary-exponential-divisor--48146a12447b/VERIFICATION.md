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

Run `python3 verify_density_bound.py` from the extracted package. The program is standalone, standard-library-only and recomputes all relevant rational prime-tail bounds and finite weighted sums.

Observed output:

```
CERTIFICATE_OK
leaf_count 2097152
common_denominator 9037114296609938214167920266348510000000
fixed_point_denominator 10000000
certified_upper_numerator 72112510149983208955226454671586496051993960400
certified_upper_denominator 90371142966099382141679202663485100000000000000
certified_upper_decimal 0.797959478913
tail_first_moment_bound 71 / 5000
tail_second_moment_bound 31 / 50000
strict_gap_from_4_over_5_numerator 922021114481483790584537296007919740030198000
```

The checker verifies the exact rational inequalities for the first two prime-tail moments, all \(8^7\) finite cylinders, integer denominator normalization, and strict comparison with \(4/5\). The infinite-density argument additionally requires the symbolic Chinese-remainder and convergent divisor-series steps proved in `RESULT.md`; finite enumeration alone cannot establish them. No independent validation has been performed.
