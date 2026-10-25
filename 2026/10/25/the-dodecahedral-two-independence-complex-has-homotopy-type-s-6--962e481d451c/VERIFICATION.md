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

The standalone source `verify_dodecahedron.cpp` encodes all vertices and edges of \(\operatorname{GP}(10,2)\) and enumerates all 1,048,576 possible vertex subsets. It checks that the recursive forbidden-triple test agrees with a direct connected-component test in every case. It verifies 60 forbidden triples, the complete face vector, the full facet-dimension distribution, 31,570 ordinary Morse pairs, and the two critical nonempty cells (one zero-cell and one six-cell).

The checker constructs all 410,520 directed cover incidences of the augmented face poset, reverses exactly the matched ones and performs a complete topological sort on 63,143 faces. Every face is visited, proving there is no closed gradient path. The ordinary nonempty face poset is an induced subgraph of this acyclic directed graph. The resulting CW complex has a point and one six-cell; thus it is homotopy equivalent to \(S^6\).

Reproduce with `c++ -std=c++17 -O2 verify_dodecahedron.cpp -o verifier` followed by `./verifier`. The exact final line is `VERIFY_OK`. Both GCC and Clang accepted and executed the verifier; an additional undefined-behavior-sanitized Clang execution also ended with `VERIFY_OK`.

The program is self-contained C++17; it uses only standard library headers. The certificate proves this precisely specified finite case and does not establish a uniform result over all cubic graphs. It does not address bibliographic priority or constitute independent scientific validation.
