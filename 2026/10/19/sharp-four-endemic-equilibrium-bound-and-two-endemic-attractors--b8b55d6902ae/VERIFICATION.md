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

The standalone `verify.py` uses only the Python standard library. Running `python verify.py` tests exact rational polynomial signs at five prevalence values, six independent exact denominator-clearing identities, and four certified rational bisection brackets. These are finite checks of the proposed explicit witness, not a substitute for the analytical degree bound or Jacobian stability proof. The proof uses the intermediate-value theorem, elementary degree-four root counting, and exact trace/determinant calculations. The claims do not cover global basins, stochastic epidemics, or empirical parameter accuracy.
