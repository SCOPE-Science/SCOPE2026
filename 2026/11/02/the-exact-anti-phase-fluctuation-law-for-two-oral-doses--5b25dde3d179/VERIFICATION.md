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

# Reproduction and limits

Run `python checker.py` using Python 3 standard library. In the present package, it returned `VERIFY_OK assertions=247`. The checker independently obtains the periodic concentration by geometric summation of the causal absorption–elimination response and evaluates the integrated squared deviation with numerical quadrature. It compares each direct calculation to the analytically derived phase-penalty formula for positive unequal doses, coincident/unequal rates, reversed rate ordering, and different periods. It additionally verifies phase reflection, positive off-optimum penalties and time-rescaling in test instances.

The exact global continuous-parameter result is established in `RESULT.md` by symbolic convolution, periodization and strict hyperbolic monotonicity. The finite checks are diagnostics and do not certify all parameters. The package contains no clinical trial evidence or external independent audit.
