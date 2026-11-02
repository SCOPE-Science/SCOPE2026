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

# Exact arithmetic replay

`python3 verify_quotients.py` outputs `QUOTIENT_REPLAY_OK`. This standalone Python program builds explicit quadratic extensions, confirms nonsquare defining elements, enumerates every rational argument for both genus-two quotient models over \(\mathbf F_p\) and \(\mathbf F_{p^2}\) with \(p=11,13\), and verifies the full parameter table, all equal-zeta collisions and different squares of collision parameters.

`python3 verify_direct.py` outputs `DIRECT_REPLAY_OK`. It implements a different polynomial-quotient finite-field arithmetic engine, tests every extension modulus for irreducibility, enumerates all points on the original genus-four curve over extensions of degrees one, two, three and four, constructs coefficients via Newton's identities and the genus-four functional equation, and checks the resulting numerator against the exact square formula. The script is finite exhaustive over the specified two prime fields and parameter sets. Both programs require only Python's standard library.

The mathematical proof additionally uses the explicit base-field involutions and quotient Jacobian isogeny, the Weil functional equation for genus-two curves, and Ohashi–Kudo's geometric-isomorphism criterion. The arithmetic programs are not offered as proofs of an unbounded enumeration for arbitrary prime characteristics. No independent external audit has been performed.
