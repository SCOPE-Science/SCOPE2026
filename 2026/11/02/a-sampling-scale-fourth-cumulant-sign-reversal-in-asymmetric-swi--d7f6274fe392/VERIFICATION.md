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

Run `python verify.py` with a Python 3 interpreter and SymPy installed. The script verifies the complete four-point transition-matrix identity exactly in symbolic variables, two integrated exponential product identities exactly, and a finite grid of parameter/sign boundary predictions. The symbolic identities directly check the nonstandard kernel calculation; analytic monotonicity and the multilinearity/independence argument establish the quantified theorem beyond finite tests. The proof covers all positive switch rates, all positive cadences, all stationary probabilities strictly between zero and one, and arbitrary independent localization errors with finite fourth moments. The experiment does not test arbitrary error distributions by simulation because their cancellation follows from cumulant independence, nor does it provide finite-sample confidence statements.
