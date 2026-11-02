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

# Verification

The stand-alone checker `verification/check.py` uses Python, NumPy and SciPy. Run it with `python verification/check.py` from the containing directory. The accompanying `verification/check_output.txt` records the output from the test execution.

The checks cover operational-time cumulants, the exact geometric characteristic-function product and its limiting Fourier correction, positive and negative sign intervals of \(\partial_v^2p_{\alpha,v}|_{v=1}\) in the Cauchy and Gaussian cases, and independent Fourier integrals for multiple stable indices. The analytical \(L^1\) proof in `RESULT.md` is required for the universal statement; 171 numerical assertions alone cannot certify it. Historical priority is not independently established.
