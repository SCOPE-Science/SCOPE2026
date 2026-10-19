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

# Reproducibility and scope

Execute `python verify.py` with Python 3 and SymPy. The standalone code reconstructs the generating-function algebra from the transfer-kernel identities rather than merely comparing the final rational function to itself. It verifies the exact covariance-subtraction identity, evaluates its removable unit-time limit, checks the Green–Kubo rational expression, its derivative, and the two endpoint values.

The script also implements an independent rational integration method. For \(p\in\{3/5,2/3,3/4,9/10\}\) and integer \(0\leq n\leq5\), it compares each raw two-time moment by exhaustive finite map-choice recursion and exact dyadic-cell integration against the shell transfer recurrence; all 24 cases passed. These are finite independent consistency checks, not substitutes for the proof of covariance summability and limiting variance given in `RESULT.md`.

The theorem applies only to the annealed stationary coordinate for \(1/2<p\leq1\). The critical comparison uses the invariant atom at zero; the critical map has no normalizable absolutely continuous density of the assumed form. Neither a central limit theorem nor independent expert validation is asserted.
