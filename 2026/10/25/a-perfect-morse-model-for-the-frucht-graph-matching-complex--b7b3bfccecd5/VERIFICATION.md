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

The finite proof is reproduced by the standard-library Python file `verify_frucht.py`. Its inputs specify the graph by twelve vertices and the published Frucht LCF chord sequence. All nonempty subsets of the eighteen graph edges are exhaustively tested for pairwise disjointness. The pairing is reconstructed by a fixed pivot order, and a complete directed incidence graph is topologically sorted. The check verifies the exact critical-cell counts, not a sample of faces. Additional mod-two boundary ranks are recomputed independently of the pairing.

A fully acyclic matching with one critical zero-cell and twenty critical three-cells proves the homotopy statement via finite discrete Morse theory. The mod-two calculation alone would not establish it. The included output text is an observed execution of the included verifier; it is not an external certificate. The claim has not received independent audit or validation, and literature searches cannot certify absence of all unindexed equivalent results.
