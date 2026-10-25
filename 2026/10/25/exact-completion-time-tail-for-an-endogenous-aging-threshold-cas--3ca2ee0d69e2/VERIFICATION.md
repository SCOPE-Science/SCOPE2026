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
# Reproducibility
Run `python3 verify.py` in any Python 3 installation. It uses only standard-library exact fractions and checks the exact per-draw transition algorithm for arc lengths \(m=1,\ldots,7\) and horizons \(t=0,\ldots,8\). It verifies all state masses sum to one, survival probabilities decrease, and explicit survival formulas in the cases \(m=1,2,3\). The observed assertions passed. The gamma asymptotics and moment existence dichotomy are mathematical proofs in RESULT.md; no finite executable trial is offered as their proof. Independent audit has not been performed.
