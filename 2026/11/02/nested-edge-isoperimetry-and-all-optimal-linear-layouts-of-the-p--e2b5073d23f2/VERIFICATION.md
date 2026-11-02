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

# Reproducible verification

Run `python verify_lcf.py` and `python verify_incidence.py` with Python 3.8 or later. Both rely solely on the Python standard library and should exit successfully with `PASS` output. Each exhaustively examines all \(262{,}144\) vertex subsets, independently constructing the 18-vertex graph from the signed-offset Hamiltonian presentation and the nine-three-incidence presentation. The first uses an integer boundary recurrence and counts optimal-prefix chains backward; the second counts crossing edges directly and propagates valid chains forward. The explicit isomorphism in the latter rules out accidental use of a different graph with the same name.

The verified cut-minimum sequence is \((0,3,4,5,6,7,6,7,8,7,8,7,6,7,6,5,4,3,0)\). All prefix cuts of the specified cyclic order attain those minima, giving exact cutwidth \(8\) and arrangement cost \(99\). The complete constrained-minimizer counts and exact optimum-layout count \(31{,}850{,}496\) follow from exhaustive integer algorithms; these finite checks are a proof for this specifically defined graph, not a general-parameter theorem. A small `certificate.json` repeats the checkable input and output values without replacing the executable verifier.

This package does not claim an independent audit, an independent authorship assessment, or generalization to other graphs. The existing literature establishes the cut-sum and nested-chain implication; originality here is limited to the Pappus-specific finite classification.
