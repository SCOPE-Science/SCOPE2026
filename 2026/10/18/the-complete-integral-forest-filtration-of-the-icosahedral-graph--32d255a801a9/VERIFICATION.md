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
Execute `python3 VERIFY.py` in a directory containing the accompanying `CERTIFICATE.json`. The checker reconstructs the graph, all three filtration stages, the integer algebraic reductions and the acyclic matching certificates from standard-library operations. The stored certificate is compared for exact equality with the newly reconstructed proof data. The final success marker is `VERIFIED_ICOSAHEDRAL_FOREST_FILTRATION`.

The exhaustive computations include 4096 vertex subsets per degree, each checked for acyclicity using union–find and independent DFS algorithms; all 12 five-cycle open neighborhoods; all degree-zero surface links; and the full directed Hasse graph for the 68, 323 and 983 nonempty simplices at degrees 0, 1 and 2. The acyclic matchings contain 29, 147 and 471 pairs. Degree-one has a four-by-four minor of determinant one in its exact integral Morse differential; degree-two has no Morse differential. Direct mod-two homology calculations independently give reduced Betti numbers \((6,1)\) in dimensions \((1,2)\), twenty in dimension three, and forty in dimension four.

The finite proof applies to a fixed twelve-vertex graph; the stabilization for all degree bounds follows separately from the five-cycle-neighborhood argument. Independent external audit has not been performed.
