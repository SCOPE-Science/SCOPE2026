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

# Computational verification

Execute `python3 verify_primary.py`. This constructs the actual Eulerian adjacent-swap graphs by direct enumeration, checks every candidate neighboring swap, reconstructs connected components, and verifies isolated vertices, canonical representatives and edge totals for every \(2\le n\le8\).

Compile and execute `g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt && ./verify_alt`. This separate factorial-ranking/disjoint-set implementation performs exhaustive checks for \(2\le n\le9\).

Expected final lines include `DIRECT_PASS 8 40320 128 105840` and `INDEPENDENT_PASS 9 362880 256 1128960` respectively. A finite test is a corroborating consistency check; the structural theorem follows from the complete proof in `RESULT.md`. No independent human or external mathematical audit has been conducted.
