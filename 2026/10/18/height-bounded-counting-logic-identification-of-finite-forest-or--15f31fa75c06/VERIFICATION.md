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

The mathematical proof is in `RESULT.md`. The finite tests below are exact enumerations, not substitutes for the infinite-family argument.

Run `python3 check_forest_orders.py` to enumerate all strict-poset presentations with topological labels on up to six vertices, confirm the height-sensitive colour-histogram claim against all competing posets, and compare the claimed orbit partition for every increasing-labelled forest on up to seven vertices.

Run `python3 check_boundary_dags.py` to exhaust all upper-triangular directed acyclic graph presentations on up to six vertices, determine that no forest-order counterpart can have a nonisomorphic equivalent DAG on at most five vertices, and reproduce a six-vertex obstruction.

Both scripts use only the Python standard library. They assert the expected conclusions. `verification_output.txt` contains the reproduced output of both commands. The seven-vertex rank-two witness and the six-vertex C2-equivalent pair are also proved directly in the result. Neither finite test establishes untested infinite cases, and neither is an independent review.
