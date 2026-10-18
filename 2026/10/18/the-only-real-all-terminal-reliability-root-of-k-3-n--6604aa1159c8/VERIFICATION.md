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

# Reproducible verification and its scope

Execute `python3 verify_k3n_reliability.py` in the same directory as this document. No external package or network access is required.

Observed output from the packaged source:

`VERIFY_OK independent_connected_graphs=4 edge_subsets=37440 exact_n=2..20`

The checker enumerates all \(2^{3n}\) operational edge subsets for \(2\le n\le5\) and independently builds the reliability polynomial from the counts of connected spanning subgraphs; coefficient arrays agree with the factored formula. It verifies exact derivatives, leading coefficients and degrees, plus rational evaluations and the \(K_{2,n}\) comparison. The all-real and all-integer quantifiers depend on the displayed analytic proof; finitely many computations cannot establish them. The 2014 source's complete text was not available for inspection. Independent audit and validation have not occurred.
