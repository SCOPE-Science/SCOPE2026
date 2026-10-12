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

# Finite semantic verification

The standalone Python 3 program `verify.py` uses only the standard library. Execute it in an arbitrary clean directory with `python verify.py`.

Direct procedure: for every \(1\le n,m\le6\), enumerate all \(m^n\) labeled functions \([n]\to[m]\). Independently evaluate the Boolean modal preservation equation for every one of the \(2^m\) subsets and each quota pair \((\ell,k)\). Compare resulting counts against the sorted-fiber partition formula, the balanced-existence arithmetic criterion, the dual-quota identity, and endomorphism permutations. Enumerate all \(3^9=19683\) functions \([9]\to[3]\) for the sample and check the three quotas separately.

Actual run output:

```text
VERIFY_OK direct_function_tables 82200 threshold_parameter_comparisons 441 positive_hom_families 74 nine_to_three_direct_maps 19683 nine_to_three_counts (1680, 11130, 1680)
```

The tests are finite. The all-parameter result rests on the mathematical proof in `RESULT.md`, not on extrapolation from enumeration. No independent human or external proof audit was performed.
