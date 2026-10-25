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

# Reproducibility and verification

Run `python3 verify_queens5.py` with a standard Python 3 interpreter. The script has no third-party package dependencies and uses exact integer operations and rational fractions. It checks legal faces, matching coverage, acyclicity of the entire directed face-incidence graph, the critical-cell vector, the signed integral cancellation differential, and an independent exact-rational simplicial boundary rank.

Expected final line: `VERIFY_OK_QUEENS5_INTEGRAL_HOMOTOPY`.

The verification report `verification_output.txt` records the actual execution from this package's source. The proof's input enumeration and its computational steps are finite and exhaustively checked; no unsupported extrapolation to other board orders is made. The associated scientific literature comparison is same-model only; no independent validation has been performed.
