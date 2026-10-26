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

The standard-library program `verify.py` exhaustively enumerates the 16,383 canonical cycle vectors, computes exact rank-three Hintikka signatures, and confirms 143 signatures. Its separate direct-triple enumerator independently confirms the local signature method on all 731 canonical vectors with at most 19 points and 509 additional sampled vectors; sample seed is fixed in code. The count for at most 18 points is 142, so the 19-point bound is sharp after the symbolic canonical reduction in `RESULT.md`.

Run `python verify.py` and compare its output with `verification_output.txt` and the regenerated `minimal_representatives.csv`. Every number is computed from finite integer and tuple/set operations; no external packages, random services, or proof assistants are needed. The proof that arbitrary cycle lengths and multiplicities reduce to these cases is mathematical, not computational. Additional spot checks for long cycles and extra copies are tests only. Independent audit and validation have not been performed.
