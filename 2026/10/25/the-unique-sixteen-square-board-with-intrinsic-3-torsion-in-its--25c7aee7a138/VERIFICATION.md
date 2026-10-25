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

# Verification protocol and limits

Execute `python3 verify_chessboard_16.py` in a clean directory using the included script. The program requires only the Python standard library and derives every rook simplex, symmetry representative, signed integer boundary, unit-pivot reduction and mod-three rank from definitions. It exhausts all induced subboards of the five-by-five chessboard with up to sixteen squares, modulo independent permutations of rows and columns.

The `verification_output.txt` file is the actual captured output from a successful execution. It includes the complete canonical-class counts, exceptional residual column, mod-three ranks and ambient cycle checks. The accepted mathematical claim is limited to this finite range; the program does not prove general statements about other board sizes. The full-board integral group is taken from cited peer-reviewed mathematics; the relevant mod-three computations and inclusion witness are verified directly.

No independent audit has been performed.
