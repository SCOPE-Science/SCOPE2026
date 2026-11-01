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

# Verification of the integral three-cut formula

Running `python3 verify.py` with Python standard library reconstructs every connected three-vertex induced subgraph of the relevant Cartesian product, forms all higher 3-wise-connected subsets up to a dimension that excludes unexamined facets, and separately compares all faces against the coordinate-line, square and long-edge predicted facets. It then calculates boundary ranks over \(\mathbb F_2\), including every nonzero chain degree.

The tested factor tuples are \((2,2,2)\), \((2,2,3)\), \((2,3,3)\), \((3,3,3)\), \((2,3,4)\), and \((2,2,5)\). The resulting \((\beta_1,\beta_2)\) of the Alexander dual are respectively \((4,1)\), \((12,6)\), \((36,20)\), \((108,53)\), \((72,43)\), and \((40,28)\), with no higher homology in these computations. The checker prints `CARTESIAN_CLIQUE_ORDINARY_THREE_CUT_DUAL_CHECK_OK` on complete success.

The finite mod-two computation does not establish torsion-freeness or any theorem for untested parameters. The integral all-parameter proof is the face classification, the explicit elementary collapse sequence, simple connectivity of the two-dimensional cell model, and combinatorial Alexander duality in `RESULT.md`. It establishes the integral assertion without extrapolating from data. No independent audit has been performed.
