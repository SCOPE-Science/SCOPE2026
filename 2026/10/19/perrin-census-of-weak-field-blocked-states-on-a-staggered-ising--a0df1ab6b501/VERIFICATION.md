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

# Reproducibility and limits

Run `python verify_staggered.py` with Python 3 and SymPy. The script checks the direct one-spin flip inequalities on every physical spin vector for even sizes 4 through 18; it independently computes the cyclic spin-pair transfer matrix and verifies expected regime-wise traces. It additionally compares every configuration at sizes at most 14 with the prohibited cyclic words `11` and `000`, verifies the field-opposing-spin census for all even sizes through 18, and checks the cubic characteristic polynomial and larger Perrin recurrence samples.

The all-size proof is the four-step argument in `RESULT.md`; numerical enumeration for finitely many sizes is not a proof of an infinite statement. No independent expert audit or external formal certificate has been performed. Only a self-review is recorded. The treatment of zero-energy moves matters at field endpoints; no assertion is made about stochastic absorption probabilities or finite-temperature kinetics.
