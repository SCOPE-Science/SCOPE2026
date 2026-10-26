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
# Mathematical verification

The analytic argument reduces the full incidence graph Laplacian to the Johnson graph, proves an explicit shell-current sign rule, and evaluates the absolute current sum through a separately checked degree-two dual potential.

Run `python verify_boolean_layer_hodge.py` with SymPy installed. The observed result was:

`BOOLEAN_ADJACENT_RANK_HODGE_OK orbit_cases=54 orbit_edge_types=872 full_cases=9 full_edges=445 symbolic_identities=PASS`

The 54 orbit solves and nine grounded whole-graph solves use exact rational arithmetic. The symbolic check expands the dual-potential Laplacian equations for arbitrary integer parameters. These checks do not constitute a computational proof over infinitely many ranks and sizes; the unrestricted assertion rests on the written analytic proof. No independent mathematical audit has been performed.
