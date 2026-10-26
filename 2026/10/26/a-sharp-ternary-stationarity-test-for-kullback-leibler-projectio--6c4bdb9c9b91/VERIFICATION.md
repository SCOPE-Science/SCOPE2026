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
# Mathematical verification notes

The analytical proof is in `RESULT.md`, Steps 1–5. Run `python verify.py` with Python 3 and no third-party dependencies. The exact-rational checks return:

- 175 normalized positive KL reference/target stationarity identities.
- 49 exact realizations of prescribed \(x>1\), \(0<y<1\) by positive ternary perturbation parameters.
- A Pearson chi-squared example with directional derivative exactly `-33/5120` at the equal-mean reference and a consistent nonzero symmetric finite difference.

The first two families check formulas on finite rational grids; neither proves a statement about all positive real arguments. The theorem's universal quantifiers are established by explicit analytic inversion of the parameters and the derivative identity. The finite-difference check is only a consistency test and is not an error bound for other inputs. The test code is self-contained and uses no external data.

Self-review: passed. Independent audit: not yet performed.
