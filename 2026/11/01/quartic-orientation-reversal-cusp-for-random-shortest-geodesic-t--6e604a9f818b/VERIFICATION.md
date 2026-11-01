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

Run `python3 klein_triangle_checker.py` with Python 3 and numpy. The program checks exact conditional probabilities, rational coefficients and direct Monte Carlo simulation for aspect ratios 1, 1.5, 2.5 and 4. The successful run printed `ALL_CHECKS_PASSED`. The proof of the universal inequality relies on the threshold integration and Fourier orthogonality detailed in RESULT.md, rather than on numerical simulations. No independent mathematical audit has been performed.
