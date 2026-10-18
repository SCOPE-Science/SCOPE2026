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

`python3 verify.py` requires Python 3.10 or later and no packages beyond the standard library. It reconstructs the graph as ordered pairs, enumerates all nonempty subsets, builds and validates the complete discrete-Morse matching, computes signed integral Morse differentials and integral cycle representatives, computes both rational symmetry characters from integral matrices, and tests their representation laws. All 863 simplices, 3432 face-poset covering relations, and 24 graph symmetries are checked. Ordinary mod-two simplicial boundary ranks provide a separate consistency check. Expected deterministic output is supplied as `verify_output.json`.

The computed zero Morse differential is an exact integer result for the fully enumerated finite complex. The homotopy-type deduction additionally uses the standard discrete-Morse CW theorem and the Hurewicz isomorphism for a 2-connected 3-skeleton. The program does not establish a claim for graphs other than the specified twelve-vertex graph, and a self-review does not constitute independent validation.
