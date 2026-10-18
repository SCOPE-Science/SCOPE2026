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

# Computational verification
The included `verify.py` tests the exact scheme multiplier, analytically derived moment identities, the second-moment expression already appearing in the motivating paper, numerical quadrature for the fractional-moment boundary, and numerical approach to the predicted stiff asymptotic. Execute `python verify.py` with Python 3, NumPy, and SciPy. Numerical checks have finite precision and finite sample sizes. The proof, not the test program, supplies the all-parameter and infinite-iteration conclusions. No independent audit has been performed.
