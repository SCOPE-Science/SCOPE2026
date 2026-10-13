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

The accompanying `verify.py` was run directly with Python 3 and printed

`EXACT_CERTIFICATE_OK k2=[10] k4=[34] brute_ceiling=10000 valuation_checks=2268 bound_layers=120`

The finite computations are consistency checks, not infinite certification. The unconditional argument requires exact multiplicativity and cross divisibility, the full \(2\)-adic valuation identity for odd primes at even powers, and the exponent-growth inequality for every \(a\ge 2k\). These steps are proved in `RESULT.md`. The verifier checks all bounded exponent levels at \(k=2\) and \(k=4\); the general finite sieve is a theorem, not a completed enumeration for every exponent. Earlier literature may contain uncatalogued equivalent statements, and the short 2006 source could not be read in full.
