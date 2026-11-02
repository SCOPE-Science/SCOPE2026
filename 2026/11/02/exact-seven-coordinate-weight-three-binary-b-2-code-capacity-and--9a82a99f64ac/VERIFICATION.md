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

The exhaustive finite certificate consists of `verify.cpp` (C++17) and an independent direct-sum check `verify_orbit.py` (Python 3). Run `c++ -O3 -std=c++17 verify.cpp -o verify && ./verify && python3 verify_orbit.py`. Their expected outputs are documented in `RESULT.md`; both were actually run against the packaged sources. The C++ code generates all 35 candidate triples and all integer-sum collisions, verifies the six-vertex C4-free maximum by enumerating 32768 graphs, branches exhaustively over candidates, and counts 48 extremal codebooks containing a fixed triple. The Python code separately checks the complete relabeling orbit by direct coordinatewise sums. The exhaustive finite search is a checkable computational proof for only this seven-coordinate weight-three case. Independent scientific validation has not been performed.
