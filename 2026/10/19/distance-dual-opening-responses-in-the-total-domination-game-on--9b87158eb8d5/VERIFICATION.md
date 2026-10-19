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

Run `g++ -O2 -std=c++17 verify_exact.cpp -o verify_exact && ./verify_exact` and `python3 verify_recursive.py` in a directory containing the embedded source files. Both outputs should equal the included `exact_out.txt` and `recursive_out.txt`, ending with `VERIFY_OK`.

The C++ implementation builds the dodecahedral graph from an explicit thirty-edge list and the Desargues graph as the two-/three-subset containment incidence graph on a five-element set. It verifies explicit twenty-vertex isomorphism permutations with the appropriate generalized Petersen graphs. It computes the exact two-person minimax recurrence **for every one** of the \(2^{20}\) possible dominated-vertex masks, for both possible players. Descending numeric-mask order is safe because adding a nonempty new dominated subset strictly raises the binary mask. Every nonfinal mask has a legal move, as all vertices have neighbors. Both score arrays are therefore completely determined, not sampled.

The independently structured Python script builds \(\operatorname{GP}(10,2)\) and \(\operatorname{GP}(10,3)\) directly, runs cached recursion from initial states and validates all twenty first moves, all 380 ordered opening pairs and all shell distances. The scripts check the listed values via assertions. Identical outputs of the two mathematical constructions and algorithms were obtained. The verifier outputs are not independent external review.

Finite boundaries: two graphs of order twenty, first two legal moves and optimal continuations only. No infinite-family consequence or unverified partial search is claimed. This package does not include publisher full texts and needs no proprietary dependencies.
