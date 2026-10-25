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
# Reproducible finite checks and boundaries

Run `python3 verify_clique_glue.py 6` with standard Python 3 to enumerate every face of each of the 25 complexes with \(2\le a,b\le6\). The script constructs the two glued cliques at the level of individual edges, recognizes forbidden triangles from adjacency, computes complete mod-two augmented boundary matrices, and independently verifies each face-count coefficient using the explicit cone-and-join decomposition. The recorded output in `verification_output.txt` reports `CASES=25 TOTAL_FACES=4875 ALL_F_POLYNOMIALS_AND_BETTI_MATCH` followed by `VERIFY_OK`.

This finite experiment only verifies mod-two Betti vectors in finitely many cases. It does not establish an integral wedge structure or an infinite family of homotopy equivalences. The mathematical proof instead uses simplicial face classification, the join-connectivity theorem, nullhomotopic cofibration mapping-cone splittings, and a one-cell attachment to a connected CW space. Nontrivial unproved extension cases (more than two cliques or larger shared intersections) are not asserted.
