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

# Reproducible finite verification

Compile the complete `verify_degree2_six.cpp` with a standard C++17 compiler. It enumerates each multiplicity assignment to the 63 nonempty vertex supports, with every vertex in three colors exactly, then fully checks all four maximal graph classes. The search is finite and backtracking prunes only logically impossible partial colorings. The separate Python implementation `verify_support_count.py` counts the same support vectors by memoization and checks the expected integer.

```sh
g++ -O3 -std=c++17 verify_degree2_six.cpp -o verify_degree2_six
./verify_degree2_six
python3 verify_support_count.py
```

Expected console output:

```text
PASS C6 canonical_color_list_types=2406208
PASS C3+C3 canonical_color_list_types=2406208
PASS C4+K2 canonical_color_list_types=2406208
PASS C5+K1 canonical_color_list_types=2406208
VERIFY_OK
INDEPENDENT_SUPPORT_COUNT_OK 2406208
```

All listed checks were actually executed successfully. A valid proportional list-coloring is an assignment selecting a listed color for each vertex, proper on every edge, using each color between the floor and ceiling of one third of its incidence-support size. Every available color has support of size at least one; every support vector corresponds to exactly one unrestricted-palette list assignment up to color relabelling.

The finite theorem follows because every six-vertex maximum-degree-two graph is contained in one of the four tested graphs and proportional choosability passes to subgraphs. This is not an unbounded-order experiment or a proof of the all-length path conjecture. Independent review and historical-priority certification remain unperformed.
