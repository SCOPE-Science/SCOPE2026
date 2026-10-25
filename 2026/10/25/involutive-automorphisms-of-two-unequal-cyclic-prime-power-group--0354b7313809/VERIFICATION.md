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

# Verification record
Run `python3 involution_verify.py` with Python 3. No additional dependencies are required. The checker enumerates all automorphisms of the stated constrained matrix form for 27 triples \((p,a,b)\), explicitly computes their squares on the generators of \(C_{p^a}\oplus C_{p^b}\), and compares the count with the claimed formula.

The actual terminal line obtained from this standalone program was:

`RANK_TWO_INVOLUTION_CENSUS_OK 27_cases`

The proof separately covers all odd primes and all binary exponent-gap and low-exponent regimes. Finite enumeration is corroboration only. The exact-order-two count excludes the identity and equals the stated order-dividing-two count minus one. The numerical checker does not address publication priority, equal exponents, higher rank, or an independent external audit.
