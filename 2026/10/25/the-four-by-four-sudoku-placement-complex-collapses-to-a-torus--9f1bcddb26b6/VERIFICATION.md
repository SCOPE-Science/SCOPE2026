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

# Finite verification

Run `python3 verify.py` from a directory containing the accompanying files. The verifier uses only Python 3's standard library. It checks the adjacency of the sixteen-cell Sudoku graph, all \(2^{16}\) candidate masks, exact counts of faces by dimension, the exhaustive deterministic 32-pair free-face collapse, and the face vector of the remaining surface. It then checks every edge's triangle incidence, each vertex's circular link, connectedness, consistent global triangle orientations, and Euler characteristic zero. The last output line must be `VERIFY_OK`.

A collapse pair is only accepted if the lower face has precisely one strict remaining coface, so the program cannot substitute a chain cancellation for a simplicial collapse. The surface classification step is the standard mathematical theorem that a connected closed orientable triangulated surface of Euler characteristic zero is homeomorphic to the torus. No extension to higher-order Sudoku boards or numerical inference about them is made.

This is a finite reproducible proof and an internal scientific review. No independent audit was performed.
