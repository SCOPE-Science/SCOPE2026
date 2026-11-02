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

The exact count is the classical formula I_(p^a)(q)=(q^(p^a)-q^(p^(a-1)))/p^a for every prime power q. The proof is symbolic, using Dirichlet's theorem, primitive roots modulo odd prime squares, and lifting-the-exponent. The source code verify.py independently recomputes integer-valued counts and checks the predicted gcd for 17 small prime-power-degree cases and field sizes up to 70; this is not an exhaustive check of the infinite q-domain.

Direct test result: VERIFY_OK cases= 17 all_prime_power_samples<=70 and exact_gcd_witnesses. No proof assistant or third-party certification was used. The external independent audit remains not performed.
