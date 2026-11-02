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

The elementary proof in `RESULT.md` establishes the theorem for every height, branching vector, and variable width, without using the computations as an induction step.

To replay the finite corroboration, run `python verify.py` (Python standard library, no external input). Its complete output is embedded as `verification_output.txt`.

The script checks 21 complete leaf structures, 210 independent comparisons of ordered distinct-tuple distance-type spectra at widths 2, 3, and 4, all annulus-reconstruction equations, and 120068 compatible partial isometries for four parameter pairs, including a positive and negative separation pair. The extension check compares all possible new-leaf distance profiles on both sides for each partial isometry of length strictly less than the pebble budget. The finite checks cannot establish the unrestricted logical theorem on their own. The proof and the historical-priority assessment remain subject to independent scrutiny.
