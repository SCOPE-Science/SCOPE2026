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

# Verification of the selected-fitness asymptotics

The proof is contained in `RESULT.md`. Run `python3 verify.py` with a standard Python 3 interpreter; no third-party libraries are required. The executable computes the original within-host differential equation and its implicit vulnerable-host infectious duration, verifies an analytic square-completion identity with exact rational arithmetic, checks finite values against the analytic exponential upper envelope, and illustrates convergence of the fitness-maximizing phenotype toward \(10\) at small positive \(c\). It also compares induced mortality against the analytic asymptotic constant \(10mJ(9/2,1/m)\). The successful final line is `VERIFY_OK`.

The numerical integration and bounded optimizer illustrate the claim but cannot establish uniqueness, uniform-in-mixture behavior, or a continuum limit on their own; those conclusions follow from the global envelope, \(C^2\) perturbation argument and tail-gap proof. Independent audit is not performed.
