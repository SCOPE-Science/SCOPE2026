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

# Reproducibility and verification

The theorem has a symbolic finite portion and an analytic infinite tail. `CHECKER.py` runs with Python 3 and the standard `fractions` module, checks all exact-degree ranks from zero through twenty-eight by two independent rational methods, verifies exceptional null identities, and checks the rational inequalities invoked in the Bernstein argument. `CHECKER_OUTPUT.txt` is the output of the actual script replay. Beyond degree twenty-eight no sampling or extrapolation is used: the published Legendre–Bernstein inequality yields strict diagonal dominance for every later Gram matrix. No external or independent audit has been performed. The reader can inspect the recurrence and Gram matrix assembly directly to check the finite proof obligations.
