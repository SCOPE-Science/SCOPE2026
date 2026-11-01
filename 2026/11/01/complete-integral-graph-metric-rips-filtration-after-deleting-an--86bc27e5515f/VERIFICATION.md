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

# Reproducible scientific checks

Run `python3 verify_affine_deletion.py` with a standard Python 3 installation. The program uses no third-party packages, external data, or network access. The output must match `verification_output.txt` and terminate with `VERIFY_OK`.

For order three, the checker independently builds the incidence graph from prime-field coordinates with one direction deleted, checks every pairwise shortest-path distance, exhaustively enumerates the simplices at inclusive radii two and three and checks exact reduced mod-two boundary ranks. It also confirms that the proof's two radius-two subcomplexes cover the full complex and intersect in exactly the original graph. The radius-two face vector is `(18,81,108,18)`, with mod-two Betti vector `(1,0,26,0)`; radius three has face vector `(18,135,540,1215,1458,729)` and Betti vector `(1,0,0,0,0,64)`. The prime-order-five case verifies the all-pairs distance classification and the predicted partition into ten forbidden five-vertex blocks, without enumerating its huge simplicial complex.

**Proof versus calculation:** The finite checks do not certify the theorem for arbitrary affine planes. The all-order integral assertion rests on the distance classification, exact two-piece simplicial cover, homotopy pushout splitting and scale-three join decomposition proved in `RESULT.md`. There is no external or independent audit, and the code does not attempt to certify a journal-priority claim.
