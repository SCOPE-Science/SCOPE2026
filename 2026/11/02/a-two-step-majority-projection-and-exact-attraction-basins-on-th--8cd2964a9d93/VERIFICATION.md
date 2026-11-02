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

# Reproducible verification

The state-space size is exactly \(2^{14}=16{,}384\), and both executable implementations process all its labelled elements. These checks were performed directly against the packaged sources:

- `python3 check_fano.py` regenerates the seven Fano lines as unordered triples \(\{a,b,a\mathbin{\mathrm{xor}}b\}\), checks the complete ten-case projection of all 128 subsets, its idempotence and fibers, the fixed-state hexagons, then explores the full graph dynamics by a path-following implementation. The recorded output is `check_fano_output.txt`; every assertion passed.
- `g++ -std=c++17 -O2 -Wall -Wextra check_heawood.cpp -o check_heawood && ./check_heawood` independently constructs the cubic incidence graph from an explicit line list, builds the entire Boolean transition map, calculates its functional digraph through indegree peeling, and checks exact basins, first-entry counts, \(F^4=F^2\), and a sharpness witness. Its recorded output is `check_heawood_output.txt`; every assertion passed.

The exact proof in `RESULT.md` is separate from these runs: all 128 Fano subsets fall into ten disjoint incidence types. That finite symbolic classification establishes the two-step projection and resultant recurrence structure without sampling. The verification programs use different Fano-graph construction methods and different recurrence-enumeration algorithms. Neither is an independent external audit.

Limits: the theorem is restricted to synchronous binary strict-neighbor majority on the fourteen-vertex Heawood graph. The computations establish exact finite results but not priority relative to every historical publication. Historical literature comparisons and remaining originality risks are recorded in `REVIEW.md` and `AUDIT.json`.
