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

The standalone standard-library script `verify_picard_inert.py` reconstructs coefficient polynomials directly from multinomial coefficients modulo each tested prime. It verifies the exact bivariate discriminant/Hasse identity, the nonzero scalar, the degree and squarefree normalized Hasse polynomial, absence of roots on the singular boundary, and polynomial coefficient cases in 23 primes \(p\equiv5\pmod6\) from \(5\) to \(197\). It terminates with `PICARD_INERT_PRIME_CARTIER_CHECKS_PASS`.

The complete proof for *all* such primes is in RESULT.md: the Cartier-basis computation, coefficient differential equation, Lucas divisibility, uniqueness of the polynomial differential-equation solution, and ODE-based squarefreeness. Finite-prime checks cannot establish the universal quantifier on their own.

The finding makes no statement about the full Newton polygon outside the superspecial locus, finite-field point frequencies, or unmarked isomorphism classes. Independent auditing and external validation have not been performed.
