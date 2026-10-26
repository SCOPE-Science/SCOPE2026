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

Run `python checks/verify.py` from the extracted package directory with Python 3; the checker uses only the standard library. The script expands the confluent-residue expression exactly over rational coefficients and checks the classification on every five-node multiset from the stated bounded window that contains zero. It separately checks the exceptional identity and a nonzero control polynomial.

Recorded output is preserved in `checks/verification.txt`. The finite window is a diagnostic only. The infinite statement is proved by the multiplicity argument in RESULT.md, including the nonzero lowest coefficient in every nonexceptional repeated pattern and the explicit residue cancellation in the exceptional pattern. No independent mathematical audit has been performed.
