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

# Finite verification and proof dependencies

The executable `certificates/check_crown.py` reconstructs the crown graph from its cross-edge rule without using a precomputed simplicial table, checks every nonempty vertex subset for \(n=2,3,4,5,6\) against the proved two-row/tetrahedral covering description, and computes mod-two boundary ranks directly. It checks signed Lefschetz fixed-face traces for all \(S_n\times C_2\) elements when \(n=3,4,5,6\); these are 12, 48, 240, and 1440 exact checks. The recorded stdout is in `certificates/verification_output.txt`. To rerun with Python 3, invoke `python3 certificates/check_crown.py` from the containing directory.

The proof's non-finite dependencies are the dominated-vertex strong collapse, simplicial homotopy pushout along cofibrations, and the long exact homology sequence of \((X_n,L_n)\). The integer exterior-square identification comes from a split-exact free abelian sequence, not any mod-two calculation. No computation alone is used to infer an all-parameter theorem, and no external independent scientific check is claimed.
