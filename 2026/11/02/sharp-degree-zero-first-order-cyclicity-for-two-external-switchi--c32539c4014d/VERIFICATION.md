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

The companion `verify.py` uses only the Python 3 standard library and can be executed with `python3 verify.py`. It checks polynomial identities exactly with rational coefficients: \(p(t)=(t-1)(9-t)\), \(p'q-pq'=-2(t^2+5t-34)\), the factorization at coefficient ratio \(1/2\), and the exact two squared-radius roots. It also checks the critical quadratic expression and compares separately computed midpoint quadrature of the angular radial forcing against the analytic Melnikov formula for sample transverse radii.

The independent numerical quadrature does not prove the uniform zero-count theorem. The proof comes from the sign of a quadratic derivative numerator on the whole open interval, together with positivity of the denominator. Near the two simple roots, standard implicit-function continuation of the smooth transverse return map proves hyperbolic cycles. All claims are first-order bifurcation claims; the package does not certify a global cycle maximum or mathematical priority.
