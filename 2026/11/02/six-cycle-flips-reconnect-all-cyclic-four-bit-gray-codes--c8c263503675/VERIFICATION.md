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

# Verification of the finite short-flip classification

The two source files are standalone and require no input data. Run `python3 verify.py`, followed by `c++ -std=c++17 -O2 verify_alt.cpp -o verify_alt && ./verify_alt`. Both implementations must terminate successfully and print `FULL_VERIFY_OK` or `INDEPENDENT_VERIFY_OK`.

Python enumerates the 24 squares and 128 hexagons independently of the Hamiltonian cycles and builds flip adjacency by XOR. C++ builds Hamiltonian masks separately and instead enumerates every unordered pair, recognizing a valid flip by connectedness and degree conditions on its symmetric-difference edge set.

Both obtain 1344 Hamiltonian cycles; 1920 square-only transitions with components 240 of size 1 and one of size 1104; 9408 hexagon-only transitions forming one component; 11328 combined transitions forming one component; and, for the latter two graphs, eccentricity distribution {5:432, 6:912}. These certify radius 5 and diameter 6. All distances use complete breadth-first searches, no sampling. The two programs provide reproducible exact finite enumeration, not an independent scholarly audit.
