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

The mathematical argument proving the sharp maximum is in `RESULT.md`. `check.py` requires only Python 3's standard library. It evaluates the relevant one-dimensional quantile integrals by composite Simpson quadrature after the change \(u=1-e^{-y}\), then checks the analytic maximum formula, parameter-space feasibility, and local strictness. Run `python3 check.py` from the extracted directory; the last line should read `CHECK_OK`.

Two parameter cases were checked: \((\theta,\beta)=(2,1.5)\) and \((1,1)\). Separately, 55-decimal-digit quadrature found the first case's correlation coefficients \(a=0.3222022088524795167\ldots\), \(b=0.0958623973370279477\ldots\), whence \(\rho(1,1)=0.4180646061895074645\ldots\) and \(\rho_{\max}=0.4426431191991010677\ldots\). For the second case, the optimum was \(0.4483806527184230116\ldots\). The standard-library checker deliberately uses tolerances that account for endpoint smoothness and finite truncation.

Numerical checks are illustrative, not a proof of universal optimality and not a rigorous interval-arithmetic certificate. The exact universal proof relies on copula factorization, monotonicity of the Chen quantile, and a two-dimensional linear-program geometry argument. No independent audit, external certification or implementation of the originating study was evaluated.
