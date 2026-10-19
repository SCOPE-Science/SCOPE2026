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

Run `python reproduce.py` with Python 3, NumPy and SciPy. The script independently samples 300,000 row-weighted Gaussian one-step updates at each of six dimension/moment settings, evaluates three noncentral chi-square reciprocal moments in two different ways, and checks central second-moment identities across a finite dimension grid. The program has been executed successfully. Sampling is not an exhaustive check and cannot prove divergent integrals. The theorem's exact all-dimensional moment boundary follows from polar integration in `RESULT.md`, and the closed central moment formula follows from independent gamma/beta distribution identities.

No independent audit has been performed. There is no claim of multi-step/stationary convergence or finite precision performance.
