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

# Reproducible mathematical checks

The analytic proof in RESULT.md characterizes the infinite spectrum. The accompanying pure computational artifact `verify.py` checks only necessary algebraic and finite-dimensional consequences. It runs in a standard Python environment with `requirements.txt` installed (for example, `python -m pip install -r requirements.txt` followed by `python verify.py`).

The exact rational power-series expansion of the boundary determinant has the first four coefficients \(12,-2,1/40,-1/15120\); normalization by \(12\) therefore gives \(1,-1/6,1/480,-1/181440\). The independently integrated \(TT^*\) kernel is \(K(x,y)=m/2-m^2/(6M)\), with \(m=\min(x,y)\) and \(M=\max(x,y)\); its first two positive power traces are \(1/6\) and \(17/720\). The script verifies these rational equalities.

The root-finding component uses high-precision special-function-free convergent series, then compares four inverse-square-root roots against a 350-node Gaussian Nyström matrix of the independent kernel. Observed singular approximations were \(0.3915493382518084,0.1005754215648547,0.0448912903665687,0.0252869731426519\). Numerical root-finding is not an isolation certificate; 350-node comparisons are not an exhaustive proof or a replacement for the stated singular-endpoint regularity argument. No independent audit has been performed.
