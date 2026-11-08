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

## Reproduction

Execute `python3 verify.py` with Python 3.8+ in the same directory. The file is independent of nonstandard packages. It verifies the exact genus-two Cartier coefficients, two polynomial-elimination identities over characteristic five, Euclidean gcd certificates for fifteen distinct smooth parameters, the factorization into a linear term and an irreducible degree-fourteen term by Rabin's test, the full prime-field parameter census, and two direct point-count cross-checks. Output marker: `VERIFY_SQUARE_JAC_P5_OK`.

## Mathematical scope

The proof of the genus-four assertions also uses the two genus-two quotients arising from involutions, the prime-to-five Jacobian isogeny induced by them, and the classical genus-two Cartier/\(5\)-rank/ Newton-polygon correspondence. Finite-field point counts are checks only; the geometric classification depends on the algebraic identities and Rabin certificate. The parameter count is not an isomorphism-class count. No external mathematical audit was performed.
