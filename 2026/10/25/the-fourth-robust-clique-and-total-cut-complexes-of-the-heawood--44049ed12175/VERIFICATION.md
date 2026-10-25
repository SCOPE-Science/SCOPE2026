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

# Verification record

The embedded `robust4_verify.py` and `morse_certificate.json` form a standalone reproducible certificate. Run them together using `python robust4_verify.py morse_certificate.json` with Python 3 and no third-party dependencies.

The certificate specifies the Fano incidence lines, all 1469 matched nonempty-face pairs, the 93 unmatched faces and a deterministic vertex pivot order. The verifier reconstructs the graph and independently tests the robust face predicate both via all independent four-subsets and via a dynamic maximum-independent-set recurrence. It verifies the matching is disjoint, complete, codimension-one and acyclic by topologically sorting **all** oriented Hasse covering relations. It separately computes the mod-two boundary ranks and checks the Alexander-dual complex's facet purity and full two-skeleton.

Expected verified values: 14 vertices, 21 graph edges, 147 independent four-sets, 3032 faces including the empty face, 1469 matching pairs, critical vector with one vertex and 92 five-simplices, 13846 Hasse covers and 3031 visited vertices in the topological sort. Mod-two reduced Betti ranks are \((0,0,0,0,0,92)\). The combinatorial Alexander dual has 13352 faces including the empty face, 147 ten-vertex facets, and all subsets of cardinality at most three. The run must end in `VERIFY_OK`; any failed asserted equality terminates execution.

The exhaustive certificate plus Forman's discrete-Morse theorem proves an *integral homotopy type*, not merely the finite-field Betti vector. The dual conclusion additionally requires standard integral Alexander duality and Whitehead/Hurewicz arguments stated in `RESULT.md`; the verifier itself does not implement abstract homotopy equivalence. The result is specific to the Heawood graph and fourth robustness. No independent mathematical audit has occurred.
