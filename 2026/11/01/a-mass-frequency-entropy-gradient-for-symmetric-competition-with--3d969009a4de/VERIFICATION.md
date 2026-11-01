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

# Verification and limits

The submitted analytic proof begins with the exact general-dimensional change of variables \(S=\sum_i x_i\), \(p_i=x_i/S\). Its key algebraic step is the identity
\[
\dot\Phi=(\dot S/S)^2+2\sum_i\dot p_i^{\,2}/p_i.
\]
The proof also verifies proper superlevels using strictly positive entries of \(A\) and \(\mu>0\), then invokes the standard finite-dimensional analytic-gradient convergence theorem. The conclusion is a theorem about every positive-time trajectory, not an extrapolation from finite simulations.

The `CHECKER.py` file contains exact rational, standalone field/gradient/dissipation checks on two distinct symmetric positive competition matrices, two positive mutation rates, four frequency vectors and two mass values (32 cases), plus an exact discriminant check for the positive multistable case. It requires only the Python standard library. The checker passed after extraction from the submitted embedded file. These finite checks validate symbolic identities at test points; they are not a formal proof of the universal quantified result.

Limitations: the interacting growth matrix must be symmetric with strictly positive entries; mutation is positive and uniform all-to-all. The theorem establishes individual limit points but not a uniform rate, basin boundary, carrying manifold, or priority against uninspected literature. Self-review does not constitute independent scientific audit.
