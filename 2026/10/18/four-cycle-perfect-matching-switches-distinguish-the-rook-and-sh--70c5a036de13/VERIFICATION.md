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

# Reproducibility

Run `python3 enumerate.py certificate.json` to regenerate every finite state and transition. Run `python3 verify_certificate.py certificate.json` to validate all 48 host edges per graph, every matching, every switch, and every shortest-path eccentricity against the supplied certificate. Compile and execute `independent.cpp` under C++17 for a separate partner-array implementation and independent shortest-path checks.

The matching enumeration covers every eight-edge perfect matching because the least unused vertex has exactly one partner. The local switch generator examines both other pairings of each disjoint matching-edge pair, which exhausts all alternating four-cycle switches. The graph traversal processes every state, not a sample. For the rook graph, the 72 isolated states also follow from the four-cycle count in the proof.

Computed output files are included. The finite certificates and source programs are part of this package and can be checked without external services. The check establishes the stated finite results, not novel implications outside these two graphs or independent external validation. Relevant literature may be incomplete.
