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

# Reproduction and proof boundary

Run `python3 verify_periods.py`. This is a standalone Python 3 verifier using only integer arithmetic and the standard library; it recomputes the 9-term weighted polynomial, cross-multiplies exact integer polynomials to verify the displayed rational generating function, performs modular Euclidean polynomial gcds, and tests period divisibility for the first twelve primes \(2,3,5,7,11,13,17,19,23,29,31,37\). For each predicted period it also verifies failure at every maximal proper divisor. The first 151 exact coefficients are checked independently against direct four-part partition enumeration.

The exact all-prime theorem is not inferred from these samples. Its proof uses the identities \(P(1)=864\), \(P(-1)=32\), \(P\bmod\Phi_3=6q\), \(P\bmod\Phi_4=-12\), the exceptional characteristic gcd computations, the reduced-denominator period criterion, and Frobenius multiplicity. The verifier reproduces integer identities and representative prime cases but does not independently survey all possible prior literature or supply an external mathematical audit.
