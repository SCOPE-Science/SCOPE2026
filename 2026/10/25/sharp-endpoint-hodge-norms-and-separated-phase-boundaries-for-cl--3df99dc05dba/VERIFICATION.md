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

# Verification of the clique-augmented biclique norm theorem

The standalone Python checker uses exact rational arithmetic. It constructs each unweighted graph and independently tests the explicit Laplacian dipole potentials for the three edge classes. It computes absolute column sums directly over actual edges, compares all formulas, and checks sharp upper bounds at tested parameters. For 23 graphs it independently inverts the grounded integer Laplacian and reconstructs every projection column, providing a calculation independent of the proposed orbit potentials.

Successful run:

`CLIQUE_AUGMENTED_BICLIQUE_EXACT_OK orbit_cases=5712 orbit_edges=882504 grounded_graphs=23 grounded_columns=1013 sharp_limit_samples=3`

All exact rational comparisons passed. The five symbolic identities used to simplify the orbit-current sums were separately checked with exact algebra. The proof applies to every integer parameter in the stated domain; the enumerated finite range alone would not establish its universal quantifiers, uniqueness in the literature, or optimality among nonorthogonal projections.
