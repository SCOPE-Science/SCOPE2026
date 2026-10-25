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
# Verification notes

The principal proof is the finite root-of-unity expansion and the exact cancellation of the quadratic terms. The standalone checker `check_mod3.py` independently evaluates the conditional covariance as a rational binomial sum and as a rational expression in the field \(\mathbb Q(\omega)\) with \(\omega^2+\omega+1=0\).

Run `python3 check_mod3.py` with Python 3. The performed test used seven exact rational biases, the integers \(3\le n\le30\), and all three residues: **588 exact comparisons passed**, together with the fair-bit sign-cycle assertions in that range. No floating-point roundoff enters these tests.

The infinite sign-reversal proof additionally uses periodicity/density of circle rotations. The irrational-angle arcsine limit invokes standard Weyl equidistribution; the checker does not certify equidistribution by enumeration. The algebraic proof itself is self-contained apart from the standard equidistribution result. Independent review and validation are not claimed.
