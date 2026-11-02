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

Run `python -m pip install -r requirements.txt` and `python verify.py` with the files embedded here. The verifier uses independent adaptive quadrature of the exact Fourier coefficients and a general-purpose matrix exponential. It reported `PASS 461 check groups` in the final scientific test. Tested data include distinct orders on both sides of the unit-order sign transition, multiple mesh widths, early/late times, exact \(lpha=2\) Fourier coefficients, the unique threshold on both sides and the near-order-one scaled threshold and negative dip.

The analytical proof in `RESULT.md` establishes all orders and all times. No finite computation establishes the infinite-time or all-order conclusion by itself. Numerical quadrature tolerances and floating-point roundoff limit the verifier, while no formal-machine or independent external mathematical audit has been performed.
