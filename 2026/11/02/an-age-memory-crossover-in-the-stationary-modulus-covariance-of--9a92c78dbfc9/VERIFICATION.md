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

# Reproduction and scope

Install Python 3.10+ and SciPy, then run `python verify.py`. The supplied `verification_output.txt` is from this run of the standalone source file. The program checks the exact covariance by two independently implemented integrals, strictly positive decomposition terms, large-lag normalization for subcritical, critical and supercritical exponents, the exact Brownian coefficient, and the Brownian one-quarter age share.

All 73 assertions completed successfully with numerical quadrature. The numerical tests are finite and do not prove the limiting theorem; the detailed analytic dominated-convergence proof is in `RESULT.md`. No independent mathematical review or formal external audit has been performed.
