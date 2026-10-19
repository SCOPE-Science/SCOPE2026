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

The exact 24-vertex LCF graph, complete minimum-set list, and all exchange edges are contained in `mcgee_certificate.json`. `enumerate_mcgee.py` recursively enumerates **every** independent set, decides maximality by neighborhood coverage, exhaustively enumerates automorphisms by distance-compatible extension, and constructs all 146 BFS distance rows. `verify_mcgee.cpp` is a structurally separate verifier that tests all 16,777,216 subsets in C++17, checks the 146 minimum solutions, forms all one-token jumps by comparing pairs, independently verifies each is an edge-slide, and runs all 146 shortest-path searches. `check_mcgee_certificate.py` independently searches every subset of size at most eight and validates the published certificate and 32 explicit automorphisms.

To reproduce:

```sh
python3 enumerate_mcgee.py > primary_output.txt
g++ -std=c++17 -O2 -Wall -Wextra verify_mcgee.cpp -o verify_mcgee
./verify_mcgee > cxx_output.txt
python3 check_mcgee_certificate.py > checker_output.txt
```

The exact output records are provided for comparison. No randomness or third-party mathematical library is needed. Complete enumeration establishes cardinality eight and the exact 146 minima. The path searches are exhaustive on the finite 146-vertex exchange graph; they make no statement about other input graphs or infinite families. An external independent audit has not been performed.
