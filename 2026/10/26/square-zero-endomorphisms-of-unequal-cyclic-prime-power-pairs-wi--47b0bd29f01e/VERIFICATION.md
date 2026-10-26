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

# Verification

The proof in `RESULT.md` reduces the complete count to four congruences, a product-fiber calculation over the length-two residue ring, and separately verified boundary exponents.

Run `python3 verify.py` without external dependencies. The checker independently loops over coordinate representatives and verifies all four equations of the square-zero condition. It exhaustively checks 37 finite parameter triples at primes 2, 3, 5, and 7, and checks the product-fiber lemma for all four primes. Expected output includes `SQUARE_ZERO_MIXED_P_GROUP_OK 37 exhaustive_cases`.

Finite enumeration cannot prove an infinite claim, nor can its absence of counterexamples establish novelty. The written case analysis is the proof for all primes and all covered exponents. Independent mathematical validation has not been performed.
