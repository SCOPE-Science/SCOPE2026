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

# Verification record

The standalone `rook_min_fort_verifier.py` implements the defining rook-graph open-neighborhood test independently of the theorem, exhaustively enumerating 1,156,934 nonempty candidate vertex subsets across ten labeled rectangular boards from 2-by-2 through 4-by-5. It computes the inclusion-minimal forts directly, compares classified sets with the four proposed families, and, for all boards of at most sixteen cells, verifies membership equivalence for every nonempty vertex subset in both directions. An independent recursive counting implementation checks the coefficientwise minimal-fort polynomial; the stored program output is `rook_min_fort_verification.txt` and ends `ALL_ASSERTIONS_PASSED`.

Command: `python3 rook_min_fort_verifier.py`. The finite computation checks only specified boards. The unlimited-domain result requires the written four-case degree argument and species-counting argument in RESULT.md. There is no independent audit or formal machine-checked proof.
