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

Run `python verify.py` with Python 3 and SciPy. The script uses deterministic seed 480231, direct quadrature of the Cauchy Poisson integral, exact Cauchy threshold and sign tests, positive half-stable mixing quadrature, and independent stable-mixture Monte Carlo at three parameter settings. It reported `PASS: 253 grouped checks; analytic Cauchy potential, threshold, monotonicity, and half-stable Monte Carlo.`

The numerical operations do not prove the theorem for all time, index values, drifts, gains, or sampling spacings. The analytical proof in `RESULT.md` supplies those quantifiers; in particular, the integrability and Borel–Cantelli step are not certified by simulations. The scientific priority assessment is provisional and independent validation has not been performed.
