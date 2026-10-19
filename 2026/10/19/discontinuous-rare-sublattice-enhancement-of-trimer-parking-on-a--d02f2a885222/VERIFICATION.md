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

# Reproducibility and scope

Run `python verify.py` in a Python 3 environment with NumPy and SciPy. The script uses independently counted geometric unions of trimer starts for sixteen interval sizes at both parity classes and tests the three-variable ODE for several flux ratios. Monte Carlo uses a fixed random seed and independent first-arrival clocks on a 1000-site periodic line.

The exact endpoint is \(J(0)=0.3515014624274595\) and the positive-rate endpoint limit is \(0.14849853757254047\). The rate-one ODE yields \(J(1)=0.17634703682266166\). The finite simulations agree within their estimated sampling uncertainties. The script's acceptance check allows six standard errors plus a numerical margin.

Numerical simulations are finite-volume evidence only. The proof of the infinite-line statement and interchange-of-limits failure is in `RESULT.md`; no independent audit has been performed.
