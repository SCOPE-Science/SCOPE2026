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
# Reproduction and scope
With Python, install the dependencies listed in `requirements.txt` and execute `python check.py`. The diagnostic printed on success is `CHECK_OK`. Symbolic checks verify \(\dot r=y^2(1-r^2)\) independently from the asserted ratio formula. Arbitrary-precision checks compare both branches of the exact time expression with the scalar-time integral for negative, zero and positive parameters, test the finite endpoint amplitude and the simple-pole leading constant, and compare representative small-distance cases with all three asymptotic regimes and the near-critical crossover.

The mathematical justification for every parameter and every trajectory in the stated domain is in `RESULT.md`: an exact scalar solution, monotonicity of the physical-time integral, uniqueness of the denominator zero, an explicit Taylor expansion, and compact-uniform bounds on a positive kernel. None of the finite tests proves a universal statement, and no external or independent audit has been performed.
