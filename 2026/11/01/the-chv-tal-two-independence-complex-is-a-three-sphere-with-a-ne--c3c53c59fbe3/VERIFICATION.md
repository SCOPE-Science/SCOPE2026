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

# Verification

Run `python3 verify_chvatal_twoind.py` beside the included `MORSE_PAIRS.json`, with Python 3 and its standard library. The provided `CHECKS.txt` contains the exact expected console output. The checker reconstructs all masks rather than trusting certificate counts. It tests the 4096 possible vertex subsets using two independent definitions of the simplices; enumerates all 1428 face-cover incidences; independently reconstructs and compares the 211 matching pairs; topologically sorts the entire reversed-matching Hasse digraph; and determines the two critical cells of dimension zero and three. This complete acyclic matching yields the integral \(S^3\) homotopy type by discrete Morse theory. The checker also calculates chain boundary ranks modulo \(2,3,5\), enumerates the entire graph automorphism group, validates the specified generators, and calculates every signed Lefschetz trace in both the new complex and the ordinary-independence comparator.

Counts: 424 nonempty simplices; \((12,66,148,142,52,4)\) faces by dimension; 211 matched pairs; 1428 Hasse incidences; two critical faces, integer masks `2048` and `232`; 8 graph automorphisms. Mod-prime reduced Betti ranks occur only in degree three. The integer homotopy conclusion rests on the matching's complete acyclicity and CW cell dimensions, not on those modular checks.

Limitations: finite exact verification on this labeled graph, not all graphs or higher independence parameters. The action is characterized on integral homology, not by a geometric equivariant homotopy equivalence. No external validation or independent audit is represented by this document.
