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
The exact source ODE was checked against equation (6) of the cited 2024 open full text.

For every \(q,\eta,r>0\) and state in the feasible simplex,
\[
\frac{d}{dt}(x+y+z)=-\eta z,
\qquad
\frac{d}{dt}(x+y)=-\eta r xz.
\]
These exact identities imply extinction of the integrable infection and convergence to an equilibrium. For balanced seeded states, the comparison
\[
x(t)\le u,
\qquad z(t)\le\delta e^{-\eta(1-ru)t}
\]
proves the global depletion bound and supplies a dominating function for the derivative at vanishing seed.

The accompanying `verify.py` implements direct integration of the original reduced ODE by classical fourth-order Runge–Kutta, with a small fixed step. It checks positivity and mass dissipation, a chosen pair of infectious seed sizes against the analytical linear coefficient, and a numerical intermediate-value bracket around an interior prescribed final susceptible fraction. Numerical tests do **not** verify the infinite-time proof, all parameter values, or formal novelty. Those claims rest on the exact argument and literature comparisons supplied in the result and scientific review.
