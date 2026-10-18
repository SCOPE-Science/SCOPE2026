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

The calculation can be repeated with `python3 verify_cograph.py` using Python 3 and no packages beyond the standard library. The program enumerates each graph's actual edges, detects all induced four-vertex paths by checking the degree multiset \(\{1,1,2,2\}\) on four vertices, tests every selected vertex subset for containment of such a path, and determines inclusion-maximality through every possible one-vertex extension.

The recorded successful run was:

```
VERIFICATION_OK bivariate_profiles=129 direct_subsets=169304 explicit_P4_masks=2576 crown_facets_orders=3..8 coefficientwise_tests=9282
```

Direct exhaustive profiles include all \(1\le a,b\le6\) and all \(0\le t\le\min(a,b)\), plus crowns of orders seven and eight. Each coefficient of the full bivariate induced-cograph polynomial is checked, as are maximal crown-face coefficients for all crown orders from three to eight. Additional exact-integer formula comparisons cover \(9282\) monotonicity triples with \(3\le a,b\le30\). The general case is justified by the structural proof and the nonnegative combinatorial coefficient argument, not by these finite checks. This program does not inspect publication priority and is not independent external scientific validation.
