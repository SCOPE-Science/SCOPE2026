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

# Verification details

Run `python3 check_unit_shiha_order.py` with the Python 3 standard library. A reproducibility run passed **1,850 checks**. It used rational arithmetic to check the moment-gap identity for eight powers and three parameter pairs, independent numerical quadrature with a sixth-power endpoint change of variables to check the explicit stop-loss primitive, several sharp-phase deductible tests, and exact rational checks of the critical mean and variance.

The exact proof requires no numerical root enclosure: uniqueness of the CDF crossing follows from strict concavity, and the sharp stop-loss classification follows from its sign pattern and the power-moment formula. The reported decimal pivot and example deductible are illustrations and not assumptions. The checker samples finitely many points and parameters, so it is not a completeness or independent scientific certificate.

The source equations inspected are the unit Shiha CDF (2.6), density (2.5), and moments (3.3), together with the original Shiha mixture and quantile discussion. The full claim has not undergone independent scientific audit.
