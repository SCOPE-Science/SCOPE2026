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

Run `python verify.py` using Python 3.9 or later with no external dependencies. The checker independently constructs each finite Zimin word both by its recursion and its binary valuation formula. For each finite word it enumerates all contiguous factors and, for every distinct factor, unions the position masks of all its occurrences. A candidate set is an attractor if and only if it intersects every such union. This direct factor-occurrence check is separate from the proof's maximal-letter reasoning.

Successful execution produced:

```
VERIFY_OK exhaustive_subsets_n1_to4=32906 optimal_candidates_n1_to6=33867 large_random_sets=80 center_neighborhood_checks=502 whole_attractor_polynomial_derived_from_symbol_classes
```

The `exhaustive_subsets_n1_to4` count is \(2^1+2^3+2^7+2^{15}=32906\). The `optimal_candidates_n1_to6` count is \(1+2+8+64+1024+32768=33867\). The program also verifies the maximal-symbol centered neighborhoods through order eight and tests eighty pseudorandom minimum candidates at order seven. The generating polynomial follows symbolically from the disjoint, independently selectable classes of symbol occurrences, rather than from fitting a numerical series.

Boundary and normalization checks: \(Z_1=1\) has one attractor, consisting of position one; empty position sets are rejected. All occurrences are linear and entirely internal to \(Z_n\). No attempt is made to certify arbitrary orders by finite enumeration, and no independent scientific review has been performed.
