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

# Verification of the graph-negation census

The mathematical claim is proved in `RESULT.md`, including a complete row normal form, all graph strata, Burnside fixed-point counts, and the unrestricted graph-realization construction. Executable programs provide additional finite checks.

Run `g++ -std=c++17 -O2 verify_exhaustive.cpp -o verify_exhaustive` followed by `./verify_exhaustive`; its expected output is:

```
DIRECT_CENSUS_OK T=7820 F=1021 graph_counts=729,81,81,16,81,16,16,1 fixed_points=1021,41,41,10,10,41 isomorphism_classes=194
```

Run `python3 verify_graph.py`; its expected output is:

```
GRAPH_CLASSIFICATION_OK total=1021 classes=194 graph_counts=[729, 81, 81, 16, 81, 16, 16, 1] witness_graphs=75
```

`verify_exhaustive.cpp` generates candidate operation rows using elementary inequalities and checks every remaining importation and double-negation condition; its \(512000\) row combinations exhaust the restricted search space by the normal-form proof. `verify_graph.py` independently generates graph-indexed candidate rows and checks all five original axioms on the full \(8^3\) argument set. It additionally verifies the graph witness formula for all simple graphs on one through four vertices. The programs do not constitute a proof about infinite graphs or establish publication priority; those are separate mathematical and literature questions. All results are reproducible with a standard C++17 compiler and Python 3's standard library.
