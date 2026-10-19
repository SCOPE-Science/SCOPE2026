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

# Reproducible finite-distance verification

Run `python3 verify_python.py` to enumerate the complete derangement matching spaces and perform breadth-first search on explicitly built switching graphs. Run `g++ -std=c++17 -O2 verify_cpp.cpp -o crown_check && ./crown_check` for an independently enumerated perfect-matching search with direct on-demand neighbor generation. Both are standard-library-only standalone programs. Their expected JSON outputs are `verify_python.out` and `verify_cpp.out` (format differs, mathematical fields match).

The verification spans **all** matching states, not a random sample, for each \(4\le n\le9\). Conjugation of derangements preserves matching flips; a BFS from every cycle-type representative therefore suffices to determine the complete eccentricity and farthest-vertex spectrum. For \(n=9\), each BFS visits exactly \(133,496\) states; all eight cycle types are represented. Both programs independently verify a unique inverse at distance ten for cycle type \((3,3,3)\), with no source of another type attaining distance ten.

The analysis certifies only the displayed six finite sizes, not an asymptotic theorem. A verification program successfully reproducing an output file is not independent external mathematical review.
