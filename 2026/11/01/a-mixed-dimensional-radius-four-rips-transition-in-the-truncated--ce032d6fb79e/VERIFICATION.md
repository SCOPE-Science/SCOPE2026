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

# Exact finite verification and limits

Run `python3 verify_truncated_dodecahedron.py`. The program uses Python standard library only, builds the dodecahedral graph from the explicit generalized-Petersen adjacency, and creates its truncated graph from directed incidences. It computes all shortest-path distances and exhaustively generates all simplices through radius four. It checks the exact mod-two boundary ranks in every degree and verifies the radius-four Euler characteristic 14 independently of the boundary-rank calculation.

For the relative simplicial collapses it constructs every proposed pair and verifies, on the complete currently remaining face set, that the lower face has exactly one immediate coface, the paired upper face, which is maximal. It checks 320+540=860 pairs from radius three to two and 90+90=180 pairs from radius two to one, with exact equality of the final face sets. The graph-theoretic homotopy identification of the first Rips stage then uses the twenty disjoint filled triangles in the connected cubic graph.

The recorded command output is stored as `verification_output.txt` and ends `VERIFY_TRUNCATED_DODECAHEDRON_RIPS_MOD2_PASS`. The executable code, not the output log alone, is the verification method. This verification concerns only the finite graph and stages 1–4; radius-four integral homology, the precise homotopy type, and any later barcode deaths were not verified and are not claimed.
