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

# Reproducible checks and limits

Execute `python3 verify_apery.py` using an ordinary Python 3 interpreter (standard library only). The script independently constructs the original Apéry-family coefficients and the complete translated coefficients by integer binomial convolution; it tests every coefficient modulo the prime, the constant coefficient modulo its square, and five independent integer-value identities.

Observed output:

`CHECK_OK cases=189 coefficients=4350 evaluation_identities=945 Wieferich_boundary_1093=confirmed`

The independent integer-value comparisons detect coefficient-translation errors. The prime-1093 test only confirms one explicitly excluded arithmetic boundary; it is not an assertion that the theorem fails there. Exact finite checks cannot establish universal irreducibility: the full proof uses divisibility of all intermediate binomial coefficients, an exact central-binomial congruence modulo a prime square, and the Eisenstein criterion. The eligibility of a prime must be established separately by computing the Fermat quotient; infinitude of eligible primes is not assumed.

No independent mathematical audit has been performed.
