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

# Reproducibility and evidence boundaries

Run `python3 verify_subdivided_cube.py` with Python 3.10+ and NumPy available. The script independently builds the once-subdivided cube for each dimension from one through six, measures all shortest-path distances by breadth-first search, and verifies every closed-form distance, every integral Walsh invariant-block identity, the exact signed obstruction, and the predicted centered and uncentered numerical spectra.

The observed successful output begins `SUBDIVIDED_CUBE_EXACT_BLOCKS_AND_BFS_OK`, includes 80,857 point-pair checks and 447 Walsh basis dimensions, and reports 12 numerical spectral comparisons. The integer graph-distance, block, and witness checks are exact; the floating spectral checks use an explicit tolerance. The infinitely many dimensions are covered by the proof in RESULT.md, not by the finite computational checks.

The literature search and same mathematical model proof review support the included originality assessment but do not replace independent evaluation. No external audit, formal proof certificate, or exhaustive bibliography claim is represented by this document.
