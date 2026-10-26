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

# Verification of the paired busy-period detection theorem

Run `python verification.py` using Python 3 with SciPy. The included `verification_output.txt` records the actual observed output of this standalone script.

The script completed 125 assertions: a recursive count of Catalan birth--death paths; independent integer convolution checks of generalized ballot numbers; normalization and mean tests for moderate-load count laws; direct finite-divergence and Fisher-information comparisons; and a comparison of the exact gamma-CDF optimal testing sum with separate numerical integration of the minimum of the two joint densities. The displayed numerical example is \((\lambda,\lambda_1,\mu,k)=(1,1.25,3,2)\).

This is finite corroboration rather than proof of infinitely supported distribution identities, strictness for all admissible rates, full-path sufficiency, or asymptotic likelihood convergence. Those assertions depend on the mathematical proof in `RESULT.md`. No independent mathematical validation has been performed.
