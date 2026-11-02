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

The finite portion is replayable with `python3 verify.py` alongside `certificate.json`. Every certificate row is reconstructed against the ten-point path graph, not trusted as input. The checker verifies all sixteen distinct maximal independent sets, counts membership frequencies in ten columns, checks eight fixed-query traces at coordinates 1, 4, and 7, and validates all paths in the complete depth-four adaptive query tree. Direct exact VC-support searches and a memoized two-branch rank recursion cover every path order from 1 through 10. The two-component direct-product membership count is also checked. Its standard-library run printed:

```
PATH10_CERTIFICATE_PASS concepts=16 balanced_positions=2 VC=3 Ldim=4 tree_leaves=16
FIRST_PATH_GAP_PASS [(0, 0), (1, 1), (1, 1), (1, 1), (2, 2), (2, 2), (2, 2), (3, 3), (3, 3), (3, 4)]
TWO_COMPONENT_PRODUCT_PASS maximal_independent_sets=256
ALL_NEW_FINITE_CHECKS_PASS
```

The proof for all positive component counts is mathematical: componentwise maximal independence gives an exact Cartesian product; fixed-support shattering decomposes componentwise; depth-four adaptive trees concatenate; and concept cardinality forbids greater depth. These infinite quantifiers are not inferred from the finite checker. The proof does not claim a connected-family extension or a classification of all paths.
