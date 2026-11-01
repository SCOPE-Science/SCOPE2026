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

# Exact finite verification

Run `python3 verify.py` in a directory containing `collapse_pairs.txt`. The checker uses only the Python standard library. It reconstructs the 24-edge graph, enumerates every 16-bit mask, and compares component-based admissibility with forbidden-connected-subset tests for both cutoffs; the cutoff-two local-degree test is also compared. The checker then regenerates the stored collapse sequence independently and replays the saved sequence against the complete *current* complex, checking each free codimension-one face, the unique coface, maximality, pair disjointness, and that all remaining faces are exactly the target complex.

Recorded checks: 16 vertices, 24 edges, 48 forbidden connected triples, 112 connected quadruples; 6,813 and 15,197 augmented faces; 8,384 relative faces; 4,192 elementary collapses; ordinary Euler characteristic 4 on both complexes; exact final subcomplex equality. The SHA-256 of `collapse_pairs.txt` is `f4a86667e6dd6e17b3278642a4258743bef355aa336cbf51b60cbc3abc976ff7`. The executable prints `MOBIUS_KANTOR_RELATIVE_COLLAPSE_VERIFIED` on success; `verification_output.txt` contains its actual recorded standard output.

This is a complete finite proof for the labeled graph and chosen cutoffs. The checker does not prove a statement about other graphs or filtrations, and it does not independently validate originality or conduct an external audit.
