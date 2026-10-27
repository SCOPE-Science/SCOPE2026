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

Compile each of the two included C++17 sources with an optimizing C++ compiler and run without arguments. `reset_enum.cpp` enumerates all \(3125^2\) ordered pairs via bitmask BFS and tests strong connectivity through forward/reverse reachability. `reset_independent.cpp` enumerates the same pairs with frontier-by-length reachability and Floyd–Warshall transitive closure.

Observed output in `counts_bfs.txt` and `counts_layers.txt` agrees in all \(16\) finite-threshold bins, each of the two connectivity categories, the two nonsynchronizing subtotals, and the two moment totals. The entire population check is \(1,582,216+120,024+5,629,065+2,434,320=9,765,625\). The first-moment check is \(18,821,345+11,030,640=29,851,985\). The complete table is in `joint_counts.csv`.

The 2016 published marginal high-tail isomorphism-class sequence for lengths \(11\) to \(16\) is \((46,43,23,11,4,1)\). Multiplication by \(240\) reproduces this finite census's corresponding marginal counts exactly. This external comparison confirms the high tail only, not the other bins or their connectivity splits.

All computations certify the finite sample-space statement, not a universal formula for other state counts. No independently performed scientific audit or external validation is implied by the existence of separately implemented verification programs.
