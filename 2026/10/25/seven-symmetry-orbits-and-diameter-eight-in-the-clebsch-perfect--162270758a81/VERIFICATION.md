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
# Finite verification

The graph is the Cayley graph on the sixteen four-bit words with XOR generators `1, 2, 4, 8, 15`; its 40 edges are independently reconstructed. The complete proof computes the finite 705-state reconfiguration graph using all eligible matchings and all valid alternating quadrilaterals, not sampling or a randomized test.

Run `python3 verify.py`; expected final line: `ALL_VERIFY_OK`. This enumerates matchings using a first-uncovered-vertex recursion, independently counts them by a subset recurrence, constructs all flips by cross-pairings, checks the complete adjacency relation against all unordered matching pairs, runs 705 exhaustive breadth-first searches, verifies the 2160 edges and the full distance spectrum, and applies 1920 explicitly constructed graph automorphisms to recover the seven symmetry types and all direction profiles.

Compile `c++ -std=c++17 -O2 -Wall -Wextra verify_alt.cpp -o verify_alt` and run `./verify_alt`; expected final line: `ALL_VERIFY_OK`. This separately enumerates all matchings as 40-bit edge masks, constructs the switch graph solely by symmetric differences, and recomputes all breadth-first distances. Its independent outputs include 705 states, 2160 undirected edges, radius 7, and diameter 8.

The unordered-pair shortest-path histogram is `1:2160, 2:8040, 3:22360, 4:45160, 5:64800, 6:61920, 7:34880, 8:8840`. The sum of those eight counts is 248160, the exact number of unordered pairs of distinct matchings. The five radius-seven centers are the five matchings consisting entirely of edges of one generator direction.

These programs establish a finite exhaustive certificate for this graph only. The previously known count of 705 is included solely as a coverage and correctness check. No independent audit has been performed.
