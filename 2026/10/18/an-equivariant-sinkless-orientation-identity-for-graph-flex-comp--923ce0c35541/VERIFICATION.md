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

# Reproducible finite checks

Run `python3 verify.py` using the extracted standard-library Python program. Its recorded output is `verification_output.txt`. The program enumerates full orientation spaces and graph automorphisms, constructs each canonical sink-set-indexed cube, computes signed fixed-cell characters, independently counts fixed sinkless orientations, checks the edge-orbit reversing obstruction and independent vertex-orbit inclusion-exclusion formula, and compares actual sinkless-orientation orbits with the Burnside average. Eleven distinct finite graph families were checked and the completed run ended with `VERIFY_OK graph_families=11`.

The integral sign of a fixed cubical cell comes from the permutation of coordinates based at its canonical all-sink corner. The all-orders result follows from the determinant proof in RESULT.md, not extrapolation from the finite test range. No external or independent scientific audit is represented by these checks.
