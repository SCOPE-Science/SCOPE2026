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

# Executable checks and limits

The standard-library C++17 program `proof_checker.cpp` is the primary finite proof certificate. Run:

```
g++ -std=c++17 -O2 proof_checker.cpp -o proof_checker
./proof_checker
```

It enumerates the binary length-eight \((2,1)\) burst-output balls, checks that each has cardinality eight, constructs the complete disjointness graph, validates the fourteen-word correcting code, verifies the eight-word linear span, and exhaustively excludes all cliques of cardinality fifteen or more by a complete graph-coloring branch-and-bound. Its observed completion reads `VERIFIED maximum size 14, maximum linear size 8, packing bound 16, search nodes 430977`.

The supplementary `verify_independent.py` uses string slices rather than integer bits and solves the independent incidence-matrix packing problem using NumPy and SciPy. Run `python3 verify_independent.py`. Its observed completion reads `INDEPENDENT_CHECK_OK 14 8 14`. It is a consistency test, not a substitute for the exhaustive search proof. Both codes are for exactly length eight, not an indefinitely extending assertion. No independent external audit is recorded.
