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

Run `python verify.py certificate.json` in the directory containing the embedded artifacts. The verifier uses only the Python standard library and rebuilds the graph and complex from the explicit Cayley generators rather than trusting stored face lists.

It checks all graph degrees and all adjacent/nonadjacent common-neighbor counts, enumerates all neighborhood faces, checks the face vector, reconstructs the toggle matching, checks all matched pairs, orients all Hasse covers, and verifies acyclicity by a complete topological sort. It then recomputes simplicial boundary ranks independently over three prime fields, checks Euler characteristic, and performs a complete backtracking chromatic-number check.

The certificate is finite and exhaustive for this graph. It does not certify any infinite family, equivariant refinement, or literature originality claim. The literature comparison is documented separately in the review materials.
