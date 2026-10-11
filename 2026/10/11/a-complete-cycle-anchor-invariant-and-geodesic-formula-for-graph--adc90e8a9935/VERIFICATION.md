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

The mathematical argument constructs the integral gradient by spanning-tree integration of a difference orientation cochain and uses an extremal-potential source/sink flex at each step. Its per-vertex counting lower bound proves the resulting path is geodesic. This proof applies for every finite connected simple graph with at least one edge, with no finite-size cutoff.

Run `python3 verify_flex.py` using Python 3 standard library only. The executable independently constructs the directed-cycle vertex set, solves the signed edge equations over integers, predicts reachability and the exact median/anchored distance, and compares against breadth-first distances among all edge orientations. Observed final output: `VERIFY_OK graphs=11 ordered_orientation_pairs=62804`. The examined graphs include complete, complete-bipartite, paths, cycles, multiple chords, and two directed-cycle blocks joined by a bridge. Enumerated finite tests are corroboration, not substitutes for the universal mathematical proof.

The cochain and shortest-path proof is not a claim that all earlier source/sink flip theory is new. Only the stated complete cyclic-component invariant and distance theorem is asserted. Independent audit has not been performed.
