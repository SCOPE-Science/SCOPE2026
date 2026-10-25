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
# Reproducibility and proof boundaries

The proof derives the mixed covariance from the circular Gaussian logarithm identity, rather than inferring a derivative of an uncontrolled error term. The relevant parameter domain is \(L>1\) and fixed \(\alpha,\beta>0\) as \(\epsilon\downarrow0\). The threshold and exact sign classification apply only to \(L=2\), while the series gives the stated sufficient negative-covariance regime at other intensities.

Run `python check_hyperbolic_covariance.py` with Python 3.10+, SciPy and SymPy. The script evaluates an exact finite-radius integral independently of the boundary-series prediction, checks a symbolic quartic factorization and root interval, compares the closed expression with the series, and tests the known determinantal and intensity-two variance special cases. There were 43 passing assertions on the completed source artifact. Numerical convergence and finite spot tests are corroboration and are not themselves proofs of the infinite-parameter statements.

At the threshold the leading covariance term is zero; no finite-radius sign conclusion is claimed. No independent external validation was conducted.
