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

The full standalone verifier is `verify.py`. Run it with `python3 verify.py` from the extracted package directory; it uses only Python's standard library. Its actual replay output is `verify_output.txt`.

The verifier constructs both graphs from the explicit coordinate rules, verifies degree six and exactly two common neighbors for each distinct vertex pair, enumerates all 32 triangles per graph, and tests each of the 65,536 vertex subsets with two logically different predicates. It then constructs every Morse pair from the stated deterministic vertex order and performs a topological sort of the entire oriented face-poset Hasse diagram, including the empty face.

The certified counts are: rook graph, 7,343 faces (including empty), 3,664 pairs, fifteen critical five-cells, 37,744 incidence checks; Shrikhande graph, 8,951 faces, 4,471 pairs, nine critical six-cells, 48,288 incidence checks. Each augmented matching pairs the empty face with one singleton; removing that pair gives one critical vertex in ordinary simplicial Morse theory. Independent mod-two reductions of the *full* augmented chain groups yield Betti ranks fifteen in degree five and nine in degree six, respectively.

The homotopy equivalences follow from discrete Morse acyclicity and the absence of other critical dimensions, not from mod-two ranks alone. The verifier does not search the mathematical literature or establish priority. The only unverified scientific issue is possible unindexed prior equivalent coverage; independent audit has not been performed.
