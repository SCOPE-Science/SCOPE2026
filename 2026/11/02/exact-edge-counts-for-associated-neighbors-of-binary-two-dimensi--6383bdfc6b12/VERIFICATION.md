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

# Verification and scope

The proof in `RESULT.md` applies to every integer \(n\ge2\). No external mathematical certification has been performed.

Actual reproducibility procedures (Python 3 standard library only):

- `python verify_direct.py`: exhaustively forms distinct binary two-dimensional subspaces, checks the LCD Gram determinant, and implements the associated-neighbor definition for every pair. Run and checked at lengths \(2\) through \(7\); see `verification_direct.txt`.
- `python verify_lines.py`: separately enumerates odd common lines and corresponding odd-norm vectors in each orthogonal complement, then counts pairs with inner product one. Run and checked at lengths \(2\) through \(9\); see `verification_lines.txt`.

Both programs run with exact integer arithmetic and print a terminal `*_OK` line only if all formula assertions succeed. Numerical checking through length nine does not prove the unrestricted theorem; the proof is the three-step argument in `RESULT.md`. The historic research presentation identified by the 2025-04-03 repository date has not been inspected in full, so exact novelty remains subject to that and other priority risk.
