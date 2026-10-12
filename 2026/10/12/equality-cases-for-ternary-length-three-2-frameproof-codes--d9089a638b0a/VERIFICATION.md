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

Run `python3 artifacts/verify.py` with Python 3. The program uses only the standard library. It reconstructs the 27 ternary words, the descendant relation, and all forbidden triples; exhaustively searches size 10 and size 9; checks every maximum directly; independently enumerates Latin squares of order 3; and exhausts the 1296 natural Hamming isometries.

Expected decisive lines are `VERIFY_OK`, `size10 0`, `labeled_maxima 12`, `latin_graphs 12`, `orbits 1`, `orbit_size 12`, and `stabilizer 108`. The census digest is `d8c210cb586e908b7a7c5b4fb1a23d89c8895d6f5ddd6ad3b1b3d40428240c9c`.

The verifier establishes only the finite ternary length-three statement. It does not certify a general-q equality classification. The maximum nine is independently known from the separating-hash bound; the exhaustive size-10 failure is included as an internal finite cross-check of the same parameter.
