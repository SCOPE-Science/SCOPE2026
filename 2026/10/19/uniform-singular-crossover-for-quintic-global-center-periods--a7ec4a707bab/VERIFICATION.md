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

Run `python verify_crossover.py` using Python 3 with SymPy and SciPy. The extracted standalone script checks the polynomial first-integral derivative, the exact comparison of weighted moments at seven scales and six positions (42 checks), the two-sided finite-amplitude enclosure at 28 parameter pairs, beta-function endpoint agreement, and monotonicity on the sample grid. A successful execution prints `CHECK_OK`. The analytical proof, not the finite examples, justifies the universal inequalities and limiting profile. No independent audit has been performed.
