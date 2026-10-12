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

The mathematical proof has two independent layers: a symbolic realizability theorem and a finite exhaustive count.

For necessity, minimum converse-well-founded rank of each occurring depth-one type supplies lower-rank witnesses. Transitivity forces every witness successor-set to be a subset of its parent's required valuation set. Induction on minimum rank therefore reproduces the support closure.

For sufficiency, the closure stage of a type is a finite rank. For each requested valuation, choose an earlier-stage witness with a nested successor-set. Edges always lower the stage; after transitive closure the frame is finite and irreflexive. Nested successor-sets guarantee that no unintended valuation can appear below a node, while the chosen witnesses guarantee that every intended valuation does appear.

`verify_depth2.py` then checks all \(256\) candidate spectra for the one-variable case. Its fixed-point test accepts exactly \(85\). A second exhaustive test searches linear orders of each candidate spectrum and verifies the equivalent earlier-witness condition; the two procedures have zero mismatches. For every accepted spectrum the checker constructs the witness frame, computes its transitive closure, and recomputes every node type and the root spectrum; there are zero construction failures.

The recorded output is:

`{"accepted_spectra":85,"construction_failures":0,"depth2_pointed_types":170,"equivalence_classes":"2^170","permutation_mismatches":0,"size_distribution":{"0":1,"1":2,"2":5,"3":12,"4":21,"5":22,"6":15,"7":6,"8":1},"total_candidate_spectra":256}`

The checker is exhaustive and terminates over finite search spaces. It is evidence for the numeric census, not a substitute for the symbolic proof of the realizability criterion.
