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

The scalar theorem follows from the determinant identity for Schatten-four norm, two consecutive sharp amplitude reductions, and the exact trigonometric root optimization displayed in RESULT.md. The completely bounded statement uses the published two-by-two lifting theorem of Arhancet, arXiv:2609.29643, Theorem 3.2. Neither the finite diagnostics nor any numeric search proves the theorem.

To reproduce the finite checks, run `python3 check_s4_phase.py` with Python 3 and NumPy. The code covers seven sharp phase witnesses, 8,400 deterministic pseudo-random complex-matrix inequalities and four row/column phase-gauge invariances (8,418 checks total). Equality at phase zero holds for every nonzero matrix; the nonzero-phase witnesses use the explicit formula in the proof. The code does not test all matrices or establish the cited amplified-norm result.

The scientific novelty conclusion is provisional pending independent historical review. No independent audit was performed.
