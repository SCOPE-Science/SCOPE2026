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
# Verification of the projection formulas

The analytical proof is in RESULT.md; its parameter quantifiers are unrestricted integers \(a,b\ge2\). The crucial checks are substitution of the three explicit dipole-potential patterns into the graph Laplacian, counting currents using their strict potential-level order, and exact factorization of the candidate column-sum differences. Each is shown algebraically in the proof.

To reproduce the supplementary finite experiment, execute `python CHECK.py` using Python 3 standard library only. The script independently constructs a grounded Laplacian, inverts it over rational numbers and checks all 400 edge columns of sixteen graphs, then 20 additional representative edge columns from four parameter configurations. It separately compares all displayed rational phase identities and bounds for 1,089 parameter pairs; its expected stdout is:

`EDGE_CLIQUE_SUM_EXACT_OK graph_configurations=20 projection_columns=420 exhaustive_edge_columns=400 comparison_cases=1089`

The finite checks cannot replace the proof for all parameter pairs. No formal proof assistant and no independent mathematical audit have been used. The claim is restricted to canonical Euclidean-orthogonal projections.
