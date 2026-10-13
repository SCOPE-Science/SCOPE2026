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

Run `python verify.py` after installing dependencies from `requirements.txt`. The program solves the implicit real-tilt renewal equation with a bracketed scalar root search for six admissible parameter families (including an exactly classical limit), and differentiates the resulting root numerically. It independently propagates a complete 91-site density matrix under the specified site-resolved Lindblad generator at two late times and measures the mean and variance slopes, without using the two-state renewal reduction in that calculation. The successful run reports `VERIFY_OK scgf_curvatures=6 finite_chain=2 max_drift_error=4.42e-08 max_diffusivity_error=1.01e-05`.

The finite-chain calculation has distant absorbing numerical boundaries and tests fixed finite times; it does **not** independently certify the infinite-chain limit, all real tilt parameters, or the mathematical uniqueness assertion. Those claims rely on the Bessel identities, positive-kernel renewal construction, Perron-root monotonicity, and analytic implicit differentiation given in `RESULT.md`. No independent audit is claimed.
