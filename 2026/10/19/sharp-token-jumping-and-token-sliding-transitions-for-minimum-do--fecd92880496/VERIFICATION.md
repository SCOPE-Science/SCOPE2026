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
# Reproducible checks and their limits

The two included programs are standalone and use different representations and constructions. `verify_direct.py` independently generates **every** three-vertex subset of the Kneser pair graph for \(5\le n\le10\), explicitly tests closed-neighborhood domination, and constructs every legal jump and slide from the exact resulting optimum sets. It enumerates the connected components by breadth-first search and writes `direct_output.json`.

The C++17 `verify_constructive.cpp` builds all triangles and all three-edge matchings without using the Python domination enumeration, directly checks every candidate's domination property and every exchange edge, and checks the predicted components and degrees for \(5\le n\le11\). It writes `constructive_output.txt`. The verification commands are provided in RESULT.md. Both were actually executed; outputs in this package were produced by those executions.

These finite checks validate boundary cases, algorithm consistency and the formulas on the checked range; they are **not** a proof for unbounded orders. The infinite theorem is proved by the target-edge installation invariant and the two-slide simulation in RESULT.md. No human/independent audit, formal proof-assistant certification or priority certification was performed.
