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

# Verification

All computations are exhaustive finite checks with an explicitly justified complete normal form, not experiments extrapolated to larger state sets. Compile `reach_census.cpp`, `independent_waves.cpp` and `violation8.cpp` with a C++17 compiler; execute `reach_census.cpp` with argument `8` and execute the other two without arguments. The resulting `violation8.txt` is the input to `orbit_check.py`, run in the directory containing the file.

The first program enumerates all \(8^8\) second-letter maps, filtering rank seven, and visits reachable nonempty subsets using forward BFS. The second enumerates all \(\binom82\cdot8\cdot7\cdot6!\) rank-seven maps in a different order and independently computes complete reachability and shortest-path multiplicities via levels. Both agree on \(1{,}128{,}960\) rank-seven maps, \(1{,}093{,}632\) completely reachable maps and \(544\) violating maps. Every violation has one hard six-subset, at distance \(17\); no other size violates. The word histogram is \(384,96,32,32\) for multiplicities \(2,3,4,5\). The rotation-orbit checker confirms \(68\) classes in orbits of size eight, partition \(48,12,4,4\), and independently computes shortest-path counts for each representative.

The embedded execution results were produced from the included source files, and the third enumerator output was compared byte-for-byte with the embedded canonical list. This does not establish historical priority or independent expert validation. The full text of one related scientific record was not accessible; no external audit was undertaken.
