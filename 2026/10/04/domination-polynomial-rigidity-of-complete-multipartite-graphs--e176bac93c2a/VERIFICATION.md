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

The symbolic proof uses only the multipartite support of a selected vertex set. A nonempty set either lies in one part or meets at least two parts; these cases determine its external neighborhood and domination status exactly.

The included `verify.py` independently enumerates vertex subsets, computes external neighborhoods and domination directly, and compares the resulting polynomials with the formulas. It then reconstructs the part-size multiset separately from each polynomial.

Recorded output:

```text
VERIFY_OK
definition_level_types = 128
vertex_subsets_checked_per_polynomial = 64916
ordinary_D_formula_and_inverse_types_through_30 = 28598
J_collisions_checked = 0
D_collisions_checked = 0
```

The definition-level enumeration covers every complete multipartite isomorphism type of orders two through ten. The ordinary-polynomial inverse is additionally replayed on every complete multipartite isomorphism type through order thirty. These finite checks corroborate but do not replace the all-orders proof.
