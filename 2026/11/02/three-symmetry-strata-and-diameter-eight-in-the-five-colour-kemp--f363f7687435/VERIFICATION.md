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

## Reproducible finite checks

Run `python3 verify_primary.py`, then `g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt` and `./verify_alt`. Both self-contained programs reconstruct all 66,240 legal states and Kempe edges and verify 547,200 undirected edges, the three degree/symmetry classes, exact distance profiles and radius seven/diameter eight. The Python certificate compares bichromatic edge incidence directly; the C++ certificate uses a separate endpoint-component algorithm. Their agreement is repeatability, not an external independent scholarly audit. The formal classification is finite and relies on exhaustive traversal, not sampling.
