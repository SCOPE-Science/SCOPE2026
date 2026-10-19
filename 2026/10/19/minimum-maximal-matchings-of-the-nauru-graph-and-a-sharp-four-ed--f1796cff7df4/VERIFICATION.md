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

# Finite verification

The host graph is the explicit 24-vertex generalized Petersen graph with the 36 edges specified in `RESULT.md`. An eight-edge matching is maximal exactly when its eight omitted vertices form an independent set. The cubic edge-domination count gives the lower bound eight without computation.

The Python program `verify_by_unmatched.py` enumerates every eight-element vertex subset, checks the independence condition, and uses the least-remaining-vertex rule to enumerate every complementary perfect matching. It finds 2,964 independent eight-sets, of which 2,874 have no complementary perfect matching and 90 have exactly one. The C++17 program `verify_by_matching.cpp` directly enumerates the vertex matching decisions, rejecting branches with adjacent unmatched vertices, and returns the same 90 unique minimal maximal matchings. Their lists agree entry by entry.

The complete canonical configuration list, all exchange edges for budgets one to four, the three 30-vertex components and eccentricity data are in `certificate.json`. The supplementary `matchings_cpp.txt` independently records the direct C++ enumeration. The checker `check_certificate.py` revalidates the canonical graph, every optimum and transition, BFS connectivity and eccentricity, and actions of rotation and reflection. All three programs and the certificate were replayed successfully using their supplied paths, with the recorded outputs `verification_python.txt`, `verification_cpp.txt`, and `verification_check.txt`.

Reproduce from a single directory holding these files:

```sh
python3 verify_by_unmatched.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_by_matching.cpp -o verify_by_matching
./verify_by_matching
python3 check_certificate.py
```

The SHA-256 of the deterministic UTF-8 `certificate.json` is `4fdad93ab72e812b23de4ffe5e1b1bf818cd8b849b96c19d79f88112306c5a6b`. This certificate and the source programs support exhaustive results **only for the specified finite graph**. No theorem about arbitrary generalized Petersen graphs, reconfiguration through nonmaximal intermediate states, or external independent validation is supplied.
