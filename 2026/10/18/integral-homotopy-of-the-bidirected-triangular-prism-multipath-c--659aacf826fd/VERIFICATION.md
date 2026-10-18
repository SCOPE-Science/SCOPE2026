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

# Reproducible checks

Run `python3 verify_prism.py` with a standard Python 3 interpreter. The script uses only the Python standard library and reconstructs its data from an explicit nine-edge graph, never relying on external precomputed certificates.

Its checks cover: all \(2^{18}\) arc subsets; independently enumerated valid arc sets; all 2256 codimension-one face incidences; topological-sort acyclicity of a 326-pair Morse matching; integral projected chain differentials; independent mod-2 and mod-101 boundary ranks; five independent degree-two integral cocycles; six exact rational four-cycles; and 90 Alexander–Whitney cup product evaluations.

Expected final marker: `VERIFIED_PRISM_MULTIPATH_WEDGE`.

Expected face counts including the empty face: `(1, 18, 108, 260, 240, 60)`.
Expected unmatched critical-cell counts by dimension: `(1, 0, 5, 22, 6)`.
Expected field boundary ranks in dimensions one to four: `(17, 91, 164, 54)`.

The integral homotopy conclusion additionally invokes standard discrete Morse equivalence, classification of attaching maps to a wedge of two- and three-spheres in dimension three, and the cup-product/attaching-map formula. A finite enumeration by itself is not a general theorem about other graphs. Independent audit has not been performed.
