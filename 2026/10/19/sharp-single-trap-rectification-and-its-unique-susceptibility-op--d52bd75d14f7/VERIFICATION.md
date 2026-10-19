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

The attached `verify.py` enumerates the finite-state process from its physical transition rules, rescales time by two, checks the equilibrium detailed-balance product law, and solves the two stationary perturbation equations **exactly** in symbolic rational arithmetic. It confirms both coefficients, all polynomial coefficient signs, the 16-sign transformed derivative, a unique positive root by Descartes' rule plus endpoint signs, and the numerical optimum. Six additional independent exact finite-driving solutions corroborate the Taylor expansions at three trap rates and two small biases. Execute `python verify.py` in a Python 3 environment with SymPy. No external data files are required.

The mathematical sign and uniqueness results are consequences of exact algebra and Descartes' theorem, not numerical simulations. Limitations: the assertion is about the near-equilibrium quadratic response, not the full finite-driving response; the 16-state theorem does not establish a large-system limit. No independent external validation has been performed.
