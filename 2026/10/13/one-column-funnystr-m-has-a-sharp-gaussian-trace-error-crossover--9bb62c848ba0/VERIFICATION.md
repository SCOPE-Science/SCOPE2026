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

# Verification notes

Reproduce the checker with `python verify.py` in the extracted file directory. Python 3 standard library suffices. The observed output is `CHECKS_OK algebra=100 quadrature=16 constants=2`.

The rational checks confirm the spectral trace/eigenvalue identity on selected matrices and pass counts. The quadrature tests evaluate a transformed exact Gaussian integral and compare its \(\theta=1\) specialization to the exact elementary formula. The two constant checks confirm \(C_{1/2}=2/\pi\) and \(C_1=1\). These checks are finite examples, not exhaustive proofs of all real exponents, all pass counts, or an originality guarantee. The analytic dominated-convergence argument, endpoint estimates, and beta-integral evaluation appear in `RESULT.md`. No independent audit has been performed.
