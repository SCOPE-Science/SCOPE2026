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

# Verification record

The complete source files are `artifacts/census_bfs.cpp`, `artifacts/census_floyd.cpp` and `artifacts/check_nine_profiles.cpp`. Each has a corresponding text output named `bfs_output.txt`, `floyd_output.txt` or `nine_profiles_output.txt` in the same directory. Only a standard C++17 compiler is required. For example, from the extracted package root:

```
g++ -O3 -std=c++17 artifacts/census_bfs.cpp -o census_bfs
./census_bfs > replay_bfs.txt
diff -u artifacts/bfs_output.txt replay_bfs.txt

g++ -O3 -std=c++17 artifacts/census_floyd.cpp -o census_floyd
./census_floyd > replay_floyd.txt
diff -u artifacts/floyd_output.txt replay_floyd.txt

g++ -O3 -std=c++17 artifacts/check_nine_profiles.cpp -o check_nine_profiles
./check_nine_profiles > replay_nine_profiles.txt
diff -u artifacts/nine_profiles_output.txt replay_nine_profiles.txt
```

The first two counters exhaust every integer mask for every bipartition of orders \(5\) through \(9\). The main computation enumerates \(2^{20}\) masks of size \(4\times5\), with no graph-isomorphism pruning, heuristics, samples, random tests, or timeout-dependent exclusions. Connectivity and shortest-path multiplicity are computed independently via BFS and Floyd--Warshall with layer dynamic programming. The code paths are readable and contain no external or omitted dependencies. The third BFS-based classifier independently gives the three \(9\)-vertex maximizing profiles and counts \(120\), \(240\), \(60\).

Limits: these checks prove only the exhaustive finite-range graph statement. The externally reviewed status remains not performed, and no publication-level independent validation is claimed.
