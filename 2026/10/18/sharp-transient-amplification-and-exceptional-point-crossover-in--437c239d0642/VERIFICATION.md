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

`verification.py` is a stand-alone Python 3 standard-library program. Run it with `python3 verification.py`. Its checks compare the exact \(2\times2\) semigroup norm against an independently evaluated real-matrix spectral norm, test global maximizers over a parameter grid, and check the exceptional-point and simultaneous damping/frequency crossover formulas. The actual checker extracted from the packaged record was executed successfully.

The infinite-time optimization and joint limits are proved symbolically in RESULT.md. The finite numerical tests alone cannot establish either statement for all real parameters. The linear model is not a nonlinear or stochastic amplification certificate. Unavailable full texts and incompletely inspected supplemental literature are recorded as originality risks in AUDIT.json. No independent audit has occurred.
