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

The theorem has an all-orders analytic proof. The exact finite verifier is included as `artifacts/verify.py` and may be run with `python3 artifacts/verify.py` using only the Python standard library.

The checker constructs extreme dual Lipschitz potentials from connected tight-edge graphs; for each graph containing a triangle, it evaluates the rank-two operator on every edge molecule and every extreme norming functional. It also constructs shortest-path auxiliary potentials for every flat graph edge of each extreme dual potential and checks the two norm-one decompositions with rational arithmetic. Actual run output:

`VERIFY_OK connected_graphs=770 triangle_graphs=541 dual_extremes=13376 norming_tests=58372 splittings=24466 n=3..5 exact=True`

The finite check covers all connected labeled simple graphs with three through five vertices only. It does not prove results for larger graphs, general metrics, or complex scalars. The proof establishes the all-order assertion using finite-dimensional polytope extremality, graph-integral Lipschitz potentials, and a rank-two operator with exact norm and numerical-radius bounds. The precise limits and assumptions are given in `RESULT.md`. Independent review has not been performed.
