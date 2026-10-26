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

# Verification scope

The result is mathematically proved in `RESULT.md`. The standalone `verify.py` uses the Python standard library and checks numerical trajectories against the separate triangular reduction, the exact three-species expression, parameter scaling, and the zero-predation boundary. Execute `python verify.py` from a directory containing that file. The output reports the number of tested comparisons and prints the common five-species predicted composition.

The checker uses fixed-step fourth-order Runge–Kutta integration; numerical agreement is corroborative and neither exhaustive nor a proof of convergence for arbitrary parameters, arbitrary finite species counts or infinite time. The universal assertion instead follows from positive-simplex invariance, a logistic lower comparison, divergence of the top-population clock, an inductive integrability argument for even coordinates, and asymptotically logistic total biomass. Independent audit and independent validation were not performed.
