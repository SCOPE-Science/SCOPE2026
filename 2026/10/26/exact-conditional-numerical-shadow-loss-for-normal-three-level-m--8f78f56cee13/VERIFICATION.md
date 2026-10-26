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

The exact proof reduces the Haar law to a uniformly distributed probability simplex with independent coordinate phases. It checks all normal spectral multiplicity and affine-collinearity cases, including the singular boundary at coincident eigenvalues. The critical slice integral is \(\int_0^1L_r(t)^3\,dt=1/4\) for every \(0<r<1\), proving the universal diagonal defect coefficient \(1/24\); the off-diagonal coefficient \(1/12\) follows from the exact complex Haar fourth moment.

Run `python verify.py` with NumPy installed to reproduce six deterministic-seed finite empirical comparisons. The script uses 400,000 independent Haar vectors; reported tolerances cover Monte Carlo fluctuations and are not proof of any untested parameter range. The infinite statements rest on the exact argument in RESULT.md. No independent audit has been performed.
