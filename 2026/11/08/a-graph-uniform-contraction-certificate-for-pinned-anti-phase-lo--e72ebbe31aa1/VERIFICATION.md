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

# Reproducibility and verification

Run `python check.py` from the directory containing this file, with Python 3, SymPy, and NumPy installed. The program uses exact symbolic arithmetic for the parameter identities, endpoint identities, and rational witness and uses numerical full-Jacobian spectra only as cross-checks on finite graphs. It checks 10 graph examples spanning cycles, complete bipartite graphs, hypercubes, and square tori, a total of 116 vertices.

Observed result:

`VERIFY_OK symbolic_identities=6 endpoint_checks=5 graph_families=10 vertices=116 rational_orbits=10 full_Floquet_matrices=10 uniform_four_step_bound=71/2 - 17*sqrt(17)/2 explicit_rational_multiplier=100/529`

The non-numerical all-graph proof appears in `RESULT.md`: double stochasticity of the normalized bipartite adjacency gives the complete two-step multiplier spectrum; matrix multiplication gives the graph-uniform four-step norm; differentiation and an elementary radical bound yield strict contraction; a uniform second-derivative bound supplies an explicit attracting ball. The checker does **not** prove a universal statement by finite enumeration. Neither independent scientific validation nor a definitive priority audit has been performed.
