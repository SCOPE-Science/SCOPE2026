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

The theorem is proved by the radial-generator transformation, the squared-Bessel backward Laplace equation, Poisson last-reset conditioning and orthogonal-polynomial degree-lowering. These operations establish the infinitely many allowed parameter values and lags; simulation cannot do that.

From a directory containing the embedded `check_bessel_reset.py`, install `numpy`, `scipy`, `sympy` in a normal Python environment and run `python check_bessel_reset.py`. The script carries out 54 passing tests in the reviewed execution, including the exact generator on the first two transformed monomials, symbolic centered/orthogonal polynomial identities and asymmetric degree-one/degree-two lag coefficients. Separately it evaluates six noncentral-chi-square Monte Carlo estimates of the stationary two-time Laplace transform (250000 draws each), moment estimates and reconstruction identities, and nine Bessel-density versus age-gamma integral comparisons.

The resulting checks compare independent implementations of the transform and are numerical illustrations only. Claim scope: stationary Poisson origin resetting, singular radial zero-flux extension, \(D_0>0\), \(r>0\), \(\alpha\in[0,1]\). No finite-sample reconstruction stability, non-Poisson memory model, full angular path law or independence certification is provided.
