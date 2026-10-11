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

`verify.py` is a standalone exhaustive checker. It constructs the triangular prism, generates all eighteen primitive gradient pairs, examines every nonempty subset, and retains exactly the acyclic compatible collections. It then replays the fixed face-poset matching used in the proof.

The checker verifies all \(6606\) Hasse covers, reverses the \(831\) matched covers, and topologically sorts the resulting directed graph. A topological order containing all \(1727\) faces proves the matching acyclic. The unmatched faces consist of one vertex and \(64\) four-simplices.

As an independent check on the resulting homology, the program constructs the mod-\(2\) boundary matrices and obtains ranks \(17,109,319,386\), hence reduced Betti vector \((0,0,0,0,64)\). This homology calculation is corroborative; the homotopy equivalence itself comes from the complete acyclic matching.

The computation is finite and exhaustive. It proves only the stated graph case and does not claim a family theorem.
