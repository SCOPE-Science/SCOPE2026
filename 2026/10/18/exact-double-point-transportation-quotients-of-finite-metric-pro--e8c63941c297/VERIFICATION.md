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
# Verification details

Execute `python verify_dp_product.py` under Python 3 with SymPy installed. The script uses exact rational arithmetic, without floating-point comparisons, to compute distance profiles and the double-point seminorm directly from the full product distance matrix. It compares the result to the sum of norms calculated independently on the factor marginals.

The exhaustive coefficient tests examine every \(\{-1,0,1\}\)-valued zero-total vector for products with sizes \((2,2)\), \((2,3)\), \((3,3)\), \((2,2,2)\), and an unequal-weight path/product case \((2,3)\). The respective test-vector counts are 19, 141, 3139, 1107, and 141. Three additional products of sizes \((3,3)\), \((2,3,2)\), and \((2,2,2,2)\) each receive 350 deterministically generated integer signed vectors. All eight instances independently compare the rank of the centered full distance matrix against the sum of the factor ranks, and construct a nonzero four-point signed rectangle in the seminorm kernel.

Separately, the factor polytope unit-ball vertices are enumerated from subsets of active rational inequalities for \(q=2,3,4,5\). The exact counts are 2, 6, 14, 30, and the computed rational coordinate sets coincide precisely with the two-level-cut formula. The facet inequalities are justified analytically in the result, not inferred solely from numerical convex hulls.

Expected final line: `ALL EXACT PRODUCT-NORM, NULLITY, AND FACTOR-VERTEX TESTS PASSED`.

These finite computations do not establish the universal claims by themselves. The complete argument uses separation of coordinate maxima/minima, an explicit right inverse to the marginal map, rank-nullity, and elementary polarity. No external or independent validation has been undertaken.
