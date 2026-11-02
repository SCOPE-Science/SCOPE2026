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

# Reproducibility and scope
The complete finite verifier is embedded as `petersen_exact.cpp`, to be compiled as C++17 with no nonstandard dependencies. Run:

```sh
c++ -O3 -std=c++17 -Wall -Wextra -pedantic petersen_exact.cpp -o petersen_exact
./petersen_exact 4 33
./petersen_exact 5 41
```

Results obtained on the attached exact source:

```
LOWER_EXHAUSTIVE k=4 cap=33 explored_partial=5868128 complete_tuples=1912264 feasible_at_most_cap=0
CERTIFIED_LOWER_BOUND 34
WITNESS k=4 weight=34 VALID=true
LOWER_EXHAUSTIVE k=5 cap=41 explored_partial=366823529 complete_tuples=77570086 feasible_at_most_cap=0
CERTIFIED_LOWER_BOUND 42
WITNESS k=5 weight=42 VALID=true
```

Each integer loop is complete for its defined finite domain. The checker lists the five-position labelings from \(\{0,2,3\}^5\), computes all exact minima over inner five-position labelings, and prunes only when the necessary lower bound exceeds the requested budget. The direct upper-bound verifier uses the original undirected Petersen adjacency, not the precomputed dynamic table. No numerical tolerance, randomized heuristic, third-party optimization library, or unstated certificate path is needed for this exhaustive proof. Independent audit is not represented or inferred.
