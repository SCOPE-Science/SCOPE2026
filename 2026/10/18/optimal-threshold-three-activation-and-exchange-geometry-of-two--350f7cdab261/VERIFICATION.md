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

This package contains `verify_forward.py`, `verify_peeling.cpp`, `forward_output.txt`, `peeling_output.txt`, and `certificate.json`. Re-run both methods from the package root (Python 3 standard library; any conforming C++17 compiler):

```
python3 verify_forward.py replay_certificate.json
cmp certificate.json replay_certificate.json
g++ -std=c++17 -O2 verify_peeling.cpp -o verify_peeling
./verify_peeling
```

The forward program enumerates all labeled four-subsets, simulates the synchronous three-neighbor process, checks a finite group action, builds both optimum-exchange graphs and runs breadth-first search from every state. Its regenerated certificate is compared byte-for-byte with `certificate.json` in the package replay. The separate C++ verifier reconstructs its own adjacency lists and follows complement-core peeling instead of infection, then independently enumerates the complete jumping/sliding neighborhoods and exact distances. The two saved outputs record actual executions.

The proof certifies finite exhaustive facts for the sixteen-vertex rook and Shrikhande graphs at threshold three; it does not imply a statement about all graphs sharing their degree, diameter, spectrum, or intersection parameters. An independent external mathematical audit has not been performed.
