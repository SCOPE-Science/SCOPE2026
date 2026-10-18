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

Run `python verification.py` after installing dependencies from `requirements.txt`. The program performs exact integer and rational symbolic operations with SymPy and prints a `VERIFY_OK` message upon success. Its calculations produce the eleven coefficientwise positivity identities required for the seven-state exact interval, the degree-18 numerator identity, the strict coefficient-sign tests after the two Descartes transformations, and exact rational positive/negative transition witnesses. The script also checks nine sample even orders as a consistency test.

The general even-order result is proved in `RESULT.md` by formal power-series identities and a shortest-path argument. Replaying finite instances cannot by itself establish a theorem for all orders or all Markov generators. There has been no independent external audit or validation.
