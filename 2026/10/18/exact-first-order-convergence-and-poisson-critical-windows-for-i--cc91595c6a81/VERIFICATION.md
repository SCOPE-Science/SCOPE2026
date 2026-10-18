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

The included `check.py` independently computes \(q\)-round two-sided Ehrenfeucht–Fraïssé games for bounded colored equivalence structures sharing their truncated \(q\)-profiles, and compares exact binomial class-event probabilities with Poisson approximations.

Command: `python check.py`

Observed result: `COLORED_EQUIVALENCE_VERIFY_OK EF=246 probability=36`.

The program checked 246 matched-profile pairs with small structures and ranks one through three, plus 36 numerical probability cases. These are finite sanity checks, not exhaustive verification of all structures, growth sequences or first-order formulas. The full mathematical theorem is justified by the profile/game argument, multinomial Poisson convergence, and explicit first-order witness sentences in `RESULT.md`. The cited probability inequalities and finite-rank game lemma are proved or reconstructed there. Scientific priority beyond accessible sources remains unverified by an independent reader.
